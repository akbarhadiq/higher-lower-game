import art
from game_data import data
import random


def comparison_data():
    compare_data = random.choice(data)
    return compare_data


def compare_follower_count(follower_a, follower_b):
    highest_follower = ""
    if follower_a > follower_b:
        highest_follower = "a"
    elif follower_b > follower_a:
        highest_follower = "b"

    return highest_follower


comparison_data_a = comparison_data()
comparison_data_b = comparison_data()
score = 0


def game():
    global comparison_data_a, comparison_data_b, score
    print(art.logo)
    print(
        f"Compare A : {comparison_data_a['name']}, a {comparison_data_a['description']}, "
        f"from {comparison_data_a['country']}")

    print(art.vs)

    print(
        f"Against B : {comparison_data_b['name']}, a {comparison_data_b['description']}, "
        f"from {comparison_data_b['country']}")

    foll_count_a = comparison_data_a['follower_count']
    foll_count_b = comparison_data_b['follower_count']

    highest_foll_count = compare_follower_count(foll_count_a, foll_count_b)

    user_guess = input("")

    if user_guess == highest_foll_count:
        print("Correct!")
        comparison_data_a = comparison_data_b
        comparison_data_b = random.choice(data)
        score = score + 1
        game()

    else:
        print(f"Incorrect!, your total score is {score}")


game()
