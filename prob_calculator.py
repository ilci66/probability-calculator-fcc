import copy
import random

class Hat: 
  
  def __init__(self, **colors):
    self.contents = []
    for k,v in colors.items():
      for x in range(v):
        self.contents.append(k)

  def draw(self, number):
    allPopped = []
    if number > len(self.contents):
      return self.contents
    for x in range(number):
      popped  = self.contents.pop(random.randint(0,len(self.contents)-1))
      allPopped.append(popped)
    return allPopped


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  expected_balls_copy = copy.deepcopy(expected_balls)
  hat_copy = copy.deepcopy(hat)
  gotten_balls = hat_copy.draw(num_balls_drawn) 

  

  count = 0
  wantedballs = []
  for k,v in expected_balls_copy.items():
    print(str(k),v, range(v))
    for i in range(int(v)):
      wantedballs.append(k)

  for i in range(num_experiments):
    expected_balls_copy = copy.deepcopy(expected_balls)
    hat_copy = copy.deepcopy(hat)
    gotten_balls = hat_copy.draw(num_balls_drawn)

    # for x in range(len(wantedballs)):
# implement this logic here out of time for today
# fruits1 = ['Mango','orange','jackfruit']
# fruits2 = ['Mango','orange',]
# # new_list=  all(item in fruits1 for item in fruits2)
# # if new_list is True:
# #     print("True")    
# # else :
# #     print("False")
# count = 0
# for x in range(len(fruits2)):
#   if fruits2[0] in fruits1:
#     print("yep")
#     fruits2.remove(fruits2[0])
#   if len(fruits2) == 0:
#     count += 1 

# print(fruits2, count)

  # for i in range(num_experiments):
  #   check = all(item in wantedballs for item in hat.contents)
  #   if check:
  #     count += 1

  return count / num_experiments

hat = Hat(black=6, red=4, green=3)
print(hat.contents)