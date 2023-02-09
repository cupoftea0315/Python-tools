# coding: utf-8
"""This python project is designed to change the characteristics of some specific words in a word file"""

import os
import docx
from docx.shared import RGBColor, Pt
from docx.enum.text import WD_COLOR_INDEX

os.chdir('D:/Python_test_folder')
doc = docx.Document('D:/Python_test_folder/[IELTS]《雅思词汇真经》总结.docx')


def change(r):
    # r.font.bold = True
    r.font.color.rgb = RGBColor(255, 51, 153)
    # r.font.highlight_color = WD_COLOR_INDEX.YELLOW
    r.font.size = Pt(10.5)
    r.font.name = u"Times New Roman"


for paragraph in doc.paragraphs:  # Temporarily serving for '[IELTS]《雅思词汇真经》总结.docx'
    for run in paragraph.runs:
        # print(run.text)
        if run.text == ')':
            change(run)
        elif run.text == '(':
            change(run)
        elif run.text == '(n)':
            change(run)
        elif run.text == '(adj)':
            change(run)
        elif run.text == '(v)':
            change(run)
        elif run.text == '(adv)':
            change(run)
        elif run.text == 'n)':
            change(run)
        elif run.text == 'adj)':
            change(run)
        elif run.text == 'v)':
            change(run)
        elif run.text == 'adv)':
            change(run)
        elif run.text == 'v)(n)':
            change(run)
        elif run.text == 'n)(v)':
            change(run)
        elif run.text == 'v)(adj)':
            change(run)
        elif run.text == 'adj)(v)':
            change(run)
        elif run.text == 'adj)(n)':
            change(run)
        elif run.text == 'n)(adj)':
            change(run)
        elif run.text == 'v)(adv)':
            change(run)
        elif run.text == 'adv)(v)':
            change(run)
        elif run.text == 'adv)(n)':
            change(run)
        elif run.text == 'n)(adv)':
            change(run)
        elif run.text == 'adj)(adv)':
            change(run)
        elif run.text == 'adv)(adj)':
            change(run)
        elif run.text == 'n':
            change(run)
        elif run.text == 'adj':
            change(run)
        elif run.text == 'v':
            change(run)
        elif run.text == 'adv':
            change(run)

if __name__ == '__main__':
    doc.save('[IELTS]《雅思词汇真经》总结(new).docx')
