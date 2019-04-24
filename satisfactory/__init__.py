from satisfactory.game import Game

def get_next_building_for_supply_chain(buildings):
    print("\nselect next building for the supply chain:")
    for building in buildings:
        print(building.id, building.name)

    print("\ncalculate? Enter 0")
    selected_id = input("select an id:\n")

    print("\n\n\n")
    for building in buildings:
        if building.id == selected_id:
            return building

    return None

def print_supply_chain(supply_chain):
    print("curent supply chain")
    if supply_chain != None and len(supply_chain) > 0:
        for index in range(0, len(supply_chain)):
            print(supply_chain[index].name)
            if index < len(supply_chain) - 1:
                print"||"

if __name__ == "__main__":
    game = Game()

    supply_chain = [game.buildings[0], game.buildings[2], game.buildings[5]]
    while True:
        print_supply_chain(supply_chain)
        next_building = get_next_building_for_supply_chain(game.buildings)

        if next_building == None:
            game.calculate(supply_chain)
            break
        else:
            supply_chain.append(next_building)


