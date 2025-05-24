print("Name: Kushagra Suri")
print("USN: 1AY24AI058")
print("Section: M")
class Item:
    def __init__(self, name, item_type, value):
        self.name = name
        self.item_type = item_type
        self.value = value
class Inventory:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, item_name):
        self.items = [item for item in self.items if item.name != item_name]
    def display_inventory(self):
        for item in self.items:
            print(f"{item.name} - Type: {item.item_type}, Value: {item.value}")
sword = Item("Sword", "Weapon", 150)
shield = Item("Shield", "Armor", 100)
potion = Item("Health Potion", "Consumable", 50)
inventory = Inventory()
inventory.add_item(sword)
inventory.add_item(shield)
inventory.add_item(potion)
inventory.display_inventory()
