import requests
from bs4 import BeautifulSoup
import re
import MySQLdb
import sys

def query(query):

	url = "https://www.bing.com/search?q="
	for x in query:
		url = url+x+"+"
	url=url[0:-1]
	url=url+"&first=00"
	return url

def search(url):
	result=[]
	try:
		response_code = requests.get(url)
		print response_code.status_code
		if response_code.status_code == 200:
			html = response_code.text
			tags = BeautifulSoup(html,"lxml")
			for hs in tags.findAll('li',attrs={'class':'b_algo'}):
				links = hs.find('h2').find('a')
				result.append(links['href'])			
	except requests.ConnectionError:
		print "no internet connection"
	finally:
		return result

def crawl(list_q,id_no):

	try:
			z=add_to_db(list_q,id_no)
			response_code = requests.get(list_q)
			print response_code.status_code
			if response_code.status_code == 200:
				html = response_code.text
				tags = BeautifulSoup(html,"lxml")
				flag = 0
				for ac in tags.findAll('a', attrs={'href':re.compile("^http")}):
					global crawled
					global id_from
					#print '\n-------------------------------------------------------------------------------\n'
					#print crawled
					#print '\n-------------------------------------------------------------------------------\n'
					
					if ac['href'] not in crawled:
						if parse(ac['href']):
							print 'added: '+ac['href']
							crawled.add(ac['href'])
							#id_no=id_from
							crawl(ac['href'],z)
						else:
							print 'not added: '+ac['href']
							crawled.add(ac['href'])

	except requests.ConnectionError:
		print "no internet connection"
	finally:
		pass
		
def parse(url):
	flag =0
	c = False
	if '?' not in url:
		if '#' not in url:
			rsp_cd = requests.get(url)
			if rsp_cd.status_code == 200:
				lnk_html = rsp_cd.text
				lnk_tags = BeautifulSoup(lnk_html,"lxml")
				for script in lnk_tags(["script", "style"]):
   						script.extract()
   				text = lnk_tags.get_text()
   				text = text.encode('utf-8')
   				txt_set = text.split(' ')
				#print txt_set
				global q
				for txt_a in q:
					for txt_b in txt_set:
						if txt_a.lower() == txt_b.lower():
							flag=flag+1
				global l_q
				if l_q<=flag:
					c = True
				else:
					c= False
	return c

def add_to_db(url,from_url):
	global id_next
	global id_from
	try:
		conn = MySQLdb.connect("localhost","root","password","database")
		c = conn.cursor()
		c.execute("""INSERT INTO dump (id,url,from_url,urlsha1) VALUES (%s,%s,%s,SHA1(%s))""",(id_next,url,from_url,url))
		conn.commit()
		c.close()
		id_from=id_next
		id_next+=1
	except:
		pass
	return id_from

id_next=1
id_from=0
crawled=set()
q = sys.argv[1:]
l_q = len(q)
url = query(sys.argv[1:])
print url
y=search(url)
for x in y:
	print "crawling: "+x
	#add_to_db(x,0)
	id_from=0
	crawl(x,id_from)
