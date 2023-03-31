#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 14:16:10 2023

@author: fromentin
"""

N=7
S=[[0,2],[2,4],[3,5],[1,2],[2,4],[4,6]]
C=[-2,0,3]

full=set(range(N))

#S=[1,2,3,1,2,3]
def next(E):
    res=set([])
    for x in E:
        for c in C:
            if x+c>=0 and x+c<N:
                res.add(x+c)
    return res

def prev(E):
    res=set([])
    for x in E:
        for c in C:
            if x-c>=0 and x-c<N:
                res.add(x-c)
    return res

def comp(p):
    res=full.difference(set(p))
    return res

def forward(F):
    flag=False
    for i in range(1,len(F)):
        T=F[i].intersection(next(F[i-1]))
        if len(T)<len(F[i]):
            F[i]=T
            flag=True
    return flag
        
def backward(F):
    flag=False
    for i in range(len(F)-2,-1,-1):
        T=F[i].intersection(prev(F[i+1]))
        if len(T)<len(F[i]):
            F[i]=T
            flag=True
    return flag
    
def moves(F):
    p=F[0].pop()
    res=[p]
    for i in range(1,len(F)):
        t=F[i].intersection(set([p+c for c in C]))
        p=t.pop()
        print(p)
        res.append(p)
    return res
 
def contre(S):
    F=[comp(p) for p in S]
    flag=True
    while flag:
        flag=False
        flag|=forward(F)
        flag|=backward(F)
    if len(F[0])==0:
        return False
    return moves(F)