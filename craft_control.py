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
   if direction == "N":
      position[1] -= 1
   elif direction == "S":
      position[1] += 1
   elif direction == "E":
      position[0] -= 1
   elif direction == "W":
      position[0] += 1
   elif direction == "U":
      position[2] -= 1
   elif direction == "D":
      position[2] += 1

def turn_right(direction, belly_direction):
   if direction == "N":
      return "E" 
   elif direction == "E":
      return "S"
   elif direction == "S":
      return "W"
   elif direction == "W":
      return "N"
   elif direction == "U" or "D":
      if belly_direction == "N":
         return "E"
      elif belly_direction == "E":
         return "S"
      elif belly_direction == "S":
         return "W"
      elif belly_direction == "W":
         return "N"
   
def turn_left(direction, belly_direction):
   if direction == "N":
      return "W"
   elif direction == "W":
      return "S"
   elif direction == "S":
      return "E"
   elif direction == "E":
      return "N"
   elif direction == "U" or "D":
      if belly_direction == "N":
         return "W"
      elif belly_direction == "W":
         return "S"
      elif belly_direction == "S":
         return "E"
      elif belly_direction == "E":
         return "N"

def turn_up(direction, belly_direction):
   if direction == 'N':
      return 'U', 'N'
   elif direction == 'E':
      return 'U', 'E'
   elif direction == 'S':
      return 'U', 'S'
   elif direction == 'W':
      return 'U', 'W'
   elif direction == 'D':
      return 'U', belly_direction


def turn_down(direction, belly_direction):
   if direction == 'N':
      return 'D', 'N'
   elif direction == 'E':
      return 'D', 'E'
   elif direction == 'S':
      return 'D', 'S'
   elif direction == 'W':
      return 'D', 'W'
   elif direction == 'U':
      return 'D', belly_direction

def chandrayaan_3(position, direction, commands):
   belly_direction = direction
   for command in commands:
      if command == "f":
         move_forward(position, direction)
      elif command == "b":
         move_backward(position, direction)
      elif command == "r":
         direction = turn_right(direction, belly_direction)
      elif command == "l":
         direction = turn_left(direction, belly_direction)
      elif command == "u":
         direction, belly_direction = turn_up(direction, belly_direction)
      elif command == "d":
         direction, belly_direction = turn_down(direction, belly_direction)

   return position, direction