
"""BASIC SETUP OF THE GAME
1. Create the screen of some dimensions
2.Title
3.Clock for frame rate

#initialise pygame
#set the screen dimensions for the game
#now create a display surface; assign it to the screen variable;
#set_mode takes a tuple of dimensions
#set a title
#set a clock variable to control the frame rate of the game
#it contains a Clock object
CHECKING FOR EVENTS
create an invisible rectangle ball for the ball position
it won't be visible
it's coordinates are 0,0 - top left of screen
the width and height are 30


"""
import pygame
import sys
import random
def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.x=screen_width/2 - 10
    ball.y = random.randint(10,100)
    ball_speed_x*=random.choice([-1,1])
    ball_speed_y*=random.choice([-1,1])

def point_won(winner):
    global player_points, cpu_points
    if winner == 'cpu':
        cpu_points+=1
    if winner == 'player':
        player_points+=1
    reset_ball()
def animate_ball():
    global ball_speed_x, ball_speed_y
    ball.x+=ball_speed_x
    ball.y+=ball_speed_y  
    #reverse the directions/bounce when it leaves frame
    if ball.bottom>=screen_height or ball.top<=0:
        ball_speed_y*=-1
    if ball.right>=screen_width:
        point_won('cpu')
    if ball.left<=0:
        point_won('player')
        
    if ball.colliderect(player) or ball.colliderect(cpu):
        ball_speed_x*=-1


    
def animate_player():
    global player_speed
    player.y+=player_speed
    if player.top<=0:
        player.top=0
    if player.bottom>=screen_height:
        player.bottom=screen_height
def animate_cpu():
    global cpu_speed
    cpu.y+=cpu_speed
    if ball.centery<=cpu.centery:
        cpu_speed=-6
    if ball.centery>=cpu.centery:
        cpu_speed=6
    if cpu.top<=0:
        cpu.top=0
    if cpu.bottom>=screen_height:
        cpu.bottom=screen_height


pygame.init()



screen_width=1280
screen_height=800
FONT=pygame.font.SysFont("Consolas", int(screen_width/20))

screen=pygame.display.set_mode((screen_width, screen_height),pygame.RESIZABLE)


pygame.display.set_caption("ATARI PONG")


#clock and pos
clock = pygame.time.Clock()
ball=pygame.Rect(0,0,40,40)
ball.center=(screen_width/2, screen_height/2)
#speeds
ball_speed_x=10
ball_speed_y=10
player_speed=1
cpu_speed=0
#points
cpu_points, player_points = 0, 0
score_font=pygame.font.SysFont("Comic Sans", 100)


#control paddle
cpu=pygame.Rect(0,0,20,100)
cpu.centery=(screen_height/2)

#player paddle
player=pygame.Rect(0,0,20,100)
player.midright=(screen_width, screen_height/2)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:#pressed a key
            if event.key == pygame.K_UP:#pressed up arrow
                player_speed=-6
            if event.key == pygame.K_DOWN:
                player_speed=6
        if event.type == pygame.KEYUP:#pressed a key
            if event.key == pygame.K_UP:#pressed up arrow
                player_speed=0
            if event.key == pygame.K_DOWN:
                player_speed=0
   

    animate_ball()
    animate_player()
    animate_cpu()
    screen.fill('black')#clear the traces
    cpu_score_surface=score_font.render(str(cpu_points),True, "white")
    player_score_surface=score_font.render(str(player_points),True, "white")
    screen.blit(cpu_score_surface,(screen_width/4, 20))
    screen.blit(player_score_surface,(3*screen_width/4, 20))
   
    #draw net and game objects
    pygame.draw.line(screen, "red", (screen_width/2,0),(screen_width/2, screen_height), width=3)
    pygame.draw.ellipse(screen, "white",ball)
    pygame.draw.rect(screen,"white",cpu)
    pygame.draw.rect(screen,"white",player)
    pygame.display.update()

    
    clock.tick(60)







            
