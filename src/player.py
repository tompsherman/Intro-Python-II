# Write a class to hold player information, e.g. what room they are in
# currently.
# from room import Room

class Player:
    
    def __init__(self, room):
        self.room = room

    def move(self, direction):
        bearing = f"{direction}_to"

        if hasattr(self.room, bearing):
            new_room = getattr(self.room, bearing)
            # print(new_room)
            self.room = new_room
            # print(self.room)
        else:
            print("DANGER! DANGER! TURN AROUND!")

    def __str__(self):
        return f"{self.room}"

tom = Player("office")

# print(tom)