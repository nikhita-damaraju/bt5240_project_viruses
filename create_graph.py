#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 10:58:47 2019

@author: debomita
"""

import pandas as pd
import networkx as nx
from tkinter import Tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

Tk().withdraw()
source_file = askopenfilename()
print(source_file)

file = pd.read_csv(source_file, sep = "\t")
file = file[file["combined_score"]>=200]

nodelist = []

for col in ['protein1', 'protein2']:
    nodelist.extend(file[col].unique().tolist())

nodelist = set(nodelist)

edgelist = [(row['protein1'], row['protein2']) for index, row in file.iterrows()]


G = nx.Graph()
G.add_nodes_from(nodelist)
G.add_edges_from(edgelist)
    
    
print(nx.info(G))