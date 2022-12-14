letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#dictionary letter_to_points with letters as keys and points as values
letter_to_points = {
    key: value for key, value in zip (letters, points)
}

#adding element to the dictionary that has a key of " " and value of 0
letter_to_points[" "] = 0

#creating a function that returns how many points a word is worth
def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letter_to_points.get(letter, 0)
        return point_total

#creating a dictionary with each player's words
player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "player2": ["EARTH", "EYES", "MACHINE"],
    "player3": ["ERASER", "BELLY", "HUSKY"],
    "player4": ["ZAP", "COMA", "PERIOD"]
}

#creating an empty dictionary

player_to_points = {}

for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word)
    player_to_points[player] = player_points

print(player_to_points)