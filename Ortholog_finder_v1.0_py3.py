# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 17:41:10 2021

@author: minkj
"""
#________________ option parse _______________________________
import sys 

args = sys.argv[1:]

option_dict={'-score':'50'}
for i in range(len(args)):
    if args[i].startswith("-"):
        try:
            option_dict[args[i]]=args[i+1]
        except:
            if args[0]=="-help":
                print ("""
_____________________________________________________________________________

Usage;

-help       show option list
-seq1       file name of seq1
-seq2       file name of seq2
-score      minimum score (default: 50)
_____________________________________________________________________________
""")
                quit()
                
                
                
import os
import csv

print ("Running blast 1..")
blast1=os.system("blastn -task dc-megablast -outfmt 5 -max_target_seqs 1 -query %s -subject %s -out temp1.xml" % (option_dict['-seq1'], option_dict['-seq2']))
print ("Running blast 2..")
blast2=os.system("blastn -task dc-megablast -outfmt 5 -max_target_seqs 1 -query %s -subject %s -out temp2.xml" % (option_dict['-seq2'], option_dict['-seq1']))

if blast1==0:
    if blast2==0:
        print ("Parsing blast 1..")
        parsing1=os.system("python 0_blast_parsing___xml_format_v2.6.py3.py -num_hsp 1 -lim_evalue 1 -lim_score %s -num_hit 1 -xml temp1.xml" % option_dict['-score'])
        print ("Parsing blast 2..")
        parsing2=os.system("python 0_blast_parsing___xml_format_v2.6.py3.py -num_hsp 1 -lim_evalue 1 -lim_score %s -num_hit 1 -xml temp2.xml -seq_parse 1" % option_dict['-score'])
        if parsing1==0:
            if parsing2==0:
                outcsv=csv.writer(open(option_dict['-seq1'][:25]+"___"+option_dict['-seq2'][:25]+"_ortho.csv",'w',newline=''))
                
                csv1=csv.reader(open("temp1.csv",'r'))
                csv2=csv.reader(open("temp2.csv",'r'))
                
                name_dic={}
                for row in csv1:
                    if row[0]=="Query_name":
                        outcsv.writerow(row)
                    else:
                        if row[4] != "-":
                            name_dic[row[0]]=row[4]
                for row in csv2:
                    if row[0]!="Query_name":
                        if row[4] !="-":
                            if row[4] in name_dic:
                                if row[0]==name_dic[row[4]]:
                                    outcsv.writerow(row)

print ("Completed!!")
                        
                        
                        
                        