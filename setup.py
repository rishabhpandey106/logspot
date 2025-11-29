from setuptools import setup, find_packages

setup(
    name="logspot",
    version="0.1.0",
    description="Reusable /logs route for Flask apps",
    packages=find_packages(),
    install_requires=[
        "Flask>=2.0.0",
    ],
)
