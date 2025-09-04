from setuptools import setup, find_packages

setup(
    name="db_helper_library",
    version="0.1.0",
    description="A helper library for testers (DB, API, Selenium utils)",
    author="Manesh Kadam",
    packages=find_packages(),
    install_requires=[
        "mysql-connector-python",
        "requests"
    ],
)
