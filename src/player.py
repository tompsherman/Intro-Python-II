# Write a class to hold player information, e.g. what room they are in
# currently.
# from room import Room

class Player:
    
    def __init__(self, current_room, item_inventory):
        self.current_room = current_room
        self.item_inventory = item_inventory

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
        output = f"{self.current_room}"

        if len(self.item_inventory) > 0:

            for i, item in enumerate(self.item_inventory):

                output += f"\nyou have {len(self.item_inventory)} items in inventory:\n\t [{i}]   {item}\n"

        else: 
            output += f"\nyou have no items in inventory\n"

        return output

tom = Player("office", [])

# print(tom)