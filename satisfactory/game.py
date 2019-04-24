from satisfactory.building import Building
from satisfactory.convoyer_belt import ConvoyerBelt


class Game():

    def __init__(self):
        self.buildings = []
        self.convoyer_belts = []
        self.init_buildings()
        self.init_convoyer_belts()

    def print_supply_chain(supply_chain):
        if supply_chain != None and len(supply_chain) > 0:
            for index in range(0, len(supply_chain)):
                print(supply_chain[index].name)
                if index < len(supply_chain) - 1:
                    print"||"

    def calculate(self, supply_chain):
        for index in range(0, len(supply_chain)):
            print(supply_chain[index].name)

            if index < len(supply_chain) - 1:
                factor = supply_chain[index].items_per_minute_output() / supply_chain[index + 1].items_per_minute_input()
                supply_chain[index + 1].count *= factor

            print("count: " + str(supply_chain[index].count))
            print("items per minute input: " + str(supply_chain[index].items_per_minute_input()))
            print("items per minute output: " + str(supply_chain[index].items_per_minute_output()))
            print("\n")


    def init_buildings(self):
        # id, name, input, output, time, power, input_amount, output_amount
        self.buildings.append(Building(1, "Miner Mk.1", 0, 1, 1, 5, 0, 1))
        self.buildings.append(Building(2, "Miner Mk.2", 0, 1, 1, 5, 0, 2))
        self.buildings.append(Building(3, "Smelter Iron Ignot", 1, 1, 2, 4, 1, 1))
        self.buildings.append(Building(4, "Smelter Copper Ignot", 1, 1, 2, 4, 1, 1))
        self.buildings.append(Building(5, "Smelter Copper Carterium", 1, 1, 4, 4, 4, 1))
        self.buildings.append(Building(6, "Constructor Iron Plate", 1, 1, 4, 4, 2, 1))
        self.buildings.append(Building(7, "Constructor Iron Rod", 1, 1, 4, 4, 1, 1))
        self.buildings.append(Building(8, "Constructor Wire", 1, 1, 4, 4, 1, 3))
        self.buildings.append(Building(9, "Constructor Cable", 1, 1, 4, 4, 2, 1))

    def init_convoyer_belts(self):
        #n name, items_per_minute
        self.convoyer_belts.append(ConvoyerBelt("Mk.1", 60))
        self.convoyer_belts.append(ConvoyerBelt("Mk.2", 120))
        self.convoyer_belts.append(ConvoyerBelt("Mk.3", 270))
        self.convoyer_belts.append(ConvoyerBelt("Mk.4", 450))