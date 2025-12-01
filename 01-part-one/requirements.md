# Domain requirements

## Background

Imagine a safe with a combination dial. I need a program that can take input from a file that turns the dile.

### The dial 

The dial can turn to the left and to the right, the dial has a total of 100 clicks. From 0 to 99.

To turn the dial to the left, the face value of the dial is lowered with the amount of clicks turned.

To turn the dial to the right, the face value is increased with the amount of clicks.

### Start value

The turn dial has a starting value that can be set.



### Turn dial to the right

I want tell the dial to turn Right x steps. This should turn the dial to the right which will add the value of the dial from the initial value.
The format will be R50 for Right 50 clicks. The initial letter assign turn direction, right adds to the dial value. the number is followed after the letter tells how many clicks to turn. 


### Counter

Each time the dial stops at 0 i want a zero-counter to add 1 to the value, starting with 0 as initial value.
