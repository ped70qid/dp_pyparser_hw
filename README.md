### Dependency Parsing Homework

###### uv commands
- `uv init`
- `uv run script.py`
- `uv add <dep>`


wierd stuff happening when you name test funcitons the same, then only one test passes or failes even though more are defined --> overloading??


labels are gathered in train\3, also need to be saved still to the pickle file

Lines are not split correctly, make sure that `line.split('\t')` is used

how to use the `run.ps1`file?
-> just run in powershell terminal (seperate)

Vim stuff:
---
- 'gh' for hover
- 'gj' and 'gk' for linewise movement in blocks

TODO: 
--------------
- adjust scoring function to something like $scoring()=s\_heads() + s\_labels()$ so you dont get these huge classes, with the Tupels $(head,label)$
- remove old Moves_lab stuff 
- probably add labels in `transitions()`
- should i use the PerceptronTagger, for predicting the lables first? -> new Features as well?
- Parser.train_one() --> transitions(...) gets called here with 'guess'. better with 'best'?
- transitions() --> add() label param added
- why features implemented as dict[str, 1]??? 1 is unneccessary? -> onehot encoding basically
- fix dumping and loading classes for labels --> look at PerceptronTagger

Branch
- add label features --> because of pad_tokens() label list is shorter than tags and words
- scoring
- get_gold_moves, and get valid_moves dont care about the labels. ONly make sure, that moves get returned in the new format, with all the labels attached

1. new classes - done
2. update train_one() with new arcs 
3. make function to deal with the moves from get_valid_moves() and get_gold_moves()
4. update parse() to tuples
5. get rid of the second Perceptron() originally used for labels

Explainations:
---
- Perceptron().classes => Moves (shift, right, left)