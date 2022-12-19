Inverse Text Normalization
==========================

.. image:: https://img.shields.io/pypi/v/itnpy2.svg
   :target: https://pypi.python.org/pypi/itnpy2
   :alt: PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/itnpy2.svg
    :target: https://pypi.python.org/pypi/itnpy2/
    :alt: Supported Python versions

.. image:: https://github.com/barseghyanartur/itnpy/workflows/test/badge.svg
   :target: https://github.com/barseghyanartur/itnpy/actions
   :alt: Build Status

.. image:: https://readthedocs.org/projects/faker-file/badge/?version=latest
    :target: http://itnpy2.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/barseghyanartur/itnpy/blob/main/LICENSE
   :alt: MIT

A simple, deterministic, and extensible approach to 
`inverse text normalization <https://www.google.com/search?q=inverse+text+normalization>`__
(ITN) for numbers.

Overview
--------

This package converts raw spoken-form text (speech recognition output) into 
user-friendly written-form text. It works best for converting spoken numbers 
into numerical digits, or other translation tasks that do not modify word ordering. 
A `csv <https://github.com/barseghyanartur/itnpy/blob/master/assets/vocab.csv>`__
file is provided to define the basic rules for transforming spoken tokens into 
written tokens, and extra pre/post-processing may be applied for more specific 
formatting requirements, i.e. dates, measurements, money, etc.

----

.. image:: https://raw.githubusercontent.com/barseghyanartur/itnpy/master/assets/terminal.png
   :target: https://raw.githubusercontent.com/barseghyanartur/itnpy/master/assets/terminal.png
   :alt: Terminal

These examples were produced by running this
`script <https://github.com/barseghyanartur/itnpy/blob/master/scripts/docs.py>`__.

Installation
------------

This package supports Python versions >= 3.7

To install from `PyPI <https://pypi.org/project/itnpy2>`__:

.. code-block:: shell

    pip install itnpy2

To install locally:

.. code-block:: shell

   pip install -e .

Tests
-----

To run tests, use ``pytest`` in the root folder of this repository:

.. code-block:: shell

    pytest

Issues
------

This package has been verified on a limited set of 
`test-cases <https://github.com/barseghyanartur/itnpy/tree/master/tests/assets/>`__.
For any translation mistakes, feel free to open a pull request and update 
`failing.csv <https://github.com/barseghyanartur/itnpy/blob/master/tests/assets/inverse_normalize_numbers/failing.csv>`__
with the input, expected output, and mistake; thanks!

Citation
--------

If you find this work useful, please consider citing it.

.. code-block:: text

   @misc{hsu2022itn,
     title        = {A simple, deterministic, and extensible approach to inverse text normalization for numbers},
     author       = {Brandhsu},
     howpublished = {https://github.com/barseghyanartur/itnpy},
     year         = {2022}
   }
