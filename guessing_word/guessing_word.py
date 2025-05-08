import random

#word in pool
words =['wonder', 'water', 'earth', 'land', 'sea', 'throw']

GUESS =10

print(f"Guess the word!! you have {GUESS} chances.")

guess_word = random.choice(words)

#convert the words into dash

word_selected=[ '-' for _ in guess_word ]

while GUESS> 0 and '-' in word_selected:
    char = input("guess any character!!! ").lower()

    if char in guess_word:
        for i in range(len(guess_word)):
            if guess_word[i]==char:
                word_selected[i] = char
    else:
        GUESS -=1
        print('wrong guess!!!')
    print('current word: ',''.join(word_selected) )

if '-' in word_selected:
    print("youn have lost the game :( ")
else:
    print("Congratulations! You guessed the word ", guess_word)
