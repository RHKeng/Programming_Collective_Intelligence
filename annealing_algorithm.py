import random

import math


def annealing_algorithm(domain,costf,T=10000.0,cool=0.95,step=1):
    vec_list=[]
    vec_result=[]
    for i in range(10):
        # Initialize the values randomly
        vec = [float(random.randint(domain[i][0], domain[i][1]))
               for i in range(len(domain))]
        vec_list.append(vec)

    for vec in vec_list:
        while T > 0.1:
            # Choose one of the indices
            i = random.randint(0, len(domain) - 1)

            # Choose a direction to change it
            dir = random.randint(-step, step)

            # Create a new list with one of the values changed
            vecb = vec[:]
            vecb[i] += dir
            if vecb[i] < domain[i][0]:
                vecb[i] = domain[i][0]
            elif vecb[i] > domain[i][1]:
                vecb[i] = domain[i][1]

            # Calculate the current cost and the new cost
            ea = costf(vec)
            eb = costf(vecb)
            p = pow(math.e, (-eb - ea) / T)

            # Is it better, or does it make the probability
            # cutoff?
            if (eb < ea or random.random() < p):
                vec = vecb

                # Decrease the temperature
            T = T * cool
        vec_result.append(vec)

    vec_return = [float(random.randint(domain[i][0], domain[i][1]))
           for i in range(len(domain))]

    for Vec in vec_result:
        Vec_cost = costf(Vec)
        vec_return_cost = costf(vec_return)
        if Vec_cost<vec_return_cost:
            vec_return=Vec

    return vec_return,costf(vec_return)