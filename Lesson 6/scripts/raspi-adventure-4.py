#!/usr/bin/env python3

# Title: The Silly Sentence Generator 3000
# Author: Your Name
# The game is set in medieval days: a time of stone castles,
# knights with swords, and (some say) mythical beasts that breathe fire.
# Your main character is a young boy named Raspi.1 One day Raspi is
# out gathering firewood and gets lost in the forest. He stumbles upon the
# entrance to a cave. # He peers in the entrance and finds that the cave splits
# into a left tunnel and # a right tunnel. He remembers a folk tale his
# grandmother used to tell of a mysterious cave in this very forest that holds
# enormous treasures. It’s said the treasure is guarded by a ferocious fire-
# breathing dragon. Raspi can’t resist the temptation to explore the cave;
# although he knows he should turn back, he walks slowly into the dark cavern

# Display the title and instruction
print("*" * 80)
print("* Raspi's Cave Adventures *")
print("*" * 80)

# 1st Choice: Left or Right Cave?
print("You see the cave split into a left and right tunnel")
print("Do you choose go left or right?")
cave_choice = input("Enter L for left or R for right: ").upper()
if (cave_choice == "L" or cave_choice == "LEFT"):
    # Left cave
    print("You walk into the left cave.")
    print("The cave opens up to a large room with an underground river.")
    print("You notice a small boat on the edge of the river.")
    print("Do you use the boat, swim, or walk along the side of the river?")
    river_choice = input("Enter B for boat, S for swim, or W for walk: ").upper()

    if river_choice == "W" or river_choice == "WALK":
        # You walk along the edge of the river
        print("You walk along the narrow edge of the river.")

    elif river_choice == "B" or river_choice =="BOAT":
        # You hop in the boat
        print("You step in the boat and start drifting down the river.")

    elif river_choice == "S" or river_choice == "SWIM":
        # You jump in the water and start swimming
        print("You dive into the water and start swimming down the river.")

    else:
        # Wrong input
        print("You seem to have trouble making good decisions!")
        print("Suddenly a stalactite falls from the ceiling and bonks you on the head.")
        print("Game Over!!!")

elif (cave_choice == "R" or cave_choice == "RIGHT"):
    # Right cave
    print("You walk into the right cave. The cave starts sloping downward.")
else:
    # Wrong input
    print("You seem to have trouble making good decisions!")
    print("Suddenly a stalactite falls from the ceiling and bonks you on the head.")
    print("Game Over!!!")
