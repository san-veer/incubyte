def move_forward(position, direction):
   if direction == "N":
      position[1] += 1

def move_backward(position, direction):
   return

def turn_left(position, direction):
   return

def turn_right(direction):
   if direction == 'N':
      return 'E'

def turn_up(position, direction):
   return

def turn_down(position, direction):
   return

def chandrayaan_3(position, direction, commands):
   for command in commands:
      if command == "f":
         move_forward(position, direction)
      if command == "r":
         direction = turn_right(direction)

   return position, direction