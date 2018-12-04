
from objectBase import objectBase

class post1(objectBase):


    def __init__(self):
        super().__init__()

        self.objectLookup[self.thread_id_tag] = None
        self.objectLookup[self.text1_tag] = None
        self.objectLookup[self.poster_tag] = None
        self.objectLookup[self.timestamp1_tag] = None
    
    thread_id_tag = "thread_id"
    @property
    def thread_id(self):
        return self.objectLookup[self.thread_id_tag]

    @thread_id.setter
    def thread_id(self, value):
        self.objectLookup[self.thread_id_tag] = value

    text1_tag = "text1"
    @property
    def text1(self):
        return self.objectLookup[self.text1_tag]

    @text1.setter
    def text1(self, value):
        self.objectLookup[self.text1_tag] = value

    poster_tag = "poster"
    @property
    def poster(self):
        return self.objectLookup[self.poster_tag]

    @poster.setter
    def poster(self, value):
        self.objectLookup[self.poster_tag] = value
        
    timestamp1_tag = "timestamp1"
    @property
    def timestamp1(self):
        return self.objectLookup[self.timestamp1_tag]

    @timestamp1.setter
    def timestamp1(self, value):
        self.objectLookup[self.timestamp1_tag] = value
