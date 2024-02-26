# Screen object - All data of the screen will be store in there
class Screen():
    def __init__(self, size:tuple, caption:str) -> None:
        
        # Size
        self.size = size
        self.width = size[0]
        self.height = size[1]

        # Title
        self.caption = caption

# Screen data
WIN = Screen((900,500),"RPG game")