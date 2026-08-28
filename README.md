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

Explainations:
---
- Perceptron().classes => Moves (shift, right, left)