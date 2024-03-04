title = input("would you like to play?(yes/no)")
if title == "yes":
    answer = input("you reach a crossroad,would you like to take left or right?")
    if answer == "left":
        print("you have selected left so welcome to quiz!")
        print("answer the question.")
        answer = input("how many times can you subtract 10 from 100?")
        if answer == "once":
            print('correct!')
        else:
            print(
                "incorrect!once is answer as next time you would be subtracting 10 from 90first.")
        answer = input(
            "if you were running a race and passed the person in second place,what place would you be in now?")
        if answer == "second":
            print('correct!')
        else:
            print("incorrect!answer is second.")
        answer = input(
    "what occurs once in a minute,twice in a moment but never in thousand years?")
        if answer == "M":
            print('correct!')
        else:
            print("incorrect!answer is M")
        answer = input("what has a head,a tail but does not have a body?")
        if answer == "coin":
            print('correct!')
        else:
            print("incorrect!answer is coin.")
        answer = input("which thing we purchase to eat but never eats it?")
        if answer == "plate":
            print('correct!')
        else:
            print("incorrect!answer is plate.")
            print("you have finished the quiz.thanks for participating.")
    elif answer=="right":
        import random
        from collections import Counter
        someWords = '''apple banana mango strawberry
        orange grape pineapple apricot lemon coconut watermelon
        cherry papaya berry peach lychee muskmelon'''
        someWords = someWords.split(' ')
        word = random.choice(someWords)
        if __name__ == '__main__':
            print('Guess the word! HINT: word is a name of a fruit')
            for i in word:
                print('_', end = ' ')	
            print()
            playing = True
            letterGuessed = ''			
            chances = len(word) + 2
            correct = 0
            flag = 0
            try:
                while (chances != 0) and flag == 0: #flag is updated when the word is correctly guessed
                    print()
                    chances -= 1
                    try:
                        guess = str(input('Enter a letter to guess: '))
                    except:
                        print('Enter only a letter!')
                        continue
                    if not guess.isalpha():
                        print('Enter only a LETTER')
                        continue
                    elif len(guess) > 1:
                        print('Enter only a SINGLE letter')
                        continue
                    elif guess in letterGuessed:
                        print('You have already guessed that letter')
                        continue
                    if guess in word:
                        k = word.count(guess) #k stores the number of times the guessed letter occurs in the word
                        for _ in range(k):
                            letterGuessed += guess # The guess letter is added as many times as it occurs
                    for char in word:
                        if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                            print(char, end = ' ')
                            correct += 1
                        elif (Counter(letterGuessed) == Counter(word)): 
                            print("The word is: ", end=' ')
                            print(word)
                            flag = 1
                            print('Congratulations, You won!')
                            break # To break out of the for loop
                            break # To break out of the while loop
                        else:
                            print('_', end = ' ')
                if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
                    print()
                    print('You lost! Try again..')
                    print('The word was {}'.format(word))
            except KeyboardInterrupt:
                print()
                print('Bye! Try again.')
                exit()
    else:
        print("invalid choice!please input valid choice.") 
else:
    print("ok!you want to exit.Next time please try to participate.")
    exit                  
                

                