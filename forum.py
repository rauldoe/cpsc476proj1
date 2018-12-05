
from objectBase import objectBase

class forum(objectBase):

    def __init__(self):
        super().__init__()

        self.objectLookup[self.name_tag] = None
        self.objectLookup[self.creator_tag] = None

        self.objectDataTypeLookup[self.name_tag] = 'str'
        self.objectDataTypeLookup[self.creator_tag] = 'str'  

    name_tag = "name"
    @property
    def name(self):
        return self.objectLookup[self.name_tag]

    @name.setter
    def name(self, value):
        self.objectLookup[self.name_tag] = value
    
    creator_tag = "creator"
    @property
    def creator(self):
        return self.objectLookup[self.creator_tag]

    @creator.setter
    def creator(self, value):
        self.objectLookup[self.creator_tag] = value


