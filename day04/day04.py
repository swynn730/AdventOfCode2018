# Test data for part 1; 10 (guard ID) * 24 (minute most asleep) = 240
# They also slept the most in general (20 + 25 + 5) = 50. 
# Step 1, Find out who slept the most. Step 2, find the minute they fell asleep at most often.
#
# Test data for part 2; 99 (guard ID) * 45 (minute most asleep) = 4455
# Step 1, Find the minute the guard fell asleep at most often.
# Of all the guards, which guard is most frequently asleep on the same minute?
# guard_shifts = [
# "[1518-11-01 00:00] Guard #10 begins shift",
# "[1518-11-01 00:05] falls asleep",
# "[1518-11-01 00:25] wakes up",
# "[1518-11-01 00:30] falls asleep",
# "[1518-11-01 00:55] wakes up",
# "[1518-11-01 23:58] Guard #99 begins shift",
# "[1518-11-02 00:40] falls asleep",
# "[1518-11-02 00:50] wakes up",
# "[1518-11-03 00:05] Guard #10 begins shift",
# "[1518-11-03 00:24] falls asleep",
# "[1518-11-03 00:29] wakes up",
# "[1518-11-04 00:02] Guard #99 begins shift",
# "[1518-11-04 00:36] falls asleep",
# "[1518-11-04 00:46] wakes up",
# "[1518-11-05 00:03] Guard #99 begins shift",
# "[1518-11-05 00:45] falls asleep",
# "[1518-11-05 00:55] wakes up",
# ""
# ]
# Part 1 
# Answer should be 39584.
#
# Part 2 
# Answer should be 55053.
import re

with open("input.txt") as f_handle:
	guard_shifts = f_handle.read()
	guard_shifts = guard_shifts.split("\n")

# Remove empty indices [""] at the end of the list.
while guard_shifts[-1] == "":
	guard_shifts = guard_shifts[:-1]

EXTRACT_TIMESTAMP_PATTERN = "\\[.+\\]"
EXTRACT_TIMESTAMP_MINUTE_PATTERN = ":[0-9]+"
EXTRACT_ID_PATTERN = "#[0-9]+"
AWAKE = "wakes up"
SHIFT_BEGINS = "begins shift"

# Sort the shift data by the provided timestamp, in ascending order.
sorted_guard_shifts = sorted(guard_shifts, key = lambda guard_shift: re.findall(EXTRACT_TIMESTAMP_PATTERN, guard_shift)[0], reverse = False) 

# How many minutes each guard slept. Example: (20 + 25 + 5) = 50.
guards_total_minutes_asleep = {}
# How many times each guard fell asleep at a particular minute in time. Example: at minute 24.
guards_minute_asleep_freq = {}

for guard_shift_idx, guard_shift in enumerate(sorted_guard_shifts):

	# Shift just started for a particular guard.
	if SHIFT_BEGINS in guard_shift:
		current_guard_id = re.findall(EXTRACT_ID_PATTERN, guard_shift)[0]

	# The difference between when a guard is awake versus when they first fell asleep is the amount of time they spent asleep.
	elif AWAKE in guard_shift:
		previous_timestamp = sorted_guard_shifts[guard_shift_idx - 1]
		current_timestamp = sorted_guard_shifts[guard_shift_idx]
		asleep_minute_start = int(re.findall(EXTRACT_TIMESTAMP_MINUTE_PATTERN, previous_timestamp)[0].strip(":"))
		awake_minute_start = int(re.findall(EXTRACT_TIMESTAMP_MINUTE_PATTERN, current_timestamp)[0].strip(":"))
		total_minutes_asleep = awake_minute_start - asleep_minute_start

		# Keep track of how much time (minutes) each guard spent asleep.
		guards_total_minutes_asleep[current_guard_id] = guards_total_minutes_asleep.get(current_guard_id, 0) + total_minutes_asleep	
		
		# Used to calculate the minute each guard spends asleep the most. 
		# Each minute spent asleep is stored alongside the guard id.
		# The value is the frequency or amount of times this key combination occurs. Example: ("#10", 34): 2.
		for i in range(asleep_minute_start, awake_minute_start):
			guards_minute_asleep_freq[(current_guard_id, i)] = guards_minute_asleep_freq.get((current_guard_id, i), 0) + 1

# The guard who slept the most.
selected_guard_id = max(guards_total_minutes_asleep, key = guards_total_minutes_asleep.get)
max_minute_asleep = 0
max_minute_asleep_freq = 0

# Part 1
for key, val in guards_minute_asleep_freq.items():
	# We only care about the guard who slept the most.
	if key[0] == selected_guard_id:
		if max_minute_asleep_freq == 0:
			max_minute_asleep_freq = val
			max_minute_asleep = key[1]
		else:
			if val > max_minute_asleep_freq:
				max_minute_asleep_freq = val
				max_minute_asleep = key[1]	

# Cleaning up the data so we can do math on it.
selected_guard_id = int(selected_guard_id.strip("#"))
final_result_part_1 = selected_guard_id * max_minute_asleep

print("The ID of the guard X the minute said guard spent most asleep is:", final_result_part_1)

# Part 2
for key, val in guards_minute_asleep_freq.items():
	# All the guards are up for grabs.
	if max_minute_asleep_freq == 0:
		max_minute_asleep_freq = val
		selected_guard_id = key[0]
		max_minute_asleep = key[1]	
	else:
		if val > max_minute_asleep_freq:
			max_minute_asleep_freq = val
			selected_guard_id = key[0]
			max_minute_asleep = key[1]	

# Cleaning up the data so we can do math on it.
selected_guard_id = int(selected_guard_id.strip("#"))
final_result_part_2 = selected_guard_id * max_minute_asleep	

print("The guard most frequently asleep on the same minute x that minute is:", final_result_part_2)