class HApp:
    white = True
    whitelist = []

    def isblocked(self, qq):
        if self.white == self.whitelist.__contains__(qq):
            return False
        else:
            return True
