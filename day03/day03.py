# Test data for part 1; claim 1 and claim 2 overlap a total of 4 square inches.
# #1 @ 1,3: 4x4
# #2 @ 3,1: 4x4
# #3 @ 5,5: 2x2
# Translates to the following:
# claim_pos_x_list = [1, 3, 5]
# claim_pos_y_list = [3, 1, 5]
# claim_width_list = [4, 4, 2]
# claim_height_list = [4, 4, 2]
# Part 1 
# Answer should be
import re
claim_pos_x_list = []
claim_pos_y_list = []
claim_width_list = []
claim_height_list = []
with open("input.txt") as f_handle:
	claims = f_handle.read()
	claims = claims.split("\n")
	for claim in claims:
		claim_rectangle = findall("[0-9].[0-9]", claim)
		claim_pos_x, claim_pos_y = claim_rectangle[0].split(",")
		claim_width, claim_height = claim_rectangle[1].split("x")
		claim_pos_x_list.append(claim_pos_x)
		claim_pos_y_list.append(claim_pos_y)
		claim_width_list.append(claim_width)
		claim_height_list.append(claim_height)

claim_coords_list = []
for idx in range(len(claim_pos_x_list)):
    ideal_height = claim_pos_y_list[idx] + claim_height_list[idx]
    claim_pos_y_tmp = claim_pos_y_list[idx]
    while claim_pos_y_tmp < ideal_height:
        for w in range(claim_width_list[idx]):
            claim_coords_list.append((claim_pos_x_list[idx] + w, claim_pos_y_tmp))
        claim_pos_y_tmp += 1


print(len(set(claim_coords_list)))
print(len(claim_coords_list) -len(set(claim_coords_list)))