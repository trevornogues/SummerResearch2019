#!python2
from graph_tool.all import *

g = Graph()
ug = Graph(directed = False)

ug = Graph()
ug.set_directed(False)
assert ug.is_directed() == False

