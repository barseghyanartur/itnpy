import os

from setuptools import find_packages, setup

###############################################################################
name = "itnpy2"
author = "Brandhsu"
author_email = "brandondhsu@gmail.com"
license = "MIT"
url = "https://github.com/barseghyanartur/itnpy"
description = (
    "A simple, deterministic, and extensible approach to inverse "
    "text normalization for numbers"
)
###############################################################################


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

packages = find_packages("src")

install_requires = [
    __lib.strip()
    for __lib in open(
        os.path.join(os.path.dirname(__file__), "requirements.txt"), "r"
    ).readlines()
]

setup(
    name=name,
    version=version["__version__"],
    author=author,
    author_email=author_email,
    maintainer="Artur Barseghyan",
    maintainer_email="artur.barseghyan@gmail.com",
    license=license,
    url=url,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
    package_dir={"": "src"},
    packages=packages,
    install_requires=install_requires,
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
    ],
)
