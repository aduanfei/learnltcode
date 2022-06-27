import bisect
def bisect_left(A,x):
    #内置api
    bisect.bisect_left(A,x)
    #手写
    l,r=0,len(A)-1
    while l<=r:
        mid=(r+l)//2
        if A[mid]>=x: r=mid-1
        else: l=mid+1
    return l


def bisect_right(A,x):
    l,r=0,len(A)-1
    while l<=r:
        mid=(r+l)//2
        if A[mid]<=x:l=mid+1
        else: r=mid-1
    return l
