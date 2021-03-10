# Implement a class to hold room information. This should have name and
# description attributes.
class Room:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"You are in the {self.name}:\n\n\t{self.description}"

office = Room("office", "your man-made prison with a beautiful outlook of nature")

# print(office)