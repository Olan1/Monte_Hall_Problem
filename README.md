# Monte_Hall_Problem

<p>The Monty Hall Problem is a ficticious game show in which you are a contestant
who is given the task of picking 1 of 3 doors. Behind 1 door is a brand new car,
behind the other 2 are goats. Once you have picked a door (eg: no. 1), the game
show host, who knows what is behind each door, opens a door that the contestant
has not picked, and does not contain the car (eg: no. 2). The host then offers
you a chance to change your pick and choose door no. 3. Is it to your advantage
to switch your choice?<p>
<p>The answer is yes. Originally the contestant had a 1 in 3 chance (33%) of picking
correctly, and a 2 in 3 chance (66%) of being wrong. Once the host removes an
unpicked door from the equation, the probability of your original choice being
correct is still 33%, and 66% chance it is wrong. Therefore, the remaining
unopened door has a 66% chance of hiding a brand new car.<p>
<p>This programme will run this game a specified number of times, with the
contestants choice of door being picked each time by a random number generator.
With every iteration of the game, a new contestants choice will be generated,
and the location of the prize door changed. The host will open a door not picked
by the user and not containing the prize, and will give the user the option to
keep or change their door. This will also be decided using a random number
generator. A record will be kept of how many times the contestants initial choice
was correct, and how many times the contestant was correct if they changed doors
mid-game. The final counts will be graphed on a bar chart using matplotlib.<p>
