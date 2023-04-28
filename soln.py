import itertools
 
m=int(input())
total_ways = set()
absent_ways = set()
for i in range(1, m+1):
    in_str = 'P'*i + 'A'*(m-i)
    in_lst = list(in_str)
    permutations = list(itertools.permutations(in_lst))
    result = set([''.join(permutation) for permutation in permutations])
    for k in result:
        if 'AAAA' not in k:
            total_ways.add(k)
            if k[-1] == 'A':
                absent_ways.add(k)
print(len(total_ways))
print(len(absent_ways),'/',len(total_ways), sep='')
