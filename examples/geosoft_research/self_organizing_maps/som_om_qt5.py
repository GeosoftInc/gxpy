# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 10:15:34 2014

INSTALLATION

This script depends on PyGt5, which **cannot** be run from ESRI ArcGIS Pro Python.

To install PyQt5, open a command window as administrator and navigate to your Python
folder (the folder that contains python.exe):

   scripts\pip install pyqt5

see https://www.riverbankcomputing.com/software/pyqt/intro for PyQt copyright.

@author: Ian MacLeod, Geosoft, 2014-17
"""
#TODO: save classification map
#TODO: add some Help
#TODO: graphics - show the som adjusting as it goes.

#import pydevd
#pydevd.settrace('localhost', port=34765, stdoutToServer=True, stderrToServer=True)

import os
import sys
import math
import json
import numpy as np
import argparse as argp

from PyQt5 import QtGui, QtWidgets

import geosoft.gxpy.gx as gxp
import geosoft.gxpy.gdb as gxgdb
import geosoft.gxpy.utility as gxu

try:
    import mvar
except:
    # this depends on the modules folder being up two folders from this source file
    modules_folder = os.path.split(os.path.split(os.path.split(__file__)[0])[0])[0]
    sys.path.append(modules_folder)
    import modules.mvar as mvar

from som_om_ui_qt5 import Ui_som_om


def _(s):
    return s


def decimate(data,maxn):
    ndata = len(data)
    if (ndata > maxn) and (maxn > 0):
        nth = math.ceil(ndata/maxn)
        base = np.arange(0,len(data))
        select = (base%nth)==0
        return(data[select])
    else:
        return(data)

class SOMException(Exception):
    pass

###############################################################################################

class SomDialog(QtWidgets.QDialog, Ui_som_om):

    def __init__(self, gdb, settings):
        super(SomDialog, self).__init__(None)
        self.setupUi(self)

        self.gdb = gdb
        self.settings = settings
        self.class_err = settings['CLASS_ERR']
        self.filter = settings['FILTER']
        self.stopRequest = False
        self.savedVal = {}
        indata = settings['INPUT_DATA']
        self.chans = sorted(indata, key=str.lower)
        self.norms = [indata[c] for c in self.chans]

        sf = mvar.similarity_functions()
        self.som_param = settings.get('SOM_PARAMETERS', (4, 2, sf[0]))

        #connect slots
        self.classButton.clicked.connect(self.classify)
        self.outClass.textChanged.connect(self.outClassChanged)
        self.norm.currentIndexChanged.connect(self.allNorms)
        self.stopButton.clicked.connect(self.stopIt)

        self.initialiseDialog()

    def refresh(self):

        def channorm(chanList,normList,chan,norm):
            if len(chan):
                chanList.setCurrentIndex(chanList.findText(chan))
                normList.setCurrentIndex(norm)

        #clear channel lists
        self.chan_1.clear()
        self.chan_2.clear()
        self.chan_3.clear()
        self.chan_4.clear()
        self.chan_5.clear()
        self.chan_6.clear()
        self.chan_7.clear()
        self.chan_8.clear()
        self.chan_9.clear()
        self.chan_10.clear()
        self.chan_11.clear()
        self.chan_12.clear()
        self.chan_13.clear()
        self.chan_14.clear()
        self.chan_15.clear()
        self.chan_16.clear()
        self.filterChan.clear()

        #set channel lists to database channels
        chans = self.gdb.list_channels()
        chans[''] = None
        for c in sorted(chans.keys(), key=lambda k: k.lower()):
            self.chan_1.addItem(c)
            self.chan_2.addItem(c)
            self.chan_3.addItem(c)
            self.chan_4.addItem(c)
            self.chan_5.addItem(c)
            self.chan_6.addItem(c)
            self.chan_7.addItem(c)
            self.chan_8.addItem(c)
            self.chan_9.addItem(c)
            self.chan_10.addItem(c)
            self.chan_11.addItem(c)
            self.chan_12.addItem(c)
            self.chan_13.addItem(c)
            self.chan_14.addItem(c)
            self.chan_15.addItem(c)
            self.chan_16.addItem(c)
            self.filterChan.addItem(c)

        # set norm list
        for n in ['no','normal','lognorm']:
            self.norm.addItem(n)
            self.norm_1.addItem(n)
            self.norm_2.addItem(n)
            self.norm_3.addItem(n)
            self.norm_4.addItem(n)
            self.norm_5.addItem(n)
            self.norm_6.addItem(n)
            self.norm_7.addItem(n)
            self.norm_8.addItem(n)
            self.norm_9.addItem(n)
            self.norm_10.addItem(n)
            self.norm_11.addItem(n)
            self.norm_12.addItem(n)
            self.norm_13.addItem(n)
            self.norm_14.addItem(n)
            self.norm_15.addItem(n)
            self.norm_16.addItem(n)

        #set default channels
        chans = self.chans
        norms = self.norms
        n = len(chans)
        if n >= 1: channorm(self.chan_1,self.norm_1,chans[0],norms[0])
        if n >= 2: channorm(self.chan_2,self.norm_2,chans[1],norms[1])
        if n >= 3: channorm(self.chan_3,self.norm_3,chans[2],norms[2])
        if n >= 4: channorm(self.chan_4,self.norm_4,chans[3],norms[3])
        if n >= 5: channorm(self.chan_5,self.norm_5,chans[4],norms[4])
        if n >= 6: channorm(self.chan_6,self.norm_6,chans[5],norms[5])
        if n >= 7: channorm(self.chan_7,self.norm_7,chans[6],norms[6])
        if n >= 8: channorm(self.chan_8,self.norm_8,chans[8],norms[8])
        if n >= 9: channorm(self.chan_9,self.norm_9,chans[8],norms[8])
        if n >= 10: channorm(self.chan_10,self.norm_10,chans[9],norms[9])
        if n >= 11: channorm(self.chan_11,self.norm_11,chans[10],norms[10])
        if n >= 12: channorm(self.chan_12,self.norm_12,chans[11],norms[11])
        if n >= 13: channorm(self.chan_13,self.norm_13,chans[12],norms[12])
        if n >= 14: channorm(self.chan_14,self.norm_14,chans[13],norms[13])
        if n >= 15: channorm(self.chan_15,self.norm_15,chans[14],norms[14])
        if n >= 16: channorm(self.chan_16,self.norm_16,chans[15],norms[15])

        #output channels
        self.outClass.setText(self.class_err[0])
        self.outError.setText(self.class_err[1])

        #filter
        self.filterChan.setCurrentIndex(self.filterChan.findText(self.filter[0]))
        self.filterVal.setText(self.filter[1])

        #database name
        self.databaseName.setText(self.gdb.file_name)

    def results(self):
        indata = {}
        for i in range(len(self.chans)):
            indata[self.chans[i]] = self.norms[i]
        self.settings['INPUT_DATA'] = indata
        self.settings['FILTER'] = self.filter
        self.settings['CLASS_ERR'] = self.class_err
        self.settings['SOM_PARAMETERS'] = self.som_param
        return self.settings

    def initialiseDialog(self):

        self.refresh()

        self.stopB(False)

        # similarity
        sf = mvar.similarity_functions()
        for i in sf:
            self.similarity_func.addItem(str(i))
        self.similarity_func.setCurrentIndex(sf.index(self.som_param[2]))

        # classifications
        lc = mvar.SOM.list_dim()
        for i in lc:
            self.nClasses.addItem(str(i))
        self.nClasses.setCurrentIndex(lc.index(self.som_param[0]))
        self.anomPercent.setText(str(self.som_param[1]))

    def stopB(self,b):
        self.stopButton.setEnabled(b)
        self.classButton.setEnabled(not b)
        if not b:
            self.stopRequest = False

    def stopIt(self):
        self.stopRequest = True
        self.progLabel.setText('Stopping...')

    def outClassChanged(self):
        outClass = self.outClass.text().strip()
        if outClass:
            self.outError.setText(outClass+'_eud')


    def allNorms(self,index):
        self.norm_1.setCurrentIndex(index)
        self.norm_2.setCurrentIndex(index)
        self.norm_3.setCurrentIndex(index)
        self.norm_4.setCurrentIndex(index)
        self.norm_5.setCurrentIndex(index)
        self.norm_6.setCurrentIndex(index)
        self.norm_7.setCurrentIndex(index)
        self.norm_8.setCurrentIndex(index)
        self.norm_9.setCurrentIndex(index)
        self.norm_10.setCurrentIndex(index)
        self.norm_11.setCurrentIndex(index)
        self.norm_12.setCurrentIndex(index)
        self.norm_13.setCurrentIndex(index)
        self.norm_14.setCurrentIndex(index)
        self.norm_15.setCurrentIndex(index)
        self.norm_16.setCurrentIndex(index)

    def classify(self):

        def progress(label, value=None, som=None):
            self.progLabel.setText(label)
            if value != None: self.progressBar.setValue(int(value))
            QtWidgets.qApp.processEvents()

        def stop_check():
            QtWidgets.qApp.processEvents()
            return self.stopRequest

        def addChan(cb,cn,c,n):
            cc = cb.currentText()
            if len(cc) == 0: return
            if cc in c: return
            c.append(cc)
            n.append(cn.currentIndex())

        chan = []
        norm = []
        addChan(self.chan_1 ,self.norm_1 , chan, norm)
        addChan(self.chan_2 ,self.norm_2 , chan, norm)
        addChan(self.chan_3 ,self.norm_3 , chan, norm)
        addChan(self.chan_4 ,self.norm_4 , chan, norm)
        addChan(self.chan_5 ,self.norm_5 , chan, norm)
        addChan(self.chan_6 ,self.norm_6 , chan, norm)
        addChan(self.chan_7 ,self.norm_7 , chan, norm)
        addChan(self.chan_8 ,self.norm_8 , chan, norm)
        addChan(self.chan_9 ,self.norm_9 , chan, norm)
        addChan(self.chan_10,self.norm_10, chan, norm)
        addChan(self.chan_11,self.norm_11, chan, norm)
        addChan(self.chan_12,self.norm_12, chan, norm)
        addChan(self.chan_13,self.norm_13, chan, norm)
        addChan(self.chan_14,self.norm_14, chan, norm)
        addChan(self.chan_15,self.norm_15, chan, norm)
        addChan(self.chan_16,self.norm_16, chan, norm)
        self.chans = chan
        self.norms = norm

        self.som_param = (int(self.nClasses.currentText()),
                          min(max(0.0,float(self.anomPercent.text())),95.0),
                          self.similarity_func.currentText())

        self.filter = (self.filterChan.currentText().strip(), self.filterVal.text().strip())
        if (len(self.filter[0]) == 0) or (len(self.filter[1]) == 0):
            self.filter = ('','')

        self.class_err = (self.outClass.text(), self.outError.text())

        gdbChans = self.gdb.list_channels()
        if (self.class_err[0] in gdbChans) or (self.class_err[1] in gdbChans):
            butts = QtWidgets.QMessageBox.Yes
            butts |= QtWidgets.QMessageBox.No
            response = QtWidgets.QMessageBox.question(self,"Field exist in database",
                                                  '"{}" or "{}" exists. Overwrite?'
                                                  .format(self.class_err[0],self.class_err[1]),
                                                  buttons=butts)
            if response != QtWidgets.QMessageBox.Yes:
                return

        self.stopB(True)
        try:
            mvar.SOMgdb( self.gdb,
                         chan,
                         normalize=norm,
                         ch_filter=self.filter,
                         dim=self.som_param[0],
                         per=self.som_param[1],
                         similarity=self.som_param[2],
                         progress=progress, stop=stop_check, class_err=self.class_err)

        except Exception as e:
            QtWidgets.QMessageBox.information(self,
                                              "Classification failed",
                                              '{}'.format(e),
                                              buttons=QtWidgets.QMessageBox.Ok)
            raise

        self.done(0)

###############################################################################################
if __name__ == '__main__':
    '''
    Self-Organizing maps
    '''

    # get command line parameters

    parser = argp.ArgumentParser(description=_("SOM analysis of data in a Geosoft database"))
    args = parser.parse_args()
    print("GeoSOM copyright 2016 Geosoft Inc.\n")

    gxc = gxp.GXpy()
    settings = gxu.get_shared_dict()
    print(settings)
    #input('continue...')

    # defaults
    if 'CLASS_ERR' not in settings:
        settings['CLASS_ERR'] = ('Class', 'EuD')
    if 'FILTER' not in settings:
        settings['FILTER'] = ('', '')
    if 'SOM_PARAMETERS' not in settings:
        settings['SOM_PARAMETERS'] = (4, 2, mvar.similarity_functions()[0])

    gdb_name = os.path.normpath(settings['GDB_NAME'])
    gdb = gxgdb.Geosoft_gdb.open(gdb_name)

    #launch GUI
    app = QtWidgets.QApplication([])
    form = SomDialog(gdb, settings)
    form.show()
    app.exec_()

    results = form.results()
    gxu.set_shared_dict(results)
