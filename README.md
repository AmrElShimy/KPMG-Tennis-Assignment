#  KPMG Python Tennis Scoreboard Assignment

## Overview
This project is a score calculator for Tennis matches. It has a simple calculation and score validation methods with a
UI to display what it might look like looking a Tennis scoring board during a match. This code is full implemented in Python.
"tkinter" library is used to create a render of the scoring board. Tennis terminologies are used to view the score.

## How to Run?
Make sure that you have Python installed on your device. The project was implemented on **Python (Version 3.10.0)**.
Make sure the packages are installed. Make sure ```pip``` is installed on your machine. You can install the packages in the ```requirements.txt``` file.

```
pip install -r requirements.txt
```

To run the application (depending on the alias you have for Python):

```
python main.py
```
OR
```
python3 main.py
```


## Tennis Scoring Rules

Tennis has a rather interesting scoring system. The points increment irregularly than any other sports. The score goes as follows:

- 1 point -> 15
- 2 point -> 30
- 3 point -> 40 (Match Point)
- 4 - > Match

But it is not that simple. A player wins the game if they have at least two point difference of in the score. Things
become a little bit more interesting once the scores are tied in at the match point. This is called a "Deuce". A player
needs to score two times in a row to be able to win. The player who scores the first point has an advantage. If the other player
scores, they go back to "Deuce".

### Example
```
 -----------------------------------------------------
| Player 1 | Player 2      | Score Displayed          |
| ----------------------------------------------------|
| 3        |  3            |   Deuce                  |  
| 4        |  3            |   Advantage for Player 1 |
| 4        |  4            |   Deuce                  |
| 4        |  5            |   Advantage for Player 2 |
| 3        |  6            |   Player 2 wins          |  
 -----------------------------------------------------
```

There are also some terminologies that are used regularly in Tennis. For example, when the scores are below 40 and tied, 
the score as said as the number and "All" is added to it. A score of zero is also referred as "Love". The following table
might give an idea about that:

```
 -----------------------------------------------------
| Player 1 | Player 2      | Score Displayed          |
| ----------------------------------------------------|
| 0        |  0            |   Love All               |  
| 1        |  0            |   15 - Love              |
| 0        |  1            |   Love - 15              |
| 2        |  2            |   30 All                 |
| 3        |  2            |   40 - 30                |  
 -----------------------------------------------------
```

## Code Explanation
The code has to main methods that implement and validate the scoring of the Tennis match.

### Functions:

#### _**validate_tennis_scores(score1, score2)**_

This functions validates if the scores entered are valid to the scoring rules of Tennis. There are 3 rules that need to
checked:
- _Scores can't be negative numbers_
- _Scores can't have an incremental difference of more than 2 if a deuce has not been reached_

#### _**calculate_score(score1, score2)**_

This functions checks and displays the scores according to the state of the game taking into consideration deuces, advantages, and basic score.

## UI and Functionality (How to Use)
The UI uses Python's "tkinter" library to render the buttons, the frame, and text inputs. There are two main views that UI has.
The first and the main one is a view with two text inputs, one for each player. You can press the "Generate Random Scores"
button to generate random scores and view how would they look like in a scoreboard. You can also enter the scores and press the
"Submit Scores" button to for manual input. You can also upload an Excel or CSV with two columns that could hold the score.
The application parses the CSV and creates a display where you can navigate between scores. Invalid scores would be displayed as invalid.


## To Run The Tests ##

Make ```unittest``` package is installed. To run the tests:

```
python -m unittest discover -s tests 
```

OR

```
python3 -m unittest discover -s tests 
```