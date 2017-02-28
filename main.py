import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import statsmodels.api as sm
import statsmodels.formula.api as smf
from bokeh.plotting import figure
from bokeh.io import push_notebook,show,output_notebook
from ipywidgets import interact


with open("c_elegans_manual_plus_iso/") as uniprot:
    uniprot =uniprot.read()
    seqs = re.(".*", uniprot[1:5000])
    print(seqs)
    #print(uniprot[1:1200])
uni_subset =uniprot[1:10000]
def uniprot_fasta_tableconv(fasta_file):
    fasta_file = uni_subset.split(">")
    for i in fasta_file:
        tmp=i.split("|")
        tmp = [tmp[0]+tmp[1], tmp[2]]
        tmp = 
        #tmp = i.split("OS=")
        #tmp[1] = tmp[1].split("GN=")
        #tmp[]
    
    
    
    
        print(tmp)

        def protein_stats(stats_file):
    with open(stats_file) as stats:
        stats = stats.read()
        stats = stats.rstrip()
        stats = stats.split("\n")
       
        
        stats = [x.split(":") for x in stats]
        count = -1
        
        
        
        #For each row replace the value in the second item with a stripped version
       
        #print(stats)
        error = None
        
        for i in stats:
            count += 1
            value = stats[count][1]
            stats[count][1] = value.lstrip()
            if value == "":
                stats[count][1] = None
                continue
            try:
                float(i[1])
            except:
                
                stats[count][1] = stats[count][1].split(" ")
        #if error != None
        #    stats
        #[float(x[1]) for x in stats]
        #stats = [x[1].rstrip(" ") for x in stats]
        #stats = [x.rstrip(" ") for x in stats if " " in x]
        
        pro_name = stats_file[:-12]    
        
        """if stats[5][1]!= None:
            df_range = len(stats[5][1])
        else:
            df_range = 1"""
        stat_table = pd.DataFrame({"protein" : pd.Series(pro_name, index=list(range(1)), dtype=object),
                                  "tot_aa"  : np.array(stats[0][1], dtype="int32"),
                                   "pct_disord" : np.array(stats[1][1], dtype="float32"),
                                   "thirty_disord" : np.array(stats[2][1], dtype="int32"),
                                   "fifty_disord" : np.array(stats[3][1], dtype="int32"),
                                   "seg_disord" : np.array(stats[4][1], dtype="int32")#,
                                   #"len_dist" : pd.Series(stats[5][1], dtype="float32")
                                       
                                  
                                })
        #print(stats_file, "successfully put into table form")
        return(stat_table)
datf=None
#handle = open("c_elegans_manual_plus_iso/filenames.txt")
#[print(x) for x in handle]
#row_index = [x[:-13] for x in handle]
#row_index = pd.Index(row_index)
#print(row_index)
handle = open("filenames.txt")
counter = 0
for i in handle:
    #print(i)
                
    protein=i.rstrip()
    #protein += ".stats"
    #print(protein)
    #row_index = {x for x in protein}
    #print(row_index)
    try:
        single_row = protein_stats(protein)
    except:
        #print(protein, "failed")
        continue
    
    if datf is None:
        datf = single_row
    else:
        datf = datf.append(single_row)
    if counter == 20000: break
    counter += 1
        
#print(datf)
handle.close()