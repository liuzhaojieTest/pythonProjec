num = 100


def main():
    desktop_path = "E:\\tests\\"   # 存放路径
    count = 0
    for i in range(num):
        full_path = desktop_path + "blxw_" + str(count) + '.txt'    # 命名方式定义
        file = open(full_path, 'w')     # 以写入的方式打开文件
        file.write("hello python!")     # 写入的内容
        print(full_path)
        count += 1


if __name__ == '__main__':
    main()
