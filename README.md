# Chinese Checkers AI
## Install instructions
```
pip install -r requirements.txt
```

## Usage

### Human vs. AI
```
python3 ai_vs_human.py -d=depth -h=heuristic
```

### AI vs. AI
```
python3 ai_vs_ai.py -d1=depth -h1=heuristic -d2=depth -h2=heuristic
```

#### Arguments range
```
depth = [2, 3, ...]
heuristic = [EUCLIDEAN, V_DISPLACEMENT, EMPTY_GOAL, CLUSTERING]
```

