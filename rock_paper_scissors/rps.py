#!/usr/bin/python
import sys

example = [['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'], ['paper', 'rock'], ['paper', 'paper'], [
    'paper', 'scissors'], ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]

example2 = [["rock"], ["paper"], ["scissors"]]

# should retrun an array of length 3^n, each arrary having n elements.


def rock_paper_scissors(n):

    plays = ["rock", "paper", "scissors"]
    array = []

    def throw(p):
        if p == "rock":
            return "paper"
        if p == "paper":
            return "scissors"
        if p == "scissors":
            return "rock"
    if n == 0:
        return
    for i in range(n):
        array.append([throw(plays[i])])


print(rock_paper_scissors(2))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
