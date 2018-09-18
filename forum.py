class forum:
    id = 1
    name = "name3"
    creator = "creator5"

    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'creator': self.creator,
        }