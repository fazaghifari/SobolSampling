Sobol Sampling
==========
[![PyPI](http://img.shields.io/pypi/v/sobolsampling.svg)](https://pypi.python.org/pypi/sobolsampling)

[Sobol sequences](https://en.wikipedia.org/wiki/Sobol_sequence) are an example of quasi-random low-discrepancy sequences. They were first introduced by the Russian mathematician Ilya M. Sobol.

This Python function was translated from the original c++ program by Frances Kuo and Stephen Joe https://web.maths.unsw.edu.au/~fkuo/sobol/

# Dependencies
This function requires numpy to run.

# Installation
Sobol Sampling works with Python 3, to install write:

```
pip install sobolsampling
```

# Usage
```{python}
from sobolsampling.sobol_new import sobol_points

nsamp = 10  # The number of points
dim = 3  # The dimension
points = sobol_points(nsamp, dim)
print(points)

# [[0.     0.     0.    ]
#  [0.5    0.5    0.5   ]
#  [0.75   0.25   0.25  ]
#  [0.25   0.75   0.75  ]
#  [0.375  0.375  0.625 ]
#  [0.875  0.875  0.125 ]
#  [0.625  0.125  0.875 ]
#  [0.125  0.625  0.375 ]
#  [0.1875 0.3125 0.9375]
#  [0.6875 0.8125 0.4375]]
```
