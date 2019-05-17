# django_rest_api_basic
Basic working with django rest api

Start by creating a python environment in current location

>virtualenv env

Then activate the environment 

>env\Scripts\activate

Install all the dependencies from requirement file requirements.txt

>pip install -r requirements.txt

Ready to go now-----------------------------

>python manage.py runserver

(if everything works fine, as it will)

Go to browser and open the link - http://127.0.0.1:8000/users/

POST for imputing new data to table
GET for getting all the data from the table

Then according to the input visit - http://127.0.0.1:8000/users/1/   or  http://127.0.0.1:8000/users/2/

There you will get two more option to PUT and DELETE for that specific entry in the table
PUT for updating the current showing data
Delete for deleting the current showing data 

For updating the parameters modify accordingly in the models.py and serializers.py

Thats all for this project. Feel free to raise any query
