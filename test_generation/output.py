# -*- coding: utf-8 -*-
# author             :Hoang Kim Bang
# class              :K55CC
# MSSV               :10020016

# Cac thu vien dươc import tai day
import input
import unittest
import inspect
import itertools
import math

# Doc file input.py
doc = input.main.__doc__


# Dem so bien
num = doc.count(':')  
print "So bien :  %i " %num


# Doc gia tri bien
# Hai mang luu gia tri cac bien
A1 = []
A2 = []

# Doc gia tri bien trong dau docstring roi luu vao hai mang A1 va A2
i = 0
j = -1
while(i<len(doc)):
    n = ''
    if(doc[i]=='['):
        k = i+1
        
        while(doc[k]!=';'):
            n += doc[k]
            k+=1
        a = int(n)
        n = ''
        k+=1
        
        while(doc[k]!=']'):
            n += doc[k]
            k+=1
        b = int(n)
        A2[j].append(a)
        A2[j].append(b)
        A1[j].append((a+b)/2)
        n = ''
            
    if((i+1)<len(doc) and doc[i+1]==':'):
        j+=1
        A1.append([])
        A2.append([])
        
    i+=1


# Xu ly ngoai le
# Neu ngoai le xay ra se in ra thong bao "wrong input"
for n in range (0, len(A2) ):
        for i in range(0, len(A2[n])-2,2):
            if (A2[n][i+3]-A2[n][i])*(A2[n][i+2]-A2[n][i+1]) < 0:
                raise Exception("wrong input")
            
            if len(A2[n]) > 4 and ( A2[n][4]-A2[n][1])*(A2[n][5]-A2[n][0]) < 0 :
                raise Exception("wrong input")
                      
# Lop unittest      
class TestSequense(unittest.TestCase):
    pass

def test_generator(a, b):
    def test(self):
        self.assertEqual(a,b)
    return test

# Chuc nang chinh
if __name__ == '__main__':
    print "\nTest case : "
    for e in itertools.product(*A1):
        print e
        test_name = 'test_%s' %str(e)
        test = test_generator(input.main(*e) , "gia tri tra ve")
        setattr(TestSequense, test_name, test)
    unittest.main()
