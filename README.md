### RW Utility ###
Little package which handles formatting in regards to terminal for windows and unix

You can install the module so available for all your python programs by running the following:

`python setup.py install`

If in Linux or Mac OS you will need to do `sudo`.

#### Color codes for Bash Prompts

As a new addon there are color codes implemented for command prompt:

```
RAWU_FCBLACK   = "\033[1;30m"
RAWU_FCRED   = "\033[1;31m"
RAWU_FCGREEN   = "\033[1;32m"
RAWU_FCYELLOW  = "\033[1;33m"
RAWU_FCBLUE  = "\033[1;34m"
RAWU_FCMAGENTA = "\033[1;35m"
RAWU_FCCYAN  = "\033[1;36m"
RAWU_FCGRAY  = "\033[1;37m"
RAWU_FCDARK  = "\033[1;38m"
RAWU_FCWHITE  = "\033[1;97m"

RAWU_BCBLACK   = "\033[1;40m"
RAWU_BCRED   = "\033[1;41m"
RAWU_BCGREEN   = "\033[1;42m"
RAWU_BCYELLOW  = "\033[1;43m"
RAWU_BCBLUE  = "\033[1;44m"
RAWU_BCMAGENTA = "\033[1;45m"
RAWU_BCCYAN  = "\033[1;46m"
RAWU_BCGRAY  = "\033[1;47m"
RAWU_BCDARK  = "\033[1;100m"
RAWU_BCWHITE  = "\033[1;107m"

RAWU_BOLD    = "\033[;1m"
RAWU_DIM    = "\033[;2m"
RAWU_UNDERLINED = "\033[;4m"
RAWU_REVERSE = "\033[;7m"

RAWU_BOLD_RESET    = "\033[;21m"
RAWU_DIM_RESET    = "\033[;22m"
RAWU_UNDERLINED_RESET = "\033[;24m"
RAWU_REVERSE_RESET = "\033[;27m"

RAWU_RESET = "\033[0;0m"
```

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
