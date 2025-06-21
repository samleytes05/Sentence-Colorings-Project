import re
import networkx as nx
import matplotlib.pyplot as plt
from networkx import greedy_color


class Sentence():
    
    def __init__(self, text):
        
        self.text = text
        self.tokens = tokenize(text)
        self.numtokens = tokenCount(self.tokens) 
        self.unique_tokens = unique_tokenizer(self.tokens)
        self.numUniqueTokens = utokenCount(self.unique_tokens) 
        self.graph = buildGraph(self.unique_tokens, self.tokens)
        self.colorings_dict = colorings(self.graph)
        self.mincolors = minColorings(self.colorings_dict) 

    def __str__(self):
        return self.text

def utokenCount(unique_tokens):
    i=0
    for el in unique_tokens:
        i+=1
    return i
def tokenCount(tokenslist):
    i=0
    for el in tokenslist:
        i+=1
    return i

def tokenize(text):
    return re.findall(r"\w+|[^\w\s]", text)

def unique_tokenizer(tokens):
    tempList = []
    for el in tokens:
        if el not in tempList:
            tempList.append(el)
    return tempList




def buildGraph(unique_tokens, tokens):
    graph = nx.Graph()
    for el in unique_tokens:
        graph.add_node(el)



    for i in range(0, len(tokens) - 1):
        graph.add_edge(tokens[i], tokens[i+1])

    return graph


def colorings(graph):
    d = dict()

    d['largest_first'] = nx.greedy_color(graph, strategy='largest_first', interchange=False)
    d['independent_set'] = nx.greedy_color(graph, strategy='independent_set', interchange=False)
    d['random_sequential'] = nx.greedy_color(graph, strategy='random_sequential', interchange=False)

    return d

def minColorings(coloring_dict):

    color_counts = {
        strat: max(coloring.values()) + 1
        for strat, coloring in coloring_dict.items()
    }
    min_count = min(color_counts.values())
    ##print("Color counts per strategy:", color_counts) ##test case
    return min_count



## this only shows a coloring alg, just for visuals rn, later not needed 
'''def draw_colors(graph):
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
    pass '''


##sample_sent = Sentence("Sam and Nicole like boba and french toast but french boba.")
##sample_sent = Sentence('“To none of these interrogatories, whereof every one was more pathetically delivered than the last, did Mrs Varden answer one word: but Miggs, not at all abashed by this circumstance, turned to the small boy in attendance—her eldest nephew—son of her own married sister—born in Golden Lion Court, number twenty-sivin, and bred in the very shadow of the second bell-handle on the right- hand door-post—and with a plentiful use of her pocket- handkerchief, addressed herself to him: requesting that on his return home he would console his parents for the loss of her, his aunt, by delivering to them a faithful statement of his having left her in the bosom of that family, with which, as his aforesaid parents well knew, her best affections were incorporated; that he would remind them that nothing less than her imperious sense of duty, and devoted attachment to her old master and missis, likewise Miss Dolly and young Mr Joe, should ever have induced her to decline that pressing invitation which they, his parents, had, as he could testify, given her, to lodge and board with them, free of all cost and charge, for evermore; lastly, that he would help her with her box upstairs, and then repair straight home, bearing her blessing and her strong injunctions to mingle in his prayers a supplication that he might in course of time grow up a locksmith, or a Mr Joe, and have Mrs Vardens and Miss Dollys for his relations and friends.”')


##test cases 
'''print(sample_sent.text)
print(sample_sent.tokens)
print(sample_sent.unique_tokens)
print(sample_sent.graph)
print(sample_sent.colorings_list)

nx.draw(sample_sent.graph, with_labels=True)
plt.show()

draw_colors(sample_sent.graph)

print(sample_sent.numUniqueTokens)
print(sample_sent.numtokens)

print(sample_sent.mincolors)'''
#print('done')
