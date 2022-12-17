Inverse Text Normalization
==========================

.. raw:: html

   <div>
   <img src="https://badgen.net/pypi/v/itnpy2">
   <img src="https://badgen.net/pypi/python/itnpy2">
   <img src="https://badgen.net/github/license/barseghyanartur/itnpy">
   <img src="https://badgen.net/badge/code%20style/black?color=black">
   </div>


A simple, deterministic, and extensible approach to 
`inverse text normalization <https://www.google.com/search?q=inverse+text+normalization>`_ 
(ITN) for numbers.

Overview
--------

This package converts raw spoken-form text (speech recognition output) into 
user-friendly written-form text. It works best for converting spoken numbers 
into numerical digits, or other translation tasks that do not modify word ordering. 
A `csv <https://github.com/barseghyanartur/itnpy/blob/master/assets/vocab.csv>`_ 
file is provided to define the basic rules for transforming spoken tokens into 
written tokens, and extra pre/post-processing may be applied for more specific 
formatting requirements, i.e. dates, measurements, money, etc.

----

.. raw:: html

   <div align="center">
       <img src="https://raw.githubusercontent.com/barseghyanartur/itnpy/master/assets/terminal.png" width=60%>
   </div>



.. raw:: html

   <div align="center">
       These examples were produced by running this <a href="https://github.com/barseghyanartur/itnpy/blob/master/scripts/docs.py">script</a>.
   </div>


Installation
------------

This package supports Python versions >= 3.7

To install from `pypi <https://pypi.org/project/itnpy2>`_\ :

.. code-block:: shell

   $ pip install itnpy2

To install locally:

.. code-block:: shell

   $ pip install -e .

Tests
-----

To run tests, use ``pytest`` in the root folder of this repository:

.. code-block:: shell

   $ ls
   LICENSE         assets          scripts         src
   README.md       requirements.txt    setup.py        tests

   $ pytest

Issues
------

This package has been verified on a limited set of 
`test-cases <https://github.com/barseghyanartur/itnpy/tree/master/tests/assets/>`_. 
For any translation mistakes, feel free to open a pull request and update 
`failing.csv <https://github.com/barseghyanartur/itnpy/blob/master/tests/assets/inverse_normalize_numbers/failing.csv>`_ 
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
