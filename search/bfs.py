import collections
def bfsearch(graph):
    visited=set()
    def bfs():
        q=collections.deque([])
        while(q):
            cur=q.popleft()
            if(visited[cur]):
                continue
            for w in graph[cur]:
                if(w):
                    q.push(w)



