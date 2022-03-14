# crm Package

The objective of crm Package is build a private Python Package for development purpose

## Deployment

This Project is deployed to a private pypi server.  
[Private Server Link](https://pypi.miadvg.com)  
Have the .pyrc file in the project root before deployment.  

Deployed using [Twine](https://twine.readthedocs.io/en/latest/)  
To Deploy it to the server use the commands below.  

```
python setup.py sdist bdist_wheel
```

```
twine upload -r local dist/* --skip-existing
```

To check the Package is Build correctly by this command before deploying

```
twine check dist/*
```

This will show you the available or previously built packages

## Installation as a Package
To Install this package into your project 

```
pip install --extra-index-url https://pypi.miadvg.com crm-python-sdk
```

After successful installation, to set up the configuration simply type  
```crm```  
in your terminal and give your authentications asked in the terminal prompt.

## Documentation
Get the Package Documentation at  
[click here](http://logics-sdk-doc.miadvg.com)

## Built With

* [Python](https://www.python.org/) - Language Used
* [Requests](https://requests.readthedocs.io/en/stable/) - Library for HTTP requests
* [Psycopg](https://www.psycopg.org/docs/) - PostgreSQL Database Adapter for Python


### Folder Structure

```
crm_pack/                 # Root Folder
|- config.py            # File that consists settings
|- base/                # Root application module that consists base module file
|- service/             # Utility folder
    |- case 
    |- file 
    ..
    ..
|- .gitignore/          # gitignore folder
```
