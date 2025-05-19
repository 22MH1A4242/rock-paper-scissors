import unittest
from main import determine_winner

class TestRPSGame(unittest.TestCase):
    def test_tie(self):
        self.assertEqual(determine_winner("rock", "rock"), "It's a tie!")
    
    def test_user_wins(self):
        self.assertEqual(determine_winner("rock", "scissors"), "You win!")
    
    def test_computer_wins(self):
        self.assertEqual(determine_winner("scissors", "rock"), "Computer wins!")

if __name__ == "__main__":
    unittest.main()
