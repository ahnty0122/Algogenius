import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
# ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기
# ['AB', 'AC', 'BA', 'BC', 'CA', 'CB']

from itertools import combinations
a = [1,2,3]
combi = combinations(a, 2)
# ['AB', 'AC', 'BA', 'BC', 'CA', 'CB']
    
print(list(combi))