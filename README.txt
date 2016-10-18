## Purpose

We would like you to develop a simple application called “The battle of the hashtags”.

The application should allow an administrator to create ‘battles’ between two hashtags, comparing the number of typos in tweets tagged with them. 

A programmatic and automated approach should be used to fetch tweets from the hashtags in question, on a periodic basis.

After a predetermined amount of time, the winning hashtag will be the one with the smallest total number of typos.

The technical requirements are as follows:

Python and Django should be used
Data should be persisted in an SQL based datastore
Security aspects should be taken into consideration
Delivery needs to happen through a git repository with run instructions

The functional requirements are as follows:

As an admin, I should be able to use a CRUD to configure battles (Create, Read, Update, Delete) 
As an admin, I should be able to specify how long a battle will run for, with start and end date times (please use a datepicker)
As an admin, I should be able to login/logout

There is no frontend required for this exercise, however, an API endpoint should be exposed to return the current result for a specific battle id, in JSON format. It should return the battle name, start and end date times, the hashtags and their number of typos and which one is the winner at that moment.

As a developer we realise how busy you must be, but if you do get some time and want to take things further, here are some suggestions to enhance the app:

Use docker images
Use different comparison parameters to define victory (longer tweets, most frequent, etc)
Build a simple frontend
Extend the API to also allow battles to be created with a POST request
Anything else you can think of that would benefit this app

## Reference

http://www.arruda.blog.br/programacao/django-celery-in-daemon/

http://fat-controller.sourceforge.net/index.html

http://www.celeryproject.org/

https://pypi.python.org/pypi/django-celery

http://www.bogotobogo.com/python/Multithread/python_multithreading_Daemon_join_method_threads.php

https://docs.python.org/2/library/threading.html#thread-objects

## Features of the project

Admin page with Django
	Login / Logout
	CRUD of battles

RESTful API endpoints with DRF (Django REST Framework) 
	All result is JSON
	Login / Logout
	CRUD of battles

API Documentations with Swagger

Security Management through permission management in GUI and API

Automatic and periodic retrieval of tweets using tweepy

Data storage using Sqlite
	If you want, postgresql, mysql are also possible.

Multiple compare criteria
	Number of typos
	Longer tweets
	More frequent tweets

## How to use

Set up environment
	pip install -r requirements.txt
	(recommend use virtual environment)

Run the project
	python manage.py runserver 8000

Through the browser as an admin
	Go to http://localhost:8000/admin and use credential root/newfirst as an admin
	You can CRUD of battles there.

For api
	On the browser go to http://localhost:8000 (or http://127.0.0.1/api-auth/login/) and login using credential (root/newfirst) as an admin and CRUD of battles there through RESTful API

	After login, you can go to 	http://localhost:8000/docs and browse APIs with nice swagger docs.

	You can also use curl or httpie to check RESTful APIs
		Retrieve all battles:
			curl -H "Accept: application/json" -H "Content-type: application/json" -X GET http://localhost:8000/battle/|json_pp
		Retrieve specific battle:
			curl -H "Accept: application/json" -H "Content-type: application/json" -X GET http://localhost:8000/battle/1/|json_pp
		Create a battle:
			curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -u root:newfirst -d '{"name":"REST test battle", "tag1":"happy", "tag2": "car", "start_time":"2016-05-30 12:20:33", "end_time":"2016-05-31 02:26:33"}' http://localhost:8000/battle/|json_pp
		Delete a battle:
			curl -H "Accept: application/json" -H "Content-type: application/json" -X DELETE -u root:newfirst http://localhost:8000/battle/4/|json_pp

	* Now it is using username/password credential for authentication. If you want token authentication is also possible.
	* I allowed only GET, POST, HEAD, DELETE methods after analysing the project. (If you want, I can implement all.)
	* json_pp is just for formatting JSON.
	* In Retrieval and deletion use appropriate battle id in url.

* Be careful with timezone!

## Deploy:

	This can be deployed on any server using fabric with minor configuration.
	

