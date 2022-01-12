# coding:utf-8
import math

#########
# 1071 = 2*462 + 147
# 462 = 3*127 + 21
# 147 = 7*21 + 0

def euclideanAlgorithm1(a,b):
    while(b!=0):
        # Calculate Division
        q = int(math.floor(a/b))
        r = a%b
        
        # Print
        str = "%s/%s = %s*%s + %s" % (a,b,q,b,r)
        print(str)
        
        a = b
        b = r
    
    return a
    
    
def euclideanAlgorithm2(a,b):
    # Exit condition
    if(b==0):
        return a
    
    # Calculate Division
    q = int(math.floor(a/b))
    r = a%b
        
    # Print
    str = "%s/%s = %s*%s + %s" % (a,b,q,b,r)
    print(str)
        
    a = b
    b = r
    
    res = euclideanAlgorithm2(a,b)
    
    return res
    
res = euclideanAlgorithm2(1071,462)
print(res)






