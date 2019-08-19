# Learn how to create a setup file
# Similarly how java ships as a .jar file , python ships either as a .tar.gz file or .whl file

import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name='real_python_client',
    # ignore test files for packaging
    packages=setuptools.find_packages(exclude=['t', 't.*']),
    version= '1.0.0',
    description='real_python_client',
    author='your name',
    author_email='your_own@email.com',
    url='git url of this project',
    classifiers=[],
    package_data={
    },
    install_requires=requirements
)
