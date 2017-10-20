### extends 'class_empty.py'
### block Header
from . import gxapi_cy
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXVV:
    pass
### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
    def get_data_np(self, start: int, num_elements: int, dtype: int):
        r, a = self._wrapper.get_data_array(start, num_elements, 5)
        return (r, np.asarray(a))
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer