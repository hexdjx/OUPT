import cv2 as cv
import os
import numpy as np
from pytracking.evaluation import get_dataset
import matplotlib.pyplot as plt

_tracker_disp_colors = {1: (0, 255, 0), 2: (255, 0, 0), 3: (0, 0, 255),
                        4: (123, 0, 123), 5: (255, 255, 255), 6: (0, 0, 0),
                        7: (123, 123, 123), 8: (199, 18, 237), 9: (255,255,0)}
# _tracker_disp_colors = {1: (0, 255, 0), 2: (255, 0, 0), 3: (0, 0, 255),
#                         4: (255, 255, 255), 5: (0, 0, 0), 6: (255, 128, 0)
#                         }

OUPT = './results/OUPT'
ATOM = './results/ATOM'
DaSiamRPN = './results/DaSiamRPN'
DiMP = './results/DiMP'
ECO = './results/ECO'
KYS = './results/KYS'
PrDiMP = './results/PrDiMP'
SiamRPN = './results/SiamRPN++'


dataset = get_dataset('otb')
sequence = 'David' #
if sequence is not None:
    dataset = [dataset[sequence]]

for seq in dataset:
    ATOM_file = '{}/{}.txt'.format(ATOM, seq.name)
    DaSiamRPN_file = '{}/{}.txt'.format(DaSiamRPN, seq.name)
    DiMP_file = '{}/{}.txt'.format(DiMP, seq.name)
    ECO_file = '{}/{}.txt'.format(ECO, seq.name)
    KYS_file = '{}/{}.txt'.format(KYS, seq.name)
    PrDiMP_file = '{}/{}.txt'.format(PrDiMP, seq.name)
    SiamRPN_file = '{}/{}.txt'.format(SiamRPN, seq.name)
    OUPT_file = '{}/{}.txt'.format(OUPT, seq.name)

    # if os.path.isfile(d_file):
    gt = seq.ground_truth_rect
    ATOM_bb = np.loadtxt(ATOM_file)
    DaSiamRPN_bb = np.loadtxt(DaSiamRPN_file, delimiter=',')
    DiMP_bb = np.loadtxt(DiMP_file)
    ECO_bb = np.loadtxt(ECO_file)
    KYS_bb = np.loadtxt(KYS_file)
    PrDiMP_bb = np.loadtxt(PrDiMP_file)
    SiamRPN_bb = np.loadtxt(SiamRPN_file)
    OUPT_bb = np.loadtxt(OUPT_file)

    output_path = './video/{}/'.format(seq.name)
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for frame_num, frame_path in enumerate(seq.frames):
        im = cv.imread(seq.frames[frame_num])
        # im = cv.cvtColor(im, cv.COLOR_BGR2RGB)
        # plt.imshow(im)

        pred_bb =[gt[frame_num]]
        for i, s in enumerate(pred_bb, start=1):
            pred_s = s
            i=9
            tl = tuple(map(int,[pred_s[0], pred_s[1]]))
            br = tuple(map(int,[pred_s[0]+pred_s[2], pred_s[1]+pred_s[3]]))
            col = _tracker_disp_colors[i]
            cv.rectangle(im, tl, br, col, 2)
            plt.imshow(im)
            plt.show()

        cv.imwrite('{}/{}.jpg'.format(output_path, frame_num), im)

print('done!')
