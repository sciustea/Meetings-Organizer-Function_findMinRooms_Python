# Stefana Ciustea
# Assignment 1 - CS 310 at BC
# 10/07/2022


# "Design a function to help organize multiple meetings during a day. Each meeting will have a start time and end time. Each meeting will need to reserve a private conference room during that time. Your function will take all the meeting schedules and calculate the minimum number of conference rooms you will need. The requirements are:"

# "1.	The function will take the input as a sequence of lists, each list only contains two numbers, the start time and the end time. For simplicity, we assume the time is just a float number in the range of 0.0 to 24.0. For example, the function may be given the following input:"
# "findMinRooms([1.2, 3.4], [2.3, 5.0], [3.1, 8.0])"
# "Code should return 3 as the result, since during this time window [3.1, 3.4], all three meetings will be going on in parallel. Another example:"
# "findMinRooms([1.2, 3.4], [2.3, 5.0], [4.1, 8.0])"
# "this will return 2. Another example:"
# "findMinRooms([1.2, 3.4], [2.3, 5.0], [3.1, 8.0], [1.0, 10.0])"
# "this will return 4."

# "2.	The function should be able to handle any number of arguments. 

# "3.	The sequence of meetings can be input in any order."

# "4.	The function should handle all wrong inputs gracefully, by catching all errors and display meaningful error messages. There should be no error/crash from the system."

# "5.	No brutal force O(N^2) implementation, i.e., by checking each meeting against every other meeting to count the time overlaps. Hint: Need to re-organize and sort the data in some way, after that, only need to go through the data once to find the answer."


def findMinRooms(*times):
    for time in times:
        for hour in time:
            if type(hour) != float and type(hour) != int:
                return "Error: At least one of the hours is not a float number"
            if hour < 0.0 or hour > 24.0:
                return "Error: At least one of the hours is not in the range of 0.0 to 24.0"
        if type(time) != list:
            return "Error: Input is not a sequence of only lists, as expected"
        if len(time) != 2:
            return "Error: At least one of the meetings does not contain only 2 numbers, the start time and the end time, as expected"
        if time[1] < time[0]:
            return "Error: For at least one of the meetings, the end time is after the start time"
    begins = sorted([time[0] for time in times])
    ends = sorted([time[1] for time in times])
    meetings_count, present_count, sp, ep = 0, 0, 0, 0
    while sp < len(times):
        if begins[sp] < ends[ep]:
            present_count += 1
            sp += 1
        else:
            present_count -= 1
            ep += 1
        meetings_count = max(meetings_count, present_count)
    return meetings_count