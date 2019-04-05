from setuptools import setup, find_packages
from random_password_generator import __name__, __version__, __description__, __url__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=__name__,
    version=__version__,
    url=__url__,
    license="MIT",
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Valerio Preti",
    author_email="valerio.preti.rpg@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click>=7.0",
    ],
    python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*",
    entry_points={
        "console_scripts": [
            "rpg = random_password_generator.rpg:rpg",
        ],
    },
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
)