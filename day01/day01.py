import re
finalFreq = 0
with open("input.txt") as f_handle:
	f_content = f_handle.read()
	subtractFreqs = re.findall("-[0-9]*", f_content)
	addFreqs = re.findall("\\+[0-9]*", f_content)
	for sub in subtractFreqs:
		finalFreq -= int(sub.split("-")[1])
	for add in addFreqs:
		finalFreq += int(add.split("+")[1])	
print("The final frequency value is:", finalFreq)			
				
