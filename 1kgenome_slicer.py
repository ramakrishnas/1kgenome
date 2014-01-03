#!/usr/bin/python

#Data slicer of 1000genome data
#needs Bed file as argument

# python 1kgenome_slicer.py ~/Work/1kGenome/20110521/BaitsCascade.bed

import glob
import os
import re
import sys
import time

print "start time= '%s'"%(time.ctime())
print "\n"

infile = open(sys.argv[1], 'r')

for line in infile:
	info = line.strip('\n').split('\t')
	chr = re.sub('chr', '', info[0])
	coord = chr+":"+str(info[1])+"-"+str(info[2])

#	os.system("tabix -h /Users/ramakrishnasompallae/Work/1kGenome/20110521/ALL.chr"+chr+".phase1_release_v3.20101123.snps_indels_svs.genotypes.vcf.gz "+coord+" | bgzip -c > Cascade."+re.sub(':', '_', coord)+".20110521.genotypes.vcf.gz")
	 

read_files = glob.glob("Cascade.*20110521.genotypes.vcf.gz")
print len(read_files)

os.system("cp "+read_files[0]+" Cascade_bait_1kgenome_orig.vcf.gz")
print read_files[0]
for i in range(1,len(read_files)):
	file = read_files[i].strip('\n')
	print file
#	print "vcf-concat Cascade_bait_1kgenome_orig.vcf.gz "+file+" | bgzip -c > Cascade_bait_1kgenome_temp.vcf.gz"
	os.system("vcf-concat Cascade_bait_1kgenome_orig.vcf.gz "+file+" | bgzip -c > Cascade_bait_1kgenome_temp.vcf.gz")
	os.system("cp Cascade_bait_1kgenome_temp.vcf.gz Cascade_bait_1kgenome_orig.vcf.gz")

os.system("vcf-sort Cascade_bait_1kgenome_orig.vcf.gz | bgzip -c > Cascade_bait_1kgenome.vcf.gz")
#os.remove("Cascade_bait_1kgenome_temp.vcf.gz") 
print "start time= '%s'"%(time.ctime())	

#	os.system("tabix -h /Users/ramakrishnasompallae/Work/1kGenome/20110521/ALL.chr"+chr+".phase1_release_v3.20101123.snps_indels_svs.genotypes.vcf.gz "+coord+" | bgzip -c > Cascade."+coord+"20110521.genotypes.vcf.gz")

#commands
#tabix -h http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20110521/ALL.chr17.phase1_release_v3.20101123.snps_indels_svs.genotypes.vcf.gz 17:1471000-1472000 | perl vcf-subset -c HG00098 | bgzip -c > HG00098.chr17_1451000-1472000.20110521.genotypes.vcf.gz
#tabix -h /Users/ramakrishnasompallae/Work/1kGenome/20110521/ALL.chr7.phase1_release_v3.20101123.snps_indels_svs.genotypes.vcf.gz 7:76825588-76826308 | bgzip -c > Cascade.7_76825588-76826308.20110521.genotypes.vcf.gz

#vcf-concat Cascade.10_101802136-101802376.20110521.genotypes.vcf.gz Cascade.10_101808513-101808633.20110521.genotypes.vcf.gz | bgzip -c > Cascade_bait_1kgenome.vcf.gz
git@github.com:ramakrishnas/1kgenome.git