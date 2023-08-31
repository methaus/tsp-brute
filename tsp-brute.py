# Travelling Salesman Problem (TSP) 
# code from https://www.guru99.com/travelling-salesman-problem.html (ALTERED)
# access: 31/8/23

from itertools import permutations
from sys import maxsize

graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
startnode = 0

def tsp(graph, startnode):
	#array of reacheble nodes
	vertex = []
	
	#search of reacheble nodes
	for i in range(len(graph)):
		if i != startnode:
			vertex.append(i)

	min_cost = [ maxsize, -1 ]
	next_permutation = list(permutations(vertex)) #joint of all path combinations

	#calculate the cost of all path combinations
	for i in next_permutation:
		nonPathTest = None
		current_cost = 0
		lastnode = startnode

		#calculate the cost jump to jump
		for j in i:
			if graph[lastnode][j] == -1: #if -1 have not a path
				nonPathTest = True
				break
			else:
				current_cost += graph[lastnode][j]
				lastnode = j

		if nonPathTest == True:
			print("-1")
			continue

		current_cost += graph[lastnode][startnode]

		#calculate if its the better
		if min_cost[0] > current_cost and current_cost != 0:
			min_cost[0] = current_cost
			min_cost[1] = i

	if min_cost[1] == -1:
		return "not hamiltonian graph"
	else:
		return "better path costs {}, for path {}".format(min_cost[0], min_cost[1])

print(tsp(graph, startnode))