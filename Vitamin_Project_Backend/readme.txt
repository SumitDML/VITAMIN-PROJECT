1. Install Python 3.10.3 or higher

2. Install PgAdmin4 or Postgres on your operating system.

3. write the following command to install libraires and packages in order to run django application: 
    pip install -r requirements.txt

4.Go to /Vitamin_Project_Backend/Project_Backend/settings.py file then change the database details according to your db details. 

5.To make the migrations use:
	python manage.py makemigrations
	python manage.py migrate
	or 
	python3 manage.py makemigrations
	python3 manage.py migrate
	
6.To run the server:
	python3 manage.py runserver
	or
	python manage.py runserver
	
Default port is 8000  
 
Note: if you have multiple python version installed then make sure to use every python command and pip command 
with version specified. For e.g. pip3.10 install -r requirements.txt, python3.10 manage.py runserver


7.Project setup is completed.
