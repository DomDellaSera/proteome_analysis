import pandas as pd
import numpy as np
from tabularformatter import disorder_statistics_table_generator
import logging
import re
import os



logger = logging.getLogger()
logging.disable(logging.DEBUG)

def iterative_generation(dir = "tests/b_malayi_reviewed/"):
    #This file is running a for loop to generate the table by calling disorder_statistics_table_generator 
    #for each row
    # Input: A directiory location with our stat files
    # Output: A raw table of the data from the statistics
    
    from getfilenames import stats_File_Names 
    file_Names = stats_File_Names()
    logging.debug(file_Names)
    problem_proteins = []
    data_Table = None
    
    for i in file_Names:
                    
        protein=i.rstrip()
        protein = dir+protein

        try:
            single_row = disorder_statistics_table_generator(protein)
        except:
            raise Exception
            problem_proteins.append(protein)
            exit()
         
        try:
            data_Table = data_Table.append(single_row)
        except:
            data_Table = single_row
        

    return(data_Table)


def extract_headers(uniprot_fasta = "fasta/brugia_malayi_reviewed.fasta"): 
                                                                          
# Purpose: To scan the fasta header and extract the protein name, gene name , etc
# Input: Fasta file | Output: Fasta header -'>sp|P27541|HSP70_BRUMA Heat sn OS=Brugia malayi GN=HSP70 PE=3 SV=1'
    
    with open(uniprot_fasta) as fasta_raw:  

        fasta_raw = fasta_raw.read()
        return(re.findall(">.*", fasta_raw))            

def extract_Header_Info(fasta_headers): #Input: Fasta Header; Output [filename, protein_name, gene name]
    extracted_Info = []
    for header in fasta_headers:
        filename=[]
        split_header = header.split(" ")
        filename.append(split_header.pop(0))
        filename = re.findall(">sp\|(.*)\|", header)[0]
        
        header_Concat = " ".join(split_header)
        
        protein_name = re.findall("(.*\s*.*)\sOS", header_Concat)[0]
        try:
            gene_name= re.findall(">sp.*GN=(.*) PE", header)[0]
        except:
            gene_name="NaN"
        extracted_Info.append([filename,protein_name,gene_name])
    return(extracted_Info)
    

class UniprotHeaderList: #This is for later;don't wanna break the code
    def __init__(self, file_name,protein,gene):
        self.file_name = file_name
        self.protein = protein
        self.gene = gene
        

        

def remove_Duplicate_Gene_Names(protein = str, gene = str):#THIS IS TO BE LOOPED
    #Gene names were either duplicates in the header name, or were not available

    protein_name = [x.split() for x in protein_name]
    protein_name = {protein_name}-{gene_name}
        
    return(protein_name)
    
    
def main_FileCleaning_Function(FPG = list):#Control flow for the aboe
    
    metadata = []
    

    for header in FPG:
        file_name,protein_name,gene_name = header
        
        if gene_name in protein_name and len(gene_name)!=0:
            
            protein_name = remove_Duplicate_Gene_Names(FPG)
        elif gene_name not in header[1]
            continue
        metadata.append([file_name +"/"+protein_name+"/"+gene_name])
    
    return(metadata)
        
        
            
            

def main_protein_table_writer(uniprot = 'fasta_tmp.fasta', output = 'b_malayi_reviewed_Meta.csv'):
    handle = open(output, "w")
    for i in uniprot[:]:
        if i.startswith(">") is True:
        
            protein_writer = csv.writer(handle, delimiter=",")
            row = protein_table_maker(i)
            separated_row = row.split("|")
            protein_writer.writerow(separated_row)
    
    handle.close()
    
def initialize_Protein_Disorder_Metrics(disorder_statistics = pd.DataFrame):
    with open('disorder_statistics.csv', 'w') as df:
        disorder_statistics.to_csv(df)
        return()

def dataFrameMerge(data_table = 'disorder_statistics.csv', metadata = 'b_malayi_reviewed_Meta.csv'):
    
    data_handle = open(data_table)
    meta_handle = open(metadata)
    
    unreferenced_data = pd.read_csv(data_handle)
    metaData = pd.read_csv(metadata)
    
    associative_Table = pd.merge(metaData,unreferenced_data, on = 'protein')
    with open('final_Data_Table.csv') as final_Table:
        associative_Table.to_csv(final_Table)
        
    data_handle.close()
    meta_handle.close()
    
    



if __name__ == '__main__':
    data_Table = iterative_generation()
    print({x for x in data_Table.values[55]})
    print(len(data_Table))
    data_Table.head()
    gen_ont = protein_Names_From_Fasta()
    print(gen_ont)
    main_protein_table_writer()
    
    
    