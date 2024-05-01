import numpy as np
import pandas as pd
import unittest
from montecarlo import Die
from montecarlo import Game
from montecarlo import Analyzer

class MonteCarloTestSuite(unittest.TestCase):
    """
    Module to perform unit tests on the created methods from the montecarlo module. 
    """
    
    def test_1_Die_init(self): 
        """
        Create a Die object and test if weighted_faces is created as a DataFrame from the init chunk.
        """
        test1 = Die(np.array([1, 2, 3, 4, 5, 6]))
        self.assertEqual(type(test1.weighted_faces), pd.DataFrame)
        
    def test_2_Die_weight_update(self):
        """
        Tests the weight_update method of the Die class. Specifically, tests if the first value of the weights column in the weighted_faces DataFrame is numeric or castable as a numeric.
        """
        test2 = Die(np.array([1, 2, 3, 4, 5, 6]))
        test2.weight_update(2, 100)
        self.assertTrue(isinstance(test2.weighted_faces["weights"].iloc[0],float))
        
    def test_3_Die_roll(self):
        """
        Tests the roll method of the Die class. Specifically, tests if a list is returned.
        """
        test3 = Die(np.array([1, 2, 3, 4, 5, 6]))
        self.assertTrue(isinstance(test3.roll(10), list))
    
    def test_4_Die_die(self):
        """
        Tests the die method of the Die class. Specifically, tests if the weights column is present in the returned DataFrame.
        """
        test4 = Die(np.array([1, 2, 3, 4, 5, 6]))
        self.assertTrue("weights" in test4.die().columns)
    
    def test_5_Game_init(self):
        """
        Tests the init chunk of the Game class. Specifically, tests if the die_list is initialized and a list type.
        """
        test5 = Die(np.array([1, 2, 3, 4, 5, 6]))
        test51 = Die(np.array([1, 2, 3, 4, 5, 6]))
        die_list5 = [test5, test51]
        game_test5 = Game(die_list5)
        self.assertTrue(isinstance(game_test5.die_list, list))
        
    def test_6_Game_play(self):
        """
        Tests the play method of the Game class. Specifically, tests if the amount of rows in the play_output DataFrame is properly updated with the amount of rolls input to the play method (5 in the unittest example).
        """
        test6 = Die(np.array([1, 2, 3, 4, 5, 6]))
        test61 = Die(np.array([1, 2, 3, 4, 5, 6]))
        die_list6 = [test6, test61]
        game_test6 = Game(die_list6)
        game_test6.play(5)
        self.assertEqual(len(game_test6.play_output), 5)
        
    def test_7_Game_recent_play(self):
        """
        Tests the recent_play method of the Game class. Specifically, tests MultiIndex is present when Narrow is entered as the form parameter.
        """
        test7 = Die(np.array([1, 2, 3, 4, 5, 6]))
        test71 = Die(np.array([1, 2, 3, 4, 5, 6]))
        die_list7 = [test7, test71]
        game_test7 = Game(die_list7)
        game_test7.play(5)
        self.assertTrue(isinstance(game_test7.recent_play("Narrow").index, pd.MultiIndex))
        
    def test_8_Analyzer_init(self):
        """
        Tests the init chunk of the Analyzer class. Specifically, tests that the variable game_object is in fact a Game object from the Game class.
        """
        test8 = Die(np.array([1, 2, 3, 4, 5, 6]))
        test81 = Die(np.array([1, 2, 3, 4, 5, 6]))
        die_list8 = [test8, test81]
        game_test8 = Game(die_list8)
        game_test8.play(5)
        analyze8 = Analyzer(game_test8)
        self.assertTrue(isinstance(analyze8.game_object, Game))
        
    def test_9_1_Analyzer_jackpot(self):
        """
        Tests the jackpot method of the Analyzer class. Specifically, tests that method is returning an integer.
        """
        test9 = Die(np.array([1, 2, 3, 4, 5, 6]))
        test91 = Die(np.array([1, 2, 3, 4, 5, 6]))
        die_list9 = [test9, test91]
        game_test9 = Game(die_list9)
        game_test9.play(5)
        analyze9 = Analyzer(game_test9)
        self.assertTrue(isinstance(analyze9.jackpot(), np.int64))
        
    def test_9_2_Analyzer_face_count(self):
        """
        Tests the face_count method of the Analyzer class. Specifically, tests that number of columns in the returned DataFrame is equal to the number of faces on the input die.
        """
        test10 = Die(np.array([1, 2, 3, 4, 5, 6]))
        test101 = Die(np.array([1, 2, 3, 4, 5, 6]))
        die_list10 = [test10, test101]
        game_test10 = Game(die_list10)
        game_test10.play(5)
        analyze10 = Analyzer(game_test10)
        self.assertEqual(analyze10.face_count().shape[1], len(game_test10.die_list[0].faces))
        
    def test_9_3_Analyzer_combo(self):
        """
        Tests the combo method of the Analyzer class. Specifically, tests that returned DataFrame has a MultiIndex.
        """
        test11 = Die(np.array([1, 2, 3, 4, 5, 6]))
        test111 = Die(np.array([1, 2, 3, 4, 5, 6]))
        die_list11 = [test11, test111]
        game_test11 = Game(die_list11)
        game_test11.play(5)
        analyze11 = Analyzer(game_test11)
        self.assertTrue(isinstance(analyze11.combo().index, pd.MultiIndex))
        
    def test_9_4_Analyzer_perm(self):
        """
        Tests the perm method of the Analyzer class. Specifically, tests that column in the returned DataFrame is named count.
        """
        test12 = Die(np.array([1, 2, 3, 4, 5, 6]))
        test121 = Die(np.array([1, 2, 3, 4, 5, 6]))
        die_list12 = [test12, test121]
        game_test12 = Game(die_list12)
        game_test12.play(5)
        analyze12 = Analyzer(game_test12)
        self.assertEqual(analyze12.perm().columns[0], "count")
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)