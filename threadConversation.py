
from objectBase import objectBase

class threadConversation(objectBase):

    def __init__(self):
        super().__init__()

        self.objectLookup[self.forum_id_tag] = None
        self.objectLookup[self.title_tag] = None
        self.objectLookup[self.text_tag] = None
        self.objectLookup[self.author_tag] = None
        self.objectLookup[self.timestamp_tag] = None

        self.objectDataTypeLookup[self.forum_id_tag] = 'int'
        self.objectDataTypeLookup[self.title_tag] = 'str'
        self.objectDataTypeLookup[self.text_tag] = 'str'
        self.objectDataTypeLookup[self.author_tag] = 'str'
        self.objectDataTypeLookup[self.timestamp_tag] = 'datetime'      

    forum_id_tag = "forum_id"
    @property
    def forum_id(self):
        return self.objectLookup[self.forum_id_tag]

    @forum_id.setter
    def forum_id(self, value):
        self.objectLookup[self.forum_id_tag] = value

    title_tag = "title"
    @property
    def title(self):
        return self.objectLookup[self.title_tag]

    @title.setter
    def title(self, value):
        self.objectLookup[self.title_tag] = value

    text_tag = "text"
    @property
    def text(self):
        return self.objectLookup[self.text_tag]

    @text.setter
    def text(self, value):
        self.objectLookup[self.text_tag] = value

    author_tag = "author"
    @property
    def author(self):
        return self.objectLookup[self.author_tag]

    @author.setter
    def author(self, value):
        self.objectLookup[self.author_tag] = value

    timestamp_tag = "timestamp"
    @property
    def timestamp(self):
        return self.objectLookup[self.timestamp_tag]

    @timestamp.setter
    def timestamp(self, value):
        self.objectLookup[self.timestamp_tag] = value

