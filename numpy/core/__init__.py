
from info import __doc__
from numpy.version import version as __version__

import multiarray
import umath
import _internal # for freeze programs
import numerictypes as nt
multiarray.set_typeDict(nt.sctypeDict)
import _sort
from numeric import *
from fromnumeric import *
import defchararray as char
import records as rec
from records import *
from memmap import *
from defchararray import *
import scalarmath
from function_base import *
from machar import *
from getlimits import *
del nt

from fromnumeric import amax as max, amin as min, \
     round_ as round
from numeric import absolute as abs

__all__ = ['char','rec','memmap']
__all__ += numeric.__all__
__all__ += fromnumeric.__all__
__all__ += rec.__all__
__all__ += char.__all__
__all__ += function_base.__all__
__all__ += machar.__all__
__all__ += getlimits.__all__


from numpy.testing import Tester
test = Tester().test
bench = Tester().bench
