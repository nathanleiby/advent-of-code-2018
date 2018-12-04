from collections import Counter

example_input = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up"""

def parse_line(line):
    s_line = line.split("] ")
    timestamp, guard_text = s_line[0], s_line[1].strip()
    s_timestamp = timestamp[1:].split(" ")
    day, hour_min = s_timestamp[0][5:], s_timestamp[1]
    s_hour_min = hour_min.split(":")
    hour, min = s_hour_min[0], s_hour_min[1]

    return (day, hour, min), guard_text	

def lines_to_records(lines):
    # (day, guard_num, minutes)
    records = []

    cur_day = None
    cur_guard = 0
    last_min = 0
    minutes = ["."]*60
    day_to_guard = {}
    for l in lines:
        parsed = parse_line(l)
        day = parsed[0][0]
        min = int(parsed[0][2])
        event = parsed[1]

        # simplification: assume 1 guard event per day
        if event.startswith("Guard #"):
            guard_num = int(parsed[1][len("Guard #"):].split(" ")[0])
            cur_guard = guard_num

        if day != cur_day:
            day_to_guard[day] = cur_guard
            if cur_day == None:
                cur_day = day
                continue

            records.append((cur_day, day_to_guard[cur_day], minutes))

            cur_day = day
            last_min = 0
            minutes = ["."] * 60

        # if it's not a guard event, toggle asleep/awake
        print(event)
        if event == "falls asleep":
            print(day, min, "falls asleep", "last_min =", last_min)
            for i in range(last_min, min):
                minutes[i] = "."
            last_min = min
        elif event == "wakes up":
            print(day, min, "wakes up", "last_min =", last_min)
            for i in range(last_min, min):
                minutes[i] = "#"
            last_min = min

    records.append((cur_day, cur_guard, minutes))

    return records

def records_to_str(records):
    s = """Date   ID   Minute
            000000000011111111112222222222333333333344444444445555555555
            012345678901234567890123456789012345678901234567890123456789
"""
    for r in records:
        s += "{}  #{}  {}\n".format(r[0], r[1], "".join(r[2]))

    return s

def total_sleep_time_by_guard(records):
    guard_to_time = {}
    for r in records:
        guard_num = r[1]
        minutes_asleep = r[2].count("#")
        if not guard_to_time.get(guard_num):
            guard_to_time[guard_num] = 0
        guard_to_time[guard_num] += minutes_asleep
    return guard_to_time

# returns the guard who slept the most
def max_sleep_time(guard_to_time):
    max = -1
    max_guard_num = -1
    for k in guard_to_time:
        v = guard_to_time[k]
        if v > max:
            max = v
            max_guard_num = k
    return max_guard_num

def find_sleepiest_minute(records):
    # print("find_sleepiest_minute from {} records".format(len(records)))
    cnt = Counter()
    for r in records:
        minutes = r[2]
        for idx, val in enumerate(minutes):
            if val == "#":
                cnt[idx] += 1
    # print(cnt)
    # return minute AND count
    if len(cnt) == 0:
        return (0,0)
    return cnt.most_common(1)[0]


print("EXPECTED:")
visualized_records = """Date   ID   Minute
            000000000011111111112222222222333333333344444444445555555555
            012345678901234567890123456789012345678901234567890123456789
11-01  #10  .....####################.....#########################.....
11-02  #99  ........................................##########..........
11-03  #10  ........................#####...............................
11-04  #99  ....................................##########..............
11-05  #99  .............................................##########.....
"""
print(visualized_records)

ex_lines = sorted(example_input.splitlines())
ex_records = lines_to_records(ex_lines)
print("")
print("ACTUAL:")
print(records_to_str(ex_records))



assert(records_to_str(ex_records) == visualized_records)


print("")
with open("./4-input", "r") as f:
    lines = f.readlines()
    lines.sort()
    rs = lines_to_records(lines)
    print(records_to_str(rs))
    guard_to_time = total_sleep_time_by_guard(rs)
    max_count = -1
    max_min = -1
    max_guard = -1
    for guard in guard_to_time:
        filtered_rs = list(filter(lambda r: r[1] == guard, rs))
        sleepiest_min_and_count = find_sleepiest_minute(filtered_rs)
        if sleepiest_min_and_count[1] > max_count:
            max_min = sleepiest_min_and_count[0]
            max_count = sleepiest_min_and_count[1]
            max_guard = guard
        print("guard={} min={} count={}".format(guard, sleepiest_min_and_count[0], sleepiest_min_and_count[1]))
    print("MAX guard={} min={} count={}".format(max_guard, max_min, max_count))
    print("RESULT => ", max_guard * max_min)

