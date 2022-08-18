#phone = {'jimmy' : '08723456', 'jakub' : '69hotline', 'bar' : '456viper higs345'}
#
#
#def ez(name):
#	try:
#		return phone[name]
#	except KeyError:
#		return None
#
#print(ez('jimmy'))
#print(ez('sal'))
#print(phone.keys())
#print(phone.values())
#print(phone.items())

#for (k, v) in phone.items():
#	print(f'{k} =====> {v}')
#
#print('cats' < 'dogs')
#
#lis = ['yuppa', 'lovely_cans', 'the_sesh<3']


"""
def celsius2fahrenheit(c):
    fahr = (c * 1.8) + 32
    return fahr
    #print(f'that is {fahr:.1f} degreese in fahrenheit')


celsius = 21
fahr = celsius2fahrenheit(celsius)
print(f'that is {fahr:.1f} degreese in fahrenheit')
#help(celsius2fahrenheit)
"""

"""
from re import findall

s = 'Yahoooo!'
p = r'Yaho*!'
print(findall(p, s))
"""
"""
class Time(object):  
    
    def set_time(time_object, hour, min, sec):
        time_object.hour = hour
        time_object.min = min
        time_object.sec = sec

    def show_time(time_object):
        print('{:02d}:{:02d}:{:02d}'.format(time_object.hour, time_object.min, time_object.sec))


a = Time()
Time.set_time(a, 9, 12, 6)
print(a.hour)
print(a.min)
print(a.sec)

print(a.show_time())
"""
"""
import sys


calc_memory = {}

def assign(item):
    if line[0] == 'def':
        calc_memory[line[1]] = int(line[2])

calc_memory_rev = {v: k for k, v in calc_memory.items()}

for line in sys.stdin:
    line = line.strip().split()
    assign(line)
    try:
        if line[0] == 'calc':
            math = line[1:]
            total = calc_memory[math[0]]
            for i in range(len(math)):
                if math[i] == '-':
                    total = total - calc_memory[math[i + 1]]
                if math[i] == '+':
                    total = total + calc_memory[math[i + 1]]
            print(" ".join(math), total)
    except KeyError:
        print(" ".join(math), "unknown")
        """
"""
class Score(object):
    
        def __init__(self, goals=0, points=0):
            self.goals = goals
            self.points = points


        def __str__(self):
           return f'{self.goals}\n {self.points}\n {self.goals is self.points}'    

        def __eq__(self, other):
            return ((self.goals, self.points) == (other.goals, other.points))


print(f'yes\nno')
"""
"""
def __add__(self, other):
    r = self.radius + other.radius
    c = self.centre.midpoint(other.centre)
    return Circle(c, r)
"""
class Graph(object):

    def __init__(self, V):
        self.V = V
        self.adj = {}
        for v in range(self.V):
            self.adj[v] = list()

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def degreee(self, v):
        return len(self.adj[v])

    def maxDegree(self):
        return max([self.degreee(v) for v in range(self.V)])
        
    def avgDegree(self):
        return sum([self.degreee(v) for v in range(self.V)]) / self.V

class BFSPaths(object):

    def __init__(self, g, s):
        self.s = s
        self.g = g
        self.marked = [False] * g.V
        self.parent = [False] * g.V
        self.bfs(s)

    def bfs(self, s):
        queue = [s]
        self.marked[s] = True
        while queue:
            v = queue.pop(0)
            for w in self.g.adj[v]:
                if not self.marked[w]:
                    queue.append(w)
                    self.marked[w] = True
                    self.parent[w] = v

    def hasPathTo(self, v):
        return self.marked[v]

    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None
        path = [v]
        while v != self.s:
            v = self.parent[v]
            path.append(v)
        return path[::-1]


with open('graph01.txt') as f:

   V = int(f.readline())

   g = Graph(V)

   for line in f:

       v, w = [int(t) for t in line.strip().split()]
       g.addEdge(v, w)
       print(v, w)


   paths = BFSPaths(g, 2)

   print(paths.hasPathTo(6))

   print(paths.pathTo(3))


