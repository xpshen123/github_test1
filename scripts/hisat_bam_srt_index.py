import sys

list_file = sys.argv[1]
ref = sys.argv[2]
fq_dir = sys.argv[3]

#print list_file

with open (list_file) as list_file_handle:
    for line in list_file_handle:
       #print line
       line = line.rstrip()
       ele = line.split("\t")
       #print line
       cmd_str = "hisat2  -x {ref}  -U {fq_dir}/{srr_acc}.fastq | samtools view -bS - | samtools sort - -o {sample_real_name}.srt.bam\nsamtools index {sample_real_name}.srt.bam".format(ref = ref, fq_dir = fq_dir, srr_acc = ele[0], sample_real_name = ele [1])
       print cmd_str
#hisat2 [options]* -x <ht2-idx> {-1 <m1> -2 <m2> | -U <r>} [-S <sam>]
