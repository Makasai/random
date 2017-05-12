"""
n: starting number
l: list of optimal steps from that index
    l[0] will be None because you cannot get 1 from 0, according to the possible
         actions
returns tuple (# steps, path)
"""
def stepsTo1(start):
    x = [None]

    for n in range(1,start+1):
        optimalSteps = 0
        steps = 'start '
        if (n-1) != 0:
            optimalSteps = x[n-1][0] + 1
            steps = str(x[n-1][1]) + '-> -1 '
        if (n % 2) == 0:
            if x[n/2][0]+1 < optimalSteps:
                optimalSteps = x[n/2][0] + 1
                steps = str(x[n/2][1]) + '-> /2 '

        if (n % 3) == 0:
            if x[n/3][0]+1 < optimalSteps:
                optimalSteps = x[n/3][0] + 1
                steps = str(x[n/3][1]) + '-> /3 '
        x.append((optimalSteps,steps))

    return x[n]



""" George's code
def steps_to_1(n):
    min_steps_for = [None, 0]
    for i in xrange(2, n + 1):
        # Keep track of the candidates for the optimal "second step".
        min_steps_after_first = min_steps_for[i - 1]
        if i % 2 == 0:
            min_steps_after_first = min(min_steps_after_first, min_steps_for[i / 2])
        if i % 3 == 0:
            min_steps_after_first = min(min_steps_after_first, min_steps_for[i / 3])

        # Find the minimum of these candidates, then count the first step.
        min_steps_for.append(min_steps_after_first + 1)

"""
