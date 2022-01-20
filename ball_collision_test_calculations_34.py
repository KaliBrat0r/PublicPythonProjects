import pygame, sys, math, time, random

def ball_2_steps():
    global x_round_2, y_round_2, distance_2, x_steps_cs_2, y_steps_cs_2, a_2, b_2, x_steps_counter_2, x_steps_2, y_steps_2, angle

    x_steps_cs_2 = x_round_2
    y_steps_cs_2 = y_round_2
    angle_rad = math.radians(angle)
    sin = math.sin(angle_rad)
    cos = math.cos(angle_rad)
    a_2 = cos * distance_2
    b_2 =  sin * distance_2
    distance_2 += speed_2
    x_round_2 = int(round(a_2))
    y_round_2 = int(round(b_2))
    x_steps_2 = x_round_2 - x_steps_cs_2
    y_steps_2 = y_round_2 - y_steps_cs_2

    ball_2.center = ball_2.center[0]+(x_steps_2)*-1, ball_2.center[1]+y_steps_2

def reset_ball_2():
    global a_2, b_2, speed_2, distance_2, x_round_2, y_round_2, x_steps_2
    global y_steps_2, x_steps_cs_2, y_steps_2, y_steps_cs_2, x_steps_counter_2

    a_2 = 0
    b_2 = 0
    speed_2 = 1
    distance_2 = 0
    x_round_2 = 0
    y_round_2 = 0
    x_steps_2 = 0
    y_steps_2 = 0
    x_steps_cs_2 = 0
    y_steps_cs_2 = 0
    x_steps_counter_2 = 0

def draw_2():
    screen.fill((100, 100, 100))
    pygame.draw.rect(screen,color,rect)
    pygame.draw.rect(screen,color,rect_2)
    pygame.draw.rect(screen,color,rect_3)
    pygame.draw.rect(screen,color,rect_4)
    pygame.draw.rect(screen,(255,255,255),ball)
    pygame.draw.rect(screen,(255,0,0),ball_2,2)
    pygame.display.flip()
    time.sleep(0.01)
    # time.sleep(1)

clock = pygame.time.Clock()

screen_height = 960
screen_width = 1280
screen = pygame.display.set_mode((screen_width,screen_height))

# Main attributes to play width
ball_size = 50

rect_thickness = 200

ball_x = screen_width / 2 - ball_size/2

ball_y = screen_height / 2 - ball_size/2 

angle = 45 

speed_1 = 50

ball   = pygame.Rect(ball_x,ball_y, ball_size,ball_size)
ball_2 = pygame.Rect(ball_x,ball_y, ball_size, ball_size)
rect   = pygame.Rect(0,0, rect_thickness,960)
rect_2 = pygame.Rect(1280-rect_thickness,0, rect_thickness,960)
rect_3 = pygame.Rect(0,0, 1280,rect_thickness)
rect_4 = pygame.Rect(0,960-rect_thickness, 1280,rect_thickness)

#region Ball_2 vars.
a_2 = 0
b_2 = 0
speed_2 = 1
distance_2 = 0
x_round_2 = 0
y_round_2 = 0
x_steps_2 = 0
y_steps_2 = 0
x_steps_cs_2 = 0
y_steps_cs_2 = 0
x_steps_counter_2 = 0
#endregion

color = (160,160,160)

collision_color = (0,255,0)

stop_coll_dirchange = False

counter = 0

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    while counter < speed_1:

        if ball_2.colliderect(rect):

            stop_coll_dirchange = True

            reset_ball_2()
            # distance_2 = 0
    
            color = (random.randrange(0,256),random.randrange(0,256),random.randrange(0,256))

            if angle > 360:
                angle -= 180
            else:
                angle += 180

            angle *= -1

            ball_2.x = rect.x+rect_thickness+1

            ball_2_steps()
            
            counter += 1

        if  ball_2.colliderect(rect_2):

            stop_coll_dirchange = True

            reset_ball_2()
            # distance_2 = 0
    
            color = (random.randrange(0,256),random.randrange(0,256),random.randrange(0,256))

            if angle > 360:
                angle -= 180
            else:
                angle += 180

            angle *= -1

            ball_2.x = rect_2.x-ball_size-1
            
            ball_2_steps()
            
            counter += 1

        if ball_2.colliderect(rect_3):

            stop_coll_dirchange = True
            
            reset_ball_2()
            # distance_2 = 0

            color = (random.randrange(0,256),random.randrange(0,256),random.randrange(0,256))

            angle *= -1

            ball_2.y = rect_3.y+rect_thickness+1

            ball_2_steps()
            
            counter += 1
                
        if ball_2.colliderect(rect_4):

            stop_coll_dirchange = True
            
            reset_ball_2()
            # distance_2 = 0

            color = (random.randrange(0,256),random.randrange(0,256),random.randrange(0,256))

            angle *= -1

            ball_2.y = rect_4.y-ball_size-1
        
            ball_2_steps()
            
            counter += 1

        else:
            ball_2_steps()
            
            counter+=1

        if stop_coll_dirchange == True:
            
            print("collision")
                  
            stop_coll_dirchange = False
        
        #!!!!!!!!!!!!!!!!
        draw_2() #delete or comment out this line, if you want full speed
        
        # print(counter) 

    ball.center = ball_2.center

    counter = 0

    screen.fill((100, 100, 100))

    pygame.draw.rect(screen,color,rect)
    pygame.draw.rect(screen,color,rect_2)
    pygame.draw.rect(screen,color,rect_3)
    pygame.draw.rect(screen,color,rect_4)
    pygame.draw.rect(screen,(255,255,255),ball)

    pygame.display.set_caption("fps: "+ str(clock.get_fps())) #show FPS
    pygame.display.flip()
    
    clock.tick(60)

