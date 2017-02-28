import pandas as pd
import numpy as np
from tabularformatter import disorder_statistics_table_generator
import logging
import re
import os
#import pdb
logger = logging.getLogger()
logging.disable(logging.DEBUG)

def iterative_generation(dir = "tests/b_malayi_reviewed/"):
    #This file is running a for loop to generate the table by calling disorder_statistics_table_generator for each row
    # Input: A directiory location with our stat files
    # Output: A raw table of the data from the statistics
    from getfilenames import stats_File_Names 
    file_Names = stats_File_Names()
    logging.debug(file_Names)
    problem_proteins = []
    data_Table = None
    for i in file_Names:
        #print(i)
                    
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
        
    logging.debug(problem_proteins)
    #logging.debug(data_Table)
    return(data_Table)

"""
def protein_Names_From_Fasta(uniprot_fasta = "fasta/brugia_malayi_reviewed.fasta"):
    # Purpose:
    #   To scan the fasta header and extract the protein name, gene name , etc
    # Input:
    #   Fasta file with headers in Uniprot format
    # Output:
    #   temporary fast file is written to tmp THIS MAY BE PUSHING SAND AROUND
    #   list containing the following:
    #        [filename, protein_name, gene name]
    # ##################################################################################
    
    
    with open(uniprot_fasta) as uniprot:
        uniprot = uniprot.readlines()
        counter = 0
        gene_ontology=None
        filename=None
        protein_name=None
        gene_name=None
        gene_ontology=[]
        
        #print(re.findall(">.*", uniprot))
        for i in uniprot[0:]: 
            
            if i.startswith(">") is True: #Finds the fasta header
                print(filename)
                #exit()
                filename =re.findall(">sp\|(.*)\|", i)[0] #regex: everything in between the |
                protein_name =re.findall(">sp.*L (.*) OS", i)[0]# regex: From L to the naming of the organism(i.e. the protein name)
                #
                try:#
                    gene_name= re.findall(">sp.*GN=(.*) PE", i)[0] #Try assign gene names to variable
                except:
                    gene_name=None #Not unifrom dataset
                gene_ontology.append([filename, protein_name, gene_name])
        #with open('fasta_tmp.fasta', 'w') as tmp:
         #   tmp.write(uniprot)
            
            
    return(gene_ontology)
    """

def extract_headers(uniprot_fasta = "fasta/brugia_malayi_reviewed.fasta"): 
    with open(uniprot_fasta) as fasta_raw:
        fasta_raw = fasta_raw.read()
        return(re.findall(">.*", fasta_raw))
    #pdb.set_trace()
    # Purpose:
        #This takes our original fasta from uniprot and tries to return a table with the filename, protein name, and gene name
    # THIS NEEDS HEAVY DEBUGGING -- I'M NOT SURE YET WHAT IT DOES EXACTLY IN RELATION TO THE PRIOR FUNCTION
def extract_Header_Info(fasta_headers):
    extracted_Info = []
    for header in fasta_headers:
        #print(header)
        filename=[]
        split_header = header.split(" ")
        filename.append(split_header.pop(0))
        filename = re.findall(">sp\|(.*)\|", header)[0]
        header_Concat = " ".join(split_header)
        
        protein_name = re.findall("(.*\s*.*)\sOS", header_Concat)[0]
        try:
            gene_name= re.findall(">sp.*GN=(.*) PE", header)[0]
        except:
            gene_name="NaGN"
        extracted_Info.append([filename,protein_name,gene_name])
    return(extracted_Info)
    
def gene_Name_Format_Correction(list_Header):
    gene_name_length=len(gene_name)
    if gene_name in protein_name and gene_name_length!=0:

        # Many of these fasta files have the gen name inside of them so here I'm searching for a gene name in the
        # protein name and extracting it if it exists in two places
        subtractor =len(gene_name)
        length =len(protein_name)
        #old_protein_name = protein_name
        #print(protein_name)
        protein_name = protein_name[0:length-subtractor]
    #print(gene_name)
                    
    return(filename+"|"+ protein_name+"|"+ gene_name)
    
    
def main_protein_table_writer(uniprot = 'fasta_tmp.fasta', output = 'brugia_malayi_reviewed_MainDataTable.csv'):
    handle = open(output, "a")
    for i in uniprot[:]:
        if i.startswith(">") is True:
        
            
            protein_writer = csv.writer(handle, delimiter=",")
           
            row = protein_table_maker(i)
            
            separated_row = row.split("|")
            
            protein_writer.writerow(separated_row)
    handle.close()



if __name__ == '__main__':
    data_Table = iterative_generation()
    print({x for x in data_Table.values[55]})
    print(len(data_Table))
    data_Table.head()
    gen_ont = protein_Names_From_Fasta()
    print(gen_ont)
    main_protein_table_writer()
    
    
    