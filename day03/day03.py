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

claim_coords_list = []
for idx in range(len(claim_pos_x_list)):
	ideal_height = claim_pos_y_list[idx] + claim_height_list[idx]
	claim_pos_y_tmp = claim_pos_y_list[idx] + 1

	while claim_pos_y_tmp <= ideal_height:
		for w in range(1, claim_width_list[idx] + 1):
			claim_coords_list.append((claim_pos_x_list[idx] + w, claim_pos_y_tmp))

		claim_pos_y_tmp += 1

claim_coords_freqs = dict()
overlaps = 0
for claim_coord in claim_coords_list:
    claim_coords_freqs[claim_coord] = claim_coords_freqs.get(claim_coord, 0) + 1

for key, val in claim_coords_freqs.items():
    if val > 1:
        overlaps += 1

print("The number of square inches of fabric within two or more claims is:", overlaps)