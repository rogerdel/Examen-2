# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random as rnd


def func(a):
    for i in a:
        n = i**3+ i**2 + i
        print(n, end = " ")
    print("\n")
def decbin(a):    
    b = []    
    for i in a:
        b.append(("{0:b}".format(i)).zfill(8))
    return b
def bindec(a):
    d = []
    for i in a:
        d.append(int(i,2))
    return d
def mutar(l, mi):
    nl = []
    for i in l:
        s = ""
        for j in range(len(i)):
            if(j != mi):
                s += i[j]
            else:
                s += "1" if i[mi] == "0" else "0"
        nl.append(s)
    return nl

def cambiar(a,b, ci,cj):
    ca = ""
    cb = ""
    for i in range(len(a)):
        if(i>=ci and i <=cj):
            ca+= b[i]
            cb+=a[i]
        else:
            ca+=a[i]
            cb+= b[i]
    return ca, cb
def cruce(a, ci,cf):
    b = []
    for i in range(0, len(a),2):
        c1 = a[i]
        c2 = a[i+1]
        ca,cb = cambiar(c1,c2,ci,cf)
        b.append(ca)
        b.append(cb)
    return b

def stats(a):
    mn = mx = a[0]
    med = 0
    for i in a:
        mn = min(mn, i)
        mx = max(mn, i)
        med += i
    med /= len(a)
    print("Minimo:",mn)
    print("Maximo:", mx)
    print("Media:", med)

rnd.seed(100)
a = [rnd.randint(0,50) for i in range (10)]
ngens = 6
for i in range(ngens):
    print(f'------------ generacion {i+1}-----------------')  
    func(a)
    bn = decbin(a)
    nr = rnd.randint(0, len(bn[0])-2)
    l = cruce(bn,nr,nr+1)
    g = mutar(l, rnd.randint(0,len(l[0])))
    a = bindec(g)
    stats(a)