## PROJECT DOCUMENTATAION GOES HERE

### SETUP

###### DEV

- conda create -n rpc python=3.7
- activate rpc
- pip install -r requirements/dev.txt

###### PROD

- conda create -n rpc python=3.7
- activate rpc
- pip install -r requirements.txt


### USAGE INSTRUCTIONS


### BUILD
- python setup.py bdist_wheel sdist

### TEST
- pytest

### COVERAGE
- coverage run real_python_client/api.py
- coverage html