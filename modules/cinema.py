import json

class Cinema(object):
    
    def __init__(self) -> None:
        # Fetch the cinema config data
        self.config = self.get_config()
        
    def getConfig(self, fileLocation: str = 'config/cinema.json') -> dict:
        fileConfig = None
        # Read the config file
        with open(fileLocation, 'r') as file:
            fileConfig = json.load(file)
            file.close()
        return fileConfig
    
    def getCinemas(self) -> list:
        return self.config['cinemas']