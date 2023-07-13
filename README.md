# SmallPythonProjects
Here is a repo with small python projects

## Configurations
Create a virtual environmnet using the instructions presented [here](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/) or simply run the following commands.
```
pip install virtualenv
python -m venv env  
```
Then activate your enviroment (on Windows)
```
env/Scripts/activate.bat
```
## First project (Pig game)
It is a dice game where each player gets the chance to roll a dice until they hit 1 or they reach the maximum score.
Anything other than 1 is added to the total score of the player. 
If the current player hits the 1 face of the dice, its total score will be converted into a 0.