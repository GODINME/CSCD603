# Rod Cutting Recurive Solution
from math import inf 

def cut_rod(p, n):
    """
    Let p bet the profit of each rod at length i
    Let n be the size of the rod from i .. n
    Let q be the maximum profit for the length n
    """
    if n == 0:
        return 0
    
    q = -inf

    for i in range(1, n):
        q = max(q,  (p[i] + cut_rod(p, n-1-i)))
    
    return q


# Example 1
rod_length = [1, 2, 3, 4]
rod_profit = [1, 5, 8, 9]

print("Maximum profit in Example 1 is ", cut_rod(rod_profit, len(rod_profit)))
