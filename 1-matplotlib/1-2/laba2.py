import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

bc = mcolors.BASE_COLORS

with open("1.txt") as f:
    lines = f.readlines()
    N = len(lines)//2
    m=0
    for i in range(N):
        X = [float(j) for j in lines[2*i].split(" ")]
        Y = [float(j) for j in lines[2*i+1].split(" ")]

        num_set = np.random.randint(1, len(mcolors.BASE_COLORS), len(X))
        colors = [list(bc.keys())[i] for i in num_set]
    
    
        plt.plot(X, Y, c="r")
        plt.xlabel('x label')
        plt.ylabel('y label')
        m+=1
        plt.title("Frame " + str(m))
        plt.grid()
        plt.xlim([-1, 17])
        plt.ylim([-12, 14])
        plt.yticks(list(range(-12, 14, 2)))
        
        plt.savefig("pic" + str(m) +".jpg")
        plt.show()

