from setuptools import setup,find_packages

project_name = "US_VISA_APPROVAL_PREDICTOR"
HYPHEN_E_DOT="-e ."
author_name = "Linkan Kumar Sahu"
__version__ = "0.0.1"

def get_requirements(file_path="requirements.txt"):
    with open(file_path,'r') as file:
        requirements=file.readlines()
        requirements=[ r.replace('\n','') for r in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        return requirements
        
        
def get_long_description(file_path="README.md"):
    """"
    argument : file path for description of the project
    returns : returns the file content 
    
    """
    with open(file_path,'r') as file:
        content=file.read()
        return content

setup(
    name=project_name,
    version=__version__,
    author=author_name,
    author_email="sahulinkan7@gmail.com",
    long_description= get_long_description(),
    packages=find_packages(),
    install_requires=get_requirements()
)