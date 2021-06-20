import copy
import random

class Hat: 
  def __init__(self, **colors):
    self.contents = []
    for k,v in colors.items():
      for x in range(v):
        self.contents.append(k)
  # used this instead of pop, works as intended
  def draw(self, num_balls):
    if num_balls > len(self.contents):
        return self.contents
    balls = []
    for i in range(num_balls):
        random_ball = random.randint(0,(len(self.contents)-1))
        balls.append(self.contents[random_ball])
        self.contents.remove(self.contents[random_ball])
    return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  count = 0
  mid_count = 0

  for i in range(num_experiments):
    expected_balls_copy = copy.deepcopy(expected_balls)
    hat_copy = copy.deepcopy(hat)
    gotten_balls = hat_copy.draw(num_balls_drawn) 
  
    for color in gotten_balls:
      # print(color)
      if color in expected_balls_copy:
        # print(expected_balls_copy[color])
        expected_balls_copy[color] -= 1

    if all(x <= 0 for x in expected_balls_copy.values()):
      count += 1
    
  return count / num_experiments


# hat = Hat(black=6, red=4, green=3)
# print(hat.contents)