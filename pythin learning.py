"""my_list  = [4,6,9,8,4,5,6,7,8,9]
print (my_list[2:5])
for i in range(len(my_list)):
    print (my_list[i] % 3)
"""
"""
#list reverse
listo = [1,2,3,4]
print(listo[::-1])
"""
"""
#even odd print
list =[0,1,2,3,4,5,6,7,8,9]
print(f'odd:{list[0::2]}' )
print(f'even:{list[1::2]}')

"""
"""
listo = [1,3,5,7,9]
losti = [0,2,4,6,8]

for i in range(len(losti)):
    listo.append(losti[i])
listo.sort()
print(listo)
"""
"""
sample_dict = {
"name": "Kelly",
"age": 25,
"salary": 8000,
"city": "New york"}
# Keys to extract
keys = ["age", "salary"]

dict = {}

for item in keys:
    dict[item] = sample_dict[item]

print(dict)
"""

graph = {
    "6" : [4],
    "4" : [3,5],
    "3" : [2,4],
    "5" : [2,4,1],
    "2" : [1,3,5],
    "1" : [5,2]
}

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = str(queue.pop(0))
        print(m, end = " ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)



bfs(visited, graph, "6")
