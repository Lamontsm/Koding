#!flask/bin/python
2	from app import app
3	import os
4	
5	app.run(debug = False,
6	        host = os.getenv('IP', '0.0.0.0'), 
7	        port = int(os.getenv('PORT', 8080))
8	        )