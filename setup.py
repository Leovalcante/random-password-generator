from setuptools import setup, find_packages
from random_password_generator import __name__, __version__, __description__, __url__

setup(
    name=__name__,
    version=__version__,
    description=__description__,
    url=__url__,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        rpg=random_password_generator.rpg:rpg
    """
)
