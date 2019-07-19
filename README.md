### RW Utility ###
Little package which handles formatting in regards to terminal for windows and unix

You can install the module so available for all your python programs by running the following:

`python setup.py install`

If in Linux or Mac OS you will need to do `sudo`.

#### COMMANDS
Introduce the following commands:

 * `cls()` : Clears terminal window
 * `Userinput` : Instantiates a class which kan handle single user input without any echo in terminal. Can also read escape, enter, backspace and arrow keys
 * `rawput(words)` : Line input - but with arrow key functionality. Use arrow key up and down to switch to previous commands. You can setup previous commands in the words argument (as a list)
 * `locate(x,y,text)` : places a text in terminal at x,y position
 * `sepSign(item, list,lastword)` : Returns the relevant separation sign when traversing a list for the specific item. You can define is the final separation should either be 'and' or 'or' or some different
 * `doCommaSentence (list, lastword)` : Returns a complete string with each item in list correctly comma separated and with a lastword as being either 'and' or 'or'  
 * `wrapper(text,indent,width)`: Organise a text in lines (returned as a list) so they are wrapped width maximum width and indent.

There are two examples of the user inputs:

 * Example 1 - test of the Userinput class
 * Example 2 - test of rawput
