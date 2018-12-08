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
polymer = "dabAcCaCBAcCcaDA"

# Part 1 
# Answer should be.
#
# Part 2 
# Answer should be.

import re

with open("input.txt") as f_handle:
	polymer = f_handle.read()
	pass

# Use while loop and two counters
# One counter is on the current index, the other counter is looking at the next
# Use the counter to get the value of the two indexes and compare them
	# If they are equal...keep going
	# If they are not equal
		# check if they react to one another
			# if index1.lower() == index2.lower()
				# they might be able to react!
				# if index1.isupper() and index2.islower() or index1.islower() and index2.isupper()
					# they can react for sure!
					# remove index2
					# remove index1
					# we should start at the beginning again so reset counter -> counter = 0

units_remaining = 0
print("After fully reacting the scanned polymer the amount of units that remain is:", units_remaining)
print("", units_remaining)