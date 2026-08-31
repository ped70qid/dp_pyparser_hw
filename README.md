## Dependency Parsing Homework 2
### Explanation
Joined Labeled arcs:

In dem 'joined labeled arcs' Ansatz werden arcs als Tupel der Form (<move>, <label>) von einem Perceptron gescored.
Dazu musste der Code erweitert werden, um mit den Tupeln klarzukommen. Durch die Verwendung von Tupeln kann ein großer Teil des Codes wiederverwendet werden, da man leicht auf das Label und den Move zugreifen kann, ohne groß Lookup zu betreiben, oder Strings zu parsen.
Damit die 'arcs' von `get_valid_moves()` und `get_gold_moves()` das richtige Format haben fügt die Helfer-Funktion `Parser.add_labels_to_moves()` den Moves jeweils alle Label hinzu.
`Perceptron.save()` und `Perceptron.load()` wurden angepasst, um die Labels aus dem Training abzuspeichern und zu laden.
`Parser.train_one()` wurde angepasst das korrekte Label auszuwählen und and `transition()` weiterzureichen.

---

Zweiter Ansatz:

In dem 'seperated labeled arcs' Ansatz werden die label von einem zweiten Percepton vorhergesagt, und hinzugefügt.
Dazu wurde in `Parser.__init__()` ein zweites Perceptron für Label initalisiert.
`Perceptron.save()` und `Perceptron.load()` wurden angepasst, um das zweite Model zu speichern und laden.
`Parser.train_one()` wurde angepasst, das Label Model mitzutrainieren und das richtige Label an `transition()` weiterzugeben.

---

Sonstiges:

`Parser.train_one()` hat ein zusätzliches Argument bekommen, um die `gold_labels` durchzureichen.
`transition()` hat ein zusätzliches Argument bekommen, um die `label` durchzureichen und `add()` hat dieses Label überreicht bekommen.
`read_conll()` wurde korrigiert, da die Zeilen an dem falschen Charakter gesplittet wurden.
`main_test()` wurde angepasst, um den LAS zu berechnen.
`collect_labels` wurde hinzugefügt, um die Labels vor dem Training zu sammeln.

### Notes
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