# Author: Peter Finn C16407722
# Tested on python 1,2,3

import sys
if len(sys.argv) != 3:
  print("Invalid number of arguements")
  print("Usage: python lab2.py [cipher number] [path to file]")
  exit()
fileDirectory=str(sys.argv[2])
shiftNum=int(sys.argv[1]) # var shiftNum is the number of shifts

def doShift(value,shift):
	done = value + shift % 90
	if done > 90:
		done-=26
	return done

with open(fileDirectory,"r") as file1:	# opens the file
	while True:
		charecter = file1.read(1)
		if not charecter:
			break
		charecter=charecter.upper()

		if ord(charecter) <= 90 and ord(charecter) >= 65:
			result=chr(doShift(ord(charecter),shiftNum))
		else:
			result = charecter
		sys.stdout.write(result)
