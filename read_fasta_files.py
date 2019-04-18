#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:17:13 2019
Upload csv file with the fasta file names. 
Each file is used to generate two csv files listing:
 1. Host-virus proteins
 2. Human proteins
Fasta files must be saved in the same path that is 
entered for creation of above csv files.

@author: debomita

"""

import pandas as pd
from tkinter import Tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

Tk().withdraw()
# Upload csv file with list of fasta file names
source_file = askopenfilename(title = 'Upload list of fasta filenames',filetypes = (("csv files","*.csv"),("all files","*.*")))
print(source_file)

# Get destination path for creation of .csv files
dest_path = filedialog.askdirectory(title = 'Enter path for file generation')

fasta_fn = open(source_file)

# Get list of fasta file names
file_list = fasta_fn.readlines()

gen_file = [] # Initialize a list to hold the names of all human protein files generated

for file_name in file_list:

    f = open(dest_path+'/'+file_name[:-1]) #reading fasta file
    lines = f.readlines()
    
    newlines = []
    prot_id = []
    prot_id1 = []
   
    
    for line in lines: 
        if line.startswith(">"):
            line1 = line
            name, ID,info = line1.split("\t")   #splitting each item in list by tab \t to separate names and IDs
            prot_id.append(ID)               #adding protein ID to list prot_id
            #storing host virus protein names and ID in dataframe "df"
            df = pd.DataFrame({'prot_id': prot_id})
                               
            if ID[:9] == '9606.ENSP':
               prot_id1.append(ID)               #adding protein ID to list prot_id
               #storing human protein names and ID in dataframe "df1"
               df1 = pd.DataFrame({'prot_id': prot_id1})
                                  
               
    
    host_vir_file   = file_name[:-4]+'_host.csv'           
    human_prot_file = file_name[:-4]+'_human.csv'
    if human_prot_file != []:
        gen_file.append(human_prot_file) #addin human protein file names
    
    #storing dataframe into csv file
    df.to_csv(dest_path+'/'+host_vir_file, index=False, header=True)           
    df1.to_csv(dest_path+'/'+human_prot_file, index=False, header=True)
    
    df2 = pd.DataFrame({'fname':gen_file})
    df2.to_csv(dest_path+'/gen_file_list.csv', index=False, header=True)
  
print("Finished creation of files.\n")
