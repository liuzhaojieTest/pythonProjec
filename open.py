num = 100


def main():
    open_path = "D:\\Test\\"
    count = 0
    for i in range(num):
        full_path = open_path + "blush_" + str(count) + '.txt'
        fail = open(full_path, 'w')
        fail.write('Hello python!')
        count += 1


if __name__ == '__main__':
    main()
