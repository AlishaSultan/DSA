def winner(erica, bob):
    erica_score = 0
    bob_score = 0
    
    # Define a dictionary to map difficulty levels to points
    difficulty_points = {"E": 1, "M": 3, "H": 5}
    
    # Calculate scores for each day
    for i in range(len(erica)):
        erica_score += difficulty_points[erica[i]]
        bob_score += difficulty_points[bob[i]]
    
    # Compare scores and determine the winner
    if erica_score > bob_score:
        return "Erica"
    elif erica_score < bob_score:
        return "Bob"
    else:
        return "Tie"

# Test the function with sample input
erica = ["E", "H", "H"]
bob = ["E", "M", "E"]
print(winner(erica, bob))  # Output: "Erica"
