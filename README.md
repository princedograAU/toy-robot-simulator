# Toy Robot Simulator
The application is a simulation of a toy robot moving on a square tabletop, 
of dimensions 5 units x 5 units. 

#### POINTS TO REMEMBER:
- There are no other obstructions on the table surface.
- The robot is free to roam around the surface of the table, but must be prevented from 
falling to destruction. 
- Any movement that would result in the robot falling from the table must be prevented, 
however further valid movement commands must still be allowed.
- The origin (0,0) can be considered to be the SOUTH WEST most corner. 
- PLACE will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST. 
- The first valid command to the robot is a PLACE command, after that, any sequence of commands may be issued,
in any order, including another PLACE command. 
- The application should discard all commands in the sequence until a valid PLACE command has been executed. 
- MOVE will move the toy robot one unit forward in the direction it is currently facing. 
- LEFT and RIGHT will rotate the robot 90 degrees in the specified direction without changing the position of the robot. 
- REPORT will announce the X,Y and orientation of the robot. 
- A robot that is not on the table can choose to ignore the MOVE, LEFT, RIGHT and REPORT commands.
- Accepted commands: MOVE, LEFT, RIGHT, REPORT 
- Accepted Directions: NORTH, SOUTH, EAST, WEST


#### Accepted format
    PLACE X,Y,F
    MOVE
    LEFT
    RIGHT
    REPORT

#### Examples
    Example 1:

    PLACE 0,0,NORTH
    MOVE
    REPORT
    Output: 0,1,NORTH

    Example 2:
    PLACE 0,0,NORTH
    LEFT
    REPORT
    Output: 0,0,WEST

    Example 3:
    PLACE 1,2,EAST
    MOVE
    MOVE
    LEFT
    MOVE
    REPORT
    Output: 3,3,NORTH


# Environment setup
1. Install any python version and pip (python package manager) on your machine 
2. Using pip manager shipped with python install pipenv. You can follow below link https://pypi.org/project/pipenv/


# Steps to run simulator
1. Run command `pipenv install`
2. To active virtual environment run `pipenv shell`
3. Navigate to root directory of the project and run `python toy_robot_simulator/simulator`

### Note: Follow the instructions to run the simulator 

# Steps to run testcases
- ### run single test module
    Navigate to tests directory and run `python <module-name>`<br> 
    example `python test_commands.py`
- ### run entire test-suite
    Navigate to  tests directory and run `python -m unittest discover .`


#### Author: Prince Dogra
