Project Overview:
This project is a linguistics analysis on syntax structure of sentences in the English language.
This project uses Graph theory concepts, primarly colorings to model how tokens (words and punctuation) in a sentence interact.
This is done by representing sentences as graph using the tokens as nodes and computing the "chromatic number" to study grammatical complexity of the sentences.
Ultimately this project is a research project and the end goal is to generate graphs with lines of best fits to analyze trends between different aspects of the sentences.

Dependencies:
Python version 3.11.6
pandas
matplotlib
networkx
re (regex)
numpy
csv

To install these use the following lines in the command prompt after opening the file location.

conda create -n PIC16A-25S python=3.11.6
conda activate PIC16A-25S
conda install --channel=conda-forge pandas matplotlib networkx numpy


How to Run:
To run this project, in main.py add the files you want to analyze (.txt documents in same file directory as main.py) to the list of booklist = [].
Then click run and the program will seperate each sentence and parse all of them and store them in dataOutput.csv with columns of book title, number tokens, number unique tokens, and minimum colors.
Then to generate graphs that analyze different styles of token count (total, unique, or repeated) to minimum colors you go to visual.py and run.
Additionaly running this will show what each sentence looks like as a graph and a coloring of it as well for visual understanding of how each sentence is treated and converted to a graph for analysis.
The outputs expected are stated above with each of the .py files explained.

Output:
The main output is the dataOutput.csv which holds all the meta data for the parsed sentences, and from which data is pulled to generate visuals for interpretting it.

Potential Limitations:
These are the instructions and limitations include files that need to be parsed must .txt and within the same folder as the project. Also for potentially legal usage, the texts should be in the public domain.
Additionaly, sentences are seperated based on punctuation marks detection with some prelisted exceptions like Mr. Dr. , etc... this can cause some sentences with other acronyms to be split when they should not be.
Furthermore, coloring algorithms do not return the chromatic number, but an estimation of the chromatic number (true minimum number of colors). 
Graph coloring are hard to find, so this process run a few different algorithms and accepts the smallest returned number of colors as the used one.
