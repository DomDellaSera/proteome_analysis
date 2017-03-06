from table_generator import extract_headers,extract_Header_Info,gene_Name_Format_Correction

logger = logging.getLogger()

headers =extract_headers()
#headers
header_lists = extract_Header_Info(headers)
compare = zip(header_lists[1],headers)
print(compare)
fasta_head=[x[len('>sp|Q93142|FAR1_BRUMA'):] for x in headers]
product = [[x[1], " "*(70-len(x[1]))] for x in header_lists]

[product[x][0] in fasta_head[x] for x in range(0,len(product)) ]
#print(headers, header_lists,'done')

gene_Formatting = gene_Name_Format_Correction(header_lists)
logging.debug(gene_Formatting)
