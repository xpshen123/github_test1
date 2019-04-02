import sys

list_file = sys.argv[1]

#print list_file

with open (list_file) as list_file_handle:
    for line in list_file_handle:
       #print line
       line = line.rstrip()
       #print line
       cmd_str = "wget ftp://ftp.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/{a}/{b}/{c}".format(a = line[0:6], b = line, c = line + ".sra")
       print cmd_str

