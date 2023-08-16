def move_forward(position, direction):
      position[1] += 1

def move_backward(position, direction):
   return

def turn_left(position, direction):
   return

def turn_right(position, direction):
   return

def turn_up(position, direction):
   return

def turn_down(position, direction):
   return

def chandrayaan_3(position, direction, commands):
   for command in commands:
      if command == "f":
         move_forward(position, direction)

   return position, direction