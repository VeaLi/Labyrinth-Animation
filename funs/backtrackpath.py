from funs.print_lab import print_lab


def backtrackpath(x, y, lab, labcopy):
    # 4production rules
    RX = [-1, 0, 1, 0]
    RY = [0, 1, 0, -1]

    path = [[x, y]]
    L = lab[y][x]
    labcopy[y][x] = L

    for cell in range(L-1, 1, -1):
        for k in range(4):
            try:
                Xs, Ys = path[-1][0], path[-1][1]
                Xs, Ys = Xs+RX[k], Ys+RY[k]
                if lab[Ys][Xs] == cell:
                    path.append([Xs, Ys])
                    labcopy[Ys][Xs] = cell
            except Exception as e:
                pass
    return path
