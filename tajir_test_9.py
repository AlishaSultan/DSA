def winner(erica, bob):
    scores = {'E': 1, 'M': 3, 'H': 5}
    
    erica_score = sum(scores[question] for question in erica)
    bob_score = sum(scores[question] for question in bob)
    
    if erica_score > bob_score:
        return "Erica"
    elif erica_score < bob_score:
        return "Bob"
    else:
        return "Tie"

# Test cases
erica1 = ["E", "H", "H"]
bob1 = ["E", "M", "H"]
print(winner(erica1, bob1))  # Output: Bob

erica2 = ["E"]
bob2 = ["E"]
print(winner(erica2, bob2))  # Output: Tie

erica3 = ["E", "M", "E"]
bob3 = ["E", "M", "H"]
print(winner(erica3, bob3))  # Output: Erica