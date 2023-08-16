def move_forward(position, direction):
   if direction == "N":
      position[1] += 1
   elif direction == "S":
      position[1] -= 1
   elif direction == "E":
      position[0] += 1
   elif direction == "W":
      position[0] -= 1
   elif direction == "U":
      position[2] += 1
   elif direction == "D":
      position[2] -= 1

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

def turn_down(direction):
   return

def chandrayaan_3(position, direction, commands):
   for command in commands:
      if command == "f":
         move_forward(position, direction)
      elif command == "b":
         move_backward(position, direction)
      elif command == "r":
         direction = turn_right(direction)
      elif command == "l":
         direction = turn_left(direction)
      elif command == "u":
         direction = turn_up(direction)
      elif command == "d":
         direction = turn_down(direction)

   return position, direction