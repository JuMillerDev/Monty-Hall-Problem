import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def plot_all_probability_percents(results: dict, iterations: int, repetitions: int):
    plt.title(f'Monty Hall Problem guessed door probability (%) for different scenarios ({repetitions} repetititons)')
    x = [i for i in range(0, iterations+1, 1000)]
    plt.plot(x, results['same_door']/10)
    plt.plot(x, results['different_door']/10)
    plt.plot(x, results['random_door']/10)
    plt.legend(['Same door', 'Different door', 'Random not revealed door'])
    plt.ylim(0,100)
    plt.gca().yaxis.set_major_locator(MultipleLocator(5))
    plt.show()

def plot_all_numbers(results: dict, iterations: int, repetitions: int):
    plt.title(f'Monty Hall Problem guessed doors for different scenarios ({repetitions} repetititons)')
    x = [i for i in range(0, iterations+1, 1000)]
    plt.plot(x, results['same_door'])
    plt.plot(x, results['different_door'])
    plt.plot(x, results['random_door'])
    plt.legend(['Same door', 'Different door', 'Random not revealed door'])
    plt.ylim(0,1000)
    plt.gca().yaxis.set_major_locator(MultipleLocator(50))
    plt.show()