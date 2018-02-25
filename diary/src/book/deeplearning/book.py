#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/02/24 13:31
# @Author  : niuliangtao
# @Site    : 
# @File    : book.py
# @Software: PyCharm


import os

from pyPdf import PdfFileWriter, PdfFileReader


def create_new_books(pdf_file, stPage, endPage, filename='my2.pdf', output_dir='D:/pdf'):
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    input_stream = file(pdf_file, 'rb')

    pdf_input = PdfFileReader(input_stream)

    pdf_output = PdfFileWriter()

    i = stPage

    while i < endPage:
        page = pdf_input.getPage(i)  # 选取需要页面，需要注意的是第一页的编号是0
        pdf_output.addPage(page)  # 将选好的页面加入到新的pdf中

        i += 1

    outputfilename = output_dir + '/' + filename

    output_stream = file(outputfilename, 'wb')

    pdf_output.write(output_stream)

    output_stream.close()

    input_stream.close()

    return True


def run():
    root = "/Users/weidian/Documents/Dairy/"
    pdf_path = root + "assets/pdfs/deeplearning/dlbook_cn_v0.5-beta.pdf"
    output_dir = root + "assets/pdfs/deeplearning/"
    filename = "1.pdf"
    chapters = (('目录', 3, 15), ('chapter1', 29, 54), ('chapter2', 55, 74), ('chapter3', 75, 99),
                ('chapter4', 100, 114), ('chapter5', 115, 170), ('chapter6', 173, 224),
                ('chapter7', 225, 262), ('chapter8', 263, 308), ('chapter9', 309, 346),
                ('chapter10', 347, 386), ('chapter11', 387, 404), ('chapter12', 404, 444),
                ('chapter13', 445, 456), ('chapter14', 457, 476), ('chapter15', 477, 502),
                ('chapter16', 503, 529), ('chapter17', 530, 543), ('chapter18', 544, 565),
                ('chapter19', 566, 586), ('chapter20', 587, 642), ('参考文献', 643, 738))

    for chapter in chapters:
        print chapter
        filename = "dlbook_cn_" + chapter[0] + ".pdf"
        stPage = chapter[1] - 1
        endPage = chapter[2] - 1
        create_new_books(pdf_path, stPage=stPage, endPage=endPage, filename=filename, output_dir=output_dir)


if __name__ == '__main__':
    run()
