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
    name='ml_project_1',  # Use underscores instead of spaces
    version='0.1.0',
    author='Anas Asghar',
    author_email='your@email.com',  # Add email
    description='Machine Learning Project 1 Package',
    long_description=open('README.md').read(),  # Add long description
    long_description_content_type='text/markdown',
    url='https://github.com/AnsAsghar/ML-Project-1',  # Add project URL
    packages=find_packages(
        where='src',  # Specify the source directory
        include=['*'],  # Include all packages
        exclude=[]  # Exclude non-package directories if needed
    ),
    package_dir={'': 'src'},  # Tell setuptools where to find packages
    install_requires=get_requirements('requirements.txt'),
    python_requires='>=3.7',  # Specify Python version requirements
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords='machine-learning ml',  # Add relevant keywords
)