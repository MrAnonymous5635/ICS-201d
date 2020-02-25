import arcade
import random
import math

WIDTH = 800
HEIGHT = 600

window = arcade.Window(WIDTH, HEIGHT, "My Arcade Game")
arcade.set_background_color(arcade.color.BLACK)

# Initialize your variables here
circle_x = WIDTH/2
circle_y = HEIGHT/2
circle_r = 25
count = 0
text = 0 


@window.event("on_draw")
def game_loop():
    # import global variables here.
    global circle_x, circle_y, circle_r, count, text
    # update your variables here.

    # Draw things here.
    arcade.start_render()
    arcade.draw_circle_filled(circle_x, circle_y, circle_r, arcade.color.RUSTY_RED)
    arcade.draw_text(f"SCORE: {text}", WIDTH - 450, HEIGHT * 0.8, arcade.color.RED_ORANGE   , 24)


@window.event
def on_mouse_press(mouse_x, mouse_y, button, modifiers):
    global circle_r, circle_x, circle_y, count, text
    c = (mouse_x - circle_x)*(mouse_x - circle_x)
    d = (mouse_y - circle_y)*(mouse_y - circle_y)
    if (math.sqrt(c + d)) <= circle_r:
        circle_r += 25
    if math.sqrt(c + d)  > circle_r:
        print ("Miss")
        text = text -1
    if circle_r > 50:
        circle_x = random.randint(50, 750)
        circle_y = random.randint(50, 550)
        circle_r = 25
        count += 1
        text += 1


arcade.run()
