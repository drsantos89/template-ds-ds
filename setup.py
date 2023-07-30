"""Setup file for <templateds>."""
from setuptools import find_packages, setup

VERSION = "0.0.0"

DESCRIPTION = "My template for data science projects"

with open("requirements.txt") as f:
    required = f.read().splitlines()

with open("requirements-dev.txt") as f:
    required_dev = f.read().splitlines()
    
setup(
    name="templateds",
    version=VERSION,
    description=DESCRIPTION,
    author="Diogo Santos",
    author_email="drsantos989@gmail.com",
    packages=find_packages("./src"),
    package_dir={"": "src"},
    package_data={"templateds": ["py.typed"]},
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=required,
    extras_require={"dev": required_dev},
)
