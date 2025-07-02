from setuptools import setup, find_packages

setup(
    name="codesdbsn",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "flask==3.0.0",
        "pytest==7.4.3",
        "black==23.11.0",
        "pytest-cov==4.1.0"
    ],
    author="SDBSN",
    description="Projet SDBSN",
    url="https://github.com/sdbsn/codesdbsn",
)
