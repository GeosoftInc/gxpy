from grid_import import GeosoftGridImport
from map_import import GeosoftMapImport

class Toolbox(object):

    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label =  "Geosoft Tools"
        self.alias  = "geosoftarcpy"

        # List of tool classes associated with this toolbox
        self.tools = [ GeosoftGridImport, GeosoftMapImport ] 



