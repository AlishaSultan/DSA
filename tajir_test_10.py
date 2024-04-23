def batonPass(friends, time):
    cycle_length = 2 * (friends - 1)
    
    if cycle_length == 0:
        return [1, 2]

    time %= cycle_length

    if time < friends:
        return [time if time != 0 else friends, time + 1 if time != 0 else 1]
    else:
        time = cycle_length - time
        return [time + 1 if time != 0 else friends, time if time != 0 else 1]

# Test the function
print(batonPass(5, 3))  # Expected outcome: [3, 4]
print(batonPass(3, 6))  # Expected outcome: [3, 2]
