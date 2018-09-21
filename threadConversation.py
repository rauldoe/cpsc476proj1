import datetime

from flask import jsonify

from commonUtility import commonUtility
from objectBase import objectBase

class threadConversation(objectBase):

    def __init__(self):
        super().__init__()

        self.objectLookup[self.forum_id_tag] = None
        self.objectLookup[self.title_tag] = None
        self.objectLookup[self.text1_tag] = None
        self.objectLookup[self.author_tag] = None
        self.objectLookup[self.timestamp1_tag] = None
        
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

    text1_tag = "text1"
    @property
    def text1(self):
        return self.objectLookup[self.text1_tag]

    @text1.setter
    def text1(self, value):
        self.objectLookup[self.text1_tag] = value

    author_tag = "author"
    @property
    def author(self):
        return self.objectLookup[self.author_tag]

    @author.setter
    def author(self, value):
        self.objectLookup[self.author_tag] = value

    timestamp1_tag = "timestamp1"
    @property
    def timestamp1(self):
        return self.objectLookup[self.timestamp1_tag]

    @timestamp1.setter
    def timestamp1(self, value):
        self.objectLookup[self.timestamp1_tag] = value

