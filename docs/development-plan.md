# Software Development Plan

## Application Purpose

------------
***Dinner Planner aims to abolish the problem of people who can't decide what to eat for dinner.***

The design method used was aimed for both parties, the undecided and the person attached to that undecided person. Eating doesn't need to be a choir any longer!<br>

With this app, it will give the user a pleasent experience of being able to spend time picking a meal tailored to how they feel, or giving the user the ability to generate a completely random meal.
<br>
<br>

------------

## What does it do?

------------
Dinner Planner takes steps to ensure it can produce a quality product for the user.
It also aims to produce a higher quality user experience, away from the basic instant load times that terminal normally offers.

**Process**
> **1.** Runs through python or a bash script<br>
> **2.** Return username input<br>
- **2.1** Will take '-' commands in this input<br>
> **3.** Will capitalize the given name<br>
> **4.** Requests the user to input a choice between manual or random<br>
> **5.** If user selects manual option, execute dp_man()
- **5.1** Will unpack keys to show options to user
- **5.2** Continues to unpack each category for user selection
- **5.3** Prints user selection from functions created to handle each category total
> **6.** If user selects random option, execute dp_rand()
- **6.1** Follows a similar method to dp_man(), utilises the random module to choose from each category
- **6.2** Print the random key following the dp_man() method
> **7** User can terminate app at any time with CTRL-C.
- **7.1** Added error handling as CTRL-C generates a KeyboardInterrupt Error
> **8** Used TerminalMenu module to present the dictionaries into readable and interactive information. 
- **8.1** Avoiding keyboard input meant error handling for many functions was unnecessary.
- **8.2** KeyboardInterrupt Error's were easier to track and deal with.
 


