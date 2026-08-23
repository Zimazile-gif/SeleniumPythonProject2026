import configparser

config=configparser.RawConfigParser
config.read("./Configuration/CommonDetails.ini")

class ReadConfig_CommonDetails():
    def getDevUrl(self):
        return config.get("Server Connection", "dev_Url")

    def getUsername(self):
        return config.get("Login Details", "Username")

    def getPassword(self):
        return config.get("Login Details", "Password")

