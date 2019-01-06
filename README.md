# monster-tracker
A monster tracker to use while in combat in D&amp;D.

## How to use it
The program will guide the user through most of the functionality, but a guide can be seperated into several smaller parts:

### Loading of data
First, the monster data is loaded into the program. This can be done in two different ways; either
typed in interactively or read automatically from a .txt file. Using the last method, the format of the file is as follows:
'''
<name>, <AC>, <HP>
<name>, <AC>, <HP>
'''

### Tracking during battle
During the battle, you will be prompted to write the name of the monster which is currently targeted by a player. The program will then
print the info of that monster, and you will then be prompted to type in the players hit roll. The program will then either prompt you to
type in the players damage roll, or write a message, telling you the monster was not hit.

## Comments by the creator
I don't know if this functionality can be found in other programs, this was mostly written to make combat encounters easier for me.
Please, if you can, take the time to look at the code. Any comments are GREATLY appreciated, as I am trying to write better code. :)
