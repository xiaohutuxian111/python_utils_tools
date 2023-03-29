"""
@FileName：test.py
@Author：stone
@Time：2023/3/21 17:29
@Description：
"""


def read_file(filename):
    f = open(filename, encoding='utf-8')
    data = f.readlines()
    f.close()
    lis = []
    for line in data:
        lis.append(
            line.replace("\t\t\t\t\t\t\n", "@").replace('\n', "@").replace('\t', "$").replace(" ", "$").split("@")[0])
    print(lis)
    dic = {}
    key_str = ''

    for ele in lis:

        if countNum(ele) < 4:
            lispart = []
            key_str += ele.split('$')[-1]
        else:

            dic_part = {}
            dic_part[ele.split("$")[0]] = ele.split("$")[-1]
            lispart.append(dic_part)
        dic[key_str] = lispart
        key_str = ''

    print(dic)


def countNum(str):
    count = 0
    for e in str:
        if e == "$":
            count += 1
    return count


# 函数调用
data = read_file("./AdministrativeAreaCode.txt")


