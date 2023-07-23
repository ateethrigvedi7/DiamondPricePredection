from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT='-e .'

def getRequires(filepath : str) -> List[str]:
    requirements=[]
    with open(filepath) as fileObj:
        requirements = fileObj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="Diamond price predection",
    author="Ateeth B R",
    author_email="ateeth777@gmail.com",
    install_requires=getRequires("requirements.txt"),
    version='0.0.1',
    packages=find_packages()
)