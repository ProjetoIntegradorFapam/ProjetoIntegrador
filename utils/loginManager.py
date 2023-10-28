class loginManager:

    def __init__(self):

        self.__authenticated = False

    @property
    def getAuthentication(self):

        return self.__authenticated
    
    @getAuthentication.setter
    def setAuthentication(self, status):

        self.__authenticated = status
    
    def authenticate(self):

        self.__authenticated = True
        if self.__authenticated == True:
            return True
        else:
            return False
    
    def logout(self):

        self.__authenticated = False
        if self.__authenticated == False:
            return True
        else:
            return False
    
    def isAuthenticated(self):

        if self.__authenticated == True:
            return True
        else:
            return False