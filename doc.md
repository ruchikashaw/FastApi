# for installing python virtualenv 
pip3 install virtualenv

# for making a virtualenv in a project
python3 -m venv (name of the env) - generally it is kept as env 

# for running a python file 
python3 filename

# for activating an environment
source env/bin/activate
        
# for listing all packages which are installed 
pip freeze

# for installing any package in the project
pip3 install package name

# for installing all the requirements
pip3 install -r requirements.txt

# for writing the dependencies in the requirements.txt
pip3 freeze > requirements.txt 

# This is what you would probably do once you want to deploy your application to production:

pip install fastapi

# Also install uvicorn to work as the server:

pip install "uvicorn[standard]"