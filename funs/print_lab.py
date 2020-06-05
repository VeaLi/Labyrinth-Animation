def print_lab(lab):
    s = len(str(len(lab)))+1
    print(' '*s, 'Y')
    print(' '*s, '^')
    print(' '*s, '|')

    for line, k in zip(lab, range(1, len(lab)+1)):
        lineS = [str(x) for x in line]
        s = len(str(len(lab)))-len(str(k))
        for j in range(len(line)):
            if len(str(lineS[j])) >= 2:
                pass
            else:
                lineS[j] = str(lineS[j])+' '
        lineS = str(lineS).replace(',', '').replace("'", ' ').replace(
            '[', '').replace(']', '').replace(' 1 ', chr(9608)+chr(9608)+chr(9608))  # 12/8
        print(' '*s, k, '|', lineS)

    ST = str(k)+' '*s+'|'+str(line)
    s = list(ST).index('[')
    print(' '*s, '-----'*(len(line)+2), '> X')
    print('\n\n')
