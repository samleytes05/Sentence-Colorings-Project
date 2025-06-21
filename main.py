import networkx as nx
import matplotlib.pyplot as plt
from networkx import greedy_color
import csv
from color import Sentence
import re



def main(): 

    bookList = ["AbsalomAbsalom.txt", "TheHouseOfTheSevenGambles.txt", "SwansWay.txt", "MobyDick.txt", "Various.txt"]
    resualts = []  
    

    for book in bookList:
        textfile = readTxtFile(book)
        print(f"Reading {book} — {len(textfile)} characters")
        sentences = splitSent(textfile)

        for sent in sentences:
            elem = Sentence(sent)
            resualts.append([
                book, 
                elem.numtokens,
                elem.numUniqueTokens,
                elem.mincolors,
                #elem.text
                           ])
        print(f"Finished {book}")
    toCSV(resualts, "dataOutput.csv")



def readTxtFile(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        return f.read()
    
def splitSent(text):
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', text)
    ##help from chatgpt to structure this, in sources
    abbreviations = {"Mr.", "Mrs.", "Ms.", "Dr.", "Prof.", "Sr.", "Jr.", "St.", "Mt."}
    moddedSent = []

    for i in range(len(sentences)):
        if i > 0 and any(sentences[i - 1].endswith(abbr) for abbr in abbreviations):
            moddedSent[-1] += ' ' + sentences[i]
        else:
            moddedSent.append(sentences[i])

    return [s.strip() for s in moddedSent if s.strip()]


def toCSV(data, output):
    with open(output, 'w', newline = '', encoding='utf8') as f:

        writer = csv.writer(f)
        writer.writerow(['Book Name', 'Total Tokens', 'Unique Tokens', 'Min Colors'])
        writer.writerows(data)

if __name__ == "__main__":
    main()