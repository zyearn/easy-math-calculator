# author : zyearn 
from math import *
from graphics import *


def fxMax(a,b,func):
    x = a
    step  = 0.001
    y = []
    while x <= b:
        y.append(eval(func))
        x = x + 0.001
    return max(y)

def fxMin(a,b,func):
    x = a
    step  = 0.001
    y = []
    while x <= b:
        y.append(eval(func))
        x = x + 0.001
    return min(y)

def getX(a,b,func):
    if a<0 and b<0:
        xmin=1.2*a
        xmax=-0.2*a
    elif a>0 and b>0:
        xmin=-0.2*a
        xmax=1.2*b
    else:
        xmin=1.2*a-1
        xmax=1.2*b+1
    return xmin,xmax
def getY(a,b,func):
    ymin=fxMin(a,b,func)
    ymax=fxMax(a,b,func)
    if ymin<0 and ymax<0:
        yMin=1.2*ymin
        yMax=-0.2*ymin
    elif ymin>0 and ymax>0:
        yMin=-0.1*ymin
        yMax=1.2*ymax
    else:
        yMin=1.2*ymin-1
        yMax=1.2*ymax+1
    return yMin,yMax

class button:
    def __init__(self,win,center, width, height, label):

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)

    def clicked(self, p):
        return self.xmin <= p.getX() <= self.xmax and \
               self.ymin <= p.getY() <= self.ymax

    
def drawlabel(win,center,face,size,style,label):
    x,y=center.getX(), center.getY()
    a=Text(Point(x,y),label)
    a.setFace(face)
    a.setSize(size)
    a.setStyle(style)
    a.draw(win)
       


def funcdraw(a,b,func):
    win=GraphWin('function graph',550,550)
    win.setBackground('white')
    
    xll,xur=getX(a,b,func)
    yll,yur=getY(a,b,func)
    d=min(b-a,yur-yll)
    win.setCoords(xll-1,yll-1,xur+1,yur+1)

    Line(Point(xll,0.0),Point(xur,0.0)).draw(win)
    Line(Point(0.0,yll),Point(0.0,yur)).draw(win)
    Text(Point(-0.05*d,0.03*d),'O').draw(win)
    Text(Point(-0.05*d,yur-0.03*d),'Y').draw(win)
    Text(Point(xur,0.03*d),'X').draw(win)
    Line(Point(xur,0.0),Point(xur-0.04*d,0.02*d)).draw(win)
    Line(Point(xur,0.0),Point(xur-0.04*d,-0.02*d)).draw(win)
    Line(Point(0.0,yur),Point(-0.02*d,yur-0.03*d)).draw(win)
    Line(Point(0.0,yur),Point(0.02*d,yur-0.03*d)).draw(win)
    x=a
    step=0.002*(b-a)
    while x<=b:
        y=eval(func)
        p0=Point(x,y)
        p0.draw(win)
        line=Line(Point(x,0),Point(x,y))
        line.setFill('lightgray')
        line.draw(win)
        x=x+step
    Text(Point(0.7*xur,0.7*yur),'y='+func).draw(win)


def diff(a,func):
    x=a-0.00001
    y1=eval(func)
    x=a+0.00001
    y2=eval(func)
    a='%0.12f'%((y2-y1)/0.00002)
    return eval(a)

def inte(a,b,func):
    x=a
    step=0.00001
    sum=0.0
    while x<=b:
        sum=sum+0.00001*eval(func)
        x=x+0.00001
    a='%0.12f'%(sum)
    return eval(a)

def BasicOpe(win):


    b0 = button(win,Point(2,0.0),1.7,1.6,"0")
    b1 = button(win,Point(2,2),1.7,1.6,"1")
    b2 = button(win,Point(4,2),1.7,1.6,"2")
    b3 = button(win,Point(6,2),1.7,1.6,"3")
    b4 = button(win,Point(2,4),1.7,1.6,"4")
    b5 = button(win,Point(4,4),1.7,1.6,"5")
    b6 = button(win,Point(6,4),1.7,1.6,"6")
    b7 = button(win,Point(2,6),1.7,1.6,"7")
    b8 = button(win,Point(4,6),1.7,1.6,"8")
    b9 = button(win,Point(6,6),1.7,1.6,"9")
    bDot = button(win,Point(4,0.0),1.7,1.6,".")
    bPi=button(win,Point(6,0.0),1.4,1.4,"Pi")
    bE=button(win,Point(7.6,0.0),1.4,1.4,"e")

    bMul = button(win,Point(7.75,3.0),1.4,1,"*")    
    bDiv = button(win,Point(9.25,3.0),1.4,1,"/")
    bPlus = button(win,Point(7.75,1.7),1.4,1,"+")
    bMin = button(win,Point(9.25,1.7),1.4,1,"-")
    bBran1 = button(win,Point(7.75,4.4),1.4,1.0,"(")  
    bBran2 = button(win,Point(9.25,4.4),1.4,1.0,")") 
    bPower = button(win,Point(7.8,8.5),1.2,.9,"^")  
    bSqrt = button(win,Point(9.2,8.5),1.2,.9,"sqrt")
    bsin = button(win,Point(2,8.5),1.9,.9,"sin")
    basin = button(win,Point(2,7.4),1.9,.9,"arcsin")    #arcsin
    bcos = button(win,Point(4,8.5),1.9,.9,"cos")    #cos
    bacos = button(win,Point(4.0,7.4),1.9,.9,"arccos")    #arccos
    btan = button(win,Point(6,8.5),1.9,.9,"tan")    #tan
    batan = button(win,Point(6.0,7.4),1.9,.9,"arctan")    #arctan
    bsinh =  button(win,Point(2.0,10.7),1.9,.9,"sinh")
    basinh =  button(win,Point(2.0,9.6),1.9,.9,"arcsinh")
    bcosh =  button(win,Point(4.0,10.7),1.9,.9,"cosh")
    bacosh =  button(win,Point(4.0,9.6),1.9,.9,"arccosh")
    btanh =  button(win,Point(6.0,10.7),1.9,.9,"tanh")
    batanh =  button(win,Point(6.0,9.6),1.9,.9,"arctanh")
    bDel = button(win,Point(8.5,10.0),2.6,1.5,"Del")


    bAC = button(win,Point(8.5,6),2.9,1.5,"AC")

    bEqu = button(win,Point(9.3,0.0),1.4,1.5,"=")

    bEsc = button(win,Point(9.8,14.6),.4,.4,"X")

    bg = Rectangle(Point(0.5,13.0), Point(9.5,14.5))
    bg.setFill('white')
    bg.draw(win)

    show = Text(Point(5,13.75),"")
    show.draw(win)
    
    p = win.getMouse()
    while not bEsc.clicked(p):
        try:

            p = win.getMouse()

            if b0.clicked(p):
                s = show.getText()
                s = s + "0"
                
                show.setText(s)
                show.setSize(20)
                
                
            elif b1.clicked(p):
                s = show.getText()
                s = s + '1'
                show.setText(s)
                show.setSize(20)
                
            elif b2.clicked(p):
                s = show.getText()
                s = s + '2'
                show.setText(s)
                show.setSize(20)
                
            elif b3.clicked(p):
                s = show.getText()
                s = s + '3'
                show.setText(s)
                show.setSize(20)
            
            elif b4.clicked(p):
                s = show.getText()
                s = s + '4'
                show.setText(s)
                show.setSize(20)

            elif b5.clicked(p):
                s = show.getText()
                s = s + '5'
                show.setText(s)
                show.setSize(20)
                
            elif b6.clicked(p):
                s = show.getText()
                s = s + '6'
                show.setText(s)
                show.setSize(20)
                
            elif b7.clicked(p):
                s = show.getText()
                s = s + '7'
                show.setText(s)
                show.setSize(20)
                
            elif b8.clicked(p):
                s = show.getText()
                s = s + '8'
                show.setText(s)
                show.setSize(20)

                
            elif b9.clicked(p):
                s = show.getText()
                s = s + '9'
                show.setText(s)
                show.setSize(20)

            elif bMul.clicked(p):
                s = show.getText()
                s = s + '*'
                show.setText(s)
                show.setSize(20)        
                    
            elif bDiv.clicked(p):
                s = show.getText()
                s = s + '/'
                show.setText(s)
                show.setSize(20)
                
            elif bPlus.clicked(p):
                s = show.getText()
                s = s + '+'
                show.setText(s)
                show.setSize(20)
                
            elif bMin.clicked(p):
                s = show.getText()
                s = s + '-'
                show.setText(s)
                show.setSize(20)
                
            elif bAC.clicked(p):
                s = ""
                show.setText(s)
                show.setSize(20)

            elif bPi.clicked(p):
                s = show.getText()
                s = s + 'pi'
                show.setText(s)
                show.setSize(20)


            elif bE.clicked(p):
                s = show.getText()
                s = s + 'e'
                show.setText(s)
                show.setSize(20)
                
            elif bEqu.clicked(p):
                ans = eval(show.getText())
                show.setText(str(ans))
                show.setSize(20)
                

            elif bBran1.clicked(p):
                s = show.getText()
                s = s + '('
                show.setText(s)
                show.setSize(20)
                
            elif bBran2.clicked(p):
                s = show.getText()
                s = s + ')'
                show.setText(s)
                show.setSize(20)
                
            elif bPower.clicked(p):
                s = show.getText()
                s = s + '**'
                show.setText(s)
                show.setSize(20)

            elif bSqrt.clicked(p):
                s = show.getText()
                s = s + 'sqrt('
                show.setText(s)
                show.setSize(20)
                
            elif bsin.clicked(p):
                s = show.getText()
                s = s + 'sin('
                show.setText(s)
                show.setSize(20)

            elif basin.clicked(p):
                s = show.getText()
                s = s + 'asin('
                show.setText(s)
                show.setSize(20)

            elif bacos.clicked(p):
                s = show.getText()
                s = s + 'acos('
                show.setText(s)
                show.setSize(20)
 
                  
            elif bcos.clicked(p):
                s = show.getText()
                s = s + 'cos('
                show.setText(s)
                show.setSize(20)

            elif btan.clicked(p):
                s = show.getText()
                s = s + 'tan('
                show.setText(s)
                show.setSize(20)
                
            elif batan.clicked(p):
                s = show.getText()
                s = s + 'atan('
                show.setText(s)
                show.setSize(20)

            elif bsinh.clicked(p):
                s = show.getText()
                s = s + 'sinh('
                show.setText(s)
                show.setSize(20)

            elif basinh.clicked(p):
                s = show.getText()
                s = s + 'asinh('
                show.setText(s)
                show.setSize(20)

            elif bcosh.clicked(p):
                s = show.getText()
                s = s + 'cosh('
                show.setText(s)
                show.setSize(20)

            elif bacosh.clicked(p):
                s = show.getText()
                s = s + 'acosh('
                show.setText(s)
                show.setSize(20)

            elif btanh.clicked(p):
                s = show.getText()
                s = s + 'tanh('
                show.setText(s)
                show.setSize(20)
                
            elif batanh.clicked(p):
                s = show.getText()
                s = s + 'atanh('
                show.setText(s)
                show.setSize(20)


            elif bDel.clicked(p):
                s = show.getText()
                if s != "Math Error!":
                    s = s[:-1]
                    show.setText(s)
                    show.setSize(20)
                

            elif bDot.clicked(p):
                s = show.getText()
                s = s + '.'
                show.setText(s)
                show.setSize(20)              
                
        except:
            show.setText("Math Error!")
            show.setSize(20)
    
    win.close()
    


def FuncGraph():
    win = GraphWin("Calculator",400,647)
    win.setCoords(0.0,-1.0,10,15)
    drawlabel(win,Point(1.3,12),'arial',8,'bold italic','Lower limit')
    E1 = Entry(Point(2.8,12),4)
    E1.draw(win)
    drawlabel(win,Point(4.6,12),'arial',8,'bold italic','Upper limit')
    E2 = Entry(Point(6.1,12),4)
    E2.draw(win)
         
    b0 = button(win,Point(2,0.0),1.7,1.6,"0")
    b1 = button(win,Point(2,2),1.7,1.6,"1")
    b2 = button(win,Point(4,2),1.7,1.6,"2")
    b3 = button(win,Point(6,2),1.7,1.6,"3")
    b4 = button(win,Point(2,4),1.7,1.6,"4")
    b5 = button(win,Point(4,4),1.7,1.6,"5")
    b6 = button(win,Point(6,4),1.7,1.6,"6")
    b7 = button(win,Point(2,6),1.7,1.6,"7")
    b8 = button(win,Point(4,6),1.7,1.6,"8")
    b9 = button(win,Point(6,6),1.7,1.6,"9")
    bDot = button(win,Point(4,0.0),1.7,1.6,".")
    bPi=button(win,Point(6,0.0),1.4,1.4,"Pi")
    bE=button(win,Point(7.6,0.0),1.4,1.4,"e")

    bMul = button(win,Point(7.75,3.0),1.4,1,"*")    
    bDiv = button(win,Point(9.25,3.0),1.4,1,"/")
    bPlus = button(win,Point(7.75,1.7),1.4,1,"+")
    bMin = button(win,Point(9.25,1.7),1.4,1,"-")
    bBran1 = button(win,Point(7.75,4.4),1.4,1.0,"(")  
    bBran2 = button(win,Point(9.25,4.4),1.4,1.0,")") 
    bPower = button(win,Point(7.8,8.5),1.2,.9,"^")  
    bSqrt = button(win,Point(9.2,8.5),1.2,.9,"sqrt")
    bsin = button(win,Point(2,8.5),1.9,.9,"sin")    #sin
    basin = button(win,Point(2,7.4),1.9,.9,"arcsin")    #arcsin
    bcos = button(win,Point(4,8.5),1.9,.9,"cos")    #cos
    bacos = button(win,Point(4.0,7.4),1.9,.9,"arccos")    #arccos
    btan = button(win,Point(6,8.5),1.9,.9,"tan")    #tan
    batan = button(win,Point(6.0,7.4),1.9,.9,"arctan")    #arctan
    bsinh =  button(win,Point(2.0,10.7),1.9,.9,"sinh")
    basinh =  button(win,Point(2.0,9.6),1.9,.9,"arcsinh")
    bcosh =  button(win,Point(4.0,10.7),1.9,.9,"cosh")
    bacosh =  button(win,Point(4.0,9.6),1.9,.9,"arccosh")
    btanh =  button(win,Point(6.0,10.7),1.9,.9,"tanh")
    batanh =  button(win,Point(6.0,9.6),1.9,.9,"arctanh")
    bDel = button(win,Point(8.5,10.0),2.6,1.5,"Del")
    bX = button(win,Point(8.5,7.4),2.6,1.0,"Var: X")
    bDraw = button(win,Point(8.5,12),2.6,1.5,"Draw")


    bAC = button(win,Point(8.5,6),2.9,1.5,"AC")

    bEqu = button(win,Point(9.3,0.0),1.4,1.5,"=")

    bEsc = button(win,Point(9.8,14.6),.4,.4,"X")

    bg = Rectangle(Point(0.5,13.0), Point(9.5,14.5))
    bg.setFill('white')
    bg.draw(win)

    show = Text(Point(5,13.75),"")
    show.draw(win)
    
    p = win.getMouse()
    while not bEsc.clicked(p):
        try:

            p = win.getMouse()

            if b0.clicked(p):
                s = show.getText()
                s = s + "0"
                
                show.setText(s)
                show.setSize(20)
                
                
            elif b1.clicked(p):
                s = show.getText()
                s = s + '1'
                show.setText(s)
                show.setSize(20)
                
            elif b2.clicked(p):
                s = show.getText()
                s = s + '2'
                show.setText(s)
                show.setSize(20)
                
            elif b3.clicked(p):
                s = show.getText()
                s = s + '3'
                show.setText(s)
                show.setSize(20)
            
            elif b4.clicked(p):
                s = show.getText()
                s = s + '4'
                show.setText(s)
                show.setSize(20)

            elif b5.clicked(p):
                s = show.getText()
                s = s + '5'
                show.setText(s)
                show.setSize(20)
                
            elif b6.clicked(p):
                s = show.getText()
                s = s + '6'
                show.setText(s)
                show.setSize(20)
                
            elif b7.clicked(p):
                s = show.getText()
                s = s + '7'
                show.setText(s)
                show.setSize(20)
                
            elif b8.clicked(p):
                s = show.getText()
                s = s + '8'
                show.setText(s)
                show.setSize(20)

                
            elif b9.clicked(p):
                s = show.getText()
                s = s + '9'
                show.setText(s)
                show.setSize(20)

            elif bMul.clicked(p):
                s = show.getText()
                s = s + '*'
                show.setText(s)
                show.setSize(20)        
                    
            elif bDiv.clicked(p):
                s = show.getText()
                s = s + '/'
                show.setText(s)
                show.setSize(20)
                
            elif bPlus.clicked(p):
                s = show.getText()
                s = s + '+'
                show.setText(s)
                show.setSize(20)
                
            elif bMin.clicked(p):
                s = show.getText()
                s = s + '-'
                show.setText(s)
                show.setSize(20)
                
            elif bAC.clicked(p):
                s = ""
                show.setText(s)
                show.setSize(20)

            elif bPi.clicked(p):
                s = show.getText()
                s = s + 'pi'
                show.setText(s)
                show.setSize(20)


            elif bE.clicked(p):
                s = show.getText()
                s = s + 'e'
                show.setText(s)
                show.setSize(20)
                
            elif bEqu.clicked(p):
                ans = eval(show.getText())
                show.setText(str(ans))
                show.setSize(20)
                

            elif bBran1.clicked(p):
                s = show.getText()
                s = s + '('
                show.setText(s)
                show.setSize(20)
                
            elif bBran2.clicked(p):
                s = show.getText()
                s = s + ')'
                show.setText(s)
                show.setSize(20)
                
            elif bPower.clicked(p):
                s = show.getText()
                s = s + '**'
                show.setText(s)
                show.setSize(20)

            elif bSqrt.clicked(p):
                s = show.getText()
                s = s + 'sqrt('
                show.setText(s)
                show.setSize(20)
                
            elif bsin.clicked(p):
                s = show.getText()
                s = s + 'sin('
                show.setText(s)
                show.setSize(20)

            elif basin.clicked(p):
                s = show.getText()
                s = s + 'asin('
                show.setText(s)
                show.setSize(20)

            elif bacos.clicked(p):
                s = show.getText()
                s = s + 'acos('
                show.setText(s)
                show.setSize(20)
 
                  
            elif bcos.clicked(p):
                s = show.getText()
                s = s + 'cos('
                show.setText(s)
                show.setSize(20)

            elif btan.clicked(p):
                s = show.getText()
                s = s + 'tan('
                show.setText(s)
                show.setSize(20)
                
            elif batan.clicked(p):
                s = show.getText()
                s = s + 'atan('
                show.setText(s)
                show.setSize(20)

            elif bsinh.clicked(p):
                s = show.getText()
                s = s + 'sinh('
                show.setText(s)
                show.setSize(20)

            elif basinh.clicked(p):
                s = show.getText()
                s = s + 'asinh('
                show.setText(s)
                show.setSize(20)

            elif bcosh.clicked(p):
                s = show.getText()
                s = s + 'cosh('
                show.setText(s)
                show.setSize(20)

            elif bacosh.clicked(p):
                s = show.getText()
                s = s + 'acosh('
                show.setText(s)
                show.setSize(20)

            elif btanh.clicked(p):
                s = show.getText()
                s = s + 'tanh('
                show.setText(s)
                show.setSize(20)
                
            elif batanh.clicked(p):
                s = show.getText()
                s = s + 'atanh('
                show.setText(s)
                show.setSize(20)



            elif bDel.clicked(p):
                s = show.getText()
                if s != "Math Error!":
                    s = s[:-1]
                    show.setText(s)
                    show.setSize(20)
                

            elif bDot.clicked(p):
                s = show.getText()
                s = s + '.'
                show.setText(s)
                show.setSize(20)

            elif bX.clicked(p):
                s = show.getText()
                s = s + 'x'
                show.setText(s)
                show.setSize(20)

            elif bDraw.clicked(p):
                s = show.getText()
                funcdraw(eval(E1.getText()),eval(E2.getText()),s)

                
        except:
            show.setText("Math Error!")
            show.setSize(20)
    
    win.close()


def Integra():
    win = GraphWin("Calculator",400,647)
    win.setCoords(0.0,-1.0,10,15)
    drawlabel(win,Point(1.3,12),'arial',8,'bold italic','Lower limit')
    E1 = Entry(Point(2.8,12),4)
    E1.draw(win)
    drawlabel(win,Point(4.6,12),'arial',8,'bold italic','Upper limit')
    E2 = Entry(Point(6.1,12),4)
    E2.draw(win)
         
    b0 = button(win,Point(2,0.0),1.7,1.6,"0")
    b1 = button(win,Point(2,2),1.7,1.6,"1")
    b2 = button(win,Point(4,2),1.7,1.6,"2")
    b3 = button(win,Point(6,2),1.7,1.6,"3")
    b4 = button(win,Point(2,4),1.7,1.6,"4")
    b5 = button(win,Point(4,4),1.7,1.6,"5")
    b6 = button(win,Point(6,4),1.7,1.6,"6")
    b7 = button(win,Point(2,6),1.7,1.6,"7")
    b8 = button(win,Point(4,6),1.7,1.6,"8")
    b9 = button(win,Point(6,6),1.7,1.6,"9")
    bDot = button(win,Point(4,0.0),1.7,1.6,".")
    bPi=button(win,Point(6,0.0),1.4,1.4,"Pi")
    bE=button(win,Point(7.6,0.0),1.4,1.4,"e")

    bMul = button(win,Point(7.75,3.0),1.4,1,"*")    
    bDiv = button(win,Point(9.25,3.0),1.4,1,"/")
    bPlus = button(win,Point(7.75,1.7),1.4,1,"+")
    bMin = button(win,Point(9.25,1.7),1.4,1,"-")
    bBran1 = button(win,Point(7.75,4.4),1.4,1.0,"(")  
    bBran2 = button(win,Point(9.25,4.4),1.4,1.0,")")  
    bPower = button(win,Point(7.8,8.5),1.2,.9,"^")   
    bSqrt = button(win,Point(9.2,8.5),1.2,.9,"sqrt")  
    bsin = button(win,Point(2,8.5),1.9,.9,"sin")    #sin
    basin = button(win,Point(2,7.4),1.9,.9,"arcsin")    #arcsin
    bcos = button(win,Point(4,8.5),1.9,.9,"cos")    #cos
    bacos = button(win,Point(4.0,7.4),1.9,.9,"arccos")    #arccos
    btan = button(win,Point(6,8.5),1.9,.9,"tan")    #tan
    batan = button(win,Point(6.0,7.4),1.9,.9,"arctan")    #arctan
    bsinh =  button(win,Point(2.0,10.7),1.9,.9,"sinh")
    basinh =  button(win,Point(2.0,9.6),1.9,.9,"arcsinh")
    bcosh =  button(win,Point(4.0,10.7),1.9,.9,"cosh")
    bacosh =  button(win,Point(4.0,9.6),1.9,.9,"arccosh")
    btanh =  button(win,Point(6.0,10.7),1.9,.9,"tanh")
    batanh =  button(win,Point(6.0,9.6),1.9,.9,"arctanh")
    bDel = button(win,Point(8.5,10.0),2.6,1.5,"Del")
    bX = button(win,Point(8.5,7.4),2.6,1.0,"Var: X")
    bInt = button(win,Point(8.5,12),2.6,1.5,"Integrate")


    bAC = button(win,Point(8.5,6),2.9,1.5,"AC")

    bEsc = button(win,Point(9.8,14.6),.4,.4,"X")

    bg = Rectangle(Point(0.5,13.0), Point(9.5,14.5))
    bg.setFill('white')
    bg.draw(win)

    show = Text(Point(5,13.75),"")
    show.draw(win)
    
    p = win.getMouse()
    while not bEsc.clicked(p):
        try:

            p = win.getMouse()

            if b0.clicked(p):
                s = show.getText()
                s = s + "0"
                
                show.setText(s)
                show.setSize(20)
                
                
            elif b1.clicked(p):
                s = show.getText()
                s = s + '1'
                show.setText(s)
                show.setSize(20)
                
            elif b2.clicked(p):
                s = show.getText()
                s = s + '2'
                show.setText(s)
                show.setSize(20)
                
            elif b3.clicked(p):
                s = show.getText()
                s = s + '3'
                show.setText(s)
                show.setSize(20)
            
            elif b4.clicked(p):
                s = show.getText()
                s = s + '4'
                show.setText(s)
                show.setSize(20)

            elif b5.clicked(p):
                s = show.getText()
                s = s + '5'
                show.setText(s)
                show.setSize(20)
                
            elif b6.clicked(p):
                s = show.getText()
                s = s + '6'
                show.setText(s)
                show.setSize(20)
                
            elif b7.clicked(p):
                s = show.getText()
                s = s + '7'
                show.setText(s)
                show.setSize(20)
                
            elif b8.clicked(p):
                s = show.getText()
                s = s + '8'
                show.setText(s)
                show.setSize(20)

                
            elif b9.clicked(p):
                s = show.getText()
                s = s + '9'
                show.setText(s)
                show.setSize(20)

            elif bMul.clicked(p):
                s = show.getText()
                s = s + '*'
                show.setText(s)
                show.setSize(20)        
                    
            elif bDiv.clicked(p):
                s = show.getText()
                s = s + '/'
                show.setText(s)
                show.setSize(20)
                
            elif bPlus.clicked(p):
                s = show.getText()
                s = s + '+'
                show.setText(s)
                show.setSize(20)
                
            elif bMin.clicked(p):
                s = show.getText()
                s = s + '-'
                show.setText(s)
                show.setSize(20)
                
            elif bAC.clicked(p):
                s = ""
                show.setText(s)
                show.setSize(20)

            elif bPi.clicked(p):
                s = show.getText()
                s = s + 'pi'
                show.setText(s)
                show.setSize(20)


            elif bE.clicked(p):
                s = show.getText()
                s = s + 'e'
                show.setText(s)
                show.setSize(20)
                

            elif bBran1.clicked(p):
                s = show.getText()
                s = s + '('
                show.setText(s)
                show.setSize(20)
                
            elif bBran2.clicked(p):
                s = show.getText()
                s = s + ')'
                show.setText(s)
                show.setSize(20)
                
            elif bPower.clicked(p):
                s = show.getText()
                s = s + '**'
                show.setText(s)
                show.setSize(20)

            elif bSqrt.clicked(p):
                s = show.getText()
                s = s + 'sqrt('
                show.setText(s)
                show.setSize(20)
                
            elif bsin.clicked(p):
                s = show.getText()
                s = s + 'sin('
                show.setText(s)
                show.setSize(20)

            elif basin.clicked(p):
                s = show.getText()
                s = s + 'asin('
                show.setText(s)
                show.setSize(20)

            elif bacos.clicked(p):
                s = show.getText()
                s = s + 'acos('
                show.setText(s)
                show.setSize(20)
 
                  
            elif bcos.clicked(p):
                s = show.getText()
                s = s + 'cos('
                show.setText(s)
                show.setSize(20)

            elif btan.clicked(p):
                s = show.getText()
                s = s + 'tan('
                show.setText(s)
                show.setSize(20)
                
            elif batan.clicked(p):
                s = show.getText()
                s = s + 'atan('
                show.setText(s)
                show.setSize(20)

            elif bsinh.clicked(p):
                s = show.getText()
                s = s + 'sinh('
                show.setText(s)
                show.setSize(20)

            elif basinh.clicked(p):
                s = show.getText()
                s = s + 'asinh('
                show.setText(s)
                show.setSize(20)

            elif bcosh.clicked(p):
                s = show.getText()
                s = s + 'cosh('
                show.setText(s)
                show.setSize(20)

            elif bacosh.clicked(p):
                s = show.getText()
                s = s + 'acosh('
                show.setText(s)
                show.setSize(20)

            elif btanh.clicked(p):
                s = show.getText()
                s = s + 'tanh('
                show.setText(s)
                show.setSize(20)
                
            elif batanh.clicked(p):
                s = show.getText()
                s = s + 'atanh('
                show.setText(s)
                show.setSize(20)



            elif bDel.clicked(p):
                s = show.getText()
                if s != "Math Error!":
                    s = s[:-1]
                    show.setText(s)
                    show.setSize(20)
                

            elif bDot.clicked(p):
                s = show.getText()
                s = s + '.'
                show.setText(s)
                show.setSize(20)

            elif bX.clicked(p):
                s = show.getText()
                s = s + 'x'
                show.setText(s)
                show.setSize(20)

            elif bInt.clicked(p):
                s = show.getText()
                a = inte(eval(E1.getText()),eval(E2.getText()),s)
                show.setText(str("%0.2f" % a))
                show.setSize(20)

                
        except:
            show.setText("Math Error!")
            show.setSize(20)
    
    win.close()


def Differ():
    win = GraphWin("Calculator",400,647)
    win.setCoords(0.0,-1.0,10,15)
    drawlabel(win,Point(3.3,12),'arial',8,'bold italic','Differential point')
    E1 = Entry(Point(5.8,12),4)
    E1.draw(win)
       
    b0 = button(win,Point(2,0.0),1.7,1.6,"0")
    b1 = button(win,Point(2,2),1.7,1.6,"1")
    b2 = button(win,Point(4,2),1.7,1.6,"2")
    b3 = button(win,Point(6,2),1.7,1.6,"3")
    b4 = button(win,Point(2,4),1.7,1.6,"4")
    b5 = button(win,Point(4,4),1.7,1.6,"5")
    b6 = button(win,Point(6,4),1.7,1.6,"6")
    b7 = button(win,Point(2,6),1.7,1.6,"7")
    b8 = button(win,Point(4,6),1.7,1.6,"8")
    b9 = button(win,Point(6,6),1.7,1.6,"9")
    bDot = button(win,Point(4,0.0),1.7,1.6,".")
    bPi=button(win,Point(6,0.0),1.4,1.4,"Pi")
    bE=button(win,Point(7.6,0.0),1.4,1.4,"e")

    bMul = button(win,Point(7.75,3.0),1.4,1,"*")    
    bDiv = button(win,Point(9.25,3.0),1.4,1,"/")
    bPlus = button(win,Point(7.75,1.7),1.4,1,"+")
    bMin = button(win,Point(9.25,1.7),1.4,1,"-")
    bBran1 = button(win,Point(7.75,4.4),1.4,1.0,"(")  
    bBran2 = button(win,Point(9.25,4.4),1.4,1.0,")")  
    bPower = button(win,Point(7.8,8.5),1.2,.9,"^")   
    bSqrt = button(win,Point(9.2,8.5),1.2,.9,"sqrt")  
    bsin = button(win,Point(2,8.5),1.9,.9,"sin")    #sin
    basin = button(win,Point(2,7.4),1.9,.9,"arcsin")    #arcsin
    bcos = button(win,Point(4,8.5),1.9,.9,"cos")    #cos
    bacos = button(win,Point(4.0,7.4),1.9,.9,"arccos")    #arccos
    btan = button(win,Point(6,8.5),1.9,.9,"tan")    #tan
    batan = button(win,Point(6.0,7.4),1.9,.9,"arctan")    #arctan
    bsinh =  button(win,Point(2.0,10.7),1.9,.9,"sinh")
    basinh =  button(win,Point(2.0,9.6),1.9,.9,"arcsinh")
    bcosh =  button(win,Point(4.0,10.7),1.9,.9,"cosh")
    bacosh =  button(win,Point(4.0,9.6),1.9,.9,"arccosh")
    btanh =  button(win,Point(6.0,10.7),1.9,.9,"tanh")
    batanh =  button(win,Point(6.0,9.6),1.9,.9,"arctanh")
    bDel = button(win,Point(8.5,10.0),2.6,1.5,"Del")
    bX = button(win,Point(8.5,7.4),2.6,1.0,"Var: X")
    bDiff = button(win,Point(8.5,12),2.6,1.5,"Differential")


    bAC = button(win,Point(8.5,6),2.9,1.5,"AC")


    bEsc = button(win,Point(9.8,14.6),.4,.4,"X")

    bg = Rectangle(Point(0.5,13.0), Point(9.5,14.5))
    bg.setFill('white')
    bg.draw(win)

    show = Text(Point(5,13.75),"")
    show.draw(win)
    
    p = win.getMouse()
    while not bEsc.clicked(p):
        try:

            p = win.getMouse()

            if b0.clicked(p):
                s = show.getText()
                s = s + "0"
                
                show.setText(s)
                show.setSize(20)
                
                
            elif b1.clicked(p):
                s = show.getText()
                s = s + '1'
                show.setText(s)
                show.setSize(20)
                
            elif b2.clicked(p):
                s = show.getText()
                s = s + '2'
                show.setText(s)
                show.setSize(20)
                
            elif b3.clicked(p):
                s = show.getText()
                s = s + '3'
                show.setText(s)
                show.setSize(20)
            
            elif b4.clicked(p):
                s = show.getText()
                s = s + '4'
                show.setText(s)
                show.setSize(20)

            elif b5.clicked(p):
                s = show.getText()
                s = s + '5'
                show.setText(s)
                show.setSize(20)
                
            elif b6.clicked(p):
                s = show.getText()
                s = s + '6'
                show.setText(s)
                show.setSize(20)
                
            elif b7.clicked(p):
                s = show.getText()
                s = s + '7'
                show.setText(s)
                show.setSize(20)
                
            elif b8.clicked(p):
                s = show.getText()
                s = s + '8'
                show.setText(s)
                show.setSize(20)

                
            elif b9.clicked(p):
                s = show.getText()
                s = s + '9'
                show.setText(s)
                show.setSize(20)

            elif bMul.clicked(p):
                s = show.getText()
                s = s + '*'
                show.setText(s)
                show.setSize(20)        
                    
            elif bDiv.clicked(p):
                s = show.getText()
                s = s + '/'
                show.setText(s)
                show.setSize(20)
                
            elif bPlus.clicked(p):
                s = show.getText()
                s = s + '+'
                show.setText(s)
                show.setSize(20)
                
            elif bMin.clicked(p):
                s = show.getText()
                s = s + '-'
                show.setText(s)
                show.setSize(20)
                
            elif bAC.clicked(p):
                s = ""
                show.setText(s)
                show.setSize(20)

            elif bPi.clicked(p):
                s = show.getText()
                s = s + 'pi'
                show.setText(s)
                show.setSize(20)


            elif bE.clicked(p):
                s = show.getText()
                s = s + 'e'
                show.setText(s)
                show.setSize(20)
                

            elif bBran1.clicked(p):
                s = show.getText()
                s = s + '('
                show.setText(s)
                show.setSize(20)
                
            elif bBran2.clicked(p):
                s = show.getText()
                s = s + ')'
                show.setText(s)
                show.setSize(20)
                
            elif bPower.clicked(p):
                s = show.getText()
                s = s + '**'
                show.setText(s)
                show.setSize(20)

            elif bSqrt.clicked(p):
                s = show.getText()
                s = s + 'sqrt('
                show.setText(s)
                show.setSize(20)
                
            elif bsin.clicked(p):
                s = show.getText()
                s = s + 'sin('
                show.setText(s)
                show.setSize(20)

            elif basin.clicked(p):
                s = show.getText()
                s = s + 'asin('
                show.setText(s)
                show.setSize(20)

            elif bacos.clicked(p):
                s = show.getText()
                s = s + 'acos('
                show.setText(s)
                show.setSize(20)
 
                  
            elif bcos.clicked(p):
                s = show.getText()
                s = s + 'cos('
                show.setText(s)
                show.setSize(20)

            elif btan.clicked(p):
                s = show.getText()
                s = s + 'tan('
                show.setText(s)
                show.setSize(20)
                
            elif batan.clicked(p):
                s = show.getText()
                s = s + 'atan('
                show.setText(s)
                show.setSize(20)

            elif bsinh.clicked(p):
                s = show.getText()
                s = s + 'sinh('
                show.setText(s)
                show.setSize(20)

            elif basinh.clicked(p):
                s = show.getText()
                s = s + 'asinh('
                show.setText(s)
                show.setSize(20)

            elif bcosh.clicked(p):
                s = show.getText()
                s = s + 'cosh('
                show.setText(s)
                show.setSize(20)

            elif bacosh.clicked(p):
                s = show.getText()
                s = s + 'acosh('
                show.setText(s)
                show.setSize(20)

            elif btanh.clicked(p):
                s = show.getText()
                s = s + 'tanh('
                show.setText(s)
                show.setSize(20)
                
            elif batanh.clicked(p):
                s = show.getText()
                s = s + 'atanh('
                show.setText(s)
                show.setSize(20)



            elif bDel.clicked(p):
                s = show.getText()
                if s != "Math Error!":
                    s = s[:-1]
                    show.setText(s)
                    show.setSize(20)
                

            elif bDot.clicked(p):
                s = show.getText()
                s = s + '.'
                show.setText(s)
                show.setSize(20)

            elif bX.clicked(p):
                s = show.getText()
                s = s + 'x'
                show.setText(s)
                show.setSize(20)

            elif bDiff.clicked(p):
                s = show.getText()
                a = diff(eval(E1.getText()),s)
                show.setText(str("%0.2f" % a))
                show.setSize(20)

                
        except:
            show.setText("Math Error!")
            show.setSize(20)
    
    win.close()

    



def chfunc():
    win0=GraphWin('function choose',300,300)
    win0.setBackground('white')
    win0.setCoords(0.0,0.0,40.0,40.0)
    
    drawlabel(win0,Point(20.0,35.0),'arial',12,'bold','Easy-Math Calculator')

    bu1=button(win0,Point(10.0,25.0),14.0,7.0,'')
    drawlabel(win0,Point(10.0,25.0),'arial',9,'bold','BasicOperation')

    bu2=button(win0,Point(30.0,25.0),14.0,7.0,'')
    drawlabel(win0,Point(30.0,25.0),'arial',9,'bold','FunctionGraph')

    bu3=button(win0,Point(10.0,15.0),14.0,7.0,'')
    drawlabel(win0,Point(10.0,15.0),'arial',9,'bold','Integration')
    
    bu4=button(win0,Point(30.0,15.0),14.0,7.0,'')
    drawlabel(win0,Point(30.0,15.0),'arial',9,'bold','Differential')
    
    bu5=button(win0,Point(38.0,38.0),3.0,3.0,'')
    drawlabel(win0,Point(38.0,38.0),'arial',9,'bold','Esc')

    p0 = win0.getMouse()
    while not bu5.clicked(p0):
        try:
            p0=win0.getMouse()
            
            if bu1.clicked(p0):
                win = GraphWin("Calculator",400,647)
                win.setCoords(0.0,-1.0,10,15)
                BasicOpe(win)
                
            elif bu2.clicked(p0):
                FuncGraph()
            elif bu3.clicked(p0):
                Integra()
            elif bu4.clicked(p0):
                Differ()
        except:
                drawlabel(win0,Point(35.0,5.0),'arial',9,'bold','Invaid Click')

        if bu5.clicked(p0):
            win0.close()

    
chfunc()
