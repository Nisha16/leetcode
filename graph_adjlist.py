from collections import defaultdict
import pprint

class Graph(object):

	def __init__ (self, connections, directed = False):
		self._graph = defaultdict(set)
		self._directed = directed
		self.add_connections(connections)

	def add_connections(self, connections):
		for node1, node2 in connections:
			self.add(node1, node2)

	def add(self, node1, node2):
		self._graph[node1].add(node2)
		if not self._directed:
			self._graph[node2].add(node1)

	def remove(self, node):
		for n, cxns in self._graph.iteritems():
			try:
				print 'cxns: ', cxns
				cxns.remove(node)
			except KeyError:
				pass
		try:
			print 'node: ', self._graph[node]
			del self._graph[node]
		except KeyError:
			pass

	def isConnectedTo(self, node1, node2):
		return node1 is self._graph and node2 in self._graph[node1]

	def find_path(self, node1, node2, path = []):
		path = path + [node1]
		new_path = []
		if node1 == node2:
			return path
		if node1 not in self._graph:
			return None
		for node in self._graph[node1]:
			if node not in path:
				new_path = self.find_path(node, node2, path)
			if new_path:
				return new_path
		return None
		
	# def __str__(self):
	# 	return '{}({})'.format(self.__class__.__name__, dict(self._graph))

	def find_all_paths(self, start, end, path = []):
		path = path + [start]
		num_paths = []
		#new_path = []
		if start == end:
			return [path]
		if start not in self._graph:
			return []
		for node in self._graph[start]:
			if node not in path:
				new_path = self.find_all_paths(node, end, path)
				#print "new path: ", new_path
				for paths in new_path:
					num_paths.append(paths)
		return num_paths

	def find_shortest_path(self, start, end, path = []):
		path = path + [start]
		shortest = None
		if start == end:
			return [path]
		if start not in self._graph:
			return []
		for node in self._graph[start]:
			if node not in path:
				new_path = self.find_shortest_path(node, end, path)

				if not shortest or len(new_path) < len(shortest):
					shortest = new_path
		return shortest	

	def DFS_iterative(self, start):
		visited, stack = set(), [start]
		while stack:
			vertex = stack.pop()
			if vertex not in visited:
				visited.add(vertex)
				stack.extend(self._graph[vertex] - visited)
				print "stack:", stack
		return visited

	def DFS_recursive(self, start, visited=None):
		if not visited:
			visited = set()
		visited.add(start)
		for next in self._graph[start] - visited:
			self.DFS_recursive(next, visited)
		return visited

	def DFS_paths_iterative(self, start, end):
		stack = [(start, [start])]
		while stack:
			(vertex, path) = stack.pop()
			for next in self._graph[vertex] - set(path):
				if next == end:
					yield path + [next]
				else:
					stack.append((next, path + [next]))

	def DFS_paths_recursive(self, start, end, path=None):
		if path is None:
			path = [start]
		if start == end:
			yield path
		for next in self._graph[start] - set(path):
			yield self.DFS_paths_recursive(next, end, path + [next])
	
	def BFS_iterative(self, start):
		visited, queue = set(), [start]
		while queue:
			vertex = queue.pop(0)
			if vertex not in visited:
				visited.add(vertex)
				queue.extend(self._graph[vertex] - visited)
		return visited
		
	def BFS_paths(self, start, end):
		queue = [(start, [start])]
		while queue:
			(vertex, path) = queue.pop(0)
			for next in self._graph[vertex] - set(path):
				if next == end:
					yield path + [next]
				else:
					queue.append((next, path + [next]))	

#cycle in directd graph	
def cycle_directed(G):
	color = { u : "white" for u in G  }
	found_cycle = [False]

	for u in G:
		if color[u] == "white":
			dfs_visit(G, u, color, found_cycle)
		if found_cycle[0]:
			break

	return found_cycle[0]

def dfs_visit(G, u, color, found_cycle):
	if found_cycle[0]:
		return
	color[u] = "gray"
	for v in G[u]:
		if color[v] == "gray":
			found_cycle[0] = True
			return
		if color[v] == "white":
			dfs_visit(G, v, color, found_cycle)
	color[u] = "black"
	

graph1 = { 0 : [1, 2],
           1 : [],
           2 : [3],
           3 : [4],
           4 : [2] }

# assert(cycle_directed(graph1) == True)
# print("Graph1 has a cycle.")           

#cycle in undirected graph

def cycle_undirected(G):
	marked = { u : False for u in G }     # - All nodes are initially unmarked.
	found_cycle = [False]

	for u in G:
		if not marked[u]:
			dfs_visit(G, u, found_cycle, u, marked)
		if found_cycle[0]:
			break
	return found_cycle[0]
	
def dfs_visit(G, u, found_cycle, pred_node, marked):
	if found_cycle[0]:     # - Stop dfs if cycle is found.
		return
	marked[u] = True       # - Mark node.
	for v in G[u]:         # - Check neighbors, where G[u] is the adjacency list of u.
		if marked[v] and v != pred_node:  # - If neighbor is marked and not predecessor,
			found_cycle[0] = True         # then a cycle exists.
			return
		if not marked[v]:                 # - Call dfs_visit recursively.
			dfs_visit(G, v, found_cycle, u, marked)

graph1 = { 0 : [1, 2],
           1 : [0, 2],
           2 : [0, 1] }

try:
	assert(cycle_undirected(graph1) == False)
except:
	print "Cycle is found"

#print("Graph1 has a cycle.")           				


connections = [('A', 'B'), ('B', 'C'), ('B', 'D'),('C', 'D'), ('E', 'F'), ('F', 'C')]

g = Graph(connections, directed=False)
# # print (g._graph)
# pprint.pprint(dict(g._graph))
# print 'after removing A'
# #g.remove('A')
# pprint.pprint(dict(g._graph))
# g.add('G', 'B')
# print "adding G and B"
# pprint.pprint(dict(g._graph))
# print "finding path"
# print g.find_shortest_path('G', 'E')
print "DFS iterative"
print g.DFS_iterative('C')
# print "DFS recursive"
# print g.DFS_recursive('C')

# print "DFS path"
# #print list(g.DFS_paths('A', 'F'))


# g = Graph(connections)

# pprint.pprint (g._graph)																				