# Test data for part 1; claim 1 and claim 2 overlap a total of 4 square inches.
# claims = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
# Part 1 
# Answer should be 101565.
import re

claim_pos_x_list = []
claim_pos_y_list = []
claim_width_list = []
claim_height_list = []

with open("input.txt") as f_handle:
	claims = f_handle.read()
	claims = claims.split("\n")
	for claim in claims:
		claim_rectangle = re.findall("[0-9]+[,x][0-9]+", claim)

		if len(claim_rectangle) == 2:
			claim_pos_x, claim_pos_y = claim_rectangle[0].split(",")
			claim_width, claim_height = claim_rectangle[1].split("x")
			claim_pos_x_list.append(int(claim_pos_x))
			claim_pos_y_list.append(int(claim_pos_y))
			claim_width_list.append(int(claim_width))
			claim_height_list.append(int(claim_height))

# Create full set of coordinates for each claim.
claim_coords_list = []
for idx in range(len(claim_pos_x_list)):
	ideal_height = claim_pos_y_list[idx] + claim_height_list[idx]
	claim_pos_y_tmp = claim_pos_y_list[idx] + 1

	while claim_pos_y_tmp <= ideal_height:
		for w in range(1, claim_width_list[idx] + 1):
			claim_coords_list.append((claim_pos_x_list[idx] + w, claim_pos_y_tmp))

		claim_pos_y_tmp += 1

# Keep track of how often a coordinate occurs.
claim_coords_freqs = dict()
overlaps = 0
for claim_coord in claim_coords_list:
    claim_coords_freqs[claim_coord] = claim_coords_freqs.get(claim_coord, 0) + 1

# Coordinates that occur more than once overlap.
for key, val in claim_coords_freqs.items():
    if val > 1:
        overlaps += 1

print("The number of square inches of fabric within two or more claims is:", overlaps)

# Test data for part 1; claim 3 is the only claim that doesn't overlap with anything.
# claims = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
# Part 2
# Answer should be 656.
import re

claim_pos_x_list = []
claim_pos_y_list = []
claim_width_list = []
claim_height_list = []
claim_id_list = []
claim_area_list = []

with open("input.txt") as f_handle:
	claims = f_handle.read()
	claims = claims.split("\n")
	for claim in claims:
		claim_rectangle = re.findall("[0-9]+[,x][0-9]+", claim)
		claim_id = re.findall("#[0-9]*", claim)
		if len(claim_rectangle) == 2 and len(claim_id) > 0:
			claim_pos_x, claim_pos_y = claim_rectangle[0].split(",")
			claim_width, claim_height = claim_rectangle[1].split("x")
			claim_pos_x_list.append(int(claim_pos_x))
			claim_pos_y_list.append(int(claim_pos_y))
			claim_width_list.append(int(claim_width))
			claim_height_list.append(int(claim_height))
			claim_id_list.append(claim_id[0])
			claim_area_list.append(int(claim_width) * int(claim_height))

# Create full set of coordinates for each claim.
claim_coords_list = []
for idx in range(len(claim_pos_x_list)):
	ideal_height = claim_pos_y_list[idx] + claim_height_list[idx]
	claim_pos_y_tmp = claim_pos_y_list[idx] + 1

	while claim_pos_y_tmp <= ideal_height:
		for w in range(1, claim_width_list[idx] + 1):
			claim_coords_list.append((claim_pos_x_list[idx] + w, claim_pos_y_tmp, claim_id_list[idx]))

		claim_pos_y_tmp += 1

# Keep track of how often a coordinate occurs but also keep track of the claim id alongside the 
# amount of times the coordinate occurs. Example: 
# example_list = [	(1,2, "a"), (1,2, "a"), (1,2, "x"), (1,2, "b"), 
# 					(3,4, "b"), (3,4, "c"), (9,8, "d")	]
#
# Example output -> {(9, 8): [1, ['d']], (1, 2): [4, ['a', 'a', 'x', 'b']], (3, 4): [2, ['b', 'c']]}
claim_coords_freqs = dict()
for claim_coord in claim_coords_list:
	if claim_coord[:2] in claim_coords_freqs:
		claim_coords_freqs[claim_coord[:2]] = [claim_coords_freqs[claim_coord[:2]][0] + 1, claim_coords_freqs[claim_coord[:2]][1] + [claim_coord[-1]]]
	else:
		claim_coords_freqs[claim_coord[:2]] = [1, [claim_coord[-1]]]

# Only keep the coordinates and ids that occur once and that only have one id and tally up how
# often they occur.
# Example output -> {'#1': 12, '#3': 4, '#2': 12}
# The value in the dictionary is the 'area' without the duplicates so it will be less than the 
# original area of the claim.
claim_ids_freqs = dict()
for key, val in claim_coords_freqs.items():
	if val[0] == 1 and len(val[1]) == 1:
		claim_ids_freqs[val[1][0]] = claim_ids_freqs.get(val[1][0], 0) + 1

# Claims that had some duplicate coordinates will have an area less than the original area. 
# The lone intact claim with no duplicate coordinates will have an area exactly the same as the
# original area.
unique_claim_id = None
for key, val in claim_ids_freqs.items():
	claim_idx = claim_id_list.index(key)
	claim_area = claim_area_list[claim_idx]
	if val == claim_area:
		unique_claim_id = key
		break

print("The ID of the only claim that doesn't overlap is:", unique_claim_id)