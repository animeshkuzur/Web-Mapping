# Web-Mapping
There were two programs which we used to complete this project. First one (`main2.py`), created in
Python was a web crawler used to record the web links continuosly following one link to
another and recording them in a database, based on a given search term/phrase. The other
program (`display.py`) also created in Python was then used to map the recorded data into a network graph and thus produce the
final output. The search engine used was ‘Bing’.

####Prerequisite Python Modules
* MySQLdb
* BeautifulSoup
* Networkx
* Matplotlib
* Requests

####Instructions
Before executing the python scripts, create a database named `dump` with the following attributes
`CREATE TABLE dump (id INT,url VARCHAR(1000),from_url INT,urlsha1 CHAR(40))`

The first program takes input as Command Line Arguments
`main2.py <query string>`

Run `dispaly.py` after/during the execution of `main2.py`
####Output
![picture alt](https://raw.githubusercontent.com/animeshkuzur/Web-Mapping/master/graph.png "A Network Graph on the term 'Donald Trump'")

