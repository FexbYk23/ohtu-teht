class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.games = games
        self.nationality = nationality
        self.team = team
    
    def __str__(self):
        pts = self.goals + self.assists
        return f"{self.name:20} {self.team} {self.goals} + {self.assists} = {pts}"
