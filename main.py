import turtle, pyautogui, random, math

s = turtle.Screen()
#1720x961-bg ; player-100x90
s.title("space invaders")
s.bgpic("op1.gif")
s.tracer(0)

turtle.register_shape("player.gif")
turtle.register_shape("enemy.gif")
turtle.register_shape("zgoli.gif")

score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.penup()
score_pen.setposition(-550,-5)
scorestring = "%s" %score
score_pen.write(scorestring, False, align="left", font=("horta", 34, "bold"))
score_pen.hideturtle()

kill = 0
kill_pen =turtle.Turtle()
kill_pen.speed(0)
kill_pen.penup()
kill_pen.setposition(650,-5)
killstring =  "%s"%kill
kill_pen.write(killstring,False,align="left",font=("horta",34,"bold"))
kill_pen.hideturtle()

player = turtle.Turtle()
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-240)
playerspeed = 40

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -230:
        x = -230
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > +230:
        x = +230
    player.setx(x)

def move_up():
    y = player.ycor()
    y += playerspeed
    if y > -150:
        y = -150
    player.sety(y)

def move_down():
    y = player.ycor()
    y -= playerspeed
    if y < -220:
        y = -220
    player.sety(y)

no_of_enemies = 10
enemies = []
for i in range(no_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.shape("enemy.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-240,240)
    y = random.randint(20,240)
    enemy.setposition(x,y)
enemyspeed = 0.09

bullet = turtle.Turtle()
bullet.shape("zgoli.gif")
bullet.penup()
bullet.speed(0)
bulletspeed = 3
bullet.setposition(19990,1900)
bulletstate = "r"
bullet.hideturtle()

def fire_bullet():
    global bulletstate

    if bulletstate == "r":
        bulletstate = "f"
        x = player.xcor()
        y = player.ycor() + 15
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance <35:
        return True
    else : return False

turtle.listen()
turtle.onkeypress(move_left,"Left")
turtle.onkeypress(move_right,"Right")
turtle.onkeypress(move_up,"Up")
turtle.onkeypress(move_down,"Down")
turtle.onkeypress(fire_bullet, "space")

pyautogui.hotkey("win","Up")

while True:
    s.update()
    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        if enemy.xcor() > 240 or enemy.xcor()< -240:
            for e in enemies:
                y = e.ycor()
                y -= 20
                e.sety(y)
            enemyspeed *= -1
        
        if isCollision(bullet, enemy):
            bullet.hideturtle()
            bullet.setposition(19990,1900)
            bulletstate = "r"
            x = random.randint(-240,240)
            y = random.randint(20,240)
            enemy.setposition(x, y)

            kill += 1
            killstring = "%s" %kill
            kill_pen.clear()
            kill_pen.write(killstring, False, align="left", font=("horta", 34, "normal"))

            score += 5
            scorestring = "%s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("horta", 34, "normal"))

        
        if isCollision(player,enemy):
            player.hideturtle()
            for e in enemies:
                e.hideturtle()
        
        for e in enemies:
            if e.ycor() < -200:
                player.hideturtle()
                for e in enemies:
                    e.hideturtle()

    if bulletstate == "f":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
    
    if bullet.ycor() > 260:
        bullet.hideturtle()
        bulletstate="r"
