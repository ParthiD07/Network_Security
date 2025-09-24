'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''
from setuptools import find_packages # find_packages: Automatically detects all Python packages (folders with __init__.py) in your project. Saves you from manually listing them.
from setuptools import setup # setup: The main function that defines your package metadata and installation instructions.
from typing import List # Used for type hinting — tells readers (and tools like linters) that the function returns a list of strings (List[str]).

# Defines a function that reads dependencies from requirements.txt.
def get_requirements()->List[str]: # The return type is a list of strings, each string being a package name.
    """This function will return list of requirements"""
    # Initializes an empty list to store package requirements.
    requirement_lst:List[str]=[]
    try:
        with open("requirements.txt","r") as file:
            # Read lines from file
            lines=file.readlines()
            # process each line
            for line in lines:
                requirement=line.strip()
                # ignore empty line and -e .
                if requirement and requirement!="-e .": # This checks whether the variable requirement is not empty and not contains "-e ."
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt not found")

    return requirement_lst

setup(
    name="Network_security", # The name of your package (how it will be installed with pip install network-security if published).
    version="0.0.1",
    author="Parthiban D",
    author_email="parthiband2020@gmail.com",
    packages=find_packages(), # Automatically includes all Python packages (folders with __init__.py) inside your project directory.
    install_requires=get_requirements(), # Instead of hardcoding them, it calls get_requirements() to read from requirements.txt.

)
