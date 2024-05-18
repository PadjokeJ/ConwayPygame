# ConwayPygame
 This was a school project that I worked on
 I worked on it a bit more to make it compatible with the file type everyone seems to be using, and added my own saving and loading
 
 Conway's game of life is a cellular automata that simulates cells. Each cell can either be alive or dead. There are 3 rules: 
 - A live cell with 4 or more neighbouring live cells will die
 - A live cell with 1 or less neighbouring live cells will die
 - A dead cell with 3 cells will become live

## Controls
SPACEBAR : stop or start playing the simulation
LMB : draw and erase
LSHIFT : move the simulation one frame forward
F: make the simulation go SUPERSPEED
S: make the simulation go slow
SCROLL: change RLE file to load
F7 : loads the selected RLE file
F6 : loads user made pattern
F5 : creates user made pattern
F4 : clears the screen
ARROW KEYS : move around the canvas

## Adding your own RLE files
To add your own RLE files inside of the program, just drag them into the rle folder, the program will detect them automatically

Feel free to contribute to this project or modify it in any way
I do not recommend copying the code inside of this repo as it is quite unoptimised. 
In fact, this code runs at around 40fps when computing the whole board.