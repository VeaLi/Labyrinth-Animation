def read_lab(file='20x15.txt'):
    lab = []
    with open(file, 'r') as labfile:
        lab = labfile.readlines()
    lab = [[int(y) for y in list(x.strip())] for x in lab]
    return lab
