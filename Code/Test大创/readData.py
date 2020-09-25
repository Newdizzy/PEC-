

def readData(src:str , isDraw = 1):


    import numpy as np
    cnt = 0
    dataDict = {'x':[],'y':[]}


    with open(src,'r') as f:
        flag = 0 

        for line in f:
            if flag == 0 and line == 'Time/sec, Current/A\n' :
                flag = 1
                continue

            #正式数据
            if flag == 1 and line != '\n' :
                [t,c] = line.split(', ')
                dataDict['x'].append( float(t) )
                dataDict['y'].append( float(c) ) #float进行数据格式转换
                cnt += 1
    dataDict['x'] = np.array(dataDict['x'])
    dataDict['y'] = np.array(dataDict['y'])

    dataDict['readLineNumber'] = cnt

    #默认绘图
    if isDraw == 1:
        import matplotlib.pyplot as plt
        import numpy as np
        #dataDict = {'x':[],'y':[]}
        x = np.array( dataDict['x'] )
        y = np.array( dataDict['y'] )

        plt.plot(x,y)
        plt.show()

    return dataDict

if __name__ == "__main__":
    import numpy as np
    import time
    #src = '2-1-jg218-5min-PLCeSh5.txt'

    src = '2-1-100ul-30s-1.txt'
    dataDict = readData(src)
    current = dataDict['y']
    
    t = time.process_time()
    for i in range( len(current)-1 ) :
        deltI = current[i+1] - current[i]
    t = time.process_time() - t
    print(t)
