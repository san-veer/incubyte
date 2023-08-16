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
      return "E", 
   elif direction == "E":
      return "S"
   elif direction == "S":
     return "W"
   elif direction == "W":
      return "N"
   elif direction == "U" and belly_direction == "N":
      return "E", 
   elif direction == "U" and belly_direction == "E":
      return "S"
   elif direction == "U" and belly_direction == "S":
     return "W"
   elif direction == "D" and belly_direction == "W":
      return "N"
   elif direction == "D" and belly_direction == "N":
      return "E", 
   elif direction == "D" and belly_direction == "E":
      return "S"
   elif direction == "D" and belly_direction == "S":
     return "W"
   elif direction == "D" and belly_direction == "W":
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
   if direction == 'U':
      return 'N'

def turn_up(direction, belly_direction):
   if direction == 'E':
      return 'U'
   if direction == "N":
      direction = "U"
   elif direction == "U":
      direction = "S"
   elif direction == "S":
      direction = "D"
   elif direction == "D":
      direction = "N"


def turn_down(direction):
   if direction == "N":
      direction = "D"
   elif direction == "D":
      direction = "S"
   elif direction == "S":
      direction = "U"
   elif direction == "U":
      direction = "N"

def chandrayaan_3(position, direction, commands):
   belly_direction = direction
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