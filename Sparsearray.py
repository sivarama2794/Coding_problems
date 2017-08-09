""" This program gets the first line as the number of strings then the query to be searched in the strings. Sample input would be
4
aba
xyz
aba
aba
3
aba
xyz
ab 
and the output would be the count of the query in the string
Out:
2
1
0
 """
from collections import OrderedDict
n=int(input())
def sparsearray(n):
    l=list()
    d=OrderedDict()
    for i in range(0,n):
        l.append(input())
    q=int(input())
    for j in range(0,q):
        query=input()
        count=l.count(query)
        d[query]=count
    l=list(d.values())
    print(*l,sep='\n')
    return ''
sparsearray(n)