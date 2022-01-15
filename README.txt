CSCI 101 - Planetary orbit simulation

*The program starts in a paused state
Like in real life, not all configurations of planets will have a stable orbit.
Some planets will just get ejected.
Some presets that are stable are saved in the Presets folder.

=Buttons:
*Start/Pause/Unpause: Pauses/Unpauses the simulation
*Console import: Imports a planet from the console window by asking for its data
*Console export: Displays the data of all existing planets on the console window
*File import: Imports a CSV file containing the data for some planets
*File export: Exports a CSV file containing the data for all the existing planets
*Increase rate: Makes the simulation faster
*Decrease rate: Makes the simulation slower
*Clear Planets: Deletes all existing planets
*Add Sun & Earth: Adds two stable test planets with Sun and Earth textures

=How to use inputs:
*Console import:
-ID: Enter a string (Unique for each planet)
-Mass: Enter a float
-Velocity: x,y,z
	Where x and y and z are floats
-Temperature: Enter a float
-Position: x,y,z
	Where x and y and z are floats

*File import:
Enter file Name: file_name.csv
	Where file_name.csv is in Presets folder

CSV file:
ID,Mass,Velocity,Temperature,Position

The first line is treated as headers and ignored in code

*File export:
Enter file Name: file_name.csv
	Where file_name.csv will be created in Presets folder

