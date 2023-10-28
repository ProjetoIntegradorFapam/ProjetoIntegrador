class loginManager:

    def __init__(self):

        self.authenticated = False

    def authenticate(self):

        self.authenticated = True
        if self.authenticated == True:
            return True
        else:
            return False
    
    def logout(self):

        self.authenticated = False
        if self.authenticated == False:
            return True
        else:
            return False
    
    def isAuthenticated(self):

        if self.authenticated == True:
            return True
        else:
            return False