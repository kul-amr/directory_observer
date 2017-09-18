Description:
	Aim of this project is to monitor a directory on the file system for appearance of any file.
	When a file appears, it parses the file and stores the file data and success/failure outcome in sqlite db tables.
	This file observer can run all the time unsupervised, gracefully handling exceptions.
	This is capable of multi-threading if multiple files appear at the same time with a way to control the maximum number of threads that can run.

Assumptions: 
	1. File types - 
		CSV
		txt - json data
			- tab seprated data
			- comma seprated data
		If some other file of different type is added then it will not be parsed and error with message "Unknown file type" will be logged in logs table. 	
	2. These files will have users data - name and email which I need to parse.
	3. Storing the parsed data and parsing success/failure in sqlite database in tables users and parsed_files respectively.		 
	4. In case there is any error for processing any of the record for a file, then no data from that perticular file will be added to database. Error message will be logged.
	5. To check if data is getting added , I have created 2 web pages - users and logs.
		users - will display total number of users and top 100 users order by craeted_date desc
		logs - will display total number of parsed filesentry and all related details ex. filename, success/error message etc
	6. As soon as files are created, those will be added to queue and would be assigned to threads (I am currently using 5 threads)
	
Flow:	
1. run.py	:	will start the web app and will create sqlite database named harness.db and the tables
2. harness_monitor.py	:	is the script which will monitor the folder for new files. This will prompt for directory to monitor. ex. path for monitor folder from current structure
3. data folder :  This has few sample csv and txt files (with json data, comma separated data and tab separated data).One file (comdeltxt1.txt) with error induced(-one extra blank line).
				  These files can be added to monitor folder
4. create_data.py :	can create csv files for load testing.	
					This will prompt for inputs :	
												dircetory to create files ex. monitor directory which is getting monitored for new file addition
												number of records in each file
												number of files to create

5. To monitor the data creation in database, you can use users and logs webpage with date range as input.
	ex.	http://localhost:5000/logs?start_date=2017-09-17&end_date=2017-09-19 
		http://localhost:5000/users?start_date=2017-09-17&end_date=2017-09-19
