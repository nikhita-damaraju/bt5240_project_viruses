#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:36:42 2019

@author: debomita
"""
import networkx as nx
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import ast
import logging
import sys

Tk().withdraw()
# Upload the file 'gen_file_list.csv'
subgraph_file = askopenfilename(title = 'Upload "gen_file_list.csv"',filetypes = (("csv files","*.csv"),("all files","*.*")))
print(subgraph_file)

# Read the file 'gen_file_list.csv'
sub_fnames = pd.read_csv(subgraph_file)

# Get the file names in 'gen_file_list.csv' into a list
sub_fnames1 = [row['fname'] for index, row in sub_fnames.iterrows()]
for sub_line in sub_fnames1:
    
    edge_list1  = []  
    # Get the file name containing the ego graph edgelist
    edge_filename = subgraph_file[:-17]+sub_line[:-9]+'egoedges.csv'
    
    # Read the file containing the ego graph nodelist
    edge_list = pd.read_csv(edge_filename, converters={'edges': ast.literal_eval})
     # Get the ego graph edgelist into a list
    edge_list1 = [row['edges'] for index, row in edge_list.iterrows()]
    # Initialize a graph
    G_sub = nx.Graph()
    
    # Reconstruct the ego graph 
    G_sub.add_edges_from(edge_list1)
    print(nx.info(G_sub))
 #***********************************************************************************
 #*****************************Centrality measures***********************************  
    # Degree centrality
    deg_centrality = nx.degree_centrality(G_sub)

#******************************************************************************
#FILTER ENTRIES     
    nodes = []
    deg_cent = []
    hu_nodelist = []
    nodes = deg_centrality.keys()
    deg_cent = deg_centrality.values()
    deg_cent_df = pd.DataFrame({'prot_id': nodes, 'degree_centrality': deg_cent})   
    hu_nodelist = pd.read_csv(subgraph_file[:-17]+sub_line, usecols=[0])
  
    hu_df = pd.DataFrame(hu_nodelist)


#    deg_cent_df = pd.merge(hu_df, deg_cent_df, how='inner', left_index = False, right_on = 'prot_id')
#    
#    
##    deg_cent_df = deg_cent_df.filter('node','degree_centrality')
##    deg_df = pd.DataFrame({'degree_centrality':deg_centrality})
#    
#    
##    deg_df = deg_df[deg_df.isin(node_list1)]
#    
##    print(deg_centrality)
#    print(deg_cent_df)
 
#    print(deg_cent_df)
 
#****************************************************************************** 
     # Eigen vector centrality
#    eig_vec_centrality = nx.eigenvector_centrality(G_sub)
    
#REPEAT FILTER    
#    print(eig_vec_centrality)
#******************************************************************************     
    # Closeness centrality 
#    clos_centrality = []
#    hu_nlist = [row['prot_id'] for index,row in hu_nodelist.iterrows()]
#    for node in hu_nlist:
#        try: 
#            clos_centrality = nx.closeness_centrality(G_sub, u= node)
#            print(clos_centrality)
#            pass
#        except:
#           logging.basicConfig(filename='subgraph_except.log',level=logging.DEBUG)
#           logging.debug(sys.exc_info())
#           logging.info('Filename:'+sub_line+'\n')
#           pass
#
#
##*****************************************************************************
#
#    # Edge betweenness centrality
#    egde_betw_centrality = nx.edge_betweeness_centrality(G_sub)   
#REPEAT FILTER     
#******************************************************************************    
# Harmonic centrality
#    harm_centrality = nx.harmonic_centrality(G)
#REPEAT FILTER     
#******************************************************************************    
#    # Load centrality
#    ld_centrality = nx.load_centrality(G)
#REPEAT FILTER         
#******************************************************************************
    
# Write all the centrality measures found, into a csv file    
    
#******************************************************************************    
#    centrality_df = pd.DataFrame({'prot_id': ,                   #add nodes
#                                  'degree_centrality': ,         #add degree centrality
#                                  'eigen_vector_centrality': ,   #add eigen vector centrality 
#                                  'closeness_centrality': ,      #add closeness centrality
#                                  'edge_betweenness': ,          #add edge betweenness
#                                  'harmonic_centrality': ,       #add harmonic centrality
#                                  'load_centrality':             #add load centrality 
#                                  })
#    
#    
#    # Each <virus>_human.csv file would generate a file named <virus>_centrality.csv
#    # and would be saved in the same folder as gen_file_list.csv
#    
#    centrality_df.to_csv(subgraph_file[:-17]+sub_line[:-9]+'centrality.csv', index = False, header = True) 


