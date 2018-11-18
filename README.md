# Logs Analysis Project 
-----
Logs Analysis project is part of Udacity Full Stack Nano-degree. The aim of this project is to create an internal reporting tool using Python and SQL skills learned in the course and output the result in a text file based on the information from the database in order to discover what kind of articles the site's readers like. The database contains newspaper articles, authors' info, as well as the web server log for the site, which contains a database row for each time a reader loaded a web page. 

## Project Files:
 
* newsdata.py: conatins the python code that uses psycopg2 python module to connect to database, run the SQL queries and fetch data from database
* newsdata.sql: contains the sql command to create the News database and its related tables (authors, log, articles)
* README.md: readme file contains description about the project 
* output.txt: text file contains the output result of the newsdata.py file

 
## How to Run the Project: 
* cd to the downloaded folder directory 
* run `vagrant up` to bring the virtual machine online 
* run `vagrant ssh` to log into the virtual machine 
* type `cd /vagrant` to change directory into vagrant directory 
* use the command `psql -d news -f newsdata.sql` to load the data 
* connect to the database using `psql -d news` 
* create the [Views](#views), as shown below in the Views section  
* run the command `python newsdata.py` 


## Views 
* Create totalViewCount

`create view totalViewCount as
select date(time), count(status) as views
from log 
group by date(time)
order by date(time);`

* Create errorViewCount

`create view errorViewCount as
select date(time), COUNT(status) as errors
from log where status = '404 NOT FOUND' 
group by date(time) 
order by date(time);`

* Create failedRequestsRate 

`create view failedRequestsRate as
select totalViewCount.date as date, (100.0*errorViewCount.errors/totalViewCount.views) as percentage
from totalViewCount, errorViewCount
where totalViewCount.date = errorViewCount.date
order by date;`



## Output 
* check the output.txt file
 






