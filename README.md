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


### OBJECTIVE 
After finishing this project build file should be "real_python_client-1.0.0-py3-none-any.whl"
And we should be able to use below commands
> activate rpc
> pip install dist/real_python_client-1.0.0-py3-none-any.whl
> python
> from real_python_client.api import ReqresClient
> print(ReqresClient().list_users(page=2))
> print(ReqresClient().single_user(id=2))
> print(ReqresClient().single_user(id=23))

