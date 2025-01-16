import collections
import heapq

'''
Traffic affects velocity
Traffic From A tO B
4 states of traffic jam From normal to worst    
'''

#Data Samples
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]] # kms

for i in range(len(edges)):
    edges[i][-1] = edges[i][-1] * 30

print(edges)


# Google Map
class Vehicle:
    def __init__(self, cat = 'car', velocity = 0):
        vehicles_velocity = {'car': 60, 'bicycle': 50, 'bike':40} # kmh
        self.cat = cat
        self.velocity = velocity
        if velocity == 0:
            self.velocity = vehicles_velocity[cat]

class Traffic:
    def __init__(self, src, dst, state = 0) -> None:
        self.src = src 
        self.dst = dst
        self.state = state
class TrafficJams:
    def __init__(self, src, dst, state) -> None:
        self.traffics = collections.defaultdict(int) # src,dst : x , x = 0 1 2 3 4
        self.traffics[src, dst] = state

class DatMap:
    def __init__(self, src = None, dst = None) -> None: 
        self.adj = collections.defaultdict(set) # src:dst, distance
        self.n = len(self.adj)
        self.vehicle = Vehicle()

        self.src = src
        self.dst = dst   


    # undirected graphs
    def connecttwoway(self, src, dst, d): # d = distance
        self.adj[src].add((dst, d))
        self.adj[dst].add((src, d))
        self.n = len(self.adj)

    def connectoneway(self, src, dst, d):
        self.adj[src].add((dst, d))
        self.n = len(self.adj)

    def construct(self, edges):
        for src, dst, d in edges:
            self.connectoneway(src, dst, d)

    # Timen to go between Source and Destination
    def FindT(self):
        if not self.src or not self.dst:return -1
        MyVehicle = self.vehicle
        minH = [[0, self.src]]
        visited = set()
        
        while minH and self.src != self.dst:
            d, cur = heapq.heappop(minH)
            if cur == self.dst:return d / MyVehicle.velocity
            if cur in visited:continue
            visited.add(cur)

            for nxt, nD in self.adj[cur]:
                heapq.heappush(minH, (nD + d, nxt))
        return -1

    def FindD(self):
        if not self.src or not self.dst:return -1
        minH = [[0, self.src]]
        visited = set()
        
        while minH and self.src != self.dst:
            d, cur = heapq.heappop(minH)
            if cur == self.dst:return d
            if cur in visited:continue
            visited.add(cur)

            for nxt, nD in self.adj[cur]:
                heapq.heappush(minH, (nD + d, nxt))
        return -1

    # Real-Time Traffic Updates
    def TrafficUpdate(self, src, dst, state):
        pass
        

    def ChangeVehicle(self, cat):
        self.vehicle = Vehicle(cat)


Map = DatMap()
Map.construct(edges)

print(Map.FindD(0,3))
print(Map.FindT(0, 3))


    