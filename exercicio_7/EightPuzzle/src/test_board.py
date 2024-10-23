# test_board.py
import unittest
from unittest.mock import patch
import puzzle_game
from puzzle_game_with_mock import PuzzleGameWithPlayer
from shufflers_for_testing_puzzles import TestingShufflerPuzzleGame3x3To12345X786


class TestBoard(unittest.TestCase):
    
    def setUp(self):
        self.puzzle = puzzle_game.PuzzleGame(3)
        self.puzzle_with_player = PuzzleGameWithPlayer(3, "Player1")


    # PARTE 1
    def test_get_tile_sem_mock_1(self):
        tile = self.puzzle.get_tile(3, 3)
        self.assertEqual(tile, ' ')
 
    def test_get_tile_sem_mock_2(self):
        tile = self.puzzle.get_tile(3, 2)
        self.assertEqual(tile, 8)
        
    @patch('puzzle_game.PuzzleGame.get_tile')
    def test_get_tile_mock_1(self, mock_get_tile):
        mock_get_tile.return_value = ' '
        tile = self.puzzle.get_tile(3, 3)
        self.assertEqual(tile, ' ')

    @patch('puzzle_game.PuzzleGame.get_tile')
    def test_get_tile_mock_2(self, mock_get_tile):
        mock_get_tile.return_value = 8
        tile = self.puzzle.get_tile(3, 2)
        self.assertEqual(tile, 8)
        
    # PARTE 2
    def test_end_of_the_game_sem_mock_1(self):
        result = self.puzzle_with_player.end_of_the_game()
        self.assertEqual(result, "Saved")

    def test_end_of_the_game_sem_mock_2(self):
        TestingShufflerPuzzleGame3x3To12345X786.shuffle(self, self.puzzle_with_player)
        result = self.puzzle_with_player.end_of_the_game()
        self.assertEqual(result, "Game not finished")
        
    @patch('puzzle_game_with_mock.PuzzleGameWithPlayer.save_game_to_file')
    def test_end_of_the_game_com_mock_1(self, mock_save_game_to_file):
        mock_save_game_to_file.return_value = "Saved"
        result = self.puzzle_with_player.end_of_the_game()
        self.assertEqual(result, "Saved")
        
    @patch('puzzle_game_with_mock.PuzzleGameWithPlayer.save_game_to_file')
    def test_end_of_the_game_com_mock_2(self, mock_save_game_to_file):
        TestingShufflerPuzzleGame3x3To12345X786.shuffle(self, self.puzzle_with_player)
        mock_save_game_to_file.return_value = "Saved"
        result = self.puzzle_with_player.end_of_the_game()
        self.assertNotEqual(result, "Saved")

if __name__ == '__main__':
    unittest.main()