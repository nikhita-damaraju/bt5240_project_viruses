#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 10:58:47 2019
The <virus>_human.csv files listed in gen_file_list.csv should be 
saved in the same folder as gen_file_list.csv.

A log file with the name 'subgraph_except.log' will be created/
updated with the exceptions that happen during subgraph generation.

Ego graph details for each <virus>_human.csv file will be saved in a
.csv file in the same path as the <virus>_human.csv file.

@author: debomita

"""

import sys
import pandas as pd
import networkx as nx
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import logging

Tk().withdraw()
# Upload file with human PPI data
source_file = askopenfilename(title = 'Upload human PPI file',filetypes = (("csv files","*.csv"),("all files","*.*")))
print(source_file)
# Upload file with list of file names containing human proteins
# from viral-human interaction network
subgraph_file = askopenfilename(title = 'Upload "gen_file_list.csv"',filetypes = (("csv files","*.csv"),("all files","*.*")))
print(subgraph_file)

# Read Human PPI file
file = pd.read_csv(source_file, sep = " ")
# Filter out PPIs with combined_score >= 900
file = file[file["combined_score"]>=900]

# Get edge list from the file
edgelist = [(row['protein1'], row['protein2']) for index, row in file.iterrows()]


# Create graph for the human PPI network
G = nx.Graph()
G.add_edges_from(edgelist)
    
# Print the human PPI network info    
print(nx.info(G))

#********************Constructing the subgraph*********************************

ego_edgelist = []
# Read file containing file names (<virus>_human.csv)
sub_fnames = pd.read_csv(subgraph_file)
sub_fnames1 = [row['fname'] for index, row in sub_fnames.iterrows()]
for sub_line in sub_fnames1:  

    # Get node list from column 1 of file
   sub_node_list = pd.read_csv(subgraph_file[:-17]+sub_line, usecols=[0])
   sub_node_list1 = [row['prot_id'] for index, row in sub_node_list.iterrows()]
    # Initialize subgraph
   G_sub = nx.Graph() 
   for node_i in sub_node_list1:
       try:
           # Pass each node to get a subgraph of upto the 3rd nearest neighbour
           G_sub_i = nx.ego_graph(G, node_i,radius = 3, center=True, undirected=True)
           pass
       except:
           
           logging.basicConfig(filename='subgraph_except.log',level=logging.DEBUG)
           logging.debug(sys.exc_info())
           logging.info('Filename:'+sub_line+'\n')
           pass
       # Take union of the subgraphs generated for each node in the file              
       G_sub = nx.compose(G_sub,G_sub_i)
   # List ego graph edgelist    
   ego_edgelist = G_sub.edges
   
   # Save ego graph details for each <virus>_human.csv file into a .csv file
   dataf = pd.DataFrame({'edges':ego_edgelist})
   

   dataf.to_csv(subgraph_file[:-17]+sub_line[:-9]+'egoedges.csv', index = False, header = True)
   
   # Print the info for subgraphs of each file
   print("Subgraph_"+sub_line[:-4]+'\n',nx.info(G_sub))
