import os
from turtle import Screen, Turtle
from PIL import Image
import random
import winsound
import pygame



LEADERBOARD_FILE = "leaderboard.txt"

#definerar bilderna
chicken = "chickensa.png"
output_chicken = "chickensa.gif"
speed = "ishowspeed.png"
out_speed = "ishowspeed.gif"
_="_.jpg"
out_="_.gif"
backgroundimage="backgroundimage.jpg"
backgroundimage_out="backgroundimage.gif"
candy="candy.png"
output_candy="candy.gif"
level_1pic ="level1.webp"
level_2pic ="level2.webp"
level_3pic ="level3.webp"
level_1pic_out ="level1out.gif"
level_2pic_out ="level2out.gif"
level_3pic_out ="level3out.gif"
speed_pic="speed.webp"
speed_pic_out="speed.gif"


pygame.mixer.init()

background_music = r".\Take it to the edge.wav"
movement_sound = pygame.mixer.Sound(r".\movement2.wav")
eat_sound = pygame.mixer.Sound(r".\eat.wav")
lose_life_sound = pygame.mixer.Sound(r".\skrik.wav")


#skriver ut storlekarna på bilderna 
new_size = (50, 30)
candy_size = (100,50)
background_size=(800,600)
new_size_speed = (250,230)
speed_size=(35,35)
pygame.mixer.init()

background_music = r".\Take it to the edge.wav"
movement_sound = pygame.mixer.Sound(r".\movement2.wav")
eat_sound = pygame.mixer.Sound(r".\eat.wav")
#omformaterar bilderna från png till gid så att det funkar med turtle
if not os.path.exists(output_chicken):
    try:
        img = Image.open(chicken)
        img = img.resize(new_size, Image.Resampling.LANCZOS)  
        img.save(output_chicken, "GIF")
        print(f"Converted and resized {chicken} to {output_chicken} with size {new_size}.")
    except Exception as e:
        print(f"Error processing image: {e}")
        exit()
if not os.path.exists(output_candy):
    try:
        img = Image.open(candy)
        img = img.resize(candy_size, Image.Resampling.LANCZOS)  
        img.save(output_candy, "GIF")
        print(f"Converted and resized {candy} to {output_candy} with size {candy_size}.")
    except Exception as e:
        print(f"Error processing image: {e}")
        exit()
if not os.path.exists(out_speed):
    try:
        img = Image.open(speed)
        img = img.resize(new_size_speed, Image.Resampling.LANCZOS) 
        img.save(out_speed, "GIF")
        print(f"Converted and resized {speed} to {out_speed} with size {new_size}.")
    except Exception as e:
        print(f"Error processing image: {e}")
        exit()
        
if not os.path.exists(out_):
    try:
        img = Image.open(_)
        img = img.resize(new_size_speed, Image.Resampling.LANCZOS)
        img.save(out_, "GIF")
        print(f"Converted and resized {_} to {out_} with size {new_size}.")
    except Exception as e:
        print(f"Error processing image: {e}")
        exit()
if not os.path.exists(level_1pic_out):
    try:
        img = Image.open(level_1pic)
        img = img.resize(background_size, Image.Resampling.LANCZOS)  
        img.save(level_1pic_out, "GIF")
        print(f"Converted and resized {level_1pic} to {level_1pic_out} with size {background_size}.")
    except Exception as e:
        print(f"Error processing image: {e}")
        exit()
if not os.path.exists(level_2pic_out):
    try:
        img = Image.open(level_2pic)
        img = img.resize(background_size, Image.Resampling.LANCZOS)  
        img.save(level_2pic_out, "GIF")
        print(f"Converted and resized {level_2pic} to {level_2pic_out} with size {background_size}.")
    except Exception as e:
        print(f"Error processing image: {e}")
        exit()
if not os.path.exists(level_3pic_out):
    try:
        img = Image.open(level_3pic)
        img = img.resize(background_size, Image.Resampling.LANCZOS)  
        img.save(level_3pic_out, "GIF")
        print(f"Converted and resized {level_3pic} to {level_3pic_out} with size {background_size}.")
    except Exception as e:
        print(f"Error processing image: {e}")
        exit()

if not os.path.exists(speed_pic_out):
    try:
        img = Image.open(speed_pic)
        img = img.resize(speed_size, Image.Resampling.LANCZOS)  
        img.save(speed_pic_out, "GIF")
        print(f"Converted and resized {speed_pic} to {speed_pic_out} with size {new_size}.")
    except Exception as e:
        print(f"Error processing image: {e}")
        exit()


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.y_speed = random.randint(-1, -1)  #sätter bilden på de som faller
        self.set_shape_chicken() 
        self.reset_position()
        

    def set_shape_chicken(self):
        screen = self.getscreen()
        if os.path.exists(output_chicken):
            screen.register_shape(output_chicken)
            self.shape(output_chicken)

    def set_shape_candy(self):
        screen = self.getscreen()
        screen.register_shape(output_candy) 
        self.shape(output_candy) 


    def move(self):
        new_y = self.ycor() + self.y_speed
        self.goto(self.xcor(), new_y)

    def reset_position(self):
        self.goto(random.randint(-300, 300), random.randint(100, 300))  
        self.y_speed = random.randint(-4, -3)
          # bestämmer hastighet på boll
        if scoreboard and scoreboard.score > 24:  
            self.y_speed = random.randint(-7, -4) # höjer hastighet när score ökar
            screen.bgpic("level2out.gif")
            self.shape(output_candy)
        if scoreboard and scoreboard.score > 49:
            self.y_speed=random.randint(-11,-6)
            screen.bgpic("level3out.gif")
            ball.shape(output_chicken) 
        



# Paddle class
class Paddle(Turtle):
    MOVE_DISTANCE = 12  #hastighet på paddeln

    def __init__(self, position):
        super().__init__()
        self.set_shape_speed()
        self.penup()
        self.goto(position)
        self.moving_left = False
        self.moving_right = False
        self.move_task = None
        self.speed_boost_active = False  # kollar om man har fångat en power-up
    
    def activate_speed_boost(self):
        if not self.speed_boost_active:
            self.speed_boost_active = True
            self.MOVE_DISTANCE = 22  # ökar hastighet men power-up
            screen.ontimer(self.deactivate_speed_boost, 5000)  # tar bort power-up efter 5 sekunder

    def deactivate_speed_boost(self):
        self.MOVE_DISTANCE = 12  
        self.speed_boost_active = False

    def set_shape_speed(self):
        screen = self.getscreen()
        if os.path.exists(out_speed):
            screen.register_shape(out_speed)
            self.shape(out_speed)

    def move_left(self):
        if self.moving_left and self.xcor() > -380:
            self.goto(self.xcor() - self.MOVE_DISTANCE, self.ycor())
            self.move_task = screen.ontimer(self.move_left, 30)
              

    def move_right(self):
        if self.moving_right and self.xcor() < 380:
            self.goto(self.xcor() + self.MOVE_DISTANCE, self.ycor())
            self.move_task = screen.ontimer(self.move_right, 30)
              

    def start_moving_left(self):
       if not self.moving_left:  
           self.moving_left = True
           movement_sound.play() 
           self.move_left()

    def start_moving_right(self):
        if not self.moving_right:  
            self.moving_right = True
            movement_sound.play() 
            self.move_right()


    def stop_moving_left(self):
        self.moving_left = False
        if self.move_task:
            screen.ontimer(None, self.move_task)  

    def stop_moving_right(self):
        self.moving_right = False
        if self.move_task:
            screen.ontimer(None, self.move_task) 


    def exit(self): #exit funktion så man avsluta spelet
        exit()




class PowerUp(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(speed_pic_out)  
        self.color("blue")
        self.speed(0)
        self.goto(random.randint(-300, 300), random.randint(100, 300)) 
        self.y_speed = -1 

    def move(self):
        self.goto(self.xcor(), self.ycor() + self.y_speed)

    def reset_position(self):
        self.goto(random.randint(-300, 300), random.randint(100, 300))



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(0, 260)
        self.score = 0
        self.lives = 100
        self.update_display()

    def update_display(self):
        self.clear()
        self.write(f"Score: {self.score} | Lives: {self.lives}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        eat_sound.play()  
        self.score += 1
        self.lives += 5
        if scoreboard.lives >= 100:
            scoreboard.lives = 100
        self.update_display()


    def lose_life(self):
        self.lives -= random.randint(10, 25) #dikterar hur mycket liv man förloarar när man missar och lägger till ljud
        winsound.PlaySound(r".\skrik.wav", winsound.SND_ASYNC)
        self.update_display()

# Load leaderboard
def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as file:
            return [line.strip().split(": ") for line in file.readlines()]
    return []

# Save leaderboard
def save_leaderboard(leaderboard):
    with open(LEADERBOARD_FILE, "w") as file:
        for name, score in leaderboard:
            file.write(f"{name}: {score}\n")


def display_leaderboard(): #skriver ut leaderboard 
    leaderboard = sorted(load_leaderboard(), key=lambda x: int(x[1]), reverse=True)[:5]
    screen.clear()
    screen.bgcolor("white")
    screen.title("Leaderboard")
    writer = Turtle()
    writer.penup()
    writer.hideturtle()
    writer.color("black")
    writer.goto(0, 200)
    writer.write("Leaderboard", align="center", font=("Arial", 24, "bold"))
    y_pos = 150
    for i, (name, score) in enumerate(leaderboard, start=1):
        writer.goto(0, y_pos)
        writer.write(f"{i}. {name}: {score}", align="center", font=("Arial", 18, "normal"))
        y_pos -= 30
    writer.goto(0, y_pos - 50)
    writer.write("Press 'R' to restart", align="center", font=("Arial", 18, "italic"))
    screen.listen()
    screen.onkey(start_game, "r")

#startar turtle
screen = Screen()
screen.bgpic("level1out.gif")
screen.setup(width=800, height=600)
screen.title("Speed catch chicken")
screen.tracer(0)




paddle = None
ball = None
scoreboard = None
player_name = None






def play_background_music():
    winsound.PlaySound(r".\Take it to the edge.wav", winsound.SND_ASYNC | winsound.SND_LOOP)

    
def start_game():
    global paddle, ball, scoreboard, player_name, power_up

    player_name = screen.textinput("Welcome", "Enter your name:")
    if not player_name:
        player_name = "NoName"
    
    screen.register_shape(speed_pic_out)

    screen.clear()
    screen.bgpic("level1out.gif")
    screen.title("Speed Catch Chicken")
    screen.tracer(0)

    screen.register_shape(output_chicken)
    screen.register_shape(output_candy)
    screen.register_shape(out_speed)

    paddle = Paddle(position=(0, -250))
    ball = Ball()
    ball.shape(output_chicken) 
    power_up = PowerUp()
    scoreboard = Scoreboard()

    pygame.mixer.music.load(background_music)
    pygame.mixer.music.play(-1)

    screen.listen()
    screen.onkeypress(paddle.start_moving_left, "Left")
    screen.onkeyrelease(paddle.stop_moving_left, "Left")
    screen.onkeypress(paddle.start_moving_right, "Right")
    screen.onkeyrelease(paddle.stop_moving_right, "Right")
    screen.onkey(paddle.exit, "q")

    animate()




def animate():
    ball.move()
    power_up.move()  

    if ball.ycor() > 290:
        ball.reset_position()

    if ball.ycor() < -230 and abs(ball.xcor() - paddle.xcor()) < 60:
        scoreboard.increase_score()
        ball.reset_position()

    if ball.ycor() < -290:
        scoreboard.lose_life()
        ball.reset_position()

  
    if power_up.ycor() < -230 and abs(power_up.xcor() - paddle.xcor()) < 60:
        paddle.activate_speed_boost()
        power_up.reset_position()

    if power_up.ycor() < -290:
        power_up.reset_position()  

    if scoreboard.lives <= 0:
        end_game()
        return

    screen.update()
    screen.ontimer(animate, 10)

def end_game():
    global player_name
    leaderboard = load_leaderboard()
    leaderboard.append((player_name, str(scoreboard.score)))
    save_leaderboard(leaderboard)
    display_leaderboard()

# startar spelet
start_game()
screen.mainloop()
