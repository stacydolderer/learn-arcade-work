import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_grass():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)

def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()

    draw_grass()
    draw_snow_person(on_draw.snow_person1_x, 140)
    draw_snow_person(450, 180)

    if on_draw.snow_person1_x > SCREEN_WIDTH or on_draw.snow_person1_x < 0:
        on_draw.x *= -1
    on_draw.snow_person1_x += on_draw.x

on_draw.x = 1
on_draw.snow_person1_x = 150

def draw_snow_person(x, y):
    # Draw a point at x, y for reference
    #arcade.draw_point(x, y, arcade.color.RED, 5)
    
    # Snow
    arcade.draw_circle_filled(x, 60 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 140 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 200 + y, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(x - 15, 210 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, 210 + y, 5, arcade.color.BLACK)
    


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
 

    #  Finish and run
    arcade.schedule(on_draw, 1/100)
    arcade.run()


main()