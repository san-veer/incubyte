def move_forward(position, direction):
   if direction == "N":
      position[1] += 1

def move_backward(position, direction):
      if direction == "U":
         position[2] -= 1

def turn_left(direction):
   if direction == 'U':
      return 'N'

def turn_right(direction):
   if direction == 'N':
      return 'E'

def turn_up(direction):
   if direction == 'E':
      return 'U'

def turn_down(position, direction):
   return

def chandrayaan_3(position, direction, commands):
   for command in commands:
      if command == "f":
         move_forward(position, direction)
      if command == "b":
         move_backward(position, direction)
      if command == "r":
         direction = turn_right(direction)
      if command == "l":
         direction = turn_left(direction)
      if command == "u":
         direction = turn_up(direction)

   return position, direction