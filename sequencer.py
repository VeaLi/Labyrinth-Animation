# -*- coding: utf-8 -*-
"""
Created on ~

@author: VinLes
"""

from funs.read_lab import read_lab
from funs.breadth import labyrinth_breadth
from funs.astr import labyrinth_astr
import matplotlib.pyplot as plt
import time
import numpy as np
import os
from PIL import Image
# import scipy.misc  #-not woking in python 3.6>
from toimage import *
import gc
gc.enable()

# bread stand for breadth


def seq_it(mode='RGB', name='20x15.txt', alg='breadth'):
    '''
    this function works as follows:
    it crates cells with color choses then it concatenates cells into stripes,and finally in concatenates stripes into images
    row by row. For rgb it for every image in the sequence it goes 3 times for 3 channels. That is why, there are so many loops int there!

    Do not use pyplot functionality in here to save the pictures, it slows down enormously.  That's why it's commented

    Args:
        mode (str): RGB or Simple. It's better to use RGB. And it works ok. 3 channels, deeper resolution for cells
        name (str): name of file with a labyrinth
        alg (str): options {breadth, astr}
    '''

    print('Calculating ...')
    lab = read_lab(name)
    lab1 = read_lab(name)
    lab2 = read_lab(name)
    lab3 = read_lab(name)
    path = [0, 0]

    X, Y = 8, 8
    if alg == 'breadth':
        lab, path = labyrinth_breadth(x=X+1, y=Y+1, lab=lab, labcopy=lab1)
    elif alg == 'astr':
        lab, WAVE = labyrinth_astr(
            x=X+1, y=Y+1, lab=lab, labcopy=lab3, LAB=lab2)

    print('Prepareing aninmation ...')

    if mode == 'RGB':
        NW = None
        print('Animating in RGB mode, it may take time. For larger data please consider to use SIMPLE mode:).\n\n ***')

        if alg == 'breadth':
            # Names of waves up to exit
            NW = list(range(2, len(path)+2))
        elif alg == 'astr':
            NW = list(range(2, WAVE))

        t = [0.01 for _ in range(10)]
        tz = [t for _ in range(10)]

        WALL = np.array(tz)

        # empty cell custom field
        EC = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0.98, 0.98, 0.98, 0.98, 0.98, 0.98, 0, 0],
                       [0, 0.98, 0.98, 0.98, 0.98, 0.98, 0.98, 0.98, 0.98, 0],
                       [0, 0.98, 0.98, 0.98, 0.98, 0.98, 0.98, 0.98, 0.98, 0],
                       [0, 0.98, 0.98, 0.98, 0.98, 0.98, 0.98, 0.98, 0.98, 0],
                       [0, 0.98, 0.98, 0.98, 0.98, 0.98, 0.98, 0.98, 0.98, 0],
                       [0, 0.98, 0.98, 0.98, 0.98, 0.98, 0.98, 0.98, 0.98, 0],
                       [0, 0.98, 0.98, 0.98, 0.98, 0.98, 0.98, 0.98, 0.98, 0],
                       [0, 0, 0.98, 0.98, 0.98, 0.98, 0.98, 0.98, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

        # dictionary of colors
        DC, DC1, DC2 = {}, {}, {}

        def seq(lab, tocolor):
            IMG = []
            wall = 1
            for row in lab:
                tmp = []
                for item in row:
                    if item in tocolor:
                        tmp.append(DC[item])
                    elif (item == wall):
                        tmp.append(WALL)
                    else:
                        tmp.append(EC)
                IMG.append(tmp)

            IMG1 = []
            wall = 1
            for row in lab:
                tmp = []
                for item in row:
                    if item in tocolor:
                        tmp.append(DC1[item])
                    elif (item == wall):
                        tmp.append(WALL)
                    else:
                        tmp.append(EC)
                IMG1.append(tmp)

            IMG2 = []
            wall = 1
            for row in lab:
                tmp = []
                for item in row:
                    if item in tocolor:
                        tmp.append(DC2[item])
                    elif (item == wall):
                        tmp.append(WALL)
                    else:
                        tmp.append(EC)
                IMG2.append(tmp)

            return IMG, IMG1, IMG2

        IMAGES, IMAGES1, IMAGES2 = [], [], []
        tocolor = []

        for color in NW:
            if color != 1:
                tocolor.append(color)
                DC[color] = (np.where(EC == 0.98, np.random.random(), EC))
                DC1[color] = (np.where(EC == 0.98, np.random.random(), EC))
                DC2[color] = (np.where(EC == 0.98, np.random.random(), EC))

                IMG, IMG1, IMG2 = seq(lab, tocolor)
                IMAGES.append(IMG)
                IMAGES1.append(IMG1)
                IMAGES2.append(IMG2)

        ####part 2 #####

        I2, I3, I4 = [], [], []

        for IMG in IMAGES:
            STRIPES = []
            for row in IMG:
                STRIPE = []
                for item in row:
                    # print(item.shape)
                    try:
                        STRIPE[0] = np.hstack((STRIPE[0], item))
                    except:
                        STRIPE = [item]
                STRIPES.append(STRIPE[0])

            IMG2 = []
            for S in STRIPES:
                try:
                    IMG2[0] = np.vstack((IMG2[0], S))
                except Exception as e:
                    IMG2 = [S]
            I2.append(IMG2)

        for IMG in IMAGES1:

            STRIPES = []
            for row in IMG:
                STRIPE = []
                for item in row:
                    try:
                        STRIPE[0] = np.hstack((STRIPE[0], item))
                    except:
                        STRIPE = [item]
                STRIPES.append(STRIPE[0])

            IMG3 = []
            for S in STRIPES:
                try:
                    IMG3[0] = np.vstack((IMG3[0], S))
                except Exception as e:
                    IMG3 = [S]
            I3.append(IMG3)

        for IMG in IMAGES2:

            STRIPES = []
            for row in IMG:
                STRIPE = []
                for item in row:
                    try:
                        STRIPE[0] = np.hstack((STRIPE[0], item))
                    except:
                        STRIPE = [item]
                STRIPES.append(STRIPE[0])

            IMG4 = []
            for S in STRIPES:
                try:
                    IMG4[0] = np.vstack((IMG4[0], S))
                except Exception as e:
                    IMG4 = [S]
            I4.append(IMG4)

        #### part 3 ####
        try:
            os.makedirs('ANIM')
        except:
            pass

        K = list(range(len(I2)))
        for IMG2, IMG3, IMG4, k in zip(I2, I3, I4, K):
            print('done ', k, 'of ', len(path), flush=True, end='\r')
            IMG2[0] = np.stack((IMG2[0], IMG3[0], IMG4[0]), axis=2)
            toimage(IMG2[0], cmin=0.0, cmax=1.0).save('ANIM/{}.png'.format(k))

    elif mode == 'SIMPLE':
        print('Animating in SIMPLE mode, it may also take time. For larger data please consider to use ANOTHER APP:)).\n\n ***')

        NW = None
        if alg == 'bread':
            # Names of waves up to exit
            NW = list(range(2, len(path)+2))
        elif alg == 'astr':
            NW = list(range(2, np.max((np.unique(lab)))))

        t = [0.01 for _ in range(2)]
        tz = [t for _ in range(2)]

        WALL = np.array(tz)
        WALL = np.array([[0.01]])

        # empty cell
        EC = np.array([[0.98]])

        # dictionary of colors
        DC, DC1, DC2 = {}, {}, {}

        def seq(lab, tocolor):
            IMG = []
            wall = 1
            for row in lab:
                tmp = []
                for item in row:
                    if item in tocolor:
                        tmp.append(DC[item])
                    elif (item == wall):
                        tmp.append(WALL)
                    else:
                        tmp.append(EC)
                IMG.append(tmp)

            IMG1 = []
            wall = 1
            for row in lab:
                tmp = []
                for item in row:
                    if item in tocolor:
                        tmp.append(DC1[item])
                    elif (item == wall):
                        tmp.append(WALL)
                    else:
                        tmp.append(EC)
                IMG1.append(tmp)

            IMG2 = []
            wall = 1
            for row in lab:
                tmp = []
                for item in row:
                    if item in tocolor:
                        tmp.append(DC2[item])
                    elif (item == wall):
                        tmp.append(WALL)
                    else:
                        tmp.append(EC)
                IMG2.append(tmp)

            return IMG, IMG1, IMG2

        IMAGES, IMAGES1, IMAGES2 = [], [], []
        tocolor = []

        for color in NW:
            if color != 1:
                tocolor.append(color)
                DC[color] = (np.where(EC == 0.98, np.random.random(), EC))
                DC1[color] = (np.where(EC == 0.98, np.random.random(), EC))
                DC2[color] = (np.where(EC == 0.98, np.random.random(), EC))

                IMG, IMG1, IMG2 = seq(lab, tocolor)
                IMAGES.append(IMG)
                IMAGES1.append(IMG1)
                IMAGES2.append(IMG2)

        ####part 2 #####

        I2, I3, I4 = [], [], []

        for IMG in IMAGES:
            STRIPES = []
            for row in IMG:
                STRIPE = []
                for item in row:
                    # print(item.shape)
                    try:
                        STRIPE[0] = np.hstack((STRIPE[0], item))
                    except:
                        STRIPE = [item]
                STRIPES.append(STRIPE[0])

            IMG2 = []
            for S in STRIPES:
                try:
                    IMG2[0] = np.vstack((IMG2[0], S))
                except Exception as e:
                    IMG2 = [S]
            I2.append(IMG2)

        for IMG in IMAGES1:

            STRIPES = []
            for row in IMG:
                STRIPE = []
                for item in row:
                    try:
                        STRIPE[0] = np.hstack((STRIPE[0], item))
                    except:
                        STRIPE = [item]
                STRIPES.append(STRIPE[0])

            IMG3 = []
            for S in STRIPES:
                try:
                    IMG3[0] = np.vstack((IMG3[0], S))
                except Exception as e:
                    IMG3 = [S]
            I3.append(IMG3)

        for IMG in IMAGES2:

            STRIPES = []
            for row in IMG:
                STRIPE = []
                for item in row:
                    try:
                        STRIPE[0] = np.hstack((STRIPE[0], item))
                    except:
                        STRIPE = [item]
                STRIPES.append(STRIPE[0])

            IMG4 = []
            for S in STRIPES:
                try:
                    IMG4[0] = np.vstack((IMG4[0], S))
                except Exception as e:
                    IMG4 = [S]
            I4.append(IMG4)

        #### part 3 ####
        try:
            os.makedirs('ANIM')
        except:
            pass

        K = list(range(len(I2)))
        for IMG2, IMG3, IMG4, k in zip(I2, I3, I4, K):
            print('done ', k, 'of ', len(path), flush=True, end='\r')
            IMG2[0] = np.stack((IMG2[0], IMG3[0], IMG4[0]), axis=2)

            toimage(IMG2[0], cmin=0.0, cmax=1.0).save('ANIM/{}.png'.format(k))
