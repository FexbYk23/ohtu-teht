from player import Player

class PlayerStats:
    def __init__(self, reader):
        self.players = reader.players

    def top_scorers_by_nationality(self, nationality):
        players = [x for x in self.players if x.nationality == nationality]
        return sorted(players, reverse = True, key=lambda x : x.goals + x.assists)

