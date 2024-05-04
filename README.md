# sck4jh_ds5100_montecarlo
Sam Knisely Final Project DS5100

# Metadata
* Package Name: montecarlo
* Package Includes: __init__.py, montecarlo.py, montecarlo_test.py
* Additional Files in Repo: setup.py, montecarlo_demo.ipynb, montecarlo_test_results.txt, scrabble_words.txt, english_letters.txt, README.md
* LICENSE: MIT
* Written by: Sam Knisely
* UVA ID: sck4jh
* UVA Email: sck4jh@virginia.edu
* Date Created: May 1, 2024
* Built With: pandas, numpy

# Synopsis
The classes can be called in a Jupyter Notebook. See below:

```python
###Import the montecarlo module from the montecarlo package

from montecarlo import montecarlo



###Call the Die class with a numpy array parameter

#Numpy array example
import numpy as np
numpy_array = np.array([1, 2, 3, 4, 5, 6])

#Call the Die class and create the Die_Example Die object
Die_object = montecarlo.Die(numpy_array)




###Call the Game class with a list of Die objects and call the play method to play 1000 times

#Create list of Die objects
die_list = [Die_object, Die_object]

#Call the Game class and create a Game object
Game_object = montecarlo.Game(die_list)

#Call the play method to play 1000 times
Game_object.play(1000)




###Call the Analyzer class with a Game Object

Analyzer_object = montecarlo.Analyzer(Game_object)

```

# API
## Die Class
    
        """
        Required inputs: 
        - Number of faces of the die (data type = NumPy array)
    
        This class simulates die rolls. The class accepts the number of faces of the die as an input as a NumPy array in the 
        init chunk. The corresponding weights of each face can be adjusted if desired using the weight_update method. The 
        weights default to 1 if not updated. The roll method returns a list of outcomes and can be used to simulate
        as many rolls of the die as desired. The number of rolls defaults to 1. The die method returns the current state of 
        the die with the number of faces and corresponding weights.
        """
  
### Methods:

* weight_update

        """
        Required inputs: 
        - The face value to be changed (data type the same as given within the NumPy array, i.e. numeric or string)
        - The new weight for the given face (data type must be numeric or castable as numeric)
        
        This method can be used to update the weight associated with any face of the die.It takes two arguments, 
        the face value to be changed and the new weight. It checks to see if the face passed is valid value, i.e. if it 
        is in the die array. If not, raises an IndexError. It also checks to see if the weight is a valid type, i.e. if 
        it is numeric(integer or float) or castable as numeric. If not, raises a TypeError.
        """
 
* roll

        """
        Optional inputs:
        - Number of rolls (input as an integer; default is to 1)
        
        Returns:
        - Outcomes of the rolls (as a list)
        
        This method simulates the die rolls and returns the outcomes as a list. It takes a parameter of how many times the 
        die is to be rolled; defaults to 1. This is essentially a random sample with replacement, from the private die 
        data frame, that applies the weights. It returns a Python list of outcomes and does not store internally these 
        results.
        """
* die

        """
        Returns:
        - The weighted_faces data frame.
        
        This method returns the current state of the die and its associated weights.
        """

## Game Class

        """
        Required inputs: 
        - A python list that contains one or more Die objects
    
        This class consists of rolling of one or more similar dice (Die objects) one or more times. By similar dice, we mean 
        that each die in a given game has the same number of sides and associated faces, but each die object may have its 
        own weights. Each game is initialized with a Python list that contains one or more dice. Game objects have a 
        behavior to play a game, i.e. to roll all of the dice a given number of times. Game objects only keep the results 
        of their most recent play.
    
        There is an init chunk, along with a play and recent_play method. The play method takes the dice, rolls them a given 
        amount of times, and saves the outcomes in Wide format. The recent_play method returns the play output in either 
        Wide or Narrow format, as specified with Wide being default.
        """
### Methods:

* play

        """
        Required inputs: 
        - The number of times the dice should be rolled (input as an integer)
    
        This play method takes an integer parameter to specify how many times the dice should be rolled. Saves the result 
        of the play to a private data frame. The data frame is in wide format, i.e. has the roll number is a named index 
        'Roll Number', the columns for each die number use its list index as the column name, and the face rolled is the 
        instance in each cell.
        """


* recent_play

        """
        Required inputs: 
        - The form of the output dataframe (input as a string either 'Wide' or 'Narrow' ; default is 'Wide'
        
        This recent play method returns a copy of the private play data frame to the user. It takes a parameter to return 
        the data frame in narrow or wide form which defaults to wide form. The narrow form has a MultiIndex, comprising
        of the roll number and the die number (in that order), and a single column with the outcomes (i.e. the face rolled).
        This method raises a ValueError if the user passes an invalid option for narrow or wide.
        """

## Analyzer Class
        
        """
        Required inputs: 
        - A single Game object
    
        This class takes the results of a single game and computes various descriptive statistical properties about it.
    
        There is an init chunk, along with the jackpot, face_count, combo, and perm methods. The jackpot method returns 
        the amount of times a roll of the dice results in all of the same faces. The face_count method returns how many 
        times a given face is rolled in each event. The combo method returns the distinct combinations of faces rolled, 
        along with their counts. The perm method returns the distinct permutations of faces rolled, along with their counts.
        """
### Methods:

* jackpot

        """
        A jackpot is a result in which all faces are the same, e.g. all ones for a six-sided die. This jackpot method 
        computes how many times the game resulted in a jackpot. It returns an integer for the number of jackpots.
        """
        
        
* face_count

        """
        This face_count method computes how many times a given face is rolled in each event. It returns a data frame 
        of results. The data frame has an index of the roll number, face values as columns, and count values in 
        the cells (i.e. it is in wide format).
        """
        
        
* combo

        """
        This combo method computes the distinct combinations of faces rolled, along with their counts. Combinations are 
        order-independent and may contain repetitions. It returns a data frame of results. The data frame has a MultiIndex 
        of distinct combinations and a column for the associated counts.
        """
        
* perm

        """
        This perm method computes the distinct permutations of faces rolled, along with their counts. Permutations are 
        order-dependent and may contain repetitions. It returns a data frame of results.The data frame has a MultiIndex of 
        distinct permutations and a column for the associated counts.
        """


