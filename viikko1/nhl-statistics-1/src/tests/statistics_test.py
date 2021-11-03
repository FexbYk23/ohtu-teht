import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatistics(unittest.TestCase):
    
    def setUp(self):
        self.stats = Statistics(PlayerReaderStub())

    def test_search(self):
        self.assertEqual(self.stats.search("Semenko").points, 16)
    
    def test_search_not_found(self):
        self.assertEqual(self.stats.search("Pete"), None)

    def test_team(self):
        self.assertEqual(len(self.stats.team("EDM")), 3)
        self.assertEqual(len(self.stats.team("ABC")), 0)
        self.assertEqual(len(self.stats.team("DET")), 1)

    def test_top_scorers(self):
        top3 = self.stats.top_scorers(2)
        self.assertEqual(len(top3), 3)
        self.assertEqual(top3[0].points, 89+35)



