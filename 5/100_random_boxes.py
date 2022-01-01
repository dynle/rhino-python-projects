# coding:utf-8
import rhinoscriptsyntax as rs
import random

# grid layer
name = "grid"
color = rs.CreateColor([0,0,0])
visible = True
locked = False
parent = None
gridLayer = rs.AddLayer(name, color, visible, locked, parent)

# box layer
name = "box"
color = rs.CreateColor([0,0,0])
visible = True
locked = False
parent = "grid"
boxLayer = rs.AddLayer(name, color, visible, locked, parent)

# text layer
name = "text"
color = rs.CreateColor([0,0,0])
visible = True
locked = False
parent = "grid"
textLayer = rs.AddLayer(name, color, visible, locked, parent)

# grid
xNum = 10
yNum = 10
xPitch = 2100
yPitch = 2100
for y in range(yNum):
    for x in range(xNum):
        depth = random.randint(300,1800)
        width = random.randint(300,1800)
        height = random.randint(300,1800)

        # box
        p0 = yPitch*y, xPitch*x, 0
        p1 = yPitch*y+depth, xPitch*x, 0
        p2 = yPitch*y+depth, xPitch*x+width, 0
        p3 = yPitch*y, xPitch*x+width, 0
        
        p4 = yPitch*y, xPitch*x, height
        p5 = yPitch*y+depth, xPitch*x, height
        p6 = yPitch*y+depth, xPitch*x+width, height
        p7 = yPitch*y, xPitch*x+width, height
        
        points = p0,p1,p2,p3,p4,p5,p6,p7
        boxID = rs.AddBox(points)
        rs.ObjectLayer(boxID,boxLayer)
        if (height<900):
            rs.ObjectColor(boxID,rs.CreateColor([255,0,0]))
        
        # num text
        text = "NO.{}".format(x+10*y+1)
        point = [xPitch*x,yPitch*y-50,0]
        height = 150
        font = "Arial"
        font_style = 0
        justification = 1 + 262144
        textID = rs.AddText(text, point, height, font, font_style, justification)
        rs.ObjectLayer(textID,textLayer)

        # location text
        text = "W{},D{}.H{}".format(width,depth,height)
        point = [xPitch*x,yPitch*y-400,0]
        height = 150
        font = "Arial"
        font_style = 0
        justification = 1 + 262144
        textID = rs.AddText(text, point, height, font, font_style, justification)
        rs.ObjectLayer(textID,textLayer)