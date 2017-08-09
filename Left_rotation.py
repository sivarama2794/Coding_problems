"""This is a program to do left rotation in a array. 
d is the lenght of the array and n is the rotation count.
For eg: a=[1,2,3,4,5] with d=5 and n=4 becomes a=[5,1,2,3,4]"""
l=()
d,n=map(int,input().split())
a=list(input().split())
r=a[n:]+a[:n]
print(*r,sep=" ")
    