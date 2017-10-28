#Jiazhou Liu ljzhou@bu.edu
import math
import numpy as np
from scipy.linalg import solve
from scipy.optimize import linprog


def find1(matrix):
    len1=len(matrix)
    len2=len(matrix[0])
    for i in range(len1):
        for j in range(len2):
            lst=[]
            for k in range(len1):
                lst+=[matrix[k][j]]
            if (matrix[i][j]==min(matrix[i])) and (matrix[i][j]==max(lst)):
                    value=matrix[i][j]
                    lst1=[0 for x in range(len1)]
                    lst1[i]=1
                    lst2=[0 for y in range(len2)]
                    lst2[j]=1
                    return (lst1,lst2,value,'a')
            
    return ('b')

def find2(matrix):
    a=matrix[0][0]
    b=matrix[0][1]
    c=matrix[1][1]
    d=matrix[1][0]
    tr1=a+c
    tr2=b+d
    value=(a*c-b*d)/(tr1+tr2)
    p0=(c-d)/(tr1-tr2)
    p1=(a-b)/(tr1-tr2)
    p=[p0,p1]
    q0=(c-b)/(tr1-tr2)
    q1=(a-d)/(tr1-tr2)
    q=[q0,q1]
    return (p,q,value)

def find3(matrix):
    len1=len(matrix)
    len2=len(matrix[0])
    b=[0 for x in range(len1+1)]
    b[0]=1
    A=[[] for x in range(len1)]
    for i in range(len1):
        A[i]=matrix[i]+[-1]
    first=[1 for x in range(len2+1)]
    first[-1]=0
    A=[first]+A
    x=solve(A,b)
    return x


def find4(matrix):
    len1=len(matrix)
    et=[1 for x in range(len1)]
    e=[[1] for x in range(len1)]
    inverse1=np.linalg.inv(matrix).tolist()
    sum1=0
    for i in range(len1):
        for j in range(len1):
            sum1+=inverse1[i][j]
    v=1/sum1
    inv=np.matrix(inverse1)
    e1=np.matrix(e)
    et1=np.matrix(et)
    q=(v*inv*e1).tolist()
    pt=v*et1*inv
    p=(np.transpose(pt)).tolist()
    p=[x[0] for x in p]
    q=[y[0] for y in q]
    return (p,q,v)

def solvegame(matrix):
    len1=len(matrix)
    len2=len(matrix[0])
    saddle=find1(matrix)
    if saddle[-1]=='a':
        return (saddle[0],saddle[1],saddle[2])
    elif (len1==2) and (len2==2):
        return find2(matrix)
    elif (len1==len2) and (np.linalg.det(matrix)!=0):
        return find4(matrix)
    elif (len1==len2):
        q=find3(matrix)
        p=find3(np.asarray(matrix).T.tolist())
        v=q[-1]
        p1=p[0:-1]
        q1=q[0:-1]
        for i in p1:
            if i<0:
                 r1=lp(matrix)
                 matrix1=np.asarray(matrix).T.tolist()
                 matrix1=neg(matrix1)
                 r2=lp(matrix1)
                 t=(r2[0],r1[0],r1[1])
                 return t
        for j in q1:
            if j<0:
                 r1=lp(matrix)
                 matrix1=np.asarray(matrix).T.tolist()
                 matrix1=neg(matrix1)
                 r2=lp(matrix1)
                 t=(r2[0],r1[0],r1[1])
                 return t
        return t
    else:
         r1=lp(matrix)
         matrix1=np.asarray(matrix).T.tolist()
         matrix1=neg(matrix1)
         r2=lp(matrix1)
         t=(r2[0],r1[0],r1[1])
         return t


def lp(matrix):
    l1=len(matrix)
    l2=len(matrix[0])
    c=[0 for x in range(l2+1)]
    c[-1]=1
    a=[[0 for x in range(l2)] for y in range(l1)]
    for i in range(l1):
        a[i]=matrix[i]+[-1]
    q=[1 for x in range(l2+1)]
    q[-1]=0
    a=a+[q]
    b=[0 for x in range(l1+1)]
    b[-1]=math.inf
    a1=[[0 for x in range(l2+1)] for y in range(l1)]
    a1=a1+[q]
    b1=[0 for x in range(l1+1)]
    b1[-1]=1
    bounds=[(0,None) for x in range(l2+1)]
    bounds[-1]=(None,None)
    res=linprog(c,A_ub=a,b_ub=b,A_eq=a1,b_eq=b1,bounds=bounds,method='Simplex')
    v1=res.fun
    x=res.x[0:-1]
    return (x,v1)


        
            
def neg(matrix):      
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j]=0-matrix[i][j]
    return matrix
    
outfile=open('result.txt','w')     

matrix1=[[1,2,3,4,5],[3,4,5,6,7]]
matrix2=[[1,-2,3,-4],[0,1,-2,3],[0,0,1,-2],[0,0,0,1]]
matrix3=[[1,2,-1],[2,-1,4],[-1,4,-3]]
matrix4=[[0,2,1],[-2,0,-4],[-1,4,0]]
matrix5=[[10,0,7,0],[0,6,4,0],[0,0,3,3]]

print(solvegame(matrix1),file=outfile)
print(solvegame(matrix2),file=outfile)
print(solvegame(matrix3),file=outfile)
print(solvegame(matrix4),file=outfile)
print(solvegame(matrix5),file=outfile)

outfile.close()
    
    
