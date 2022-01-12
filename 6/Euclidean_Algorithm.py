# coding:utf-8
import math, random
import rhinoscriptsyntax as rs



#########
# 1071 = 2*462 + 147
# 462 = 3*127 + 21
# 147 = 7*21 + 0

def euclideanAlgorithm1(a,b):
    cnt = 0
    oriVec = [0,0,0]
    while(b!=0):
        # Calculate Division
        q = int(math.floor(a/b))
        r = a%b
        
        # Print
        str = "[%s]%s/%s = %s*%s + %s" % (cnt,a,b,q,b,r)
        print(str)
        
        # Draw rectangle
        cR = random.randint(0,255)
        cG = random.randint(0,255)
        cB = random.randint(0,255)
        color = rs.CreateColor(cR,cG,cB)
        for i in range(q):
            id = makeSrfPt(b,b)
            rs.ObjectColor(id,color)
            if(cnt%2==0):
                movePt = [b*i,0,0]
            else:
                movePt = [0,b*i,0]
            movePt = rs.VectorAdd(oriVec,movePt)
            rs.MoveObject(id,movePt)
        
        # Calculate oriVec
        if(cnt%2==0):
            tmpVec = [q*b,0,0]
        else:
            tmpVec = [0,q*b,0]
        oriVec = rs.VectorAdd(oriVec,tmpVec)
        
        # Recursion
        a = b
        b = r
        cnt += 1
    
    return a
    
    
def euclideanAlgorithm2(a,b,oriVec,cnt):
    # Exit condition
    if(b==0):
        return a
    
    # Calculate Division
    q = int(math.floor(a/b))
    r = a%b
        
    # Print
    str = "[%s]%s/%s = %s*%s + %s" % (cnt,a,b,q,b,r)
    print(str)
    
    # Draw rectangle
    cR = random.randint(0,255)
    cG = random.randint(0,255)
    cB = random.randint(0,255)
    color = rs.CreateColor(cR,cG,cB)
    for i in range(q):
        id = makeSrfPt(b,b)
        rs.ObjectColor(id,color)
        if(cnt%2==0):
            movePt = [b*i,0,0]
        else:
            movePt = [0,b*i,0]
        movePt = rs.VectorAdd(oriVec,movePt)
        rs.MoveObject(id,movePt)
        
    # Calculate oriVec
    if(cnt%2==0):
        tmpVec = [q*b,0,0]
    else:
        tmpVec = [0,q*b,0]
    oriVec = rs.VectorAdd(oriVec,tmpVec)
    
    a = b
    b = r
    cnt+=1
    
    res = euclideanAlgorithm2(a,b,oriVec,cnt)
    
    return res

def makeSrfPt(width,height):
    points = [  [0,0,0],
                [width,0,0],
                [width,height,0],
                [0,height,0]
    ]

    id = rs.AddSrfPt(points)
    return id


########################
# main
########################
#res = euclideanAlgorithm1(1071,462)
res = euclideanAlgorithm2(1071,462,[0,0,0],0)
print(res)







