import random
import sys
import numpy as np
import plots as plt


def choose_random_door(chosen_doors: list = []) -> int:
    # choose random door out of three or between two (or one) given numbers
    # print(f'chosen doors: {chosen_doors}')
    if chosen_doors == []:
        # if there is no limited choice doors
        return np.random.randint(3)
    
    return random.choice(chosen_doors)

def simulate_monty_hall_iteration(iterations_number: int, iteration_type: str) -> int:
    door_list = np.zeros(3)
    guessed_throphy_doors = 0

    for _ in range(iterations_number):
        throphy_door = choose_random_door()
        chosen_door = choose_random_door()

        door_list[chosen_door] = 1
        door_list[throphy_door] = 2

        revealed_door = choose_random_door([index for index, value in enumerate(door_list) if value == 0])
        door_list[revealed_door] = 3

        # print(door_list)
        # print(f'revealed: {revealed_door}')

        match iteration_type:
            case 'same_door':
                # if there is no door marked as chosen door (1), that means that the chosen door is the throphy door
                if not 1 in door_list:
                    guessed_throphy_doors += 1
            case 'different_door':
                # that means that the throphy door is different from chosen door, and considering the revealed door 
                # is always the 'goat' door, the other door left is the throphy door
                if 1 in door_list:
                    guessed_throphy_doors += 1
            case 'random_door':
                # choosing between two doors that weren't revealed
                random_choice = choose_random_door([index for index, value in enumerate(door_list) if value != 3])

                # if randomly chosen door is the throphy door the door is guessed correctly
                if door_list[random_choice] == 2:
                    guessed_throphy_doors += 1
            case _:
                exit('Wrong iteration type provided')

        door_list = np.zeros(3)
        
    return guessed_throphy_doors

def simulate_monty_hall(iterations:int, repetitions: int) -> dict:
    ''' three cases are considered: when the contestant always changes their choice,
                                    when the contestant always keeps their choice,
                                    when the contestant chooses at random whether to keep their choice
    '''
    iteration_steps = int(iterations/1000)
    results = {
        'same_door':  np.zeros(iteration_steps+1),
        'different_door': np.zeros(iteration_steps+1),
        'random_door': np.zeros(iteration_steps+1)
    }

    iteration_step_number = 1000
    for list_iteration in range(iteration_steps):
        list_iteration += 1 #to make iteration one based
        print(f'iterations: {list_iteration}/{iteration_steps} (in thousands)')

        for _ in range(repetitions):
            results['same_door'][list_iteration] += simulate_monty_hall_iteration(iteration_step_number, 'same_door') 
            results['different_door'][list_iteration] += simulate_monty_hall_iteration(iteration_step_number, 'different_door')
            results['random_door'][list_iteration] += simulate_monty_hall_iteration(iteration_step_number, 'random_door')

        results['same_door'][list_iteration] = results['same_door'][list_iteration]/repetitions
        results['different_door'][list_iteration] = results['different_door'][list_iteration]/repetitions
        results['random_door'][list_iteration] = results['random_door'][list_iteration]/repetitions


    return results

if __name__ == "__main__": 
    """ 
    The program based on American television show 'Let's Make a Deal'.
    Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats.
    You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat.
    He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice? 
    """

    # To Run program: py main.py 'number of iterations (in thousands)' 'number of experiment repetition for each thousand' 
    # Program Output: Plots demonstrating the probabilities of winning after changing chosen door and not changing the door.

    arg_num = len(sys.argv)
    print(f'The number of arguments: {arg_num}')

    if arg_num < 3:
        exit('Not enough arguments')

    if arg_num > 3:
        print('Only the two first user input argument is used')

    first_argument, second_argument = (float(sys.argv[1]),float(sys.argv[2]))

    if first_argument < 1000 or not first_argument%1000 == 0:
        exit('Number of iterations must be bigger than 1000 and divisible by 1000 ')

    if second_argument < 1 and not second_argument.is_integer():
        exit('Number of experiment repetitions must be the integer bigger than 1')

    results = simulate_monty_hall(int(first_argument), int(second_argument))
    
    plt.plot_all_numbers(results, int(first_argument), int(second_argument))
    plt.plot_all_probability_percents(results, int(first_argument), int(second_argument))