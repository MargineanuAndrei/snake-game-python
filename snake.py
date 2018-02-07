#First file in this app.
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from random import randint
from gi.overrides.Gdk import Window

WIDTH = 35
HEIGHT = 20
MAX_X = WIDTH - 2
MAX_Y = HEIGHT -2
SNAKE_LENGTH = 5
SNAKE_X = SNAKE_LENGTH + 1
SNAKE_Y = 3
TIMEOUT = 100

class Snake(object):
  REV_DIR_MAP = {
    KEY_UP: KEY_DOWN, KEY_DOWN: KEY_UP,
    KEY_RIGHT: KEY_LEFT, KEY_LEFT: KEY_RIGHT,
  }
  
  def __init__(self, x, y, window):
    self.body_list = []
    self.hit_score = 0
    self.timeout = TIMEOUT
    
    for i in range(SNAKE_LENGTH, 0, -1):
      self.body_list.append(Body(x - i, y))
      
    self.body_list.append(Body(x, y, '0'))
    self.window = window
    self.direction = KEY_RIGHT
    self.last_head_coor = (x, y)
    self.direction_map = {
      KEY_UP: self.move_up,
      KEY_DOWN: self.move_down,
      KEY_LEFT: self.move.left,
      KEY_RIGHT: self.move.right
    }
    
  @property
  def score(self):
    return 'Score : {}'.format(self.hit_score)

class Body(object):
  def __init__(self, x, y, char='='):
    self.x = x
    self.y = y
    self.char = char
  
  @property
  def coor(self):
    return self.x, self.y
  
class Food(object):
  def __init__(self):
    self.x = 'this is the'
    
  def method_a(self,foo):
    print(self.x + ' ' + foo)
    
food = Food().method_a('Food')

