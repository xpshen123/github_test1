import sys

list_file = sys.argv[1]
gtf_file = sys.argv[2]

#print list_file

with open (list_file) as list_file_handle:
    for line in list_file_handle:
       #print line
       line = line.rstrip()
       ele = line.split("\t")
       #print line
       cmd_str = "htseq-count -f bam -r pos {sample_real_name}.srt.bam {gtf_file} > {sample_real_name}_readcount.tab".format(sample_real_name = ele [1], gtf_file = gtf_file)
       print cmd_str
#htseq-count [options] alignment_file gff_file

