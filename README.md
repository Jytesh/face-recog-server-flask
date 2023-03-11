# Server Documentation
- Flask API server
- Two Routes
	## login
 	- Login with provided username and password
 	- Will be provided with a token
 	- Store token
		### Format
	- [ POST ] 
		- [ form ]
		- username 
		- password
	## verify
	- Submit image as file upload, and token in headers
	- Await verification
		## Format
		- [ POST ]
			- [ file ]
			- [ image.jpg ] ( name the file upload as 'image' )
			- Header: 'Token: <=TOKEN=>'
- Can use the insert.py script to insert employees
- Can use test_server.py to test the server with a test.jpg file

# App
TBD
