import argparse

# Define argument parser and output strings
parser = argparse.ArgumentParser(description="Chess Coding Exercise.")
parser.add_argument("--piece", help="Type of chess piece (Queen, Rook, Knight)")
parser.add_argument("--position", help="Current position on chess board (for example: d2)")
args = parser.parse_args()
piece = args.piece
position = args.position

# Define main function
def execute_chessercise(piece):
  # Validate the passed-in piece is either Queen, Rook, or Knight
  if piece == "Queen": return queen()
  if piece == "Rook": return rook()
  if piece == "Knight": return knight()
  
  # valid piece was not passed in, return error
  print "Invalid piece type.  Must be Queen, Rook, or Knight." 

# Define piece-specific functions
def queen():
  steps = []
  steps.extend(move(position, '+', 0, '', '*'))
  steps.extend(move(position, '', '*', '+', 0))
  steps.extend(move(position, '', '*', '', '*'))

  # Remove position from array
  while position in steps: steps.remove(position)
 
  print ', '.join(steps)

def rook():
  steps = []
  steps.extend(move(position, '+', 0, '', '*'))
  steps.extend(move(position, '', '*', '+', 0))
  steps.extend(move(position, '', '*', '', '*'))

  # Remove position from array
  while position in steps: steps.remove(position)
 
  print ', '.join(steps)
  pos = list(position)

def knight():
  steps = []
  steps.extend(move(position, '+', 1, '-', 2))
  steps.extend(move(position, '+', 1, '+', 2))
  steps.extend(move(position, '-', 1, '-', 2))
  steps.extend(move(position, '-', 1, '+', 2))
  steps.extend(move(position, '+', 2, '-', 1))
  steps.extend(move(position, '+', 2, '+', 1))
  steps.extend(move(position, '-', 2, '-', 1))
  steps.extend(move(position, '-', 2, '+', 1))

  # Remove position from array
  while position in steps: steps.remove(position)
 
  print ', '.join(steps)

# Define movement functions
def move(current_pos, x_dir, x_offset, y_dir, y_offset):
  x_pos = []
  y_pos = []
  new_pos = []

  # Split current position into column and row
  pos = list(current_pos)

  # Handle wildcards
  if x_offset == '*' and y_offset == '*':
    # Get steps FL from current position
    if pos[0] != 'a':
      x_start = ord('a')
      x_end = ord(pos[0])
      y_count = int(pos[1]) + 1
      for x in range(x_start, x_end):
        x_pos.append(chr(x))
      while len(y_pos) < len(x_pos): 
        y_pos.append(y_count)
        y_count += 1

      # Reverse y_pos array
      y_pos.sort(reverse=True)

    # Get steps FR from current position
    if pos[0] != 'h':
      x_start = ord(pos[0]) + 1
      x_end = ord('i')
      y_count = int(pos[1]) + 1
      for x in range(x_start, x_end):
        x_pos.append(chr(x))
      while len(y_pos) < len(x_pos): 
        y_pos.append(y_count)
        y_count += 1

    for i in range(0, len(x_pos)):
      # Add to array as long as y_pos element is in between 1 and 8
      if y_pos[i] in range(0,9):
        new_pos.append(x_pos[i] + str(y_pos[i]))

    return new_pos

  if x_offset == '*' and y_offset != '*':
    x_pos = list('abcdefgh')

  if y_offset == '*' and x_offset != '*':
    y_pos = list('12345678')

  # Determine new column after offset (x_offset)
  if x_dir == "+" and x_offset != '*':
    col = chr(ord(pos[0]) + x_offset)
    if ord(col) > ord('h'):
      x_pos.append('z')
    else:
      x_pos.append(col)
  if x_dir == "-" and x_offset != '*':
    col = chr(ord(pos[0]) - x_offset)
    if ord(col) <  ord('a'):
      x_pos.append('z')
    else:
      x_pos.append(col)

  # Determine new row after offset (y_offset)
  if y_dir == '+' and y_offset != '*':
    row = int(pos[1]) + y_offset
    if row > 8:
      y_pos.append(0)
    else:
      y_pos.append(row)
  if y_dir == '-' and y_offset != '*':
    # If offset is greater than pos[1], out of limit
    if (y_offset) >= int(pos[1]):
      y_pos.append(0)
    else:
      row = (int(pos[1]) - (y_offset))
      print str(row) + str(int(pos[1]))
      y_pos.append(row)

  # Join x_pos and y_pos to create the space
  for x in x_pos:
    for y in y_pos:
      if x != "z" and y != 0:
        new_pos.append(x + str(y))
   
  return new_pos

# Run program
execute_chessercise(piece)
