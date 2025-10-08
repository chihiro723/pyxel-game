class Score:
    def __init__(self):
        self.score = 0

    def updateScore(self):
        self.score += 1

    def evaluate(self, score):
        if score >= 1000:
            return "SS"
        elif score >= 800:
            return "S"
        if score >= 500:
            return "A"
        if score >= 400:
            return "B"
        if score >= 300:
            return "C"
        else:
            return "D"
        
    def getEvaluationColor(self, score):
        if score == "SS":
            return 8
        if score == "S":
            return 9
        if score == "A":
            return 10
        if score == "B":
            return 11
        if score == "C":
            return 2
        if score == "D":
            return 13
        else:
            return 5


   