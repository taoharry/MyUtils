#!usr/bin/env python
# coding:utf-8


import sys
reload(sys)
sys.setdefaultencoding('utf8')


def Read_csv_file(filename, splitLine=',', flag=True, resaultKey=0):
    """

    :param filename:  文件名
    :param flag:       第一行是否为标题
    :param splitLine:  表格分割
    :param resaultKey:  表格中第几行为唯一索引
    :return:  标题(str),值(dict)
    """
    titile,resault = [],{}

    with open(filename,'r') as f:
        lines = f.readlines()
        for i,line in enumerate(lines):
            line = line.split(splitLine)
            if len(line) == 0:
                continue
            if flag:
                if i == 0:
                    titile = line
                    continue
            if line[resaultKey] == '' or line[resaultKey] == None or resaultKey == 0:
                resault[i] = line
            else:
                line[resaultKey] = line[resaultKey].strip().strip('\n')
                resault[line[resaultKey]] = line

    return titile,resault

def Read_csv_dt(filename, splitLine=','):
    resault = {}
    with open(filename,'r') as f:
        lines = f.readlines()
        for i,line in enumerate(lines):
            line = line.split(splitLine)
            if i == 0:
                continue
            resault[line[-1]] = line
    return resault


def Write_csv_file(filename='resault.csv', title=[], resault={}, splitLine=','):
    """

    :param filename:  需要保存文件名
    :param title:     标题列表
    :param resault:   字典不关注key值,v值放入文件,v内值必须是字符串
    :param splitLine: csv文件分割符
    :return:
    """
    f = open(filename,'w')
    print 'Start write file {}'.format(filename)
    splite = '{}'.format(splitLine)
    if len(title) != 0:
        f.write(splite.join(title) + "\n")
    for k,v in resault.items():
        f.write(splite.join(v) + '\n')
    f.close()
    print 'Sucess write file {}'.format(filename)


if __name__ == "__main__":
    file = "/home/libing/桌面/short_urls.csv"
    k = {'1':['w','q',1]}
    print Read_csv_file(file,',',True,-1)
    #write_csv_file(filename='test.csv',resault=k)
