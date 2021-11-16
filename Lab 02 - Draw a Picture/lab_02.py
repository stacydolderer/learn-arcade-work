"""
This is my first drawing program with Python Arcade
"""
import arcade

arcade.open_window(600, 600, "Draw a Picture")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
