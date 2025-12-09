from setuptools import setup, find_packages

setup(
    name="logspot",
    version="0.3.0",
    description="Reusable /logs route + logging manager for Flask and FastAPI apps",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",

    url="https://github.com/rishabhpandey106/logspot",
    author="Rishabh Kumar Pandey",
    author_email="rishabhpandey230@gmail.com",

    packages=find_packages(),

    install_requires=[
        "Flask>=2.0.0",
        "fastapi>=0.95.0",    
        "uvicorn>=0.20.0",   
        "requests>=2.0.0"      
    ],

    python_requires=">=3.8",

    keywords=[
        "flask",
        "fastapi",
        "logs",
        "logging",
        "flask-logging",
        "fastapi-logging",
        "logspot",
    ],

    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Flask",
        "Framework :: FastAPI", 
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    include_package_data=True,
)
