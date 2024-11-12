x=1
y=1
r=0
g=0
b=0
def setup():
    size(1000,1000)
def draw():
    global x,r,y,g,b
    if mousePressed == True:
        if mouseButton == LEFT:
            stroke(r,g,b)
            strokeWeight(x)
            line(pmouseX,pmouseY,mouseX,mouseY)
    noStroke()
    rect(25,100,50,50)
    rect(25,175,50,50)
    rect(25,925,50,50)
    push()
    fill(243,243,241)
    rect(925,925,50,50)
    pop()
    
    push()# черный квадрат
    fill(0,0,0)
    rect(925,100,50,50)
    pop()# черный квадрат
    
    push()#белый квадрат
    fill(243,243,241)
    rect(850,100,50,50)
    pop()# белый квадрат
    
    push()# зеленый квадрат
    fill(0,255,0)
    rect(925,175,50,50)
    pop()# зеленый квадрат
    
    push()# красный квадрат
    fill(255,0,0)
    rect(850,175,50,50)
    pop()# красный квадрат
    
    push()# синий квадрат
    fill(0,0,255)
    rect(925,250,50,50)
    pop()# синий квадрат
    
    push() # желтый квадрат
    fill(255,255,0)
    rect(850,250,50,50)
    pop()# желтый квадрат
    
    push()
    textAlign(CENTER,CENTER)
    textSize(50)       
    fill(0)
    text("+",50,115)
    text("-",50,190)
    pop()
    
    push()
    fill(0)
    textSize(20)
    text(u"Рандомный цвет:",820,900)
    text(u"Выбор ширины:",20,90)
    text(u"Очистить холст:",20,900)
    pop()
def mouseClicked():
    global x,y,r,g,b
    stroke(y)
    
    push()
    if mouseX > 925 and mouseX < 975 and mouseY > 925 and mouseY < 975:# Рандомный цвет
        noStroke()
        rect(925,925,50,50)
        r=random(0,255)
        g=random(0,255)
        b=random(0,255)
    pop()
    
    if mouseX > 25 and mouseX < 75 and mouseY > 925 and mouseY < 975: # Очитска экрана
        background(200)
        
    push()
    if mouseX > 25 and mouseX < 75 and mouseY > 100 and mouseY < 150:# Увеличить толщину
        noStroke()
        rect(25,100,50,50)
        x = x + 1
    if x <= 0:
        x=1
        
    pop()
    
    push()
    if mouseX > 25 and mouseX < 75 and mouseY > 175 and mouseY < 225:# Уменьшить толщину
        noStroke()
        rect(25,175,50,50)
        x = x - 1
    pop()
    
    push()
    if mouseX > 925 and mouseX < 975 and mouseY > 100 and mouseY < 150:# Черный квадрат
        noStroke()
        rect(925,100,50,50)
        r=0
        g=0
        b=0
    pop()
    
    push()
    if mouseX > 850 and mouseX < 900 and mouseY > 100 and mouseY < 150:# Белый квадрат
        noStroke()
        rect(850,100,50,50)
        r=255
        g=255
        b=255
    pop()
    
    push()
    if mouseX > 925 and mouseX < 975 and mouseY > 175 and mouseY < 225:# Зеленый квадрат
        noStroke()
        rect(925,175,50,50)
        r=0
        g=255
        b=0
    pop()
    
    push()
    if mouseX > 850 and mouseX < 900 and mouseY > 175 and mouseY < 225:# Красный квадрат
        noStroke()
        rect(850,175,50,50)
        r=255
        g=0
        b=0
    pop()
    
    push() 
    if mouseX > 925 and mouseX < 975 and mouseY > 250 and mouseY < 300:# Синий квадрат
        noStroke()
        rect(925,250,50,50)
        r=0
        g=0
        b=255
    pop()
    
    push()
    if mouseX > 850 and mouseX < 900 and mouseY > 250 and mouseY < 300:# :Желтый квадрат
        noStroke()
        rect(850,250,50,50)
        r=255
        g=255
        b=0 
    pop()
    
    
