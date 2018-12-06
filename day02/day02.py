# Test data for part 1; sums up to 12.
# box_ids = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab", ""]
# Part 1 
# Answer should be 3952.
twice_sum = 0
three_sum = 0
with open("input.txt") as f_handle:
	box_ids = f_handle.read()
	box_ids = box_ids.split("\n")
	for box_id in box_ids:
		box_id_chars = {}
		twice_sum_found = False
		three_sum_found = False
		for char in box_id:
			box_id_chars[char] = box_id_chars.get(char, 0) + 1
		for key, val in box_id_chars.items():
			if val == 2 and not twice_sum_found:
				twice_sum += 1
				twice_sum_found = True
			elif val == 3 and not three_sum_found:
				three_sum += 1	
				three_sum_found = True
check_sum = twice_sum * three_sum
print("The checksum for the list of box IDs is:", check_sum)

# Test data for part 2; the answer is fgij because the difference is one character.
# box_ids = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz", ""]
# Part 2
# Answer should be vtnikorkulbfejvyznqgdxpaw.
from difflib import SequenceMatcher
box_id_01 = None
box_id_02 = None
keepGoing = True
count = 0
with open("input.txt") as f_handle:
	box_ids = f_handle.read()
	box_ids = box_ids.split("\n")
	box_ids_length = len(box_ids)
	box_id_length = len(box_ids[0])
	ideal_ratio = ( box_id_length - 1 ) / box_id_length
	while keepGoing:
		for idx in range(box_ids_length):
			idx_ahead = (idx + 1) % box_ids_length 
			seq = SequenceMatcher(None, box_ids[count], box_ids[idx_ahead])
			if seq.ratio() == ideal_ratio:
				box_id_01 = list(box_ids[count])
				box_id_02 = list(box_ids[idx_ahead])
				keepGoing = False
				break
		count += 1        
		count %= box_ids_length	
for idx, (b01, b02) in enumerate(zip(box_id_01, box_id_02)):
	if b01 != b02:
		box_id_01.pop(idx)
		break
print("The letters common between the two correct box IDs are:","".join(box_id_01))