import random

word_bank = [
    "rizz", "ohio", "sigma", "tiktok", "skibidi", "python", "hangman", "discord", "twitter", 
    "instagram", "snapchat", "facebook", "youtube", "coding", "algorithm", "developer", 
    "internet", "keyboard", "monitor", "programming", "debugging", "software", "hardware", 
    "machine", "learning", "artificial", "intelligence", "data", "science", "engineering", 
    "cloud", "server", "gaming", "controller", "joystick", "minecraft", "roblox", "fortnite", 
    "valorant", "counterstrike", "overwatch", "streaming", "twitch", "spotify", "netflix"
]
word = random.choice(word_bank)

guessedWord = ['_'] * len(word)
attempts = 10

while attempts > 0:
    print("Current word: " + ' '.join(guessedWord))
    guess = input("Guess a letter: ")

    if guess in word:
        for x in range(len(word)):
            if word[x] == guess:
                guessedWord[x] = guess
        print("Correct guess!")
    else:
        print("Incorrect guess!")
        attempts -= 1
        print("You have " + str(attempts) + " attempts left.")

    if '_' not in guessedWord:
        print("You win! The word was: " + word)
        break
else:
    print("You lose! The word was: " + word)