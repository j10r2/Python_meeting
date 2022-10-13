# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
def RLE_archivation(file):
    txt = open(file).read()
    lenth = 0
    wt_txt = ''
    while lenth < len(txt):
        amount = 0
        if lenth == 0 or txt[lenth] != txt[lenth-1]:
            key = txt[lenth]
        while txt[lenth] == key and lenth < len(txt):
            amount +=1
            lenth +=1
            if lenth == len(txt):
                break
        wt_txt += str(amount)+key
    with open('hw5_3.txt', 'w') as text:
        print(f'result is {wt_txt}')
        text.write(f'{wt_txt}')

def unpack(file):
    txt = open(file).read()
    lenth = 0
    wt_txt = ''
    while lenth < len(txt):
        amount = ''
        key = ''
        while txt[lenth].isdigit():
            amount += txt[lenth]
            lenth +=1
        key += txt[lenth]
        wt_txt += int(amount)*key
        lenth +=1
    with open('hw5_3.txt', 'w') as text:
        print(f'result is {wt_txt}')
        text.write(f'{wt_txt}')

RLE_archivation('file.txt')