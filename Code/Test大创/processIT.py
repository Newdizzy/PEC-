import time
import scipy.io as sio

from readData import readData
src = '2-1-jg218-5min-PLCeSh5.txt'


dataDict = readData(src,0)
sio.savemat('data.mat',dataDict)

# processT = time.process_time()
# cnt = 0
# dataDict = {'Time':[],'Current':[]}


# with open(src,'r') as f:
#     flag = 0 

#     for line in f:
#         if flag == 0 and line == 'Time/sec, Current/A\n' :
#             flag = 1
#             continue

#         #正式数据
#         if flag == 1 and line != '\n' :
#             [t,c] = line.split(', ')
#             dataDict['Time'].append( float(t) )
#             dataDict['Current'].append( float(c) ) #float进行数据格式转换
        



#         cnt += 1

# processT = time.process_time() - processT

# # print(processT)
# # print(cnt)

# # print(dataDict)

# import matplotlib.pyplot as plt
# import numpy as np
# #dataDict = {'Time':[],'Current':[]}
# time = np.array( dataDict['Time'] )
# current = np.array( dataDict['Current'] )

# plt.plot(time,current)
# plt.show()
