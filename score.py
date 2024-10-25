class Score():
    def __init__(self):
        self.score = 0
        #self.high_score = high_score

    
    def add_point(self):
        self.score += 1


    def get_score(self):
        return self.score


    def get_high_score(self):
        try:
            f = open('high_score.txt', 'r')
            high_score = f.read()
            f.close()
            return int(high_score)
        except FileNotFoundError:
            return 0
        

    def write_high_score(self):
        high_score = self.get_high_score()
        if self.score > high_score:
            f = open('high_score.txt', 'w')
            f.write(str(self.score))