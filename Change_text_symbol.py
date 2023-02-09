# coding: utf-8
"""author: scort"""

# mine
old_str = '[a;b;c]'
new_str = ''
for i in range(len(old_str)):
    if old_str[i] == ';':
        new_str = new_str + ','
    else:
        new_str = new_str + old_str[i]
print(new_str)

# python's + update for informal text
old_str = (
    '1) Gradation\n'
    'first,firstly, to begin with, to start with, in the first place\n'
    'second,secondly, further , still, furthermore\n'
    'third,thirdly, what is more, last, last but not least\n'
    'also, and then, next, besides ,moreover ,besides ,in addtion ,finally\n'
    '2) Transition\n'
    'by contrast, although, though ,yet\n'
    'at the same time ,but, despite the fact that, even so\n'
    'in contrast, nevertheless ,even though ,for all that ,on the contarary, however, in spite of\n'
    'on the other hand ,otherwise ,instead ,still ,regardless of\n'
    '3) Cause and effect\n'
    'therefore ,consequently ,because of ,for the reason ,thus ,hence ,due to ,owing to thanks to ,on\n'
    'this account , in this way ,for ,as a result, as a consequence\n'
    '4) Concession\n'
    'still, nevertheless, ,in spite of ,all the same, of course ,despite ,even so ,after all\n'
    '5) Progressive\n'
    'Furthermore, moreover ,likewise ,what is more ,besides ,also ,not only...but also... , in addtion\n'
    '6) Illustrate\n'
    'Take …for example, for instance ,for one thing ,that is ,to illustrate, as an illustration\n'
    'In some/most cases,…\n'
    '7) Refers\n'
    '…and stuff like that,…and something like that,…or whatever\n'
    '8) Explain\n'
    'as a matter of fact； frankly speaking ；in this case namely ;in other words\n'
    '9) Conclusion\n'
    'in summary；to summarize； in a word ；thus ；as has been said in brief； in conclusion；to conclude ；in fact ；finally ；in simpler terms ；indeed ；in short； in particular, that is in other words； on the whole ；to put it'
)
temp_str = old_str.replace(';', ',').replace('，', ',').replace('；', ',').replace('.', ',').replace('…', '...')
new_str = ''
for i in range(len(temp_str)):
    if temp_str[i] == ',' and temp_str[i + 1] != ' ':
        new_str = new_str + ',' + ' '
    else:
        new_str = new_str + temp_str[i]
print(new_str)
