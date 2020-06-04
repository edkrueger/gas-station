# gas-station

## Setup (Viewer)
Install pipenv `pip install pipenv`.  
Run `pipenv install` to install the env.  
Run `pipenv shell` to activate.
Run `python -m ipykernel install --user --name gas-station --display-name gas-station` to install the jupyter kernel. 

## Setup (Contributor)
Due to a pipenv issue, you may have to run `pipenv install --dev pre-commit black pylint`, if the development dependencies don't install.      
Run `pipenv run pre-commit install` to initialize the git hooks.  
Run `pipenv run pre-commit run --all-files` if there are file that were committed before adding the git hooks.  
