import unittest
from core.score_calculator import TennisScorer


class TestTennisScorer(unittest.TestCase):
    def setUp(self):
        self.scorer = TennisScorer()

    def test_valid_scores(self):
        self.assertTrue(self.scorer.validate_tennis_scores(0, 0), "Validation failed for score 0-0.")
        self.assertTrue(self.scorer.validate_tennis_scores(3, 3), "Validation failed for score 3-3.")
        self.assertTrue(self.scorer.validate_tennis_scores(4, 3), "Validation failed for score 4-3.")
        self.assertTrue(self.scorer.validate_tennis_scores(6, 4), "Validation failed for score 6-4.")
        print("All valid score tests passed.")

    def test_invalid_scores(self):
        self.assertFalse(self.scorer.validate_tennis_scores(-1, 3), "Validation should fail for score -1-3.")
        self.assertFalse(self.scorer.validate_tennis_scores(20, 1), "Validation should fail for score 20-1.")
        self.assertFalse(self.scorer.validate_tennis_scores(5, 0), "Validation should fail for score 5-0.")
        print("All invalid score tests passed.")

    def test_calculate_score(self):
        self.assertEqual(self.scorer.calculate_score(0, 0), "Love All", "Incorrect result for score 0-0.")
        self.assertEqual(self.scorer.calculate_score(0, 1), "Love - 15", "Incorrect result for score 0-1.")
        self.assertEqual(self.scorer.calculate_score(1, 0), "15 - Love", "Incorrect result for score 1-0.")
        self.assertEqual(self.scorer.calculate_score(2, 0), "30 - Love", "Incorrect result for score 2-0.")
        self.assertEqual(self.scorer.calculate_score(0, 2), "Love - 30", "Incorrect result for score 0-2.")
        self.assertEqual(self.scorer.calculate_score(1, 1), "15 All", "Incorrect result for score 1-1.")
        self.assertEqual(self.scorer.calculate_score(3, 0), "40 - Love", "Incorrect result for score 3-0.")
        self.assertEqual(self.scorer.calculate_score(0, 3), "Love - 40", "Incorrect result for score 0-3.")
        self.assertEqual(self.scorer.calculate_score(1, 2), "15 - 30", "Incorrect result for score 1-2.")
        self.assertEqual(self.scorer.calculate_score(2, 1), "30 - 15", "Incorrect result for score 2-1.")
        self.assertEqual(self.scorer.calculate_score(2, 2), "30 All", "Incorrect result for score 2-2.")
        self.assertEqual(self.scorer.calculate_score(3, 1), "40 - 15", "Incorrect result for score 3-1.")
        self.assertEqual(self.scorer.calculate_score(1, 3), "15 - 40", "Incorrect result for score 1-3.")
        self.assertEqual(self.scorer.calculate_score(3, 2), "40 - 30", "Incorrect result for score 3-2.")
        self.assertEqual(self.scorer.calculate_score(2, 3), "30 - 40", "Incorrect result for score 2-3.")
        self.assertEqual(self.scorer.calculate_score(3, 3), "Deuce", "Incorrect result for score 3-3.")
        self.assertEqual(self.scorer.calculate_score(4, 3), "Advantage Player 1", "Incorrect result for score 4-3.")
        self.assertEqual(self.scorer.calculate_score(3, 4), "Advantage Player 2", "Incorrect result for score 3-4.")
        self.assertEqual(self.scorer.calculate_score(5, 3), "Player 1 Wins", "Incorrect result for score 5-3.")
        self.assertEqual(self.scorer.calculate_score(3, 5), "Player 2 Wins", "Incorrect result for score 3-5.")
        self.assertEqual(self.scorer.calculate_score(4, 2), "Player 1 Wins", "Incorrect result for score 4-2.")
        print("All calculate score tests passed.")

    def test_invalid_calculate_score(self):
        self.assertEqual(self.scorer.calculate_score(-1, 3), "Invalid Score", "Expected 'Invalid Score' for -1-3.")
        self.assertEqual(self.scorer.calculate_score(20, 1), "Invalid Score", "Expected 'Invalid Score' for 20-1.")
        self.assertEqual(self.scorer.calculate_score(5, 0), "Invalid Score", "Expected 'Invalid Score' for 5-0.")
        print("All invalid calculate score tests passed.")


if __name__ == "__main__":
    unittest.main()
