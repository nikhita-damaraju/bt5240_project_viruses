#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 10:58:47 2019
The <virus>_human.csv files data have been merged into a .csv file 
saved in the same path as gen_file_list.csv.

A log file with the name 'subgraph_except.log' will be created/
updated with the exceptions that happen during subgraph generation.

@author: debomita

"""

import sys
import pandas as pd
import networkx as nx
import logging
      
def deg_cent(G,node):    
# Degree centrality    
    deg_centrality1 = nx.degree_centrality(G)
    deg_centrality = deg_centrality1[node]    
    return(deg_centrality)
#******************************************************************************
#def eigvec_cent(G,node):
## Eigen vector centrality
#    eig_vec_centrality1 = nx.eigenvector_centrality(G) 
#    eig_vec_centrality = eig_vec_centrality1[node]
#    return(eig_vec_centrality)
#****************************************************************************** 
def clos_cent(G,node):    
# Closeness centrality 
    clos_centrality = nx.closeness_centrality(G, u=node)   
    return(clos_centrality)
#******************************************************************************
def subgr_cent(G,node):    
# Subgraph centrality   
    subgr_centrality1 = nx.subgraph_centrality(G)
    subgr_centrality = subgr_centrality1[node]
    return(subgr_centrality)
#****************************************************************************** 
 
def centr_measures(G_sub, node, deg_centrality, clos_centrality,
                   subgr_centrality):


#   Add centrality measures to list   
    deg_centrality.append(deg_cent(G_sub,node)) 
    clos_centrality.append(clos_cent(G_sub,node))
    subgr_centrality.append(subgr_cent(G_sub,node))

#******************************************************************************
#******************************************************************************    

source_file = '/data/nikhita/sysbio/9606.protein.csv'    

# Read Human PPI file
file = pd.read_csv(source_file, sep = " ")
# Filter out PPIs with combined_score >= 900
file = file[file["combined_score"]>=900]

# Get edge list from the file
edgelist = [(row['protein1'], row['protein2']) for index, row in file.iterrows()]

# Create graph for the human PPI network
G = nx.Graph()
G.add_edges_from(edgelist)
    
#********************Constructing the subgraph*********************************
#Initialize lists
node = []
deg_centrality = []
clos_centrality = []
subgr_centrality = []

# Get node list from column 1 of file
sub_node_list = pd.read_csv('/data/nikhita/sysbio/dna.csv', usecols=[0])
sub_node_list1 = [row['prot_id'] for index, row in sub_node_list.iterrows()]
# Initialize subgraph
G_sub = nx.Graph() 
for node_i in sub_node_list1:
   try:           
   # Pass each node to get a subgraph of upto the 3rd nearest neighbour
       G_sub= nx.ego_graph(G, node_i,radius = 3, center=True, undirected=True)
# Call function for calculation of centrality measures
       centr_measures(G_sub, node_i, deg_centrality, clos_centrality, 
                          subgr_centrality)
        
       node.append(node_i)
       pass
   except:   
       logging.basicConfig(filename='/data/nikhita/sysbio/subgraph_except.log',level=logging.DEBUG)
       logging.debug(sys.exc_info())
       pass
       
#******************************************************************************    
# Write all the centrality measures found, into a csv file    
    
#******************************************************************************    
centrality_df = pd.DataFrame({'prot_id': node,                                 #add nodes
                              'degree_centrality': deg_centrality,             #add degree centrality
                              'closeness_centrality': clos_centrality,         #add closeness centrality
                              'subgraph_centrality': subgr_centrality          #add subgraph centrality
                                  })        
##  The csv file with the centrality measures would be updated 
with open('/data/nikhita/sysbio/centrality.csv', mode = 'a') as f:
    centrality_df.to_csv(f, index = False, header = False)         
     
