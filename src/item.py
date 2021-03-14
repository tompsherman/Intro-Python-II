class Item:

    def __init__(self, name, description, location):

        self.name = name
        self.description = description
        self.location = location

    def __str__(self):

        return f"{self.name} can {self.description}"