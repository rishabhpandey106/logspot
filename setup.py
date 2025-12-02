from setuptools import setup, find_packages

setup(
    name="logspot",
    version="0.1.1",
    description="Reusable /logs route for Flask apps",
    url="https://github.com/rishabhpandey106/logspot",
    author="Rishabh Kumar Pandey",
    author_email="rishabhpandey230@gmail.com",
    packages=find_packages(),
    install_requires=[
        "Flask>=2.0.0",
    ],
    python_requires=">=3.6",
    keywords="flask, logs, logging, flask-logging, flask-logs, logspot",
)
