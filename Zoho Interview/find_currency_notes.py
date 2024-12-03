# find_currency_notes

def find_currency_notes(amt):
    denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

    note_count = {}

    for notes in denominations:
        if amt >= notes:
            note_count[notes] = amt // notes
            amt %= notes

    return note_count



print(find_currency_notes(8000))

# Time Complexity: O(1), as the algorithm has a fixed number of iterations (9) that does not depend on the size of the input.

# Auxiliary Space: O(1), as the algorithm only uses a fixed amount of space to store the notes and note counters, which does not depend on the size of the input.