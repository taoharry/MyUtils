#!usr/bin/env python
# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
import xlrd
import xlwt

def Read_exal(filename,index=0,tablename='',flag=True,resaultKey=0):
    """

    :param filename:  文件名
    :param index:     表格索引
    :param tablename:  表格名
    :param flag:       第一行是否为标题
    :param resaultKey:  表格中第几行为唯一索引
    :return:  标题(str),值(dict)
    """

    title,resault = [],{}
    data = xlrd.open_workbook(filename)
    if tablename != '':
        table = data.sheet_by_name(tablename)
    else:
        table = data.sheets()[index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    for i in range(nrows):
        if flag:
            if i == 0:
                title = table.row_values(i)
                continue
        if resaultKey ==0:
            resault[i] = table.row_values(i)
        else:
            resault[table.row_values(i)[resaultKey]] = table.row_values(i)

    return title,resault


def Write_exal(filename,title,content,encode='utf8',*arg,**kwargs):
    """
    :param filename: 创建文件名,字符串
    :param title:  标题名字,列表
    :param content: 内容,字典 {key:[]}
    :param encode: 编码格式
    :return: None
    """
    newf = os.path.join(filename)
    workbook = xlwt.Workbook(encode)
    worksheet = workbook.add_sheet(filename)
    for i,name in enumerate(title):
        worksheet.write(0, i, label=name)
    lineCount = len(title)
    i =0
    for k in content:
        i +=1
        for line in range(lineCount):
            worksheet.write(i, line, label=content[k][line])

    workbook.save('%s.xls'%newf)

if __name__ == "__main__":
    file = '/home/libing/文档/提出需求_未做/晋江小说网.xlsx'
    lt,dt = Read_exal(file)
    Write_exal('test.xlsx',lt,dt)

