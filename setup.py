import glob

from setuptools import find_packages, setup

setup(
    name="kodjin-data-gen",
    packages=find_packages(exclude=[""]),
    package_data={},
    install_requires=[
        "colorlog",
        "pyyaml",
        "jinja2",
        "fhir.resources",
        "faker",
    ],
    extras_require={
        "test": []
    },
)
