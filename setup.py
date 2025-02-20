from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e'
def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns a list of requirements
    '''
    requirements = []
    
    with open(file_path) as file_obj:
        for line in file_obj:
            line = line.strip()
            
            # Filter out empty lines and comments
            if not line or line.startswith('#'):
                continue
                
            # Handle -e . for editable installs (special case)
            if line.startswith('-e'):
                continue
                
            requirements.append(line)

            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='ml_project_1',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'flask',
        'pymysql',
        'python-dotenv',
        'scikit-learn'
    ]
)