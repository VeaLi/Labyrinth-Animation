from funs.backtrackpath import backtrackpath
from funs.print_lab import print_lab


def labyrinth_breadth(x, y, lab, labcopy):
    x -= 1
    y -= 1
    W, H = len(lab[0]), len(lab)

    # 4production rules
    RX = [-1, 0, 1, 0]
    RY = [0, 1, 0, -1]

    Xs, Ys = x, y

    STOP = True
    nodes = []
    wave = 3
    # print('WAVE',wave)
    lab[Ys][Xs] = 2
    for k in range(4):
        Xs, Ys = Xs+RX[k], Ys+RY[k]
        if (lab[Ys][Xs] == 0):
            lab[Ys][Xs] = wave
            nodes.append([Xs, Ys])
        Xs, Ys = Xs-RX[k], Ys-RY[k]

    ANS = []
    for wave in range(4, len(lab)*len(lab)):
        nodes2 = []
        if (STOP):
            # print('WAVE',wave)
            for node in nodes:
                for k in range(4):
                    Xs, Ys = node[0], node[1]
                    if (Xs == 0) or (Ys == 0) or (Xs == W-1) or (Ys == H-1):
                        if (STOP):
                            ANS.append([Xs, Ys])
                            print('Terminal')
                            STOP = False

                    else:
                        # step
                        Xs, Ys = Xs+RX[k], Ys+RY[k]
                        if (lab[Ys][Xs] == 0):
                            if (STOP):
                                lab[Ys][Xs] = wave
                            if (Xs == 0) or (Ys == 0) or (Xs == W-1) or (Ys == H-1):
                                if (STOP):
                                    ANS.append([Xs, Ys])
                                    print('Terminal')
                                    STOP = False
                            nodes2.append([Xs, Ys])

        nodes = []
        nodes = [n for n in nodes2]

    print_lab(lab)
    if len(ANS) > 0:
        # print(ANS)
        path = backtrackpath(x=ANS[0][0], y=ANS[0][1],
                             lab=lab, labcopy=labcopy)
    else:
        print('No path exists')

    return (lab, path)
