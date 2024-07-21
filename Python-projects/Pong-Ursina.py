from ursina import *
app = Ursina()
# Set up the game window
window.title = "Pong"
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.color = color.black
Text(text='Press spacebar to pause', position=(0, -0.35), scale=1, origin=(0, 0), color=color.cyan)
Text(text='Press enter to reset', position=(0, -0.40), scale=1, origin=(0, 0), color=color.cyan)
Text(text='Player 1: W/S to move    Player 2: I/K to move', position=(0, -0.45), scale=1.5, origin=(0, 0), color=color.cyan)
# Constants
ball_speed = 2
paddle_speed = 5
# Create paddles
left_paddle = Entity(model='quad', color=color.cyan, scale=(0.1, 0.5), x=-2.1, collider='box')
right_paddle = Entity(model='quad', color=color.cyan, scale=(0.1, 0.5), x=2.1, collider='box')
# Create ball
ball = Entity(model='circle', color=color.cyan, scale=0.15, collider='box')
ball.velocity = Vec3(ball_speed, ball_speed, 0)
ball.position = (0, 0)
ball_moving = False
# Create walls
wall_top = Entity(model='quad', color=color.white, scale=(4, 0.1), y=1,collider='box')
wall_bottom = Entity(model='quad', color=color.white, scale=(4, 0.1), y=-1,collider='box')
# Create Pause Text and variable
paused = False
pause_text = Text(text='Paused', position=(0, 0), scale=2, origin=(0, 0), background=True)
pause_text.enabled = False
# Score variables
left_score = 0
right_score = 0
score_text = Text(text=f'{left_score} - {right_score}', position=(0, 0.3), scale=3, origin=(0, 0), color=color.cyan)
# Function to update the score text
def update_score():
    score_text.text = f'{left_score} - {right_score}'
# Function to reset the ball
def reset_ball():
    ball.x = 0
    ball.y = 0
    ball.velocity = Vec3(ball_speed, ball_speed, 0)

# Update function
def update():
    global ball_moving, paused
    if paused:
        return
    # Move paddles
    if held_keys['w'] and left_paddle.y < 0.8:
        left_paddle.y += paddle_speed * time.dt
    if held_keys['s'] and left_paddle.y > -0.8:
        left_paddle.y -= paddle_speed * time.dt
    if held_keys['i'] and right_paddle.y < 0.8:
        right_paddle.y += paddle_speed * time.dt
    if held_keys['k'] and right_paddle.y > -0.8:
        right_paddle.y -= paddle_speed * time.dt

    # Start ball movement on first input
    if not ball_moving:
        if any((held_keys[key] for key in ['w', 's', 'i', 'k'])):
            ball_moving = True
    # Update ball position only if moving already
    if ball_moving:
        ball.x += ball.velocity.x * time.dt
        ball.y += ball.velocity.y * time.dt

    # Ball collision with top and bottom walls
    if ball.intersects(wall_top):
        ball.velocity.y = -abs(ball.velocity.y)
        ball.y = wall_top.y - wall_top.scale_y
    if ball.intersects(wall_bottom):
        ball.velocity.y = abs(ball.velocity.y) 
        ball.y = wall_bottom.y + wall_bottom.scale_y 

    # Ball collision with paddles
    if ball.intersects(left_paddle):
        ball.velocity.x = abs(ball.velocity.x)
        ball.x = left_paddle.x + left_paddle.scale_x
    if ball.intersects(right_paddle):
        ball.velocity.x = -abs(ball.velocity.x)
        ball.x = right_paddle.x - right_paddle.scale_x

    # Ball out of bounds (scoring)
    if ball.x > 2.1:
        global left_score
        left_score += 1
        update_score()
        reset_ball()
    elif ball.x < -2.1:
        global right_score
        right_score += 1
        update_score()
        reset_ball()

# Use space key to pause game
def input(key):
    global ball_moving, paused, pause_text, left_score, right_score
    if key == 'space' and not paused:
        ball_moving = False
        pause_text.enabled = True
        paused = True
    elif key == 'space' and paused:
        ball_moving = True
        pause_text.enabled = False
        paused = False
    if key == 'enter':
        left_score = 0
        right_score = 0
        ball_moving = False
        update_score()
        reset_ball()

# Run the game
app.run()