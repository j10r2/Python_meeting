# pol1 = open('polinomal_1.md').read()
# list_1 = [[],[]]
# print(list_1)
def polinomal_extraction (pol, list):
    list_count = 0
    while pol[list_count] != ' ':
        num = ''
        key = ''
        while pol[list_count] != 'x' and pol[list_count] != ' ':
            num += pol[list_count]
            list_count += 1
        if pol[list_count] != ' ':
            list_count += 1
        #print(f'num{num} 1 end{list_count}')
        if pol[list_count] != '<' and pol[list_count] != ' ':
            key = 1
            list[0].append(key)
            list[1].append(int(num))
            #list.append([key, num])
            if pol[list_count] != ' ':
                num = ''
                key = 0
                while pol[list_count] != ' ':
                    num += pol[list_count]
                    list_count += 1
                #list.append([key, num])
                list[0].append(key)
                list[1].append(int(num))
            break
        elif pol[list_count] == ' ':
            key = 0
            #list.append([key, num])
            list[0].append(key)
            list[1].append(int(num))
            break
        while pol[list_count] != '>':
            list_count += 1
        list_count += 1
        #print(f' 2 end{list_count}')
        while pol[list_count] != '<':
            key += pol[list_count]
            list_count += 1
        #print(f'key{key} 3 end{list_count}')
        list[0].append(int(key))
        list[1].append(int(num))
        #list.append([key,num])
        while pol[list_count] != '>':
            list_count += 1
        #print(f'4 end{list_count}')
        list_count += 1
# polinomal_extraction(pol1, list_1)
# print(list_1)