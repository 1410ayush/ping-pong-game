# from turtle import Turtle,Screen
# from paddle import Paddle
# from ball import Ball
# from scoreboard import Scoreboard
# import time
# screen=Screen()
# scoreboard=Scoreboard()

# screen.bgcolor("black")
# screen.setup(width=600,height=600)
# screen.title("Pong")
# screen.tracer(0)

# r_paddle=Paddle((280,0))
# l_paddle=Paddle((-280,0))
# ball=Ball()

# screen.listen()
# screen.onkey(r_paddle.go_up,"Up")
# screen.onkey(r_paddle.go_down,"Down")        
# screen.onkey(l_paddle.go_up,"s")
# screen.onkey(l_paddle.go_down,"w")    
# game_is_on=True
# while game_is_on:
#     time.sleep(ball.move_speed)
#     screen.update()
#     ball.move()
#     if ball.ycor()>260 or ball.ycor()<-260:
#         ball.bounce_y()
#     if ball.distance(r_paddle)<50 and ball.xcor()>240 or ball.distance(l_paddle)<50 and ball.xcor()<-240:
#         ball.bounce_x()
#     if ball.xcor()>300:
#         ball.reset_position() 
#         scoreboard.l_point()   

#     if ball.xcor()<-300:
#         ball.reset_position()
#         scoreboard.r_point()
# screen.exitonclick()