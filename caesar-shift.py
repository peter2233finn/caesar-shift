# Author: Peter Finn C16407722
# Tested on python 1,2,3

import sys
if len(sys.argv) != 3:
  print("Invalid number of arguements")
  print("Usage: python lab2.py [cipher number] [path to file]")
  exit()
fileDirectory=str(sys.argv[2])
shiftNum=int(sys.argv[1]) # var shiftNum is the number of shifts

def doShift(value, shift):
	done = value + shift % 90
	if done > 90:
		done -= 26
	return done

if __name__ == "__main__":
	
	with open(fileDirectory,"r") as file:	# opens the file
		while True:
			character = file.read(1)
			if not character:
			  break
			unicode = ord(character.upper())

			if unicode <= 90 and unicode >= 65:
				result = chr(doShift(unicode, shiftNum))
			else:
				result = chr(unicode) # Converts unicode ID back to char
			sys.stdout.write(result)
