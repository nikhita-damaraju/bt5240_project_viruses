#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:17:13 2019
Upload csv file with the fasta file names. 
Each file is used to generate two csv files listing:
 1. Host-virus proteins
 2. Human proteins

@author: debomita
"""
import csv
import pandas as pd
from tkinter import Tk
from tkinter import filedialog

Tk().withdraw()
source_file = askopenfilename()
print(source_file)

dest_path = filedialog.askdirectory()

fasta_fn = open(source_file)
file_list = fasta_fn.readlines()
for file_name in file_list:

    f = open(file_name[:-1]) #reading fasta file
    lines = f.readlines()
    
    newlines = []
    prot_id = []
    prot_name = []
    prot_id1 = []
    prot_name1 = []
    
    
    for line in lines: 
        if line.startswith(">"):
            line1 = line
            name, ID,info = line1.split("\t")   #splitting each item in list by tab \t to separate names and IDs
            prot_name.append(name[1:])       #adding protein name without ">" to list prot_name
            prot_id.append(ID)               #adding protein ID to list prot_id
            #storing host virus protein names and ID in dataframe "df"
            df = pd.DataFrame({'prot_id': prot_id,
                               'prot_name': prot_name})
            if ID[:9] == '9606.ENSP':
               prot_name1.append(name[1:])       #adding protein name without ">" to list prot_name
               prot_id1.append(ID)               #adding protein ID to list prot_id
               #storing human protein names and ID in dataframe "df1"
               df1 = pd.DataFrame({'prot_id': prot_id1,
                                  'prot_name': prot_name1})
               
    
    host_vir_file   = file_name[:-4]+'_host.csv'           
    human_prot_file = file_name[:-4]+'_human.csv'
    
    
    #storing dataframe into csv file
    df.to_csv(dest_path+'/'+host_vir_file, index=False, header=False)           
    df1.to_csv(dest_path+'/'+human_prot_file, index=False, header=False)
    
print("Finished creation of files.")