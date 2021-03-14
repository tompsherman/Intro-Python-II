# Implement a class to hold room information. This should have name and
# description attributes.
class Room:

    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        output = f"You are in the {self.name}:\n\n\t{self.description}\n"

        if len(self.items) > 0:
            for i, item in enumerate(self.items):
                output += f"\t[{i}]  {item}\n"
        else:
            output += f"there are no items to be found"

        return output

office = Room("office", "your man-made prison with a beautiful outlook of nature", [])

# print(office)