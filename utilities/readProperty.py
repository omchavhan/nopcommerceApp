import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('comman info','base_URL')
        return url

    @staticmethod
    def getUserMail():
        username = config.get('comman info','username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('comman info','password')
        return password

