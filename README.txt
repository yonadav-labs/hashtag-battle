- Features of the project

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

- How to use
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

- Developer: Dan Thomas

