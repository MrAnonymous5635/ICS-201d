import arcade

WIDTH = 800
HEIGHT = 600

window = arcade.Window(WIDTH, HEIGHT, "My Arcade Game")
arcade.set_background_color(arcade.color.SKY_BLUE)

# Initialize your variables here
x = -50
@window.event("on_draw")
def game_loop():
    # import global variables here.
    global x
    # update your variables here.
    x += 0.5
    # Draw things here.
    arcade.start_render()
    y = 300

    arcade.draw_circle_filled(x, y, 27, arcade.color.WHITE)
    arcade.draw_circle_filled(x - 15, y - 25, 27, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 15, y - 25, 27, arcade.color.WHITE)

    arcade.draw_line(50, 50, 200, 100, arcade.color.RED, 10)


arcade.run()
