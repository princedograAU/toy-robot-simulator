import sys
from simulator import Simulator


def main():
    simulation = Simulator()
    flag = True
    while flag:
        user_input = input()
        if user_input == "EXIT":
            flag = False
            continue

        simulation.simulate(user_input)


if __name__ == "__main__":
    main()