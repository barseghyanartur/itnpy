Release history and notes
=========================
`Sequence based identifiers
<http://en.wikipedia.org/wiki/Software_versioning#Sequence-based_identifiers>`_
are used for versioning (schema follows below):

.. code-block:: text

    major.minor[.revision]

- It's always safe to upgrade within the same minor version (for example, from
  0.3 to 0.3.4).
- Minor version changes might be backwards incompatible. Read the
  release notes carefully before upgrading (for example, when upgrading from
  0.3.4 to 0.4).
- All backwards incompatible changes are mentioned in this document.

0.0.7
-----
2022-12-21

- Minor code optimizations.
- Improved test coverage.

0.0.6
-----
2022-12-20

- Tested against Python 3.11.
- Fixes in test suite.
- Fixes in docs.

0.0.5
-----
2022-12-18

- Renamed to ``itnpy2``. Re-released on the PyPI.

0.0.4
-----
2022-10-20

0.0.3
-----
2022-10-04

0.0.2
-----
2022-09-01

0.0.1
-----
2022-08-31

0.0.0
-----
2022-08-28
