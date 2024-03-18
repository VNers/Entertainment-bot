import random

films = ["Avatar", "Great Gatsby", "Oppenheimer", "Titanic", "Brain Games"]
music = ["Dance", "Flowers", "Cold Heart", "We will rock you", "Halo"]
games = ["Battlefield", "Dota2", "Lineage2", "CS.GO", "Last of us"]
jokes = ["Why are snails slow? Because they’re carrying a house on their back.",
         "What’s the smartest insect? A spelling bee!",
         "How does the ocean say hi? It waves!",
         "What do birds give out on Halloween? Tweets.",
         "What is a room with no walls? A mushroom."]
stories = ["The Rainbow Fish: This short story tells that the rainbow fish wants to know who he is by pointing to the\n individual identity and the morality of life.",
           "The Very Hungry Caterpillar:This story about a caterpillar journey as the hungry caterpillar transforms\n into a beautiful butterfly.",
           "The Little Red Hen:This story tells the importance of being hardworking, cooperative and helping others in\n this classical children tale.",
           "The Ugly Duckling: This story is a popular children tale about acceptance of someone’s appearance and \nfinding one’s true identity.",
           "Cinderella: The classic fairytale of Cinderella about kindness, love magic, and a happily ever after."]


def recommend_films():
    return random.choice(films)


def recommend_music():
    return random.choice(music)


def recommend_games():
    return random.choice(games)


def tell_joke():
    return random.choice(jokes)


def tell_story():
    return random.choice(stories)


def play_game():
    choices = ["Stone", "Scissors", "Paper"]
    user_choice = input("Make a choice (Stone, Scissors, Paper): ")
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        return "Draw! "
    elif (user_choice == "Stone" and computer_choice == "Scissors") or \
            (user_choice == "Scissors" and computer_choice == "Paper") or \
            (user_choice == "Paper" and computer_choice == "Stone"):
        return "You won!"
    else:
        return "You lose!"


def main():
    print("Hi! This is entertainment bot! ")
    while True:
        print("\nMenu:")
        print("1. Movie recommendations. ")
        print("2. Music recommendations. ")
        print("3. Games recommendations. ")
        print("4. Random joke. ")
        print("5. Short story. ")
        print("6. Play game 'Stone, Scissors, Paper'. ")
        print("7. Exit. ")

        choice = input("Choose the option (1-7): ")

        if choice == "1":
            print("Recommended movie: ", recommend_films())
        elif choice == "2":
            print("Recommended music: ", recommend_music())
        elif choice == "3":
            print("Recommended game: ", recommend_games())
        elif choice == "4":
            print("Joke for you: ", tell_joke())
        elif choice == "5":
            print("Short story for you: ", tell_story())
        elif choice == "6":
            print(play_game())
        elif choice == "7":
            print("Goodbye! ")
            break
        else:
            print("Wrong choice. Try again! ")


if __name__ == "__main__":
    main()

