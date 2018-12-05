# Part 1
# Answer should be 486.
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

# Part 2
# Answer should be 69285.
final_freq = 0
freqs_encountered = {}
dupe_freq_found = False
dupe_freq_key = None
with open("input.txt") as f_handle:
	f_content = f_handle.read()
	freq_vals = f_content.split("\n")
	while not dupe_freq_found:
		for freq_val in freq_vals:
			if dupe_freq_found:
				break	
			if "+" in freq_val:
				symbol, number = freq_val.split("+")
				final_freq += int(number)
			elif "-" in freq_val:
				symbol, number = freq_val.split("-")
				final_freq -= int(number)
			else:
				continue
			current_freq_val = freqs_encountered.get(final_freq, 0) + 1
			if current_freq_val == 2:
				dupe_freq_found = True 
				dupe_freq_key = final_freq
			else:
				freqs_encountered[final_freq] = current_freq_val	
print("The first frequency that the device reaches twice is:", dupe_freq_key)