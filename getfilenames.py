import os
import logging
logger = logging.getLogger()
logger.setLevel('DEBUG')
def stats_File_Names(file_dir = "tests/b_malayi_reviewed"):
    output_Files = {x for x in os.listdir(file_dir)}
    stat_files = {x for x in output_Files if x.endswith("fasta.stats")}
    return(stat_files)

#logging.debug(stats_File_Names())

