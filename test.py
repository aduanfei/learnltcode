import collections

d1=collections.defaultdict(int)
d1["a"]=1
d1["b"]=2
print(max(d1.values()))