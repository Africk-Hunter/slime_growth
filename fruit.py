import random


class Fruit:

  def __init__(self):
    types = ['growth', 'power']
    self.type = random.choice(types)
    self.modifier = random.uniform(1.1, 2)
