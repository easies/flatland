import pyglet
from pyglet.graphics import *
from cocos.director import director
from cocos.scene import Scene
from cocos.layer import Layer
from cocos.path import Path
from cocos.draw import Line
import math
from math import cos, sin


class Blah(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.side = 20
        self.a = (sin(54.0 / 360 * 2 * math.pi) /
                  sin(72.0 / 360 * 2 * math.pi)) * self.side

    def add_speed(self, dx, dy):
        self.speed_x += dx
        self.speed_y += dy

    def vertices(self):
        side = self.side
        x = self.x
        y = self.y
        t = 216.0 / 360 * 2 * math.pi
        acc = [x, y, x + self.a * cos(t), y + self.a * sin(t)]
        for i in range(0, 5):
            # FIXME messy.
            acc.append(acc[-2] + side * cos(i / 5.0 * 2 * math.pi))
            acc.append(acc[-2] + side * sin(i / 5.0 * 2 * math.pi))
        return acc

    def draw(self):
        pyglet.graphics.draw(7, pyglet.gl.GL_TRIANGLE_FAN,
            ('v2f', self.vertices()))


blah = Blah(0, 0)


class EventLayer(Layer):
    is_event_handler = True

    def __init__(self):
        super(EventLayer, self).__init__()

    def on_key_press(self, key, modifiers):
        print key, modifiers
        if key == 65361: # left
            blah.add_speed(-1, 0)
        elif key == 65362: # up
            blah.add_speed(0, 1)
        elif key == 65363: # right
            blah.add_speed(1, 0)
        elif key == 65364: # down
            blah.add_speed(0, -1)

    def on_key_release(self, key, modifiers):
        print key, modifiers

    def on_mouse_motion(self, x, y, dx, dy):
        print x, y, dx, dy
        blah.x = x
        blah.y = y

    def on_mouse_press(self, x, y, buttons, modifiers):
        print x, y, buttons, modifiers

    def on_mouse_release(self, x, y, buttons, modifiers):
        print x, y, buttons, modifiers


class HelloLayer(Layer):

    def __init__(self):
        super(HelloLayer, self).__init__()
        self.text = pyglet.text.Label('Hello, world',
            font_size=32,
            x=5,
            y=director.get_window_size()[1],
            anchor_x=pyglet.font.Text.LEFT,
            anchor_y=pyglet.font.Text.TOP)

    def draw(self):
        super(HelloLayer, self).draw()
        self.text.draw()
        pyglet.graphics.draw(3, pyglet.gl.GL_TRIANGLES,
            ('v2i', (0, 0, 100, 0, 100, 100)))
        Line((100, 100), (200, 200), (255, 255, 255, 255)).draw()
        blah.draw()


if __name__ == '__main__':
    director.init(caption='Flatland', width=800, height=600)
    director.show_FPS = True
#    director.window.set_fullscreen(True)
    director.run(Scene(HelloLayer(), EventLayer()))
