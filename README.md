# Bill processing project  
Two endpoints have been created. List of all bill with filtering and uploading of lists of bills in csv format.  

## Getting Started  
The first thing to do is to clone the repository:  

```sh
$ git clone https://github.com/polina-koval/bill_processing.git 
$ cd bill_processing
```  

Create a virtual environment to install dependencies in and activate it:  

```sh
$ virtualenv venv  
$ source venv/bin/activate
```

Then install the dependencies:  

```sh
(venv)$ pip install -r requirements.txt
```  

There is a file in the repo ".env.example", this file for use in local development. Duplicate this file as .env in the root of the project and update the environment variable SECRET_KEY.  

```sh
$ cp .env.example .env
```

Once pip has finished downloading the dependencies and the variable is updated:  
 
```sh
(venv)$ python manage.py runserver
```  

Navigate to `http://127.0.0.1:8000/api` to the API.  
`http://127.0.0.1:8000/api/bills` - list of existing bills
`http://127.0.0.1:8000/api/upload-bill` - upload csv file with bills.
If the bills are valid, then all of them will be stored in the database.

## Built with   
- Django  
- Django Rest Framework