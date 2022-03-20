# InTime SDK

The objective of InTime SDK is to create, configure, and manage InTime services, such as Creating and Sending SMS's. 
The SDK provides an object-oriented API as well as low-level access to InTime services.

## Deployment

This Project is deployed to pypi server.  

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
pip install intime-sdk
```

## Documentation
Get the Package Documentation at  
[click here](http://njnur.github.io)

## Built With

* [Python](https://www.python.org/) - Language Used
* [Requests](https://requests.readthedocs.io/en/stable/) - Library for HTTP requests
