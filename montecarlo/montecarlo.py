# Monte Carlo Module

"""
Import pandas as pd and numpy as np for use throughout the module
"""

import pandas as pd
import numpy as np

class Die():
    """
    Required inputs: 
    - Number of faces of the die (data type = NumPy array)
    
    This class simulates die rolls. The class accepts the number of faces of the die as an input as a NumPy array in the 
    init chunk. The corresponding weights of each face can be adjusted if desired using the weight_update method. The 
    weights default to 1 if not updated. The roll method returns a list of outcomes and can be used to simulate
    as many rolls of the die as desired. The number of rolls defaults to 1. The die method returns the current state of 
    the die with the number of faces and corresponding weights. 
        """
    
    def __init__(self, faces):
        """
        Required inputs: 
        - Number of faces of the die (data type = NumPy array)
        
        This init chunk takes a NumPy array of faces as an argument and throws a `TypeError` if not a NumPy array. The 
        array’s data type `dtype` may be strings or numbers and will raise a `TypeError` if not. The array’s values have 
        to be distinct and raises a `ValueError` if not. The weights for each face are initialized as 1.0. The face values
        along with their corresponding weights are saved as the weighted_faces dataframe with faces as the index.

        """
        self.faces = faces
        if not isinstance(faces, np.ndarray):
            raise TypeError("The input for the amount of faces needs to be a NumPy array.")
        if not np.issubdtype(faces.dtype, np.number) and not np.issubdtype(faces.dtype, np.str_):
            raise TypeError("The input for the amount of faces needs to be either numbers or strings.")
        if not np.array_equal(np.unique(faces), faces):
            raise ValueError("The input for the amount of faces needs to be distinct (unique) values.")
        weights = np.ones(len(faces))
        self.weighted_faces = pd.DataFrame(data={"weights": weights}, index=faces)
                
    def weight_update(self, face_index, weight):
        """
        Required inputs: 
        - The face value to be changed (data type the same as given within the NumPy array, i.e. numeric or string)
        - The new weight for the given face (data type must be numeric or castable as numeric)
        
        This method can be used to update the weight associated with any face of the die.It takes two arguments, 
        the face value to be changed and the new weight. It checks to see if the face passed is valid value, i.e. if it 
        is in the die array. If not, raises an `IndexError`. It also checks to see if the weight is a valid type, i.e. if 
        it is numeric(integer or float) or castable as numeric. If not, raises a `TypeError`.
        """
        if face_index not in self.weighted_faces.index:
            raise IndexError("The given value for the face is not in the faces NumPy array.")
        try:
            weight = float(weight)
        except (TypeError, ValueError):
            raise TypeError("The weight data type must be either numeric or castable as a numeric.")
        self.weighted_faces["weights"][face_index] = weight
                
    def roll(self, rolls=1):
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
        
        return [np.random.choice(self.weighted_faces.index, replace = True, 
                p = self.weighted_faces["weights"] / self.weighted_faces["weights"].sum()) for i in range(rolls)]

    def die(self): 
        """
        Returns:
        - The weighted_faces data frame.
        
        This method returns the current state of the die and its associated weights.
        """
        return self.weighted_faces
    
    
    
class Game():
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

    def __init__(self, die_list):
        """
        Required inputs: 
        - A python list that contains one or more dice
    
        This init chunk requires a Python list of one or more dice to be input. It initializes this list for use throughout 
        the Game class.
        """
        self.die_list = die_list
        self.play_output = None
        
    def play(self, rolls):
        """
        Required inputs: 
        - The number of times the dice should be rolled (input as an integer)
    
        This play method takes an integer parameter to specify how many times the dice should be rolled. Saves the result 
        of the play to a private data frame. The data frame is in wide format, i.e. has the roll number is a named index 
        'Roll Number', the columns for each die number use its list index as the column name, and the face rolled is the 
        instance in each cell.
        """
        output = []
        for i in range(rolls):
            roll_output = []
            for i in self.die_list:
                r = i.roll()
                roll_output.append(r)
            output.append(roll_output)
        self.play_output = pd.DataFrame(output)
        self.play_output = self.play_output.applymap(lambda x: x[0])
        self.play_output.index.name = "Roll Number"
    def recent_play(self, form = "Wide"):
        """
        Required inputs: 
        - The form of the output dataframe (input as a string either 'Wide' or 'Narrow' ; default is 'Wide'
        
        This recent play method returns a copy of the private play data frame to the user. It takes a parameter to return 
        the data frame in narrow or wide form which defaults to wide form. The narrow form has a MultiIndex, comprising
        of the roll number and the die number (in that order), and a single column with the outcomes (i.e. the face rolled).
        This method raises a ValueError if the user passes an invalid option for narrow or wide.
        """
    
        if form == "Wide":
            return self.play_output
        elif form == "Narrow":
            self.play_output_narrow = pd.DataFrame(self.play_output.stack())
            self.play_output_narrow.index.names = ["Roll Number", "Die Number"]
            self.play_output_narrow.columns = ["Outcome"]
            return self.play_output_narrow
        else:
            raise ValueError("The input for the form of the output must be written as 'Wide' or 'Narrow'.")
            
            
class Analyzer():
    """
    Required inputs: 
    - A single Game object
    
    This class takes the results of a single game and computes various descriptive statistical properties about it.
    
    There is an init chunk, along with the jackpot, face_count, combo, and perm methods. The jackpot method returns 
    the amount of times a roll of the dice results in all of the same faces. The face_count method returns how many 
    times a given face is rolled in each event. The combo method returns the distinct combinations of faces rolled, 
    along with their counts. The perm method returns the distinct permutations of faces rolled, along with their counts.
    """
    
    def __init__(self, game_object):
        """
        Required inputs: 
        - A single Game object
        
        This init chunk takes a game object as its input parameter and throws a ValueError if the passed value is not 
        a Game object.
        """
        
        if not isinstance (game_object, Game):
            raise ValueError ("The input must be a Game object.")
        self.game_object = game_object

        
    def jackpot(self):
        """
        A jackpot is a result in which all faces are the same, e.g. all ones for a six-sided die. This jackpot method 
        computes how many times the game resulted in a jackpot. It returns an integer for the number of jackpots.
        """
        
        test_equal = self.game_object.play_output.nunique(axis=1) == 1
        jackpot_count = test_equal.sum()
        return jackpot_count
    
    def face_count(self):
        """
        This face_count method computes how many times a given face is rolled in each event. It returns a data frame 
        of results. The data frame has an index of the roll number, face values as columns, and count values in 
        the cells (i.e. it is in wide format).
        """
        
        dice_sides = self.game_object.die_list[0].faces
        value_counts = self.game_object.play_output.apply(lambda x: x.value_counts(dropna=False), axis=1)
        face_count_output = pd.DataFrame(value_counts, index=value_counts.index, columns=dice_sides)
        face_count_output.fillna(0, inplace=True)
        face_count_output = face_count_output.astype(int)
        return face_count_output
    
    def combo(self):
        """
        This combo method computes the distinct combinations of faces rolled, along with their counts. Combinations are 
        order-independent and may contain repetitions. It returns a data frame of results. The data frame has a MultiIndex 
        of distinct combinations and a column for the associated counts.
        """
        combos = self.game_object.play_output.apply(lambda x: tuple(sorted(x)), axis=1)
        value_counts_combos = pd.Series(combos).value_counts()
        combo_output = pd.DataFrame(value_counts_combos)
        combo_output.index = pd.MultiIndex.from_tuples(combo_output.index)
        return combo_output
    
    def perm(self):
        """
        This perm method computes the distinct permutations of faces rolled, along with their counts. Permutations are 
        order-dependent and may contain repetitions. It returns a data frame of results.The data frame has a MultiIndex of 
        distinct permutations and a column for the associated counts.
        """
        perms = self.game_object.play_output.apply(tuple, axis=1)
        perm_counts = pd.Series(perms).value_counts()
        perm_output = pd.DataFrame(perm_counts)
        perm_output.index = pd.MultiIndex.from_tuples(perm_counts.index)
        return perm_output