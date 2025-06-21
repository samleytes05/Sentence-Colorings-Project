import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from color import Sentence
import networkx as nx


csvFile = pd.read_csv("dataOutput.csv")

numT = csvFile["Total Tokens"]
numUT = csvFile["Unique Tokens"]
repeatT = numT - numUT
minColors = csvFile["Min Colors"]

sortedTMC = sorted(zip(numT, minColors))
sortedUTMC = sorted(zip(numUT, minColors))
sortedReapets = sorted(zip(repeatT, minColors))

##used chatgpt to make 1 function that can run multiple types of data with proper titling in the graph
def plotTMC(Tokens, xaxisName):
    x, y = map(np.array, zip(*Tokens))
    plt.scatter(x, y)
    
    plt.xlabel(f"{xaxisName}")
    plt.ylabel("Min Colors")
    plt.title(f"{xaxisName} (per Sentence) vs Minimum Colors")


    ##polynomial
    coeff = np.polyfit(x, y, 3)
    polynomial = np.poly1d(coeff)
    x_smooth = np.linspace(min(x), max(x), num=500)
    y_smooth = polynomial(x_smooth)
    plt.plot(x_smooth, y_smooth, color='red', linewidth=2)
        
    ##log
    x_original = x[x > 0]
    y_original = y[x > 0]
    log_coeff = np.polyfit(np.log(x_original), y_original, 1)
    a, b = log_coeff
    y_log_fit = a * np.log(x_smooth[x_smooth > 0]) + b
    plt.plot(x_smooth[x_smooth > 0], y_log_fit, color='blue', linewidth=2, label="Logarithmic Fit")

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

##used chatgpt to help with making a colored graph using what I had already built in color.py
def draw_colors(graph):
    d = dict()
    d = d['largest_first'] = nx.greedy_color(graph, strategy='largest_first', interchange=False)
    node_colors = [d[node] for node in graph.nodes()]

    pos = nx.spring_layout(graph)
    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_color=node_colors,
        cmap=plt.cm.Set3,
        node_size=800,
        font_size=10,
        edgecolors="black"
    )
    plt.title("Colored Graph")
    plt.show()
    pass 




sample_sent1 = Sentence("Sam and Nicole like boba and french toast but not french boba.")
sample_sent2 = Sentence('“To none of these interrogatories, whereof every one was more pathetically delivered than the last, did Mrs Varden answer one word: but Miggs, not at all abashed by this circumstance, turned to the small boy in attendance—her eldest nephew—son of her own married sister—born in Golden Lion Court, number twenty-sivin, and bred in the very shadow of the second bell-handle on the right- hand door-post—and with a plentiful use of her pocket- handkerchief, addressed herself to him: requesting that on his return home he would console his parents for the loss of her, his aunt, by delivering to them a faithful statement of his having left her in the bosom of that family, with which, as his aforesaid parents well knew, her best affections were incorporated; that he would remind them that nothing less than her imperious sense of duty, and devoted attachment to her old master and missis, likewise Miss Dolly and young Mr Joe, should ever have induced her to decline that pressing invitation which they, his parents, had, as he could testify, given her, to lodge and board with them, free of all cost and charge, for evermore; lastly, that he would help her with her box upstairs, and then repair straight home, bearing her blessing and her strong injunctions to mingle in his prayers a supplication that he might in course of time grow up a locksmith, or a Mr Joe, and have Mrs Vardens and Miss Dollys for his relations and friends.”')
draw_colors(sample_sent1.graph)
draw_colors(sample_sent2.graph)
print(sample_sent1.mincolors, sample_sent2.mincolors)

##test cases
plotTMC(sortedTMC, "Tokens")
plotTMC(sortedUTMC, "Unique Tokens")
plotTMC(sortedReapets, "Repeated Tokens (None Zero Filtered)")
plt.show()