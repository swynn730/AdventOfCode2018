# Test data for part 1;
guard_shifts = [
	"[1518-11-01 00:00] Guard #10 begins shift",
	"[1518-11-01 00:05] falls asleep",
	"[1518-11-01 00:25] wakes up",
	"[1518-11-01 00:30] falls asleep",
	"[1518-11-01 00:55] wakes up",
	"[1518-11-01 23:58] Guard #99 begins shift",
	"[1518-11-02 00:40] falls asleep",
	"[1518-11-02 00:50] wakes up",
	"[1518-11-03 00:05] Guard #10 begins shift",
	"[1518-11-03 00:24] falls asleep",
	"[1518-11-03 00:29] wakes up",
	"[1518-11-04 00:02] Guard #99 begins shift",
	"[1518-11-04 00:36] falls asleep",
	"[1518-11-04 00:46] wakes up",
	"[1518-11-05 00:03] Guard #99 begins shift",
	"[1518-11-05 00:45] falls asleep",
	"[1518-11-05 00:55] wakes up"]
# Part 1 
# Answer should be
from datetime import datetime
import re




# year-month-day hour:minute format.
timestamps = []

with open("input.txt") as f_handle:
	#guard_shifts = f_handle.read()
	#guard_shifts = guard_shifts.split("\n")
	for guard_shift in guard_shifts:

		timestamp = re.findall("\\[(.+)\\]", guard_shift)
		if len(timestamp) > 0:
			timestamps.append(timestamp[0])

	sorted_guard_shifts = sorted(
    guard_shifts,
    key = lambda x: datetime.strptime(re.findall("\\[.+\\]", guard_shift)[0], '[%Y-%m-%d %H:%M]'), reverse=True
	)

	# sorted_guard_shifts = sorted(
 #    timestamps,
 #    key = lambda x: datetime.strptime(re.findall("\\[.+\\]", guard_shift)[0], '[%Y-%m-%d %H:%M]'), reverse=True
	# )

print(sorted_guard_shifts)
print(sorted_guard_shifts == guard_shifts)

# 
#print("The ID of the guard multiplied by the minute said guard was most asleep:", overlaps)