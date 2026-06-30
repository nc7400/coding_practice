#Code Kata 6/30/26

#Highest Scoring Word

#Rules: 
# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
# For example, the score of abad is 8 (1 + 2 + 1 + 4).
# You need to return the highest scoring word as a string.
# If two words score the same, return the word that appears earliest in the original string.
# All letters will be lowercase and all inputs will be valid.
# The script will ask the player if they'd like to play again and will display the overall 
#   highest scoring word if they decide to stop.

#List referenced to score each word
abc_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Global dictionary used to store all scores
all_scores = {}

#Scores each words, strips white space and makes input lowercase
def score(str):
    score = 0
    for letter in list(str.strip().lower()):
        score += abc_list.index(letter) + 1
    return score

#Adding word from list to dictionary while calling score function on the word for the value in the dict
def add_to_dict(list, dict):
    for word in list:
        try:
            dict[word] = score(word)

        except:
            print("Please enter valid words with no extra characters.")

#Finds the highest valued word in the scored_words dict based on the value
def find_highest(dict):
    for key, value in dict.items():
        if value == max(dict.values()):
            return print(f"'{key}' has the highest value of: {value}")

#Ask user if they would like to continue to play       
def play_again():
    
    flag = True

    while flag:    
        user_input = input("Would you like to play again? Please enter 'y' or 'n':\n")
        if user_input == "y":
            return user_input
            break
        elif user_input == "n":
            return user_input
            break
        else:
            print("You must enter 'y' or 'n'.")



#Function to take user input and score words 
def highest_scoring_word():

    scored_words = {}

    flag = True

    while flag:
        #takes user input of words to be scored
        user_words = input("\n" \
                "------------------------------------\n" \
                "Highest Scoring Word\n" \
                "------------------------------------\n" \
                "Only use spaces to separate each word, no characters or numbers.\n" \
                "Please enter words to be scored:\n")

        #splits words into a list
        split_words = user_words.split()

        #Adds split words into a dictionary as the key and score as the value
        add_to_dict(split_words, scored_words)
        add_to_dict(split_words, all_scores)

        find_highest(scored_words)

        answer = play_again()

        #Clears scored_words for repeat plays, otherwise it will
        #not display the highest scoring word for the current turn
        scored_words.clear()

        if answer == 'n':

            print("\nOf all the words played,")
            find_highest(all_scores)
            print("\n")
            break


highest_scoring_word()


   
        


