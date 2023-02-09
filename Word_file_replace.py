# coding:utf-8
"""This python project is designed to change specific words in a word file"""
import os
import docx

os.chdir('D:/Python_test_folder')
doc = docx.Document('C:/Users/Scort/PycharmProjects/pythonProject/Some_tools/self_files/[IELTS]《雅思词汇真经》总结.docx')
for paragraph in doc.paragraphs:
    if '(n)' in paragraph.text:
        paragraph.text = paragraph.text.replace('(', '[')
        paragraph.text = paragraph.text.replace(')', ']')
        # paragraph.text = paragraph.text.replace('，', ', ')

if __name__ == '__main__':
    doc.save('[IELTS]《雅思词汇真经》总结(new).docx')
