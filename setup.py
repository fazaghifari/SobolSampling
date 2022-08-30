'''
Author: Ghifari Adam Faza <ghifariadamf@gmail.com>
This package is distributed under New BSD license.
'''

from setuptools import setup
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
LONG_DESCRIPTION= """
Sobol sequences are an example of quasi-random low-discrepancy sequences. They were first introduced by the Russian mathematician Ilya M. Sobol.

This Python function was translated from the original c++ program by Frances Kuo and Stephen Joe https://web.maths.unsw.edu.au/~fkuo/sobol/
"""


metadata = dict(
    name='sobolsampling',
    version='0.1.3',
    description='Sobol Sampling Package',
    long_description=LONG_DESCRIPTION,
    author='Ghifari Adam F',
    author_email='ghifariadamf@gmail.com',
    license='BSD-3',
    packages=[
        'sobolsampling'
    ],
    install_requires=[
        'numpy'
    ],
    python_requires='>=3.6',
    zip_safe=False,
    include_package_data=True,
    url = 'https://github.com/fazaghifari/SobolSampling', # use the URL to the github repo
    download_url = 'https://github.com/fazaghifari/SobolSampling/releases',
)

setup(**metadata)
