
from graph import Graph 
from Queue import Queue
def buildGraph(wordFile):
	d ={}
	g = Graph()
	wfile = open(wordFile, 'r')
	for line in wfile:
		word = line[:-1]
		#print 'word' + '=' + ' ' + word
		for i in range(len(word)):
			list = word[:i] + '_' + word[i+1:]
			#print 'bucket' + '=' + ' ' + bucket
			if list1 in d:
				d[list].append(word)
				#print 'ddddddd' + '==' + word
			else:
				d[list] = [word]
				#print 'else' + '==' + word
	for list in d.keys():
		#print d.keys()
		#print bucket + 'bucket'
		for word1 in d[list]:
			#print 'word1' + word1
			for word2 in d[list]:
				#print 'word2' + word2
				if word1 != word2:
					g.addEdge(word1,word2)
	return g

def BFS(graph,start,target):
	queue = Queue()
	temp_path = [start]
	queue.enqueue(temp_path)
	while queue.isEmpty() == False:
		in_path = queue.dequeue()
		last_node = in_path[len(in_path)-1]
		print in_path
		if last_node == target:
			print "VALID_PATH : ",in_path
		#for link_node in graph[last_node]:
		for link_node in graph.getVert(last_node):
			if link_node not in in_path:
				new_path = []
				new_path = in_path + [link_node]
				queue.enqueue(new_path)
start = 'TOON'
target = 'PLEA'

graph = buildGraph('test.txt')
#print graph.getVertices()
print graph.getVert('SAGE')
print BFS(graph,start,target)

#def short_path()



