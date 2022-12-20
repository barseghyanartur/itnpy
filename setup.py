import os

from setuptools import find_packages, setup

try:
    with open(
        os.path.join(os.path.dirname(__file__), "README.rst"), "r"
    ) as __f:
        long_description = __f.read()
except OSError:
    long_description = ""

version = {}
try:
    with open(
        os.path.join(os.path.dirname(__file__), "src", "itnpy", "_version.py"),
        "r",
    ) as __f:
        exec(__f.read(), version)
except OSError:
    long_description = ""

install_requires = [
    "numpy",
    "pandas",
]

tests_require = [
    "coverage",
    "pytest",
    "pytest-cov",
    "pytest-django",
    "pytest-ordering",
    "pytest-pythonpath",
]

setup(
    name="itnpy2",
    version=version["__version__"],
    author="Brandhsu",
    author_email="brandondhsu@gmail.com",
    maintainer="Artur Barseghyan",
    maintainer_email="artur.barseghyan@gmail.com",
    license="MIT",
    url="https://github.com/barseghyanartur/itnpy",
    description=(
        "A simple, deterministic, and extensible approach to inverse "
        "text normalization for numbers"
    ),
    long_description=long_description,
    long_description_content_type="text/x-rst",
    python_requires=">=3.7",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=install_requires,
    tests_require=tests_require,
    keywords=[
        "inverse text normalization",
        "natural language processing",
        "speech recognition",
        "itn",
        "nlp",
        "asr",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    project_urls={
        "Bug Tracker": "https://github.com/barseghyanartur/itnpy/issues",
        "Documentation": "https://itnpy2.readthedocs.io/",
        "Source Code": "https://github.com/barseghyanartur/itnpy",
        "Changelog": "https://itnpy.readthedocs.io/"
        "en/latest/changelog.html",
    },
)
