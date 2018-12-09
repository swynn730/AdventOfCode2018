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
				polymer.pop(next_idx)	
				polymer.pop(current_idx)
				polymer_length = len(polymer)			
				non_reaction_counter = 0
				continue

		# No reaction...check the next pair of elements.
		non_reaction_counter += 1

units_remaining = len(polymer)

print("After fully reacting the polymer the amount of units that remain are:", units_remaining)