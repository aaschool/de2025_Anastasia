# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv

frame_id = '0500'
dataDir = 'D:/ToF/data/PointCloud_bin/'

frameIds = []
for i in range(500, 501):
    #frameIds.append('{:04d}'.format(i))            # new style
    frameIds.append('%(idstr)04d' % {"idstr":i})    # old style
    
for frame_id in frameIds:
    xPos = []
    yPos = []
    zPos = []
    selectZIds = []
    zId = 0            
    with open(dataDir + 'frame' + frame_id +'_x.csv') as csvfile:
        loadedFile = csv.reader(csvfile, delimiter=',')    
        for row in loadedFile:
            for val in row:
                xPos.append(float(val))
    
    with open(dataDir + 'frame' + frame_id +'_y.csv') as csvfile:
        loadedFile = csv.reader(csvfile, delimiter=',')    
        for row in loadedFile:
            for val in row:
                yPos.append(-float(val))
            
    with open(dataDir + 'frame' + frame_id +'_z.csv') as csvfile:
        loadedFile = csv.reader(csvfile, delimiter=',')    
        for row in loadedFile:
            for val in row:
                zPos.append(float(val))            
                if float(val) < 3:
                    selectZIds.append(zId)
                zId = zId+1
    
#    print(('xPos -- min:{}  max:{}').format(min(xPos), max(xPos)))
#    print(('yPos -- min:{}  max:{}').format(min(yPos), max(yPos)))
#    print(('zPos -- min:{}  max:{}').format(min(zPos), max(zPos)))
    
            
    outputFile = open(dataDir + 'XYZ/' + 'frame' + frame_id + '.xyz', 'w')
    #for i in range(0, len(xPos)):
    for i in selectZIds: 
      outputFile.write(str(xPos[i]) + ' ' + str(yPos[i]) + ' ' + str(zPos[i]) +'\n')
       #outputFile.write(str(xPos))
    
    print('frame {} saved\n'.format(frame_id))    
    outputFile.close()