'''
    The setup.py file is an essential part of packaging and
    distributing python projects.It is used by setup tools
    (or diistutils in older python versions) to define the configuration
    of your project,such as its metadata,dependencies, and more
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
        This functionwill return list of requirements
    '''
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #readLines from the file
            lines=file.readlines()
            #Process each line
            for line in lines:
                requirement=line.strip()
                #ignore the empty lines and -e.
                if requirement and requirement !='-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_list

setup(
    name='Network security',
    version='0.0.1',
    author='Sravani',
    author_email='example@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)