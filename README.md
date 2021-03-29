# Chinese Checkers AI
## Install instructions
The program uses the following libraries:
* numpy
* pygame
* scipy
* graphviz

To install all the dependencies:
```
pip3 install -r requirements.txt
```

## Usage

### Human vs. AI
##### Normal usage
```
python3 ai_vs_human.py

default: depth = 2; heuristic = CLUSTERING
```
##### Advanced usage
```
python3 ai_vs_human.py -d=depth -h=heuristic
```

### AI vs. AI
##### Normal usage
```
python3 ai_vs_ai.py

default: depth = 2; h1 = EUCLIDEAN; h2 = EMPTY_GOAL
```

##### Advanced usage
```
python3 ai_vs_ai.py -d1=depth -h1=heuristic -d2=depth -h2=heuristic
```

### Arguments range
```
depth = [2, 3, ...]
heuristic = [EUCLIDEAN, V_DISPLACEMENT, EMPTY_GOAL, CLUSTERING]
```

## Team
* Claus Lønkjær - s160108
* Leonardo Zecchin - s203509
* Francesco Romeo - s210222
* Nicolò Sponziello - s210226
