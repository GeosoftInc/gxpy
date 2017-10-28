# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:51:26 2014

@author: ian
"""

import time
import numpy as np
import random
from enum import Enum

import geosoft.gxpy.gx as gxp
import geosoft.gxpy.utility as gxu
import geosoft.gxpy.gdb as gxgdb


def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def no_stop():
    return False


class MvarException(Exception):
    pass

class NormType(Enum):
    none = 0        # none
    normal = 1      # gaussian (x-mean)/standard deviation
    lognormal = 2   # gaussian log(x)/standard deviation(log(x))

def normalize(data, norm):
    """
    Normalize data array, normalized in-place.  Normalization is based on simple Gaussian distribution, such
    that the resulting data has a mean of 0.0, and a standard deviation of 1.0.  Logarithmic normalization first
    takes the log of the data, clipped to a minimum positive value.

    If called with only NormType defined, the mean and standard deviation are calculated from the data, and returned.
    For logarithmic normalization, the minimum positive value is either the minimum of the data, if positive, or
    the standard deviation/1.0e6.

    The returned tuple can be passed to either this function to apply the normalization parameters to other data,
    or to denormalize() to convert normalized data back to original scaling.

    :param data:    1D data to normalise
    :param norm:    normalization tuple (NormType, mean, std, logmin), where:

                    =========== ===========================================
                    NormType    one of NormType enum
                    mean        mean value to remove
                    std         standard deviation
                    logmin      minimum value for logarithmic normalization
                    =========== ===========================================

                    If only NormType is provided as a single value (not a tuple), the
                    mean, std and logmin are calculated from the data.

    :returns:       tuple of normalization parameters (NormType, mean, std, logmin) which can be used
                    to normalize or denormalize data.
    """

    if isinstance(norm, tuple):

        # normalization parameters are provided

        ntype = norm[0]
        if ntype == NormType.none:
            return ntype, None, None, None

        dmean = norm[1]
        dstd = norm[2]
        dlogmin = norm[3]

        # for logarithmic normalization, take the log of the data
        if ntype == NormType.lognormal:
            data[:] = np.log(np.clip(data, dlogmin, data.max()))

    else:

        ntype = norm
        if ntype == NormType.none:
            return ntype, None, None, None

        if ntype == NormType.lognormal:
            dlogmin = data.min()
            if dlogmin <= 0.0:
                dstd = data.std()
                if dstd == 0.0:
                    return NormType.none, None, None, None
                else:
                    dlogmin = dstd/1.0e6
                    data[:] = np.log(np.clip(data, dlogmin, data.max()))
            else:
                data[:] = np.log(data)
            dmean = data.mean()
            dstd = data.std()

        else:
            dmean = data.mean()
            dstd = data.std()
            dlogmin = None

    # normalize
    data[:] = (data - dmean) / dstd

    return ntype, dmean, dstd, dlogmin

def denormalize(data, spec):
    """
    Denormalize data in-place.
    :param data:
    :param spec: normalization specification as tuple (Normalize, mean, std).
    """

    if spec[0] == NormType.none:
        return

    data[:] = data * spec[2] + spec[1]
    if spec[0] == NormType.lognormal:
        data[:] = np.exp(data)

def bmu_euclidean(classes, vector, amp=None):
    """
    BMU based on euclidean distance similarity

    :param  classes:    numpy array of class vectors, dimensioned same as vec
    :param  vector:     vector to test
    :param  amp:        ignored
    :returns:   index to BMU in classes
    """
    classes = classes.reshape(-1, len(vector))
    return int(np.square(classes - vector).sum(1).argmin())


def amp_squared(classes):
    """
    Returns conditioned amplitudes squared, for use as amp= array in bmu_cosine.
    Note that amplitudes == 0.0 will be replaced with 1.0 to prevent division by 0.
    
    :param classes: list of class centroid values
    :returns: array of vector amplitudes
    """
    amp = np.sum(np.square(classes), axis=1)
    amp[amp == 0.0] = 1.0
    return amp


def bmu_cosine(classes, vector, amp=None):
    """
    BMU based on cosine (direction) test (A dot B)/sqrt(sum[A*A] * sum[B*B]).
    See http://en.wikipedia.org/wiki/Cosine_similarity

    :param  classes:    numpy array of class vectors, shaped (-1,vec.shape[0])
    :param  vector:     vector to test
    :param  amp:        optional array of corresponding class amplitudes squared.
                        This is an optimization to avoid recalculating class amplitudes with each call.
                        Use amp_squared() to calculate amplitudes, which also replaces zero amplitudes
                        with 1.0 to avoid division by 0.

    :returns:   index to BMU in classes
    """

    # class amplitude and vector amplitude
    amp_vec = np.sum(np.square(vector))

    if amp is None:
        amp = np.sum(np.square(classes), axis=1).flatten()
        min_c = int(amp.argmin())
        if amp_vec == 0.0:
            return min_c

        # make zero-length class vectors have length 1
        amp[amp == 0.0] = 1.0

    elif amp_vec == 0.0:
        return int(amp.argmin())

    dot = np.dot(classes, vector) / np.sqrt(amp * amp_vec)

    return int(dot.argmax())

# list of similarity functions
_simfunc = {'Euclidean distance': bmu_euclidean,
            'Cosine (direction)': bmu_cosine}


def similarity_functions():
    """
    :returns: list of available built-in similarity function
    """

    def sortkey(p):
        if p == "Euclidean distance":
            return ""
        else:
            return p

    simfunc = list(_simfunc.keys())
    simfunc.sort(key=sortkey)
    return simfunc


def classify_data(classes, data, similarity=None):
    """
    Classify a provided data vector to the provided classes.  The data may not contain dummies

    :param classes:     set of classes to choose from, shaped (-1,data.shape[1])
    :param data:        array of multivariate data to classify, shape (-1,nVar)
    :param similarity:  similarity function
    :returns:           classification array

    """

    # set default similarity function to bmu_euclidean
    default_sim = bmu_euclidean

    def bmu(vec):
        return default_sim(classes, vec, amp=class_amp)

    if not (similarity is None):
        if isinstance(similarity, str):
            default_sim = _simfunc.get(similarity, None)
            if default_sim is None:
                raise MvarException("Unknown similarity function '{}'".format(similarity))
        else:
            default_sim = similarity

    # som amplitudes
    class_amp = np.sum(np.square(classes), axis=1)

    # classify
    data_classes = np.apply_along_axis(bmu, 1, data)

    return data_classes


def euclidean_distance(class_values, data):
    """
    Return array of Euclidean distance between classValue and data vectors.
    If you have an array of classes and a 1-D array of assignments that come from classify_data,
    pass classes[assignments] for classValue.

    :param class_values: numpy array of class vectors, shaped (-1,vec.shape[0])
    :param data:        data array shaped (len(assigned),classes.shape[1])
    :returns:           numpy 1D array of distances
    """
    return np.sqrt(np.square(data - class_values).sum(1))


def separations(classes):
    """
    Return the average Euclidean separation between neighboring classes in a 2D class(neuron)
    network of vectors.  Returns a 2D distance with dimension will be one less than passed classes.

    :returns:   2D array of average separation between class neurons
    """
    diff = np.zeros((classes.shape[0] - 1, classes.shape[1] - 1), dtype=float)
    for i in range(classes.shape[0] - 1):
        for j in range(classes.shape[1] - 1):
            d1 = np.linalg.norm(classes[i, j] - classes[i + 1, j])
            d2 = np.linalg.norm(classes[i, j] - classes[i, j + 1])
            d3 = np.linalg.norm(classes[i + 1, j] - classes[i + 1, j + 1])
            d4 = np.linalg.norm(classes[i, j + 1] - classes[i + 1, j + 1])
            diff[i, j] = (d1 + d2 + d3 + d4) / 4.0

    return diff


class SOM:
    """
    Self-Organizing-Map classification

    :param data:            2D array of multivariate training data (rows, variables), must be float, no dummies
    :param nclasses:        the number of classes in the network, must be one of list_dim()
    :param neighborhood:    initial training neighborhood in nodes, default includes all classes
    :param rate:            rate of focus refinements, default 0.9999
    :param focus:           number of focusing passes, default 1/(1-rate)
    :param weight:          adjustment weight for each training adjustment, default 0.01
    :param similarity:      a similarity function (classes,vector) that returns index of closest match of
                            vector to one of passed numpy array of classes.  Default is Euclidean static
                            function bmu_euclidean().  Built-in functions are:

                            ============= =======================================================
                            bmu_euclidean  closest match based on simple Euclidean distance
                            bmu_cosine     closest match based on vector direction and amplitude
                            ============= =======================================================

    :param progress:        progress function (string, percent, som), som is the current som net
    :param stop:            stop request function, returns True to stop the analysis

    :param levels:          number of anomalous levels to add, default is 0 (see below)
    :param percent:         percentage of data to consider anomalous, default is 5.0 percent

    If levels > 0, the SOM network is expanded in steps by analysing the anomalous
    data that is farthest from the existing network based on the standard deviation
    of the distance of data from the network of the previous level.

        #. Calculate an anomalous cutoff based on standard deviation distance to class
        #. Collect anomalous data that is farthest from current neurons
        #. Run SOM on this anomalous data to come up with n+1..2n classes
        #. Repeat 2 and 3 up to number of levels

    The result is a set of stratified classifications in which the higher class sets are ever more anomalous.
    Setting level=0 (the default) creates a conventional SOM.  The most useful level setting based on the
    geoscience datasets studies so far is 1, which creates a naturally anomalous set of classifications in
    the n+1 to 2n range.  For example, for a dimension 3 network classified for levels=1, the there will be 18
    classes; classes 0 to 8 are background classes, and classes 9 to 19 are anomalous classes.

    """

    # minimum and maximum dimensions
    _minDimension = 2
    _maxDimension = 16

    def __init__(self, data, nclasses,
                 neighborhood=0, rate=0.9999, focus=None, weight=0.01,
                 levels=0, percent=5.0, similarity=None,
                 progress=print, stop=None):

        # sensible inputs
        if not (nclasses in self.list_dim()):
            l = self.list_dim()
            raise MvarException("nclasses({}) must one of {}".format(nclasses, l))
        self.dim = isqrt(nclasses)
        self.nVar = data.shape[1]
        if self.nVar <= 0:
            raise MvarException("Variables ({}) must be 1 or larger".format(self.nVar))
        if rate >= 1.0:
            raise MvarException("rate({}) must be less than 1.0".format(rate))

        # training parameters
        self.trnData = data
        if neighborhood > 0:
            self.nbh = neighborhood
        else:
            self.nbh = self.dim
        if (rate >= 1.0) or (rate < 0.5):
            self.rate = 0.9999
        else:
            self.rate = rate
        if focus is None:
            self.focus = int(1 / (1 - self.rate))
        else:
            self.focus = focus
        self.weight = weight
        self.progress = progress

        # similarity function
        if similarity is None:
            self._bmu = bmu_cosine
        else:
            self._bmu = similarity

        if stop is None:
            self.stop = no_stop
        else:
            self.stop = stop

        # initialize som to random values selected from data
        self.som = np.zeros((self.dim, self.dim, data.shape[1]))
        sample = np.random.permutation(nclasses).reshape((self.dim, self.dim)) * int(data.shape[0] / nclasses)
        for i in range(self.dim):
            for j in range(self.dim):
                self.som[i, j] = data[sample[i, j], :]

        # train the SOM
        self._train()

        # expand for anomalous data
        if (levels > 0) and (percent > 0.0):

            for lev in range(levels):

                progress("Anomalous {}%, level {}".format(percent, lev + 1))

                classes = self.som.reshape(-1, self.nVar)
                cls = classify_data(classes, data, similarity=self._bmu)
                eud = euclidean_distance(classes[cls], data)
                cutoff = np.percentile(eud, int(100.0 - percent))
                data = data[eud > cutoff, :]

                # stop if we do not have a minimum amount of data
                if data.shape[0] < (self.dim * self.dim):
                    break

                s = SOM(data, nclasses, neighborhood=neighborhood,
                        rate=rate, weight=weight,
                        progress=progress, stop=self.stop)

                # add anomalous som to base som
                self.som = np.append(self.som, s.som)

        # reshape the som to a simple 1D list of variable set
        self.som = self.som.reshape((-1, data.shape[1]))

    @staticmethod
    def list_dim():
        l = []
        for i in range(SOM._minDimension, SOM._maxDimension + 1):
            l.append(i ** 2)
        return l

    def _alignment(self, vec):
        """ alignment (dot-product) similarity"""
        dot = np.dot(self.som.reshape(-1, self.nVar), vec)
        return int(dot.argmax())

    def _adjustall(self, vec):
        """
        Update all neurons to the data vec
        """
        self.som += self.weight * (vec - self.som)

    def _adjustneighborhood(self, vec, bmu, gamma):
        """
        Update neurons based on neighborhood distance from the BMU
        """

        v, h, n = self.som.shape

        ind = np.indices((v, h))
        ind[0] -= bmu[0]
        ind[1] -= bmu[1]
        dist = np.sqrt(np.square(ind[0]) + np.square(ind[1]))
        mask = np.less(dist, gamma).astype(float)
        mask *= self.weight
        mask = np.multiply.outer(mask, np.ones(n, int))
        self.som += mask * (vec - self.som)

    def _train(self):
        """ train the som """
        self.progress("Training...", 0, None)
        data = self.trnData
        gamma = float(self.nbh)
        npass = 0
        while gamma > 1.0:

            npass += 1
            if npass % 1000 == 0:
                self.progress(" Pass {}".format(npass), int(100 - (gamma - 1) * 100 / (self.nbh - 1)), self)
                if self.stop():
                    return

            vec = data[int(data.shape[0] * random.random())]  # choose a random data point from the sample data
            bmu = divmod(self._bmu(self.som.reshape(-1, vec.shape[0]), vec), self.dim)  # closest to 2D BMU

            if gamma >= self.dim:  # adjust all
                self._adjustall(vec)
            else:
                self._adjustneighborhood(vec, bmu, gamma)
            gamma *= self.rate

        # focus neurons
        for i in range(self.focus):
            if i % 1000 == 0:
                self.progress(" Focus {} of {}".format(i, self.focus), i, None)
                if self.stop():
                    return

            vec = data[int(data.shape[0] * random.random())]  # choose a random data point from the sample data
            bmu = divmod(self._bmu(self.som.reshape(-1, vec.shape[0]), vec), self.dim)
            self._adjustneighborhood(vec, bmu, 0.5)

    def density(self):
        """
        :returns: density matrix for the current SOM based on training data
        """

        # classify all the training data
        class_data = classify_data(self.som.reshape(-1, self.trnData.shape[1]), self.trnData, self._bmu)
        dens = np.bincount(class_data)

        # TODO: used to be self.som.reshape((self.dim,self.dim)) - double check why this did not work
        return dens.reshape((-1,self.dim))


def _no_stop():
    return False


class SOMgdb:
    """
    Apply SOM analysis to a Geosoft GDB

    :param gdb:         database file to process
    :param fields:      list of multivariate fields to be used in the som
    :param nomalize     list of normalizations (NormType) requested, one for each field or a single type for all
    :param dim:         som dimension.  The SOM neural network is square, so the number of base classifications is
                        (dim*dim)
    :param per:         percent cutoff for anomalous classes.  Anomalous classes are determined based on a percentage
                        of the data that least-fits the base neurons.
    :param class_err:  names of the output fields for the classification index and the Euler Distance
    :param ch_filter:   tuple( filter_channel, filter_value ), filter to only process data that matches filter_value
                        in the filter_channel.  This is to limit analysis to a specific existing classification.
    :param similarity:  a similarity function (classes,vector) that returns index of closest match of
                        vector to one of passed numpy array of classes.  Default is Euclidean static
                        function bmu_euclidean().  Built-in functions are:

                        ============= =======================================================
                        bmu_euclidean  closest match based on simple Euclidean distance
                        bmu_cosine     closest match based on vector direction
                        ============= =======================================================

    :param progress:    function called to report progress (message, percent_complete)
    :param stop:        function called to test for a stop request, return True to stop working.
    """

    def __init__(self, gdb, fields, dim=16, per=2.0, normalize=NormType.none,
                 class_err=('Class', 'EuD'), ch_filter=('', None), similarity=None,
                 progress=print, stop=None):

        # read/sample data
        self.gdb = gdb
        self.fields = list(fields)
        self.dim = dim
        self.per = per
        self.outClass = class_err[0]
        self.outDist = class_err[1]

        if ch_filter[0]:
            self.ch_filter = (ch_filter[0], gxp.rdecode(ch_filter[1]))
        else:
            self.ch_filter = ('', None)

        # similarity function
        if similarity is None:
            self._sim = bmu_euclidean
        else:
            self._sim = similarity

        self.progress = progress
        self.progress("Database: {}".format(gdb.file_name))
        self.progress("Data: {}".format(fields))

        # normalize the normalise list
        norm = []
        norm.append(normalize)
        n = len(self.fields) - len(norm)
        for i in range(n):
            norm.append(norm[-1])

        if stop:
            self.stop = stop
        else:
            self.stop = _no_stop

        # read data
        training_data = self._readdata()
        if training_data.shape[0] == 0:
            raise MvarException("No data to process.")

        # Normalize the data
        self.progress("Normalizing ...")
        self.normspecs = self._normalize(training_data, norm)

        # setup the som
        last = time.perf_counter()
        self.progress("Training the SOM ...")
        if self.per > 0.0:
            levels = 1
            per = self.per
        else:
            levels = 0
            per = 0.0
        self.som = SOM(training_data, self.dim, progress=self.progress, levels=levels, percent=per)

        self.progress("Training time {:.2f} seconds".format(time.perf_counter() - last))

        # classify the data
        self.progress("Classifying the data...")
        self._classify_db()

        som = self.som.som.reshape((-1, training_data.shape[1]))
        for i in range(som.shape[0]):
            print('{}> {}'.format(i, som[i]))

    def _readdata(self):

        self.nCh = len(self.fields)

        # read line at a time
        lines = self.gdb.list_lines(select=True)
        nl = len(lines)

        # if ch_filter, add filter to the data
        if self.ch_filter[0]:
            self.fields.append(self.ch_filter[0])

        n = 0
        data = []
        for l in lines:

            npd, ch, fid = self.gdb.read_line(l, channels=self.fields, dummy=gxgdb.READ_REMOVE_DUMMYROWS)

            # build data array
            if n == 0:
                data = npd  # .copy()
            else:
                data = np.vstack((data, npd))

            n += 1
            if self.progress:
                self.progress('{} + {} from line {}'.format(data.shape, npd.shape[0], l), n * 100 / nl)
            if self.stop():
                raise MvarException("Stop requested")
            del npd

        # filter
        if self.ch_filter[0]:
            # create filter array, True for values that match the filter value
            filt = data[:, -1] == self.ch_filter[1]

            # create final data array with only filtered values, and drop the filter from the data
            data = data[filt, :-1]
            self.fields = self.fields[:-1]

        return data

    def _normalize(self, data, norm):
        """
        Normalize data array.

        :param data:    2D data to normalise, shape (rows,variables)
        :param norm:    list of normalization types, one per variable:
        :returns:       list of normalization specs
        """

        normspecs = []
        nfields = data.shape[1]
        for i in range(nfields):
            if self.progress:
                self.progress("{}: {}".format(norm[i],self.fields[i]), i * 100.0 / nfields)
            normspecs.append(normalize(data[:,i],norm[i]))

        return normspecs

    def _apply_norms(self, data):
        """
        Normalize data to match the SOM normalization
        """
        nfields = data.shape[1]
        for i in range(nfields):
            normalize(data[:,i],self.normspecs[i])

    def _classify_db(self):

        # create output channels
        self.gdb.delete_channel(self.outClass)
        self.gdb.new_channel(self.outClass, np.int32)
        self.gdb.delete_channel(self.outDist)
        self.gdb.new_channel(self.outDist, np.float64)

        # if filter, add filter to the data
        if self.ch_filter[0]:
            self.fields.append(self.ch_filter[0])

        # put results back in the database
        lines = self.gdb.list_lines(select=True)
        nl = len(lines)
        n = 0
        for l in lines:

            ln, lsymb = self.gdb.line_name_symb(l)

            data, ch, fid = self.gdb.read_line(l, channels=self.fields)
            dummy = gxu.gx_dummy(data.dtype)

            # mask will hold True for data to be removed from output
            mask = np.apply_along_axis(lambda a: dummy in a, 1, data)
            if self.ch_filter[0]:
                filt = data[:, -1] != self.ch_filter[1]
                mask += filt
                data = data[:, :-1]  # remove filter channel
            data[mask] = 0.0
            self._apply_norms(data)
            classes = self.som.som.reshape(-1, data.shape[1])
            clss = classify_data(classes, data, similarity=self._sim)
            err = euclidean_distance(classes[clss], data)
            clss[mask] = gxu.gx_dummy(clss.dtype)
            err[mask] = gxu.gx_dummy(err.dtype)
            self.gdb.write_channel(lsymb, self.outClass, clss, fid=fid)
            self.gdb.write_channel(lsymb, self.outDist, err, fid=fid)

            n += 1
            self.progress('Writing line {}'.format(ln), (n * 100.0) / nl)
            if self.stop():
                raise MvarException("Stop requested")

        if self.ch_filter[0]:
            self.fields = self.fields[:-1]
