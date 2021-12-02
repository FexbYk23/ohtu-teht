class TennisGame:
    LEAD_SCORE_TRESHOLD = 4

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 = self.m_score1 + 1
        elif player_name == self.player2_name:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.__get_equal_score_name(self.m_score1)
        elif self.m_score1 >= self.LEAD_SCORE_TRESHOLD or self.m_score2 >= self.LEAD_SCORE_TRESHOLD:
            return self.__get_lead_text()
        else:
            return self.__get_score_name(self.m_score1) + "-" + self.__get_score_name(self.m_score2)

    def __get_equal_score_name(self, score):
        if score > 3:
            return "Deuce"
        return self.__get_score_name(score) + "-All"

    def __get_score_name(self, score):
         return ["Love", "Fifteen", "Thirty", "Forty"][score]

    def __get_lead_text(self):
        score_diff = abs(self.m_score1 - self.m_score2)
        leading_player = self.player1_name if self.m_score1 > self.m_score2 else self.player2_name
 
        if score_diff >= 2:
            return "Win for " + leading_player
        return "Advantage " + leading_player

