import unittest
import puzzle_game
# import sys
# sys.path.append('/Users/eduardo/Documents/2024-2/testes/exercicio_4/EightPuzzle')

class TestBoard(unittest.TestCase):
    
    def setUp(self):
        self.puzzle = puzzle_game.PuzzleGame(3)
 
    def test_line_all_c_uses_1(self):
        tile = self.puzzle.get_tile(3, 2)
        self.assertEqual(tile, 8)
        
    def test_line_all_p_uses_1(self):
        tile = self.puzzle.get_tile(3, 2)
        self.assertEqual(tile, 8)
        
    def test_line_all_p_uses_2(self):
            tile = self.puzzle.get_tile(3, 3)
            self.assertEqual(tile, " ")

    def test_line_all_uses_3(self):
        with self.assertRaises(puzzle_game.InvalidPositionException):
            self.puzzle.get_tile(-3, 2)
            
    def test_column_all_c_uses_1(self):
        tile = self.puzzle.get_tile(3, 2)
        self.assertEqual(tile, 8)
        
    def test_column_all_p_uses_1(self):
        tile = self.puzzle.get_tile(3, 2)
        self.assertEqual(tile, 8)
        
    def test_column_all_p_uses_2(self):
            tile = self.puzzle.get_tile(3, 3)
            self.assertEqual(tile, " ")

    def test_column_all_uses_3(self):
        with self.assertRaises(puzzle_game.InvalidPositionException):
            self.puzzle.get_tile(-3, 2)
        
    
 
if __name__ == '__main__':
    unittest.main()