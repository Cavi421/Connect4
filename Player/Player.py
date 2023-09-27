import abc

class PlayerClass(abc.ABC):

    def __init__(self, player_id: int):
        self.id = player_id
        self.SetName()

    @abc.abstractmethod
    def ThinkMove(self):
        pass

    
    @abc.abstractmethod
    def SetName(self):
        pass