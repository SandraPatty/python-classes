import array
import matplotlib.pyplot as plt
import os
import matplotlib.colors as mcolors
import numpy as np

bc = mcolors.BASE_COLORS

m = 0
directory = "dead_moroz"
files = []
files += os.listdir(directory)

for i in files:
    X = []
    Y = []
    N = "a"
    s = os.path.join(directory, str(i))
    with open(s) as f:
        lines = f.readlines()
        N = int(lines[0])
        for j in range(1, N + 1):
            x, y = map(float, lines[j].split(" "))
            X.append(x)
            Y.append(y)

    num_set = np.random.randint(1, len(mcolors.BASE_COLORS), N)
    colors = [list(bc.keys())[i] for i in num_set]
    
    
    plt.scatter(X, Y, alpha=0.5, c="r", s=40)
    plt.scatter(X, Y, alpha=0.4, c=colors, linewidths=2, edgecolors="face", s = 7)
    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.title("Number of points " + str(N))

    m+=1
    plt.gca().set_aspect('equal')
    plt.savefig("pic" + str(m) +".jpg")
    plt.show()