
# coding: utf-8

#!/usr/bin/env python3
"""
Created on Fri Apr 19 13:27:44 2019
this script reads the tsv files dowloaded from string.Viruses and converts it to a 
high confidence .csv file with columns
    protein1
    protein2
    combined_score

@author: nikhitadamaraju
"""# -*- coding: utf-8 -*-


#header files 
import pandas as pd
import networkx as nx
import csv

#script to import tsv files containing viral-host interaction graph data
f1 = open("/Users/nikhitadamaraju/Desktop/Systems Biology/Project/Viral analysis/Epstein_barr_virus.tsv")
f2 = open("/Users/nikhitadamaraju/Desktop/Systems Biology/Project/Viral analysis/Human_herpes_virus_1.tsv")
ebv = pd.read_csv(f1,delimiter='\t',encoding='utf-8')
hhv1 = pd.read_csv(f2,delimiter='\t',encoding='utf-8')
#filtering for entries that have a score greater than 0.8
hhv1 = hhv1[hhv1['combined_score']>=0.9]
ebv = ebv[ebv['combined_score']>=0.9]

#storing high confidence ppi graphs in new csv file
df_ebv = pd.DataFrame()
df_ebv[['protein1','protein2','combined_score']] = ebv[['node1_external_id','node2_external_id','combined_score']]
df_ebv.to_csv("ebv_ppi.csv",index=False)

df_hhv1 = pd.DataFrame()
df_hhv1[['protein1','protein2','combined_score']] = ebv[['node1_external_id','node2_external_id','combined_score']]
df_hhv1.to_csv("hhv1_ppi.csv",index=False)

