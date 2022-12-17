from setuptools import find_packages, setup

##########################################################################################################
name = "itnpy"
author = "Brandhsu"
author_email = "brandondhsu@gmail.com"
license = "MIT"
url = "https://github.com/barseghyanartur/itnpy"
description = "A simple, deterministic, and extensible approach to inverse text normalization for numbers"
##########################################################################################################

PATH = {}
PATH["root"] = "/Users/owner/Code/ai/ml/pypi/itnpy"
PATH["version"] = "src/itnpy"

with open(f"{PATH['root']}/README.md", "r") as f:
    long_description = f.read()

version = {}
with open(f"{PATH['root']}/{PATH['version']}/_version.py", "r") as f:
    exec(f.read(), version)


packages = find_packages("src")

install_requires = [
    lib.strip() for lib in open(f"{PATH['root']}/requirements.txt").readlines()
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
