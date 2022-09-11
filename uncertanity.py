# Uncertain decision

import json


def wald_crit(dec_matrix):
    num_of_strategies = len(dec_matrix)
    worst_payoff = [0 for col in range(num_of_strategies)]
    # Find the worst payoff for each strategy
    for strategy in range(num_of_strategies):
        worst_payoff[strategy] = min(dec_matrix[strategy])
    # Find maximum payoff in set of minimals
    max_payoff = max(worst_payoff)
    best_strategy = worst_payoff.index(max_payoff)
    return best_strategy


def max_max_crit(dec_matrix):
    num_of_strategies = len(dec_matrix)
    best_payoff = [0 for col in range(num_of_strategies)]
    # Find the best payoff for each strategy
    for strategy in range(num_of_strategies):
        best_payoff[strategy] = max(dec_matrix[strategy])
    # Find maximum payoff in set of minimals
    max_payoff = max(best_payoff)
    best_strategy = best_payoff.index(max_payoff)
    return best_strategy


def hurwicz_crit(dec_matrix, alpha):
    num_of_strategies = len(dec_matrix)
    balanced_payoff = [0 for col in range(num_of_strategies)]
    # Find the balanced payoff for each strategy
    for strategy in range(num_of_strategies):
        balanced_payoff[strategy] = (alpha * min(dec_matrix[strategy]) +
                                     (1 - alpha) * max(dec_matrix[strategy]))
    # Find maximum payoff in set of minimals
    max_payoff = max(balanced_payoff)
    best_strategy = balanced_payoff.index(max_payoff)
    return best_strategy


def laplace_crit(dec_matrix):
    num_of_strategies = len(dec_matrix)
    num_of_reactions = len(dec_matrix[0])
    average_payoff = [0 for col in range(num_of_strategies)]
    # Find the average payoff for each strategy
    for strategy in range(num_of_strategies):
        average_payoff[strategy] = sum(dec_matrix[strategy]) / num_of_reactions
    # Find maximum payoff in set of minimals
    max_payoff = max(average_payoff)
    best_strategy = average_payoff.index(max_payoff)
    return best_strategy


def savage_crit(dec_matrix):
    num_of_strategies = len(dec_matrix)
    num_of_reactions = len(dec_matrix[0])
    lost_payoff = [0 for col in range(num_of_strategies)]
    delta_matrix = [[0 for col in range(num_of_reactions)] for row in range(num_of_strategies)]
    # Calculate the matrix of deltas
    for strategy in range(num_of_strategies):
        max_payoff = max(dec_matrix[strategy])
        for reaction in range(num_of_reactions):
            delta_matrix[strategy][reaction] = max_payoff - dec_matrix[strategy][reaction]
        lost_payoff[strategy] = max(dec_matrix[strategy])
    # Find minimal lost payoff
    min_payoff = min(lost_payoff)
    best_strategy = lost_payoff.index(min_payoff)
    return best_strategy


# ---------------------------------------------------------------------------------------
variant = 'var1'
with open('tasks_2.json', 'r') as f:
    data = json.load(f)
decision_matrix = data[variant]

print(variant)
for i in range(len(decision_matrix)):
    print(decision_matrix[i])

best_str = wald_crit(decision_matrix)
print(f'Best strategy on Wald is {best_str + 1:2d}')

best_str = max_max_crit(decision_matrix)
print(f'Best strategy on max-max is {best_str + 1:2d}')

best_str = hurwicz_crit(decision_matrix, 0.3)
print(f'Best strategy on Hurwicz is {best_str + 1:2d}')

best_str = laplace_crit(decision_matrix)
print(f'Best strategy on Laplace is {best_str + 1:2d}')

best_str = savage_crit(decision_matrix)
print(f'Best strategy on Savage is {best_str + 1:2d}')
