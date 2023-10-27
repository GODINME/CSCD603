# Rod Cutting Buttom-Up or Memoization Solution
# Running Time: T(n) = O(n) ** 2 - Quadratic RunTime

from math import inf 

def cut_rod(p, n):
    """
    Let p bet the profit of each rod at length i
    Let n be the size of the rod from i .. n
    Let q be the maximum profit for the length n
    Let r be a list of substructure optimal revenue
    """
    r = [None] * (n+1)
    r[0] = 0
    

    for j in range(1, n+1):
        q = -inf
        for i in range(j):
            q = max(q, p[i] + r[j-i-1])
        r[j] = q

    return r[n]


# Example 1
rod_length = [1, 2, 3, 4]
rod_profit = [1, 5, 8, 9]

print("Maximum profit in Example 1 is ", cut_rod(rod_profit, len(rod_profit)))

