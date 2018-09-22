
from objectBase import objectBase

class post(objectBase):


    def __init__(self):
        super().__init__()

        self.objectLookup[self.thread_id_tag] = None
        self.objectLookup[self.text_tag] = None
        self.objectLookup[self.poster_tag] = None
        self.objectLookup[self.timestamp_tag] = None
    
    thread_id_tag = "thread_id"
    @property
    def thread_id(self):
        return self.objectLookup[self.thread_id_tag]

    @thread_id.setter
    def thread_id(self, value):
        self.objectLookup[self.thread_id_tag] = value

    text_tag = "text"
    @property
    def text(self):
        return self.objectLookup[self.text_tag]

    @text.setter
    def text(self, value):
        self.objectLookup[self.text_tag] = value

    poster_tag = "poster"
    @property
    def poster(self):
        return self.objectLookup[self.poster_tag]

    @poster.setter
    def poster(self, value):
        self.objectLookup[self.poster_tag] = value
        
    timestamp_tag = "timestamp"
    @property
    def timestamp(self):
        return self.objectLookup[self.timestamp_tag]

    @timestamp.setter
    def timestamp(self, value):
        self.objectLookup[self.timestamp_tag] = value
