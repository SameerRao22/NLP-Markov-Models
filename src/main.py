#!/usr/bin/python3
import matrix as m
import calc3codes as c

V = [
        [0,1,.5,0],
        [0,0,1,0],
        [1,1,1,1],
        [0,0,1,0],
        [0,0,1,0],
        [1,1,1,1]
    ]

M = [
  [1,  0,  0],
  [2,  1,  0],
  [5,  4,  1]
]

M2 = [
    [1.8, -2.32],
    [-0.25, 0.6]
    ]

M3 = [
    [4, 4, -11, 5],
    [0, 0, 0, 0],
    [-3, 0, 10, 5],
    [0, 0, 0, 0],
    [-3, 0, 10, 5]
    ]

B = [[1],[2],[3]]

M2 = m.inverse(M)
#rowSwap(M2, 1, 3)
m.mPrint(M2)
