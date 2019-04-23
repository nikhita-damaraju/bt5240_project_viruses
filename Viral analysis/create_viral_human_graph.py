#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 13:27:44 2019

The virus-human interaction file is stored as a .csv file. This script generates the 
networkx graph for the high confidence interaction file

@author: nikhitadamaraju
"""

#import sys
import pandas as pd
import networkx as nx
#from tkinter import Tk
#from tkinter.filedialog import askopenfilename
#import logging

#Tk().withdraw()
# Upload file with virus-human PPI data
#source_file = askopenfilename(title = 'Upload viral PPI file',filetypes = (("csv files","*.csv"),("all files","*.*")))

#print(source_file)

source_file = "/Users/nikhitadamaraju/Desktop/Systems Biology/Project/Viral analysis/hhv1_ppi.csv"  
# Read virus-human PPI file
file = pd.read_csv(source_file)

#Get edge list from the file
edgelist = [(row['protein1'], row['protein2']) for index, row in file.iterrows()]

# Create graph for the virus-human PPI network
G = nx.Graph()
G.add_edges_from(edgelist)
    
# Print the virus-human PPI network info    
print(nx.info(G))

deg_centrality = nx.degree_centrality(G)   
eig_vec_centrality = nx.eigenvector_centrality(G)
close_centrality = nx.closeness_centrality(G)
#egde_betw_centrality = nx.edge_betweenness_centrality(G)   
harm_centrality = nx.harmonic_centrality(G)
ld_centrality = nx.load_centrality(G)
subg_centrality = nx.subgraph_centrality(G)

centrality_df = pd.DataFrame({'prot_id': list(deg_centrality.keys()) ,                   #add nodes
                                  'degree_centrality': list(deg_centrality.values()) ,         #add degree centrality
                                  'eigen_vector_centrality': list(eig_vec_centrality.values()),   #add eigen vector centrality 
                                  'close_centrality': list(close_centrality.values()),      #add closeness centrality
                                  #'edge_betweenness': ,          #add edge betweenness
                                  'harmonic_centrality': list(harm_centrality.values()),       #add harmonic centrality
                                  'load_centrality': list(ld_centrality.values()),      #add load centrality
                                  'subgraph_centrality': list(subg_centrality.values()) #add subg centrality 
                                  })
    
    
#centrality_df.to_csv("centrality_measures_hhv1.csv",index=False)
