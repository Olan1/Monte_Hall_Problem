# -*- coding: utf-8 -*-
"""
The Monty Hall Problem

The Monty Hall Problem is a ficticious game show in which you are a contestant
who is given the task of picking 1 of 3 doors. Behind 1 door is a brand new car,
behind the other 2 are goats. Once you have picked a door (eg: no. 1), the game
show host, who knows what is behind each door, opens a door that the contestant
has not picked, and does not contain the car (eg: no. 2). The host then offers
you a chance to change your pick and choose door no. 3. Is it to your advantage
to switch your choice?

The answer is yes. Originally the contestant had a 1 in 3 chance (33%) of picking
correctly, and a 2 in 3 chance (66%) of being wrong. Once the host removes an
unpicked door from the equation, the probability of your original choice being
correct is still 33%, and 66% chance it is wrong. Therefore, the remaining
unopened door has a 66% chance of hiding a brand new car.

This programme will run this game a specified number of times, with the
contestants choice of door being picked each time by a random number generator.
With every iteration of the game, a new contestants choice will be generated,
and the location of the prize door changed. The host will open a door not picked
by the user and not containing the prize, and will give the user the option to
keep or change their door. This will also be decided using a random number
generator. A record will be kept of how many times the contestants initial choice
was correct, and how many times the contestant was correct if they changed doors
mid-game. The final counts will be graphed on a bar chart using matplotlib.
"""

# Import libraries/modules
import random as rm
from matplotlib import pyplot as plt

# Variables:
first_choice_win_count = 0      # Counter to track first choice wins
first_choice_loss_count = 0     # Counter to track first choice losses
second_choice_win_count = 0     # Counter to track second choice wins
second_choice_loss_count = 0    # Counter to track second choice losses
games = 10000                   # Number of games to be played

rm.seed()                       # Initialise the random number generator

# Iterate from 0 to number of games specified
for game in range(games):
    unopen_doors = [1, 2, 3]            # 3 unopened doors
    prize_door = rm.randint(1, 3)       # Pick a door to hide the prize
    user_choice = rm.randint(1, 3)      # Get users choice of door
    
    # Create list of hosts door options and remove the users choice
    host_choices = [1, 2, 3]
    host_choices.remove(user_choice)
    host_door_pick = rm.choice(host_choices)    # Host picks door to open
    
    unopen_doors.remove(host_door_pick) # Open hosts selected door
    
    # Give user the choice to keep or change their door
    keep_change = rm.randint(1, 2)      # Keep = 1, Change = 2
    
    # If user chooses to keep their initial choice:
    if keep_change == 1:
        # Open users door
        unopen_doors.remove(user_choice)
    # If the user chooses to change doors
    else:
        # Select new door
        second_choice = rm.choice(unopen_doors)
        # If users new choice is their original door, reselect
        while second_choice == user_choice:
            second_choice = rm.choice(unopen_doors)
            
        # Open users second choice door
        unopen_doors.remove(second_choice)
    
    # If the prize door is unopened, the user loses
    if prize_door in unopen_doors:
        # If this was the users first choice
        if keep_change == 1:
            # Increment first choice loss counter
            first_choice_loss_count += 1
        # If this was the users second choice
        else:
            # Increment the second choice loss counter
            second_choice_loss_count += 1
    # If the prize door is opened, the user wins
    else:
        # If this was the users first choice
        if keep_change == 1:
            # Increment first choice win counter
            first_choice_win_count += 1
        # If this was the users second choice
        else:
            # Increment the second choice win counter
            second_choice_win_count += 1


# Calculate the percentage of times each choice was correct/incorrect
first_choice_win_perc = (first_choice_win_count/(first_choice_win_count+first_choice_loss_count)) * 100
first_choice_loss_perc = (first_choice_loss_count/(first_choice_win_count+first_choice_loss_count)) * 100
second_choice_win_perc = (second_choice_win_count/(second_choice_win_count+second_choice_loss_count)) * 100
second_choice_loss_perc = (second_choice_loss_count/(second_choice_win_count+second_choice_loss_count)) * 100


# Pyplot barcharts
# Create 2 subplots in a single figure
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
fig.suptitle('The Monte Hall Problem')  # Add title to figure
ax1.set_title('First Choice Outcomes')  # Set axes 1 title
ax2.set_title('Second Choice Outcomes') # Set axes 2 title
ax1.set(xlabel='Outcome', ylabel='%')   # Set x & y axis labels for ax1
ax2.set(xlabel='Outcome', ylabel='%')   # Set x & y axis labels for ax2
# Source: https://matplotlib.org/devdocs/gallery/subplots_axes_and_figures/subplots_demo.html

# Set position of y-axis labels and ticks to right side of ax2 subplot
ax2.yaxis.set_label_position("right")
ax2.yaxis.tick_right()
# Source: https://stackoverflow.com/questions/13369888/matplotlib-y-axis-label-on-right-side

# Plot bar chart of first choice wins and losses
ax1.bar(['Wins', 'Losses'],
        [first_choice_win_perc, first_choice_loss_perc],
        color=['#777fff', '#54364f'])

# Plot bar chart of second choice wins and losses
ax2.bar(['Wins', 'Losses'],
        [second_choice_win_perc, second_choice_loss_perc],
        color=['#777fff', '#54364f'])
