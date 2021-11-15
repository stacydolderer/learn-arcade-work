import arcade

arcade.open_window(600, 600, "Drawing Example")

# Set the background color
#arcade.set_background_color(arcade.csscolor.SKY_BLUE)
arcade.set_background_color((145, 92, 131))
# Get ready to draw
arcade.start_render()

# (The drawing code will go here.)
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)

# Finish drawing
arcade.finish_render()






arcade.run()