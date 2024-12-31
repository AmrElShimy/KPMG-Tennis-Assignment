class TennisScorer:
    @staticmethod
    def validate_tennis_scores(score1, score2):
        if score1 < 0 or score2 < 0:
            return False

        if score1 <= 4 and score2 <= 4:
            return True

        if score1 >= 4 or score2 >= 4:
            if abs(score1 - score2) <= 2:
                return True
        return False

    def calculate_score(self, score1, score2):
        if not self.validate_tennis_scores(score1, score2):
            return "Invalid Score"

        tennis_terms = ["Love", "15", "30", "40"]

        if score1 == score2:
            if score1 < 3:
                return f"{tennis_terms[score1]} All"
            else:
                return "Deuce"

        if score1 >= 4 or score2 >= 4:
            if abs(score1 - score2) >= 2 and (score1 >= 4 or score2 >= 4):
                return f"Player {1 if score1 > score2 else 2} Wins"
            elif score1 > score2:
                return "Advantage Player 1"
            else:
                return "Advantage Player 2"

        return f"{tennis_terms[score1]} - {tennis_terms[score2]}"
