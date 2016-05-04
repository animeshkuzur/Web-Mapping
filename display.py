import networkx as nx
import matplotlib.pyplot as plt
import MySQLdb

def add_nodes():
	nodes = set()
	conn = MySQLdb.connect("localhost","root","password","database")
	c = conn.cursor()
	r = c.execute("""SELECT id FROM dump""")
	for row in c.fetchall():
    		nodes.add(row[0])

	c.close()
	return nodes

def add_edges():
	edges = set()
	conn = MySQLdb.connect("localhost","root","anni99K","xyz")
	c = conn.cursor()
	r = c.execute("""SELECT id,from_url FROM dump""")
	for row in c.fetchall():
    		edges.add((row[0],row[1]))

	c.close()
	return edges

nodes_set=add_nodes()
x=0
for x in nodes_set:
	x+=1
print "Number of vertices: "+str(x)
edges_set=add_edges()
y=0
for a in edges_set:
	y+=1
print "Number of edges: "+str(y)
#for each in nodes_set:
#	print each
G=nx.Graph()
G.add_nodes_from(nodes_set)
G.add_node(0)
G.add_edges_from(edges_set)

graph_pos=nx.random_layout(G)

plt.figure(figsize=(20,20))
nx.draw(G,graph_pos,with_labels=True,node_size=70,font_size=14)
plt.savefig("graph3.png")
plt.show()
flag=True
while flag==True:
	print "\n\t=============================MENU=============================\n"
	print "\tPress[1] to calculate the number of clicks to a particular Node\n"
	print "\tPress[2] to check if two given nodes are connect\n"
	print "\tPress[3] to quit"
	print "\n\t==============================================================\n"

	n=input("\nEnter your selection: ")
	if n == 1:
		node = input("\nEnter the id of the Node: ")
		for path in nx.all_simple_paths(G, source=0,target=node):
			print path
			for clicks in path:
				clicks+=1
			print str(clicks-1)+" Clicks\n"
			clicks=0
	elif n ==2:
		node1 = input("\nEnter first node: ")
		node2 = input("\nEnter second node: ")
		for path in nx.all_simple_paths(G, source=node1,target=node2):
			if path:
				print "\nThe two nodes are connected"
				print path
			else:
				print "\nNot connected"
	elif n ==3:
		flag = False
	else:
		print "\nEnter a valid input"
