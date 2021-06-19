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
  
  # def draw(self, number):
  #   if number > len(self.contents):
  #     return self.contents
  #   for x in range(number):
  #     self.contents.remove(random.choice(self.contents))
  #   return self.contents

  def draw(self, number):
    allPopped = []
    if number > len(self.contents):
      return self.contents
    for x in range(number):
      popped  = self.contents.pop(random.randint(0,len(newhat.contents)))
      allPopped.append(popped)
    return allPopped


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

# with every draw done check if the allpopped list contains, if so add one to count and the divide the count to num_experiments
  



hat = Hat(black=6, red=4, green=3)
print(hat.contents)