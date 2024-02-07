from collections import Counter
from random import randint

prob = [1, 2, 3, 4, 5, 6, 5, 4, 3 ,2, 1]
sum = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
analytic = {sum[i]: round(prob[i]/36, 4) for i in range(len(prob))}

def montecarlo_2dice(n):
    from random import randint
    sums = []
    for i in range(n):
        sums += [randint(1, 6) + randint(1, 6)]
    
    counts = dict(Counter(sums))
    probs = {i: round(counts[i] / n, 4) for i in range(2, 13)}

    return probs

if __name__ == '__main__':
    N = 10_000_000
    w = 10
  
    print(f"| {'Method':14} | {' | '.join(f'{i:^6}' for i in sum)} |")
    print(f"|{'-' * 16}|{'--------|'*11}")
    print(f"| {'Analytic':14} | {' | '.join(f'{analytic[i]:^6}' for i in analytic)} |")
    monte_carlo = montecarlo_2dice(N)
    print(f"| {'Monte Carlo':14} | {' | '.join(f'{monte_carlo[i]:^6}' for i in monte_carlo)} |")

