import matchers

class QueryBuilder:
    def __init__(self, matcher = matchers.All()):
        self.matcher = matcher

    def build(self):
        return self.matcher

    def playsIn(self, team):
        return QueryBuilder(matchers.And(self.matcher, matchers.PlaysIn(team)))
    
    def hasAtLeast(self, amount, attr):
        return QueryBuilder(matchers.And(self.matcher, matchers.HasAtLeast(amount, attr)))
    
    def hasFewerThan(self, amount, attr):
        return QueryBuilder(matchers.And(self.matcher, matchers.HasFewerThan(amount, attr)))

