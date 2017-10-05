#!/usr/bin/env python
import numpy as np
from numpy.distutils.system_info import get_info
import sys
import timeit


print("Numpy version: {}".format(np.__version__))
np.__config__.show()

info = get_info('blas_opt')
print('BLAS info:')
for kk, vv in info.items():
    print(' * ' + kk + ' ' + str(vv))



x = np.random.random((1000,1000))

setup = "import numpy; x = numpy.random.random((1000,1000))"
count = 5

t = timeit.Timer("numpy.dot(x, x.T)", setup=setup)
print("dot: {} sec".format(t.timeit(count)/count))
