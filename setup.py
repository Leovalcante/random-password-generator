from setuptools import setup, find_packages
from random_password_generator import name, version, description, url

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=name,
    version=version,
    url=url,
    license="MIT",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Valerio Preti",
    author_email="valerio.preti.rpg@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click>=7.0",
        "requests>=2.0"
    ],
    python_requires=">=3.7",
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