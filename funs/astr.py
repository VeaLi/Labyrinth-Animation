from funs.backtrackpath import backtrackpath
from funs.print_lab import print_lab
from funs.breadth_ import labyrinth_breadth
import numpy as np




def labyrinth_astr(x,y,lab,labcopy,LAB):

    #precomputed exact distances
    WAVE,path = labyrinth_breadth(x,y,labcopy,labcopy)
    #print_lab(WAVE)
    print('PRECOMPUTED EXACT DISTANCES ABOVE')
    #M = lambda x,y: sum(np.abs(np.array(x) - np.array(y)))
    def M(x,y):
        S=0
        S2 = 0
        S = np.abs((y[0]-x[0]))
        S2 = np.abs((y[1]-x[1])) 
        return (S+S2)
    x-=1;y-=1
    W,H = len(lab[0]),len(lab)

    
    #4production rules
    RX = [-1,0,1,0]
    RY = [0,1,0,-1]

    Xs,Ys = x,y

    STOP = [True]
    nodes = []
    wave=3
    LAB[Ys][Xs] = 2

    #exit coordinates
    EX = [np.array(lab).shape[1],np.array(lab).shape[0]]
    print('x','y',EX)
    lab[Ys][Xs] = WAVE[Ys][Xs]
    
    values2 = []
    nodes2 = []
    WW = None
    
    
    for k in range(4):
        Xs,Ys = Xs+RX[k],Ys+RY[k]
        if (lab[Ys][Xs]==0):
            lab[Ys][Xs]= WAVE[Ys][Xs] + M(EX,[Xs,Ys])
            LAB[Ys][Xs] = len(nodes2)
            values2.append(WAVE[Ys][Xs] + M(EX,[Ys,Xs]))
            nodes2.append([Xs,Ys])    
        Xs,Ys = Xs-RX[k],Ys-RY[k]

    ANS = []
  
    for wave in range(4,len(lab)**3):
        nodes = []
        if (STOP[0]):
            try:
                SMALLEST = min(values2)
            except:
                pass
            for node in nodes2[:]:
                if lab[node[1]][node[0]] == SMALLEST:
                    #print('node ',node)
                    for k in range(4):
                        Xs,Ys = node[0],node[1]
                        if (Xs==0) or (Ys==0) or (Xs==W-1) or (Ys==H-1):
                            if (STOP[0]):
                                WW = LAB[Ys][Xs] 
                                ANS.append([Xs,Ys])
                                print('Terminal 1')
                                STOP[0] = False
                                break
                                
                                        
                        else:
                            #step
                            Xs,Ys = Xs+RX[k],Ys+RY[k]
                            if (lab[Ys][Xs]==0):
                                if (STOP[0] and ~((Xs==0) or (Ys==0) or (Xs==W-1) or (Ys==H-1))):
                                    lab[Ys][Xs] = WAVE[Ys][Xs] + M(EX,[Xs,Ys])
                                    LAB[Ys][Xs] = wave#len(nodes2)
                                    nodes.append(1)
                                elif (Xs==0) or (Ys==0) or (Xs==W-1) or (Ys==H-1):
                                    if (STOP[0]):
                                        WW = LAB[Ys][Xs]
                                        ANS.append([Xs,Ys])
                                        print('Terminal 2')
                                        STOP[0] = False
                                        break
                                        
                                values2.append(WAVE[Ys][Xs] + M(EX,[Xs,Ys]))        
                                nodes2.append([Xs,Ys])
                            

        # if not fertile&&
        if len(nodes)==0:
            try:
                for v in range(len(values2)):
                    if values2[v]==SMALLEST:
                        values2[v] = float('inf')
                        #break
            except:
                pass
        elif len(set(values2))==1:
            STOP[0]=False
                        

                        
                    
    print(WW)
    if len(ANS)>0:
        #print(ANS)
        #path = backtrackpath(x=ANS[0][0],y=ANS[0][1],lab = LAB,labcopy = labcopy)
        pass
    else:
        print('No path exists')

    return (LAB,WW)

