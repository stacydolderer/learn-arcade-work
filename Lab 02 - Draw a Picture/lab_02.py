"""
This is my first drawing program with Python Arcade
"""
import arcade

arcade.open_window(600, 600, "Draw a Picture")
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
# Set the background color

# Get ready to draw
arcade.start_render()

#drawing code goes in here
#legs
arcade.draw_ellipse_filled(120, 280, 100, 350,(36, 143, 36), 150)
arcade.draw_ellipse_filled(480, 280, 100, 350,(36, 143, 36), 30)
arcade.draw_rectangle_filled(100, 260, 35, 100,(36, 200, 36), 30)
arcade.draw_rectangle_filled(500, 260, 35, 100,(36, 200, 36), 150)
#head
arcade.draw_circle_filled(300, 300, 200, (71, 209, 71))
#eyes
arcade.draw_circle_filled(175, 425, 75, (71, 209, 71))
arcade.draw_circle_filled(425, 425, 75, (71, 209, 71))
arcade.draw_circle_filled(175, 425, 50, (255,255,255))
arcade.draw_circle_filled(425, 425, 50, (255,255,255))
arcade.draw_circle_filled(175, 425, 25, (0,0,0))
arcade.draw_circle_filled(425, 425, 25, (0,0,0))

#nose
arcade.draw_ellipse_filled(260, 350, 20, 30,(36, 143, 36), 45)
arcade.draw_ellipse_filled(340, 350, 20, 30,(36, 143, 36), 315)
#mouth
arcade.draw_arc_outline(300, 250, 200, 150, arcade.csscolor.BLACK, 180, 360, 10)

#front legs
arcade.draw_rectangle_filled(120, 175, 35, 150,(36, 200, 36), 140)
arcade.draw_rectangle_filled(480, 175, 35, 150,(36, 200, 36), 215)

#toes
arcade.draw_rectangle_filled(180, 125, 10, 70, (36, 200, 36), 310)
arcade.draw_rectangle_filled(160, 125, 10, 60, (36, 200, 36), 325)
arcade.draw_rectangle_filled(160, 125, 10, 40, (36, 200, 36), 380)
arcade.draw_circle_filled(150, 90, 15, arcade.csscolor.YELLOW)
arcade.draw_circle_filled(180, 90, 15, arcade.csscolor.YELLOW)
arcade.draw_circle_filled(210, 90, 15, arcade.csscolor.YELLOW)
arcade.draw_circle_filled(450, 90, 15, arcade.csscolor.YELLOW)
arcade.draw_circle_filled(420, 90, 15, arcade.csscolor.YELLOW)
arcade.draw_circle_filled(390, 90, 15, arcade.csscolor.YELLOW)
# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
