import sys

list_file = sys.argv[1]

#print list_file

with open (list_file) as list_file_handle:
    for line in list_file_handle:
       #print line
       line = line.rstrip()
       #print line
       cmd_str = "fastq-dump {c}\nfastqc {d}".format(c = line + ".sra",d= line + ".fastq")
       print cmd_str

