# Write a class to hold player information, e.g. what room they are in
# currently.
# from room import Room

class Player:
    
    def __init__(self, current_room):
        self.current_room = current_room

    def move(self, direction):
        bearing = f"{direction}_to"

        if hasattr(self.current_room, bearing):
            new_room = getattr(self.current_room, bearing)
            # print(new_current_room)
            self.current_room = new_room
            # print(self.room)
        else:
            print("DANGER! DANGER! TURN AROUND!")

    def __str__(self):
        return f"{self.current_room}"

tom = Player("office")

# print(tom)