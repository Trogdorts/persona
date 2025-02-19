import uuid

from game.node import Character, Location, GameObject

def main():
    # Suppose your 'world' itself has an ID. If not, just use a string like "system" or "user".
    world_id = uuid.uuid4()

    # Create a location node
    home_location = Location(parent_id=world_id, data={"name": "Home"})

    # Create a character node
    alice = Character(parent_id=world_id, data={"name": "Alice", "health": 100})

    # Create an object node
    sword = GameObject(parent_id=alice.node_id, data={"name": "Sword of Destiny"})

    print(home_location)  # e.g. <Node id=... type=location parent=the_world>
    print(alice)          # e.g. <Node id=... type=character parent=the_world>
    print(sword)          # e.g. <Node id=... type=object parent=... (Alice's ID)>

    # Use the object
    sword.use()           # "You use the Sword of Destiny."

if __name__ == "__main__":
    main()
