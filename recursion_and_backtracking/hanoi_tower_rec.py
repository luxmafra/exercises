def hanoi(n, orig='A', helper='B', dest='C'):
    if n >= 1:
        hanoi(n - 1, orig, dest, helper)
        print('{} -> {} : {}'.format(orig, dest, n))
        hanoi(n - 1, helper, orig, dest)


for i in range(1, 4):
    print('####### Hanoi %s' % i)
    hanoi(i)
