
import pandas as pd
import numpy as np
import logging
import re


logger = logging.getLogger()





def disorder_statistics_table_generator(stats_file):
    with open(stats_file) as stats:
        stats = stats.read()
        stats = stats.rstrip()
        stats = stats.split("\n")
       
        
        stats = [x.split(":") for x in stats]
        count = -1
        
        
        
        #For each row replace the value in the second item with a stripped version
       
        #print(stats)
        error = None
        logging.debug(stats)
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
        logging.debug(stats)

        logging.debug(stats_file)
        logging.debug(re.findall('.*sp(.*).fasta.stats', stats_file))
        pro_name = re.findall('.*sp(.*).fasta.stats', stats_file)
        
        
        stat_table = pd.DataFrame({"protein" : pd.Series(pro_name, index=list(range(1)), dtype=object),
                                  "tot_aa"  : np.array(stats[0][1], dtype="int32"),
                                   "pct_disord" : np.array(stats[1][1], dtype="float32"),
                                   "thirty_disord" : np.array(stats[2][1], dtype="int32"),
                                   "fifty_disord" : np.array(stats[3][1], dtype="int32"),
                                   "seg_disord" : np.array(stats[4][1], dtype="int32")#,
                                   #"len_dist" : pd.Series(stats[5][1], dtype="float32")
                                   #This is actually really important info
                                       
                                  
                                })
        return(stat_table)
