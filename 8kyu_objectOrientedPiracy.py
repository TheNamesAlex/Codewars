class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    def is_worth_it(self):
        
        if -self.crew*1.5 + self.draft > 20:
            return True
        return False