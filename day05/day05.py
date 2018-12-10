# Test data for part 1; The resulting polymer contains 10 units.
# dabAcCaCBAcCcaDA  The first 'cC' is removed.
# dabAaCBAcCcaDA    This creates 'Aa', which is removed.
# dabCBAcCcaDA      Either 'cC' or 'Cc' are removed (the result is the same).
# dabCBAcaDA        No further actions can be taken.
# More detail:
	# +	In aA, a and A react, leaving nothing behind.
	# +	In abBA, bB destroys itself, leaving aA. As above, this then destroys itself, 
	# 	leaving nothing.
	# +	In abAB, no two adjacent units are of the same type, and so nothing happens.
	# +	In aabAAB, even though aa and AA are of the same type, their polarities match, 
	# 	and so nothing happens.
#polymer = "dabAcCaCBAcCcaDA"

# Part 1 
# Answer should be 10762.

with open("input.txt") as f_handle:
	polymer = f_handle.read().strip()

# Making this a mutable list makes it much easier to process.
polymer = list(polymer)

isStillReacting = True
non_reaction_counter = 0

# Continually compares the value of the current and upcoming element in the polymer sequence.
while (isStillReacting):
	polymer_length = len(polymer)

	for current_idx in range(polymer_length):
		next_idx = current_idx + 1

		# The whole polymer sequence was traversed and there were no more reactions to process.
		if non_reaction_counter >= polymer_length - 1:
			isStillReacting = False

		# To prevent from running out of elements to compare; start from the beginning.	
		if next_idx > polymer_length - 1:
			break

		current_char = polymer[current_idx]
		next_char = polymer[next_idx]

		# Possible reaction...	
		if current_char.lower() == next_char.lower():

			# This is a reaction; so remove the reactive elements.
			# The next element has to be removed before the current element to prevent an index out of range error.
			# Finally, since a reaction did in fact happen, reset the counter and then resume processing the elements.
			if ( current_char.isupper() and next_char.islower() ) or ( current_char.islower() and next_char.isupper() ):		
				del polymer[next_idx]
				del polymer[current_idx]
				polymer_length = len(polymer)			
				non_reaction_counter = 0
				continue

		# No reaction...check the next pair of elements.
		non_reaction_counter += 1

units_remaining = len(polymer)

print("After fully reacting the polymer the amount of units that remain are:", units_remaining)

# Test data for part 1; The length of the shortest polymer able to be produced is 4 units.
# Removing all A/a units produces dbcCCBcCcD. 
# 	Fully reacting this polymer produces dbCBcD, which has length 6.
# Removing all B/b units produces daAcCaCAcCcaDA. 
# 	Fully reacting this polymer produces daCAcaDA, which has length 8.
# Removing all C/c units produces dabAaBAaDA. 
# 	Fully reacting this polymer produces daDA, which has length 4.
# Removing all D/d units produces abAcCaCBAcCcaA. 
# 	Fully reacting this polymer produces abCBAc, which has length 6.
# In this example, removing all C/c units was best, producing the answer 4.
# polymer = "dabAcCaCBAcCcaDA"

# Part 2
# Answer should be 6946.

with open("input.txt") as f_handle:
	polymer = f_handle.read().strip()

# Making this a mutable list makes it much easier to process.
polymer = list(polymer)

# The characters/elements used in the polymer sequence. Keep track of only the lower case elements. 
polymer_chars = {}
for char in polymer:
	if char.islower():
		polymer_chars[char] = polymer_chars.get(char, 0) + 1

# The lower case characters from the dictionary are the only ones worth checking.
# Only do lower case so that the list only has a length of 26 and not 52.
chars_to_try_removing = "".join(polymer_chars.keys())

modified_polymers = [] 

# Traverse a copy of the polymer and remove the character pair (A/a) that might be the troublesome unit.
# Have to do this in reverse so that an index out of range error doesn't occur.
# The modified polymer with the missing character pair gets added to a list.
# The list will be traversed, each item in the list reacted and then the length of each resulting reacted polymer compared.
# The smallest length is the most efficient.
# NOTE: There has to be a better way of doing this besides trying all 26 characters.
# This is the very definition of brute forcing and it feels gross...
for char_to_try_removing in chars_to_try_removing:
	polymer_temp = polymer[:]
	count = len(polymer_temp) - 1
	while count > -1:
		if ( polymer_temp[count] == char_to_try_removing ) or ( polymer_temp[count] == char_to_try_removing.upper() ):
			del polymer_temp[count]
		count -=1
	modified_polymers.append(polymer_temp)		

units_remaining = None
idx_of_troublesome_unit = None

for modified_polymer_idx, modified_polymer in enumerate(modified_polymers):
	isStillReacting = True
	non_reaction_counter = 0

	# Continually compares the value of the current and upcoming element in the polymer sequence;
	# for each modified polymer in the list with the potential troublesome character pair/unit removed.
	while (isStillReacting):
		modified_polymer_length = len(modified_polymer)

		for current_idx in range(modified_polymer_length):
			next_idx = current_idx + 1

			# The whole polymer sequence was traversed and there were no more reactions to process.
			if non_reaction_counter >= modified_polymer_length - 1:
				isStillReacting = False

			# To prevent from running out of elements to compare; start from the beginning.	
			if next_idx > modified_polymer_length - 1:
				break

			current_char = modified_polymer[current_idx]
			next_char = modified_polymer[next_idx]

			# Possible reaction...	
			if current_char.lower() == next_char.lower():

				# This is a reaction; so remove the reactive elements.
				# The next element has to be removed before the current element to prevent an index out of range error.
				# Finally, since a reaction did in fact happen, reset the counter and then resume processing the elements.
				if ( current_char.isupper() and next_char.islower() ) or ( current_char.islower() and next_char.isupper() ):		
					del modified_polymer[next_idx]
					del modified_polymer[current_idx]
					modified_polymer_length = len(modified_polymer)			
					non_reaction_counter = 0
					continue

			# No reaction...check the next pair of elements.
			non_reaction_counter += 1

	if units_remaining == None:
		units_remaining = len(modified_polymer)
		idx_of_troublesome_unit = modified_polymer_idx
	else:
		if len(modified_polymer) < units_remaining:
			units_remaining = len(modified_polymer)
			idx_of_troublesome_unit = modified_polymer_idx	

print("The length of the shortest polymer able to be produced is:", units_remaining)
lower_case_char = chars_to_try_removing[idx_of_troublesome_unit]
upper_case_char = chars_to_try_removing[idx_of_troublesome_unit].upper()
print("The most troublesome unit/char pair in this polymer is:", lower_case_char, "/", upper_case_char)