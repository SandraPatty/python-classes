import array
import matplotlib.pyplot as plt
import numpy as np

font_color = 'sienna'
colors=['#FFEBCD', '#FFDEAD', '#F4A460', '#FFA07A', '#FF7F50', 
'#FF6347', '#CD5C5C', '#DC143C']

with open("students.txt") as f:
    
    lines = [i.split()[0].split(';') for i in f.readlines()]
    print(lines)
    preps = sorted(set(lines[i][0] for i in range(len(lines))))
    groups = sorted(set(lines[i][1] for i in range(len(lines))))
    marks = sorted(set(int(lines[i][2]) for i in range(len(lines))))
    print(marks)
    
    
    fig, axes = plt.subplots(3, 3, figsize=(7, 10), facecolor='#e8f4f0')
    fig.delaxes(ax=axes[2,2])
    fig.delaxes(ax=axes[1,2])
    M = [0] * len(preps)
    for i in range(len(preps)):
        s = 0
        M[i] = [0]*(len(marks))
        labels = [" "]*(len(marks))
        for k in range(len(lines)):
            if lines[k][0] == preps[i]: 
                a = int(lines[k][2]) - 3
                s+=1
                M[i][a] += 1
                labels[a] = M[i][a]
    
        ax = axes[i%3, i//3]
        ax.pie(M[i], labels=labels, labeldistance=.78, radius=1.2, startangle=30, 
           wedgeprops=dict(width=.5), # For donuts
           colors=colors, 
           textprops={'color':'rosybrown', 'fontweight':'bold'})
            
        ax.set_title(preps[i], fontsize=10, color=font_color, fontweight='bold')
        
        legend = plt.legend(np.roll(np.array(marks), 0), 
                                prop = { "size": 18 },
                                bbox_to_anchor=(1.5, 2.2), # Legend position
                                loc='upper left',  
                                ncol=1, 
                                fancybox=True)
        for text in legend.get_texts():
            plt.setp(text, color=font_color, alpha=0.7, fontweight='bold')
            
    fig.subplots_adjust(wspace=.2) # Space between charts

    title = fig.suptitle('Grades in dependence of teachers', y=.95, fontweight='bold', fontsize=20, color=font_color)
    # To prevent the title from being cropped
    plt.subplots_adjust(top=0.85, bottom=0.15)
    plt.savefig("preps" +".png")
    plt.show()
    
    fig, axes = plt.subplots(2, 3, figsize=(8, 8), facecolor='#e8f4f0')
 
    M = [0] * len(groups)
    for i in range(len(groups)):
        s = 0
        M[i] = [0]*(len(marks))
        labels = [" "]*(len(marks))
        for k in range(len(lines)):
            if lines[k][1] == groups[i]: 
                a = int(lines[k][2]) - 3
                s += 1
                M[i][a] += 1
                labels[a] = M[i][a]
    
        ax = axes[i%2, i//2]
        ax.pie(M[i], labels=labels, labeldistance=.78, radius=1.1, startangle=30, 
           wedgeprops=dict(width=.7), # For donuts
           colors=colors, 
           textprops={'color':'rosybrown', 'fontweight':'bold', "size": 11, 'alpha':0.8})
            
        ax.set_title(groups[i], fontsize=15, y=0.95, color=font_color, fontweight='bold')
        
    legend = plt.legend(marks, 
                                bbox_to_anchor=(0.5, -0.4),
                                prop = { "size": 16 },
                                ncol=4, 
                                fancybox=True)
    for text in legend.get_texts():
            plt.setp(text, color=font_color, alpha=0.7, fontweight='bold')
            
    fig.subplots_adjust(wspace=.18, hspace=.7) # Space between charts

    title = fig.suptitle('Grades in dependence of groups', y=.95, fontweight='bold', fontsize=20, color=font_color)
    # To prevent the title from being cropped
    plt.subplots_adjust(top=0.85, bottom=0.26)
    plt.savefig("groups" +".png")
    plt.show()
    
    
    
