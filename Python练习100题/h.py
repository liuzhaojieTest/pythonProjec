def safe():
    for j in range(1, 10):
        for i in range(1, j + 1):
            result = i * j
            print('{}X{}={}'.format(i, j, result), end='\t')
        print()
    return list
