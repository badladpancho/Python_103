#   This is going to be a simple game in order to guess
#   We are going to be using if statments while loops and other things that i have
#   learned.
#   MADE BY BADLADPANCHO


print("Player 1 enter the secret word\n");
secret_word = input("");
print("OK lets play!");
guess = ""
i = 0;
chance_limit = 3;
while guess != secret_word:
    guess = input("Player 2 Enter the guess word:\n");
    if guess == secret_word:
        print("You guessed the right word!\n");
        break;
    if i >= 3:
        print("You ran out of chances to guess the word\n");
        break;
    i += 1;
    chance_limit -= 1;
    print("you have " + str(chance_limit)+ " chances left");
