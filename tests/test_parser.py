from proj.parser import * 
from proj.parser import Parse 
import pytest 

SENT_LEN = 10

parse = Parse(SENT_LEN)

SHIFT = 0; RIGHT = 1; LEFT = 2;

def test_transition_shift():
    s = [1]
    position = transition(move= (SHIFT,"abc"), i= 2, stack= s, parse=parse)
    assert position == 3 
    assert s == [1,2]

def test_transition_right():
    s = [1,2]
    position = transition(move= (RIGHT, "abc"), i= 3, stack= s, parse=parse)
    assert position == 3 
    assert s == [1]
    