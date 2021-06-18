import copy
import random
# Consider using the modules imported above.
# mostly will be using the random module

class Hat: 
  # def __init__(self, red=None, blue=None, yellow=None, green=None, orange=None, black=None, pink=None, striped=None):
  #   self.red = red
  #   self.blue = blue
  #   self.blue = blue
  #   self.yellow = yellow
  #   self.green = green
  #   self.orange = orange
  #   self.black = black
  #   self.pink = pink
  #   self.striped = striped
  
  def __init__(self, **colors):
    self.contents = []
    print(colors)
    for k,v in colors.items():
      for x in range(v):
        self.contents.append(k)
  
  def draw(self, numOfBalls):
    if numOfballs > len(self.contents):
      return self.contents



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  def getstff():
    print('stff')


newhat = Hat(red=2, blue=4)
print(newhat.contents)

  

