# V1.5 adjusted hit position.. center => average 


#________________ option parse _______________________________
import sys 

args = sys.argv[1:]

option_dict={'-match_line':'0.2','-identity':0.6, '-width':1200.0,'-height':40.0,'-space':180.0, '-scale_set':1,'-left_space':400,'-grey_scale':1,'-layer':2, '-mark_thick':8,'-out':'default','-num_graph':50,'-width_basis':1,'-right_space':0,'-hyperlink':"",
             '-add_q_repeat':"1", '-add_q_gene':"1", '-add_h_repeat':"1", '-add_h_gene':"1", '-LTR_MYA':"0", '-LTR_density':'1','-exon_depict':1,'-sliding_win':1000000,'-max_peak':'1',
             '-LTR_dom':'1','-sp_histo':'1','-matched_pani':'1','-vertical_graph':'1'}
for i in range(len(args)):
    if args[i].startswith("-"):
        try:
            option_dict[args[i]]=args[i+1]
        except:
            if args[0]=="-help":
                print("""
_____________________________________________________________________________

Usage;

-help           show option list
-csv            csv file name
-width          width of graph in pixel (default is 1200)
-scale_set      scale of graph (default is automatic)
-identity       input identity threshold (ex. 0.99, Default is 0.60)
-height         input hight of graph (default is 40)
-space          input space between each graph (default is 180)
-left_space     space of left side (default is 400)
-grey_scale     show matched region by grey scale according to the identity
                (1: color 2: grey scale, default is 1)
-layer          number of layer of hit. 0 ~ 5 (default is 2)
-mark_thick     thickness of matched region mark. 2~10 (default is 8)
-match_line     thickness of matched region line. (default is 1)
-num_graph      number of graph that will be drawn in a page (default is 50)
                (To convert bmp file do not exceed 50. Max is approx. 200.)
-width_basis    basis of width determination.
                (1: query sequence 2: both, default is 1)
-right_space    space of right side (option)
-hyperlink      enter the name of hyperlink db folder (option)
-add_q_repeat   add marks of repeat regions in query sequence (option)
                (csv file name of blast result)
-add_q_gene     add marks of genes in query sequence (option)
                (csv file name of blast result)
-add_h_repeat   add marks of repeat regions in hit sequence (option)
                (csv file name of blast result)
-add_h_gene     add marks of genes in hit sequence (option)
                (csv file name of blast result)
-exon_depict    draw exon on the gene (1: yes (default), 2: no)
-out            output file name of output that you want to (option)
-LTR_MYA        input file name of LTR insertion time DB (csv format)
-LTR_density    graph style..
                1: MYA (default) 
                2: LTR_denity (color chart ex; 255,255,255 or green etc..)
-sliding_win    size of sliding window for drawing density.
                1000000 (default)
-max_peak       max peak in sliding windows
                1: definate (default) 2: relative
-vertical_graph 1: no 2: yes (default is 1)
-LTR_dom        dic file for LTR domain position information
-sp_histo       dic file for speciation to analyze horizontal transfer
                used with -LTR_dom option!!!
-matched_pani   dic file for matched panicoid and cluster name writing

_____________________________________________________________________________
""")
                quit()
#        else:
#            print "There maybe an option error!"
#            quit()


grey_chart={'216': (96, 120, 96), '217': (97, 120, 97), '214': (94, 120, 94), '215': (95, 120, 95), '212': (92, 120, 92), '213': (93, 120, 93), '210': (90, 120, 90), '211': (91, 120, 91), '218': (98, 120, 98), '219': (99, 120, 99), '133': (13, 120, 13), '132': (12, 120, 12), '131': (11, 120, 11), '130': (10, 120, 10), '137': (17, 120, 17), '136': (16, 120, 16), '135': (15, 120, 15), '134': (14, 120, 14), '139': (19, 120, 19), '138': (18, 120, 18), '166': (46, 120, 46), '24': (0, 24, 0), '25': (0, 25, 0), '26': (0, 26, 0), '224': (104, 120, 104), '20': (0, 20, 0), '21': (0, 21, 0), '22': (0, 22, 0), '23': (0, 23, 0), '160': (40, 120, 40), '28': (0, 28, 0), '29': (0, 29, 0), '222': (102, 120, 102), '0': (0, 0, 0), '4': (0, 4, 0), '8': (0, 8, 0), '220': (100, 120, 100), '87': (0, 87, 0), '227': (107, 120, 107), '3': (0, 3, 0), '120': (0, 120, 0), '121': (1, 120, 1), '122': (2, 120, 2), '123': (3, 120, 3), '124': (4, 120, 4), '125': (5, 120, 5), '126': (6, 120, 6), '127': (7, 120, 7), '128': (8, 120, 8), '129': (9, 120, 9), '69': (0, 69, 0), '59': (0, 59, 0), '58': (0, 58, 0), '55': (0, 55, 0), '54': (0, 54, 0), '57': (0, 57, 0), '56': (0, 56, 0), '51': (0, 51, 0), '50': (0, 50, 0), '53': (0, 53, 0), '52': (0, 52, 0), '90': (0, 90, 0), '164': (44, 120, 44), '201': (81, 120, 81), '199': (79, 120, 79), '198': (78, 120, 78), '147': (27, 120, 27), '195': (75, 120, 75), '194': (74, 120, 74), '197': (77, 120, 77), '196': (76, 120, 76), '191': (71, 120, 71), '190': (70, 120, 70), '193': (73, 120, 73), '192': (72, 120, 72), '115': (0, 115, 0), '114': (0, 114, 0), '88': (0, 88, 0), '116': (0, 116, 0), '111': (0, 111, 0), '110': (0, 110, 0), '113': (0, 113, 0), '112': (0, 112, 0), '82': (0, 82, 0), '205': (85, 120, 85), '80': (0, 80, 0), '81': (0, 81, 0), '86': (0, 86, 0), '118': (0, 118, 0), '84': (0, 84, 0), '204': (84, 120, 84), '207': (87, 120, 87), '141': (21, 120, 21), '226': (106, 120, 106), '27': (0, 27, 0), '179': (59, 120, 59), '177': (57, 120, 57), '7': (0, 7, 0), '92': (0, 92, 0), '225': (105, 120, 105), '108': (0, 108, 0), '109': (0, 109, 0), '102': (0, 102, 0), '103': (0, 103, 0), '100': (0, 100, 0), '101': (0, 101, 0), '106': (0, 106, 0), '107': (0, 107, 0), '104': (0, 104, 0), '105': (0, 105, 0), '39': (0, 39, 0), '38': (0, 38, 0), '33': (0, 33, 0), '32': (0, 32, 0), '31': (0, 31, 0), '30': (0, 30, 0), '37': (0, 37, 0), '36': (0, 36, 0), '35': (0, 35, 0), '34': (0, 34, 0), '94': (0, 94, 0), '223': (103, 120, 103), '60': (0, 60, 0), '61': (0, 61, 0), '62': (0, 62, 0), '63': (0, 63, 0), '64': (0, 64, 0), '65': (0, 65, 0), '66': (0, 66, 0), '178': (58, 120, 58), '68': (0, 68, 0), '176': (56, 120, 56), '175': (55, 120, 55), '174': (54, 120, 54), '173': (53, 120, 53), '172': (52, 120, 52), '171': (51, 120, 51), '170': (50, 120, 50), '203': (83, 120, 83), '145': (25, 120, 25), '182': (62, 120, 62), '183': (63, 120, 63), '180': (60, 120, 60), '181': (61, 120, 61), '162': (42, 120, 42), '187': (67, 120, 67), '184': (64, 120, 64), '185': (65, 120, 65), '186': (66, 120, 66), '188': (68, 120, 68), '189': (69, 120, 69), '221': (101, 120, 101), '6': (0, 6, 0), '99': (0, 99, 0), '98': (0, 98, 0), '168': (48, 120, 48), '169': (49, 120, 49), '229': (109, 120, 109), '228': (108, 120, 108), '91': (0, 91, 0), '165': (45, 120, 45), '93': (0, 93, 0), '167': (47, 120, 47), '95': (0, 95, 0), '161': (41, 120, 41), '97': (0, 97, 0), '163': (43, 120, 43), '11': (0, 11, 0), '10': (0, 10, 0), '13': (0, 13, 0), '12': (0, 12, 0), '15': (0, 15, 0), '14': (0, 14, 0), '17': (0, 17, 0), '16': (0, 16, 0), '19': (0, 19, 0), '18': (0, 18, 0), '117': (0, 117, 0), '89': (0, 89, 0), '151': (31, 120, 31), '150': (30, 120, 30), '153': (33, 120, 33), '152': (32, 120, 32), '155': (35, 120, 35), '154': (34, 120, 34), '157': (37, 120, 37), '156': (36, 120, 36), '159': (39, 120, 39), '158': (38, 120, 38), '238': (118, 120, 118), '239': (119, 120, 119), '240':(120,120,120), '83': (0, 83, 0), '234': (114, 120, 114), '235': (115, 120, 115), '236': (116, 120, 116), '237': (117, 120, 117), '230': (110, 120, 110), '231': (111, 120, 111), '232': (112, 120, 112), '233': (113, 120, 113), '48': (0, 48, 0), '49': (0, 49, 0), '46': (0, 46, 0), '119': (0, 119, 0), '44': (0, 44, 0), '45': (0, 45, 0), '42': (0, 42, 0), '43': (0, 43, 0), '40': (0, 40, 0), '41': (0, 41, 0), '1': (0, 1, 0), '5': (0, 5, 0), '9': (0, 9, 0), '85': (0, 85, 0), '146': (26, 120, 26), '200': (80, 120, 80), '144': (24, 120, 24), '202': (82, 120, 82), '142': (22, 120, 22), '143': (23, 120, 23), '140': (20, 120, 20), '206': (86, 120, 86), '209': (89, 120, 89), '208': (88, 120, 88), '148': (28, 120, 28), '149': (29, 120, 29), '77': (0, 77, 0), '76': (0, 76, 0), '75': (0, 75, 0), '74': (0, 74, 0), '73': (0, 73, 0), '72': (0, 72, 0), '71': (0, 71, 0), '70': (0, 70, 0), '96': (0, 96, 0), '79': (0, 79, 0), '78': (0, 78, 0), '2': (0, 2, 0), '47': (0, 47, 0), '67': (0, 67, 0)}

import csv
import shelve
#__________csv data parsing__data structure={query_name:[Query_length, {Hit_description:[[hit_length, Query_from, Query_to, Hit_from, Hit_to, identity], [] ]}]}
def csv_position(file_name):
    import csv
    csv_file=csv.reader(open(file_name,'r'))
    csv_dic={}
    print("\n\nData processing..\n\n")
    
    for csv_line in csv_file:
    #    csv_line=csv_file.readline().strip().split(',')
    #    if csv_line[0]=="":
    #        print "Position data conversion to dic format completed.!!"
    #        break
        
        if csv_line[0]=="Query_name":  #Just jump the first line
            pass
    
        elif csv_line[10]=="-": # to avoid fault of '-'
            csv_line[10]=0
            
        elif float(csv_line[10])>=float(option_dict['-identity']): #Identity check
    
            if '_continued' in csv_line[0]: #name trimming
                Query_name=csv_line[0].split('_continued')[0]
            elif '_continued' not in csv_line[0]:
                Query_name=csv_line[0]
    
            if Query_name not in csv_dic: #First query writing
                if '_continued' in csv_line[4]:  ##To eliminate _continued in name-start
                    hit_name=csv_line[4].split('_continued')[0]
                    csv_dic[Query_name]=[float(csv_line[1]),{hit_name:[[float(csv_line[5]), float(csv_line[2]), float(csv_line[3]), float(csv_line[6]),float(csv_line[7]),float(csv_line[10])]]}]
                elif '_continued' not in csv_line[4]:
                    hit_name=csv_line[4] ##To eliminate _continued in name_start-end
                    csv_dic[Query_name]=[float(csv_line[1]),{hit_name:[[float(csv_line[5]), float(csv_line[2]), float(csv_line[3]), float(csv_line[6]),float(csv_line[7]),float(csv_line[10])]]}]
                    
                
    
            elif Query_name in csv_dic: #Continued query writing
    
                if '_continued' in csv_line[4]: ##To eliminate _continued in name-start
                    hit_name=csv_line[4].split('_continued')[0]
                elif '_continued' not in csv_line[4]:
                    hit_name=csv_line[4] ##To eliminate _continued in name_start-end
                
                if hit_name not in csv_dic[Query_name][1]:
                    csv_dic[Query_name][1][hit_name]=[[float(csv_line[5]), float(csv_line[2]), float(csv_line[3]), float(csv_line[6]),float(csv_line[7]),float(csv_line[10])]]
                elif hit_name in csv_dic[Query_name][1]: #Overlapped hit writing
                    csv_dic[Query_name][1][hit_name].append([float(csv_line[5]), float(csv_line[2]), float(csv_line[3]), float(csv_line[6]),float(csv_line[7]),float(csv_line[10])])
    
    return csv_dic

#____________csv position parsing-start_______________________________________
csv_dic=csv_position(option_dict['-csv'])
print("\n\nMain position dic of matched region generated.!!")
if option_dict['-add_q_repeat'] != "1":
    q_repeat_dic=csv_position(option_dict['-add_q_repeat'])
    print("\n\nQuery-repeat position dic of matched region generated.!!")
if option_dict['-add_q_gene'] != "1":
    q_gene_dic=csv_position(option_dict['-add_q_gene'])
    print("\n\nQuery-gene position dic of matched region generated.!!")

    
    #___definite max gene-density calculation_start__________
    if option_dict['-max_peak']=="1":
        if option_dict['-LTR_MYA'] !="0":
            keys=list(csv_dic.keys())
                        
            gene_position_left_pre=[]
                
            x=0
            
            defi_max_gene_pre=[]
            
            for key in keys:
                if key in q_gene_dic:
                    for h_key, h_position in list(q_gene_dic[key][1].items()):
                        h_list=[]
                        for h in h_position:
                            h_list.append(h[1])
                        if option_dict['-LTR_MYA'] !="0":
                            gene_position_left_pre.append(min(h_list)) ##for gene-densitiy calculation
       
                    if option_dict['-LTR_MYA'] !="0": ##for gene-densitiy calculation
                        gene_position_left_pre.sort()
        
                    
        
                max_position=int(csv_dic[key][0])#(max(gene_position_left))
                        
                num_slide_windows=int(max_position/int(option_dict['-sliding_win'])) + 1
        
                ####___parsing gene position according to each step_start____
        
                stepwise_dic_gene={}
                windows=0
                for loop in range(num_slide_windows):
                    stepwise_dic_gene[loop]=[]
                
                    
                    for position_q in gene_position_left_pre:
                        if float(position_q) >= windows and float(position_q) < windows +int(option_dict['-sliding_win']):
                            stepwise_dic_gene[loop].append(position_q)
                            gene_position_left_pre.remove(position_q)
                    windows=windows+int(option_dict['-sliding_win'])
                   
                            
                ####___parsing gene position according to each step_end____
        
        
        
        
                ####___calculate position value for gene density according to each step_start____
        
                gene_density_for_max=[]

                for loop2 in range(num_slide_windows):
                    gene_density_for_max.append(len(stepwise_dic_gene[loop2]))
                    
                
                defi_max_gene_pre.append(max(gene_density_for_max))
        
            defi_max_gene=max(defi_max_gene_pre)
            #___definite max gene-density calculation_end__________
    
        
if option_dict['-add_h_repeat'] != "1":
    h_repeat_dic=csv_position(option_dict['-add_h_repeat'])
    print("\n\nHit-repeat position dic of matched region generated.!!")
if option_dict['-add_h_gene'] != "1":
    h_gene_dic=csv_position(option_dict['-add_h_gene'])
    print("\n\nHit-gene position dic of matched region generated.!!")
#____________csv position parsing-end_______________________________________    


#__________sub_list_generation_for separation of file_start_____________


    ##__for horizontal te transfer analysis_start__
if option_dict['-matched_pani']!='1':
    key_list_origin_pre=list(csv_dic.keys())
    key_list_origin_pre.sort()
    key_list_origin=[]##########
    ###############################################
    pani_name_dic=shelve.open(option_dict['-matched_pani'])#####################
    for key_pre in key_list_origin_pre:
        
        if key_pre in pani_name_dic:
            pani_name_list_init=pani_name_dic[key_pre]######################################
            temp_list_for_max=[]
            for pani_name_cont in pani_name_list_init:
                temp_list_for_max.append([pani_name_cont.split('_')[-1],pani_name_cont])
            temp_check=max(temp_list_for_max)[1]
            #print pani_name_list_init
        else:
            pani_name_list_init=[]
        #temp_check=[]###############################################################
        
        #for temp_cont in pani_name_list_init:#######################################
        #    temp_check.append(temp_cont.split('_')[0])##############################
        if option_dict['-csv'].split('_')[1] in temp_check:#########################
            key_list_origin.append(key_pre)
    ##__for horizontal te transfer analysis_end__
    
    
else:
    key_list_origin=list(csv_dic.keys())

key_list_origin.sort()

num_query=int(option_dict['-num_graph'])

key_list_separate=[]
separate_num=int(len(key_list_origin)/num_query)
            


for num in range(separate_num):
    sub_list=key_list_origin[num*num_query:(num+1)*num_query]
    key_list_separate.append(sub_list)
sub_list=key_list_origin[separate_num*num_query:]
key_list_separate.append(sub_list)

key_list_separate.sort()



#__________current path information for hyperlink_start________
import os
if option_dict['-hyperlink']!="":
    #path=os.getcwd()+"\\"+option_dict['-hyperlink']
    path=option_dict['-hyperlink']
#__________current path information for hyperlink_end________



###_______LTR MYA data parsing_start_____________________

if option_dict['-LTR_MYA'] !="0":
    option_dict['-layer']="0"

            

    ###  data structure;   MYA_db={sequence_ID:{position:[k2p, mya],...},...}

           
    LTR_csv_file=csv.reader(open(option_dict['-LTR_MYA'],'r'))

    MYA_db={}
    MYA_list=[]
    K2P_list=[]
    position_list=[]
    
    for csv_line in LTR_csv_file:
        if "Sequence ID" not in csv_line[0]:
            sequence_name_pre=csv_line[0].split("__")[0][:-2]
            if ">" == sequence_name_pre[0]:
                sequence_name=sequence_name_pre[1:]
            else:
                sequence_name=sequence_name_pre
            
            position_pre=csv_line[0].split("__")[1]
        
            position=position_pre.split("_")[0]

            K2P=csv_line[1]
            MYA=csv_line[2]

            if sequence_name not in MYA_db:
                MYA_db[sequence_name]={position:[K2P, MYA]}

                MYA_list.append(float(MYA))
                K2P_list.append(float(K2P))
                position_list.append(float(position))
            elif sequence_name in MYA_db:
                MYA_db[sequence_name][position]=[K2P, MYA]

                MYA_list.append(float(MYA))
                K2P_list.append(float(K2P))
                position_list.append(float(position))
                
                
    #____set definate MAX peak value-start____________
    if option_dict['-LTR_MYA']!='0':
        if option_dict['-max_peak']=="1":
            
            defi_max_pre=[]
            keys=list(csv_dic.keys())
            
            
            
            for key in keys:
                max_position=float(csv_dic[key][0])
                num_slide_windows_pre=int(max_position/int(option_dict['-sliding_win'])) + 1
                
                windows=0
                stepwise_dic_pre={}
                for loop in range(num_slide_windows_pre):
                    stepwise_dic_pre[loop]=[]
                    
                    if key in MYA_db:
                        for position2 in MYA_db[key]:
                            if int(position2) >= windows and int(position2) < windows +int(option_dict['-sliding_win']):
                                stepwise_dic_pre[loop].append(float(MYA_db[key][position2][1]))
                        windows=windows+int(option_dict['-sliding_win'])
                    else:
                        print(key," is not in the MYA_db..\n")
            
                if option_dict['-LTR_density']!='1':
                    LTR_density_pre=[]
                    for loop3 in range(num_slide_windows_pre):
                        LTR_density_pre.append(len(stepwise_dic_pre[loop3]))
                    
                    max_LTR_density_pre=max(LTR_density_pre)
                    defi_max_pre.append(max_LTR_density_pre)
            defi_max=max(defi_max_pre) # definate maximum number of sliding window
    #____set definate MAX peak value-end____________    
    
    
        
    print("\n\nLTR insertion time parsing completed.")
    ###_______LTR MYA data parsing_end_____________________


#____Preset for vertical graph drawing_start__
percentage_line="false"
if option_dict['-vertical_graph']=='2':
    option_dict['-layer']='0'
    percentage_line="true"
    option_dict['-grey_scale']='2'
if option_dict['-sp_histo']!='1':
    option_dict['-left_space']=430
    option_dict['-width']=600
    #option_dict['-left_space']=600
#____Preset for vertical graph drawing_end__

#__________sub_list_generation_for separation of file_end_____________

serial=0
for key_list in key_list_separate:
    if key_list!=[]:
        serial=serial+1
    
        #__________to determine graph width-start_______
        length_list=[]
        length_list_query=[]
        for key in key_list:
            
            length_list.append(csv_dic[key][0])
            length_list_query.append(csv_dic[key][0])
            
            for key2, item2 in list(csv_dic[key][1].items()):
                for item in item2:
                    length_list.append(item[0])
        


        print("\n\nGraphic processing..("+str(serial)+"/"+str(separate_num+1)+")")
        ##___________largest width select___________
        if option_dict['-scale_set']==1:
            if int(option_dict['-width_basis'])==1:
                option_dict['-scale']=int(float(max(length_list_query)+100)/float(option_dict['-width']))
            elif int(option_dict['-width_basis'])==2:
                option_dict['-scale']=int(float(max(length_list)+100)/float(option_dict['-width']))
        else:
            option_dict['-scale']=int(option_dict['-scale_set'])
            
        print("graph width: "+str(int(option_dict['-width'])))
        print("num query per file: "+str(int(option_dict['-num_graph'])))
        print("max seq length: "+str(int(max(length_list_query)))+" bp")
    
    
        if option_dict['-scale']<1:
            option_dict['-scale']=1
        print('scale: 1/'+str(int(option_dict['-scale'])))
    
        if int(option_dict['-width_basis'])==1:
            width=(float(max(length_list_query))+100)/float(option_dict['-scale'])+200 + float(option_dict['-left_space'])+float(option_dict['-right_space'])
        elif int(option_dict['-width_basis'])==2:
            width=(float(max(length_list))+100)/float(option_dict['-scale'])+200 + float(option_dict['-left_space'])+float(option_dict['-right_space'])
            #option_dict['-left_space']=400@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    
        if width >= 2000:
            print("Larger than graph width here!!", width, option_dict['-scale'], max(length_list))
            
        height=len(length_list_query)* int(option_dict['-space'])+300
    
    
        #__________to determine graph width-end_______
    
        #__________file name set_______
        pic_file_name=option_dict['-out']
        if option_dict['-out']=='default':
            pic_file_name=option_dict['-csv'][:-4]+"-"+str(serial)+".svg"
    
    
    
        import svgwrite
        if option_dict['-sp_histo']!='1':
            if option_dict['-matched_pani']=='1':
                width=1500
                dwg=svgwrite.Drawing(pic_file_name,(int(width),height),profile='tiny',debug=True)
            else:
                width=2000
                dwg=svgwrite.Drawing(pic_file_name,(int(width),height),profile='tiny',debug=True)
            
        else:
            dwg=svgwrite.Drawing(pic_file_name,(int(width),height),profile='tiny',debug=True)
        space=-int(option_dict['-space'])+20
    
        #______________________________color_chart_grey_scale-start_______________________________________________
    
    
        k=0
        if int(option_dict['-grey_scale'])==2:
            dwg.add(dwg.text('Similarity color',insert=(int(option_dict['-left_space']),20),fill='purple'))
            dwg.add(dwg.text('100%',insert=(int(option_dict['-left_space'])-15,45),fill='purple'))
            dwg.add(dwg.text(str(int(float(option_dict['-identity'])*100))+"%",insert=(int(option_dict['-left_space'])+85,45),fill='purple'))
            for num in range(110):
                color=grey_chart[str(num*2+1)]
                
                
                dwg.add(dwg.line((int(option_dict['-left_space'])+k,50),(int(option_dict['-left_space'])+k,60), stroke=svgwrite.rgb(int(color[0]),int(color[1]),int(color[2]),'%'), stroke_width=1))
    
                k=k+1
    #            num=int(num*(240/40))
    #            grey_chart[str(num+1)]=(20+num*1.5,20+num*1.5,20+num*1.5)
        
        
        #______________________________color_chart_grey_scale-end______________________________________________
        
        #______________________________length_scale_start______________________________________________
        
        dwg.add(dwg.text('Scale',insert=(int(option_dict['-left_space'])-5,95),fill='purple'))
        dwg.add(dwg.text('0',insert=(int(option_dict['-left_space'])-5,115),fill='purple'))
        
        digit=int(max(length_list_query)/10.0)
        length=len(str(digit))-1
        first_num=str(digit)[0]
        scale_num=int(first_num)*(10**length)
        
        num_zero=str(scale_num).count('0')
        if num_zero >= 9:
            largest_scale=str(scale_num)[:-9]+" Gbp"
        elif num_zero >= 6:
            largest_scale=str(scale_num)[:-6]+" Mbp"
        elif num_zero >= 3:
            largest_scale=str(scale_num)[:-3]+" Kbp"
        elif num_zero < 3:
            largest_scale=str(scale_num)+" bp"
        
        dwg.add(dwg.text(largest_scale,
            insert=(
                int(option_dict['-left_space'])-20+int(float(scale_num)/float(option_dict['-scale'])),115),
            fill='purple'))
        dwg.add(dwg.line(
            (int(option_dict['-left_space']),125),
            (int(option_dict['-left_space'])+int(float(scale_num)/float(option_dict['-scale'])),125),
            stroke='orange', stroke_width=6))
        
        #______________________________length_scale_end______________________________________________
        
        
        
        #==============================Graph_drawing_Query==============================
        
        for key in key_list:  #query individual
                
            if percentage_line== 'false':
                space=space+int(option_dict['-space'])
                dwg.add(dwg.text(key,insert=(float(option_dict['-left_space'])-5,150-10*int(option_dict['-layer'])+space+int(option_dict['-layer'])*10+(180-int(option_dict['-space']))*0.6),fill='purple'))
                k=0
                m=0
                n=0
            
                dwg.add(dwg.line((int(option_dict['-left_space']),200+space+int(option_dict['-layer'])*10),
                                 (int(float(option_dict['-left_space'])+csv_dic[key][0]/float(option_dict['-scale'])),200+space+int(option_dict['-layer'])*10),
                                 stroke=svgwrite.rgb(200,0,0,'%'), stroke_width=12)) # Query line
            
            
    #+++++++++++++++++++++++++++++++++++++++++++++++++horizontal TE transfer__start+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++        
            #_________Main line for Horizontal TE transfer analysis_start_
            elif percentage_line== 'true':
                
                space=space+int(option_dict['-space'])
                dwg.add(dwg.text(key,insert=(float(option_dict['-left_space'])-5,130-5-10*int(option_dict['-layer'])+space+int(option_dict['-layer'])*10+(180-int(option_dict['-space']))*0.6),fill='purple', font_size=12))
                k=0
                m=0
                n=0
            
                dwg.add(dwg.line((int(option_dict['-left_space']),240+space+int(option_dict['-layer'])*10),
                                 (int(float(option_dict['-left_space'])+csv_dic[key][0]/float(option_dict['-scale'])),240+space+int(option_dict['-layer'])*10),
                                 stroke=svgwrite.rgb(80,00,0,'%'), stroke_width=12)) # Query line
            #_________Main line for Horizontal TE transfer analysis_end_    
                
                
                
                
                #_______Draw percentage line for vertical graph and Horizontal TE transfer analysis_start____
                dwg.add(dwg.line((int(option_dict['-left_space']),225-6+space+int(option_dict['-layer'])*10),
                                 (int(float(option_dict['-left_space'])+csv_dic[key][0]/float(option_dict['-scale'])),225-6+space+int(option_dict['-layer'])*10),
                                 stroke='grey', stroke_width=0.2,
                                 stroke_dasharray='2')) # Percentage line_75%
                dwg.add(dwg.text('75%',insert=(int(option_dict['-left_space'])-25,225-3+space+int(option_dict['-layer'])*10),fill='purple', font_size=10))
                
                dwg.add(dwg.line((int(option_dict['-left_space']),210-6+space+int(option_dict['-layer'])*10),
                                 (int(float(option_dict['-left_space'])+csv_dic[key][0]/float(option_dict['-scale'])),210-6+space+int(option_dict['-layer'])*10),
                                 stroke='black', stroke_width=0.2,
                                 stroke_dasharray='3')) # Percentage line_80%
                dwg.add(dwg.text('80%',insert=(int(option_dict['-left_space'])-25,210-3+space+int(option_dict['-layer'])*10),fill='purple', font_size=10))
                
                dwg.add(dwg.line((int(option_dict['-left_space']),195-6+space+int(option_dict['-layer'])*10),
                                 (int(float(option_dict['-left_space'])+csv_dic[key][0]/float(option_dict['-scale'])),195-6+space+int(option_dict['-layer'])*10),
                                 stroke='grey', stroke_width=0.2,
                                 stroke_dasharray='2')) # Percentage line_85
                dwg.add(dwg.text('85%',insert=(int(option_dict['-left_space'])-25,195-3+space+int(option_dict['-layer'])*10),fill='purple', font_size=10))
                
                dwg.add(dwg.line((int(option_dict['-left_space']),180-6+space+int(option_dict['-layer'])*10),
                                 (int(float(option_dict['-left_space'])+csv_dic[key][0]/float(option_dict['-scale'])),180-6+space+int(option_dict['-layer'])*10),
                                 stroke='black', stroke_width=0.2,
                                 stroke_dasharray='3')) # Percentage line_90%
                dwg.add(dwg.text('90%',insert=(int(option_dict['-left_space'])-25,180-3+space+int(option_dict['-layer'])*10),fill='purple', font_size=10))
                
                dwg.add(dwg.line((int(option_dict['-left_space']),165-6+space+int(option_dict['-layer'])*10),
                                 (int(float(option_dict['-left_space'])+csv_dic[key][0]/float(option_dict['-scale'])),165-6+space+int(option_dict['-layer'])*10),
                                 stroke='grey', stroke_width=0.2,
                                 stroke_dasharray='2')) # Percentage line_95
                dwg.add(dwg.text('95%',insert=(int(option_dict['-left_space'])-25,165-3+space+int(option_dict['-layer'])*10),fill='purple', font_size=10))
                
                dwg.add(dwg.line((int(option_dict['-left_space']),150-6+space+int(option_dict['-layer'])*10),
                                 (int(float(option_dict['-left_space'])+csv_dic[key][0]/float(option_dict['-scale'])),150-6+space+int(option_dict['-layer'])*10),
                                 stroke='black', stroke_width=0.2,
                                 stroke_dasharray='3')) # Percentage line_100%
                dwg.add(dwg.text('100%',insert=(int(option_dict['-left_space'])-30,150-3+space+int(option_dict['-layer'])*10),fill='purple', font_size=10))


                dwg.add(dwg.line((int(option_dict['-left_space']),192-6+space+int(option_dict['-layer'])*10),
                                 (int(float(option_dict['-left_space'])+csv_dic[key][0]/float(option_dict['-scale'])),192-6+space+int(option_dict['-layer'])*10),
                                 stroke='blue', stroke_width=0.8,
                                 stroke_dasharray='2')) # Percentage line_speciation___red!!!!
                #dwg.add(dwg.text('86%',insert=(int(option_dict['-left_space'])-25,195-3+space+int(option_dict['-layer'])*10),fill='purple', font_size=10))


                dwg.add(dwg.line((int(option_dict['-left_space']),171-6+space+int(option_dict['-layer'])*10),
                                 (int(float(option_dict['-left_space'])+csv_dic[key][0]/float(option_dict['-scale'])),171-6+space+int(option_dict['-layer'])*10),
                                 stroke='red', stroke_width=0.8,
                                 stroke_dasharray='2')) # Percentage line_speciation___red!!!!
                #dwg.add(dwg.text('85%',insert=(int(option_dict['-left_space'])-25,195-3+space+int(option_dict['-layer'])*10),fill='purple', font_size=10))

                
                #_______Draw percentage line for vertical_graph and Horizontal TE transfer analysis_end____
    
                
                #_______Depict matched panicoid name and cluster on right side_start___
                
                if option_dict['-matched_pani']!='1':
                    pani_name_dic=shelve.open(option_dict['-matched_pani'])
                    
                    if key in pani_name_dic:
                        
                        pani_name_list_pre=pani_name_dic[key]
                        pani_name_list=[]
                        for pani_name2 in pani_name_list_pre:
                            #print option_dict['-csv']
                            if pani_name2.split('_')[0] not in option_dict['-csv']:
                                pani_name_list.append([pani_name2,"grey"])
                                
                            elif pani_name2.split('_')[0] in option_dict['-csv']:
                                pani_name_list.append([pani_name2,"red"])
                                #pani_name_list.append(pani_name2)
                        #pani_name_list.sort()
                        pani_name_list.sort()
                        p=0
                        pani_name_posi_x=0
                        for pani_name in pani_name_list:
                            
                            pani_name_posi_y=p%10
                            if pani_name_posi_y==0:
                                pani_name_posi_x=pani_name_posi_x+1
                            p=p+1
                            dwg.add(dwg.text(pani_name[0],insert=(1000+80*pani_name_posi_x, 120+space+int(option_dict['-layer'])*10+15*pani_name_posi_y), fill=pani_name[1], font_size=10))
                #_______Depict matched panicoid name and cluster on right side_end___
                            
                
                
                
                
                
                
                
                #_______Draw species histogram to analyze horizon TE transfer_start__
                if option_dict['-sp_histo']!='1':
                    sp_freq_tbl=shelve.open(option_dict['-sp_histo'])
                    species_name=key.split('___')[0]##############################################This should be corrected in every case!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    panicoid_name=option_dict['-csv'].split('_')[1]###############################This should be corrected in every case!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    
                    
                    #print species_name
                    #print sp_freq_tbl.keys()
                    if species_name+'.csv' not in sp_freq_tbl:
                        
                        print("There is no histogram info for %s..!!" % (species_name+'.csv'))#sp_freq_tbl[species_name+'.csv']
    
                
                    
                    #___Draw species histogram farme-start_____________
                    
                    comm_x=130
                    comm_y=150+space+int(option_dict['-layer'])*10
                    
                    sp_x_width=250
                    sp_y_hight=80
                    
                    dwg.add(dwg.rect(
                        insert=(comm_x,comm_y),
                        size=(sp_x_width,sp_y_hight),
                        fill='none',
                        stroke_width=0.5,
                        stroke='grey'
                    ))
                    #___Draw species histogram farme-end_____________
                        
    
    
                    #___draw tick marks and numbers on species histogram_start_____________
                    num=65
                    for k in range(8):
                        x_add_pre=sp_x_width/7.0
                        x_add_1=k*x_add_pre
                        dwg.add(dwg.line(
                            start=(comm_x+x_add_1, comm_y+sp_y_hight),
                            end= (comm_x+x_add_1, comm_y+sp_y_hight+2),
                            stroke = "black",
                            stroke_width=0.5
                        ))
                        if num != 100:
                            dwg.add(dwg.text(
                                "%s" % str(num),
                                insert=(comm_x+  x_add_1-5, comm_y+sp_y_hight+15),
                                fill='purple',
                                font_size=11
                                ))
                        num=num+5
                    dwg.add(dwg.text(
                        "100 (%)",
                        insert=(comm_x+x_add_1-8, comm_y+sp_y_hight+15),
                        fill='purple',
                        font_size=11
                        ))
                    #___draw tick marks and numbers on species histogram_end_____________
                    
                    
                    #print sp_freq_tbl[species_name+'.csv']
                    #print species_name+'.csv'
                    if species_name+'.csv' in sp_freq_tbl:
                        if sp_freq_tbl[species_name+'.csv']!={}:
                            if panicoid_name in sp_freq_tbl[species_name+'.csv']:
                                freq_dic_sp=sp_freq_tbl[species_name+'.csv'][panicoid_name]
    
                                #_____total number of histogram data_start__
                                total_num=0
                                total_sp_sum=0
                                for key_num,value_num in list(freq_dic_sp.items()):
                                    total_num=total_num+int(value_num)
                                    total_sp_sum=total_sp_sum+int(key_num)*int(value_num)
                                    
                                
                                dwg.add(dwg.text(
                                    "Total:",
                                    insert=(comm_x+5,comm_y+12),
                                    fill='black',
                                    font_size=11))
                                
                                dwg.add(dwg.text(
                                    str(total_num),
                                    insert=(comm_x+33,comm_y+12),
                                    fill='green',
                                    font_size=11))
                                
                                
                                #_____total number of histogram data_end__
                                
                                sp_freq_for_gph=[]
                                
                                max_pre=[]
                                peak_sp=[] # to draw speciation vertical line
                                
                                #____parse information for polygon_start_____________
                                for k in range(36):
                                    tag=65+k
                                        
                                    if str(tag) in freq_dic_sp:
                                        sp_freq_for_gph.append([int(tag),int(freq_dic_sp[str(tag)])])
                                        max_pre.append(freq_dic_sp[str(tag)])
                                        peak_sp.append([freq_dic_sp[str(tag)],str(tag)])
                                    else:
                                        sp_freq_for_gph.append([int(tag),'0'])
                                #sp_freq_for_gph.append([int(100),'0'])
                                #____parse information for polygon_end_____________
                                
                                
                                max_value=max(max_pre)
                                
                                peak_sp_value=max(peak_sp)
                                
                           
                                sp_freq_for_gph.sort()
                               
                                sp_posi=[]
                                
                                #___calculation position formation for polygon_start___
                                for k in range(36):
                                    x_position=comm_x+(sp_x_width/35.0)*k
                                    #y_cl_position=50+y_add+float(option_dict['-height'])-float(cl_freq_for_gph[k][1])*(float(option_dict['-height'])/float(max_value))
                                    y_sp_position=comm_y+sp_y_hight-float(sp_freq_for_gph[k][1])*(float(sp_y_hight-10)/float(max_value))
                                    #print y_sp_position################################################################################################
                                    #cl_posi.append((x_position,y_cl_position))
                                    sp_posi.append((x_position,y_sp_position))
                                sp_posi.append((x_position,comm_y+sp_y_hight))
                                #___calculation position formation for polygon_end___
                                
                                
                                #___draw polygon_start______________
                                dwg.add(dwg.polygon(
                                    points=[
                                        position for position in sp_posi
                                        ],
                                    stroke='none',
                                    fill='grey'
                                )) 
                                #___draw polygon_end______________
                                
                                
                                
                                #___draw speciation and cluster div line________
                               
                                
                                dwg.add(dwg.line(
                                    start=(comm_x+(sp_x_width/35.0)*(float(peak_sp_value[1])-65),comm_y),
                                    end=(comm_x+(sp_x_width/35.0)*(float(peak_sp_value[1])-65),comm_y+sp_y_hight),
                                         stroke='red',
                                         stroke_width=1,
                                         stroke_dasharray='4,2'
                                ))
                                #____________________________________________
                                
                                #___add peak value (speciation point) ____
                                dwg.add(dwg.text(str(peak_sp_value[1]),
                                    insert=(comm_x+(sp_x_width/35.0)*(float(peak_sp_value[1])-65)-5,comm_y-7),
                                    fill='red',
                                    font_size=11
                                    ))
                                #__________________________________________
                                
                                #__add peak point line on identity graph_start_
                                dwg.add(dwg.line((int(option_dict['-left_space']),240-6-(int(peak_sp_value[1])-70)*3+space+int(option_dict['-layer'])*10),
                                     (int(float(option_dict['-left_space'])+csv_dic[key][0]/float(option_dict['-scale'])),240-6-(int(peak_sp_value[1])-70)*3+space+int(option_dict['-layer'])*10),
                                     stroke='red', stroke_width=1,
                                     stroke_dasharray='4')) # Percentage line_100%
                                #__add peak point line on identity graph_end_
                                
                                
                                #__add average sp_identity line on identity graph_start_
                                #sp_average=float(total_sp_sum)/float(total_num)
                                #dwg.add(dwg.line((int(option_dict['-left_space']),240-6-(float(sp_average)-70)*3+space+int(option_dict['-layer'])*10),
                                #     (int(float(option_dict['-left_space'])+csv_dic[key][0]/float(option_dict['-scale'])),240-6-(float(sp_average)-70)*3+space+int(option_dict['-layer'])*10),
                                #     stroke='red', stroke_width=1,
                                #     stroke_dasharray='4')) # Percentage line_100%
                                #__add average sp_identity line on identity graph_end_
                                
                                
                                #___draw sp_average div line in histogram_start________
                               
                                
                                #dwg.add(dwg.line(
                                #    start=(comm_x+(sp_x_width/36.0)*(float(sp_average)-65),comm_y),
                                #    end=(comm_x+(sp_x_width/36.0)*(float(sp_average)-65),comm_y+sp_y_hight),
                                #         stroke='red',
                                #         stroke_width=1,
                                #         stroke_dasharray='4,2'
                                #))
                                #___draw sp_average div line in histogram _end_________
                                
                                #___add peak value (speciation point) ____
                                #sp_avg_txt=str(sp_average).split('.')[0]+'.'+str(sp_average).split('.')[1][0]
                                #dwg.add(dwg.text(sp_avg_txt,
                                #    insert=(comm_x+(sp_x_width/36.0)*(float(sp_average)-65)-8,comm_y-7),
                                #    fill='red',
                                #    font_size=11
                                #    ))
                                #__________________________________________
        
                                
                ##________________mark the matched repeat regions (repeat_masker) to query-start__________
                    if option_dict['-add_q_repeat']!="1":
                        if key in q_repeat_dic:
                            for q_key, q_position in list(q_repeat_dic[key][1].items()):
                                if 'LTR/' in q_key:
                                    mark_color=(0,0,250)
                                elif 'DNA/' in q_key:
                                    mark_color=(20,80,70)
                                else:
                                    mark_color=(0,0,0)
                
                                #mark_color=(0,0,250)################################## ignore repeat type
                                for position in q_position:
                                   
                                    z=0
                                    if (float(float(option_dict['-left_space'])+position[1]/float(option_dict['-scale']))-(float(float(option_dict['-left_space'])+position[2]/float(option_dict['-scale']))))<=0.2:
                                        z=float(option_dict['-match_line'])
                
                                    dwg.add(dwg.line(
                                        (float(float(option_dict['-left_space'])+position[1]/float(option_dict['-scale'])),200+space+float(option_dict['-layer'])*10),
                                        (float(float(option_dict['-left_space'])+position[2]/float(option_dict['-scale']))+z, 200+space+float(option_dict['-layer'])*10),
                                        stroke=svgwrite.rgb(mark_color[0],mark_color[1],mark_color[2],'%'), stroke_width=float(option_dict['-mark_thick'])
                                        )
                                            )
                ##________________mark the matched repeat regions (repeat_masker) to query-end__________


            
                ##______________LTR domain graph draw_start_____________
                if option_dict['-LTR_dom'] !="1":
                    
                    
                    #option_dict['-layer']="0"
                    import shelve
                    LTR_dom_dic=shelve.open(option_dict['-LTR_dom'])
                    key=">"+key
                    
                    if key in LTR_dom_dic:
                        
                        num_posi=0
                        for position in LTR_dom_dic[key]:
                            num_posi=num_posi+1
                            if position[2]=='GAG':
                                mark_color=(63,72,62)##################################
                            elif position[2]=='AP':
                                mark_color=(90,45,123)################################## 
                            elif position[2]=='RT':
                                mark_color=(14,80,2)################################## 
                            elif position[2]=='RNaseH':
                                mark_color=(44,76,95)################################## 
                            elif position[2]=='INT':
                                mark_color=(122,67,18)################################## 
                            elif position[2]=='ENV':
                                mark_color=(14,125,117)################################## 
                            else:
                                mark_color=(0,200,200)
                            z=0
                            
                            if (float(float(option_dict['-left_space'])+int(position[0])/float(option_dict['-scale']))-(float(float(option_dict['-left_space'])+int(position[1])/float(option_dict['-scale']))))<=0.2:
                                z=float(option_dict['-match_line'])
                            
                            
                            if option_dict['-add_q_repeat']=="1":
                                dwg.add(dwg.line(
                                    (float(float(option_dict['-left_space'])+int(position[0])/float(option_dict['-scale'])),240+space+float(option_dict['-layer'])*10),
                                    (float(float(option_dict['-left_space'])+int(position[1])/float(option_dict['-scale']))+z, 240+space+float(option_dict['-layer'])*10),
                                    stroke=svgwrite.rgb(mark_color[0],mark_color[1],mark_color[2],'%'), stroke_width=float(option_dict['-mark_thick'])
                                    )
                                        )
                                if position[2]=="RNaseH":
                                    txt="RH"
                                elif position[2]=="INT":
                                    txt="IN"
                                else:
                                    txt=position[2]
                                dwg.add(dwg.text(txt,
                                                 insert=(float(float(option_dict['-left_space'])+int(position[0])/float(option_dict['-scale'])),240+space+float(option_dict['-layer'])*10+20),
                                                 fill= svgwrite.rgb(mark_color[0],mark_color[1],mark_color[2],'%'),
                                                 font_size=11
                                                 )
                                        )
                                
                                dwg.add(dwg.text(position[3].split('__')[1],
                                                 insert=(float(float(option_dict['-left_space'])+int(position[0])/float(option_dict['-scale'])),240+space+float(option_dict['-layer'])*10+30),
                                                 fill= svgwrite.rgb(mark_color[0],mark_color[1],mark_color[2],'%'),
                                                 font_size=10                                     
                                                 )
                                        )
                            
                    ##______________LTR domain graph draw_end_____________
                    
                    
                    
                    
                    ##_____Identity graph for Horizontal TE transfer analysis_start__
                if option_dict['-vertical_graph']=='2':
                    if ">" in key:
                        key=key[1:]
                    if key in csv_dic:
                        for key2,value2 in list(csv_dic[key][1].items()):
                            for position in value2:
                                idty=float(position[5])*100
                                match_idty=(idty-70)*3.0
                                
                                color_chart_key=str(220-int(float(idty-70)/(30.0)*(220))) #__color_selection from color chart by identity___
                                color_chart=grey_chart[color_chart_key]
                                #print color_chart
                                
                                dwg.add(dwg.rect(
                                    (float(float(option_dict['-left_space'])+int(position[1])/float(option_dict['-scale'])),240+space+float(option_dict['-layer'])*10-match_idty-6),
                                    (float(int(position[2]-int(position[1]))/float(option_dict['-scale'])+1), match_idty),
                                    fill=svgwrite.rgb(color_chart[0],color_chart[1],color_chart[2],'%'), stroke_width=0
                                    )
                                        )
                                    
                    ##_____Identity graph for Horizontal TE transfer analysis_end___
    
    
    #+++++++++++++++++++++++++++++++++++++++++++++++++horizontal TE transfer__end+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
    
    
    
    
    
    
    
    
    
        ##________________mark the matched gene regions to query-start__________
            if option_dict['-add_q_gene']!="1":
    
                #____________gene color change_start___________
                gene_position=[]
    
                if option_dict['-LTR_MYA'] !="0": ##for gene-densitiy calculation
                    option_dict['-layer']="0"
                    gene_position_left=[]
                    
                x=0
                gene_position_sort=[]
                if key in q_gene_dic:
                    for h_key, h_position in list(q_gene_dic[key][1].items()):
                        h_list=[]
                        for h in h_position:
                            h_list.append(h[1])
                        gene_position_sort.append([min(h_list),h_key])
                        if option_dict['-LTR_MYA'] !="0":
                            gene_position_left.append(min(h_list)) ##for gene-densitiy calculation
                    gene_position_sort.sort()
    
    
                    if option_dict['-LTR_MYA'] !="0": ##for gene-densitiy calculation
                        gene_position_left.sort()
    
                    
                    sorted_key_list=[]
                    for key2 in gene_position_sort:
                        sorted_key_list.append(key2[1])
                    for key3 in sorted_key_list:
                        h_position=q_gene_dic[key][1][key3]
                    #____________gene color change_end___________
                        
                        if x%2==1:
                            mark_color=(251,198,14)
                        if x%2==0:
                            mark_color=(0,255,114)
                            
                        gene_color=(80,80,80) ###################### ignore gene color
                        mark_color=(250,250,250)
        
                        for h_sub_position in h_position:
                            gene_position.append([float(h_sub_position[1]),float(h_sub_position[2])])
        
                        gene_position.sort()
                        #________________whole gene draw preparation start_____
                        whole_gene=0
                        min_gene_posi=min(min(gene_position))###
                        max_gene_posi=max(max(gene_position))###
                        #________________whole gene draw preparation end_____
                        extra=0
                        if option_dict['-vertical_graph']=='2':
                            extra=40
                        for g_position in gene_position:
                                
                            z=0
                            if (float(float(option_dict['-left_space'])+g_position[0]/float(option_dict['-scale']))-float(float(option_dict['-left_space'])+g_position[1]/float(option_dict['-scale'])))<=0.2:
                                z=float(option_dict['-match_line'])
                            #________________whole gene draw start_____
                            if whole_gene==0:
                                dwg.add(
                                    dwg.line( 
                                    (float(float(option_dict['-left_space'])+min_gene_posi/float(option_dict['-scale'])),200+space+float(option_dict['-layer'])*10+extra),
                                    (float(float(option_dict['-left_space'])+max_gene_posi/float(option_dict['-scale']))+z, 200+space+float(option_dict['-layer'])*10+extra),
                                    stroke=svgwrite.rgb(gene_color[0],gene_color[1],gene_color[2],'%'), stroke_width=float(option_dict['-mark_thick'])
                                    )
                                    )###
                                whole_gene=1
                            #________________whole gene draw end_____
    
                            if option_dict['-exon_depict']==1:
                                dwg.add(
                                    dwg.line( 
                                    (float(float(option_dict['-left_space'])+g_position[0]/float(option_dict['-scale'])),200+space+float(option_dict['-layer'])*10+extra),
                                    (float(float(option_dict['-left_space'])+g_position[1]/float(option_dict['-scale']))+z, 200+space+float(option_dict['-layer'])*10+extra),
                                    stroke=svgwrite.rgb(mark_color[0],mark_color[1],mark_color[2],'%'), stroke_width=float(option_dict['-mark_thick'])
                                    )
                                    )
                        gene_position=[]
                        x=x+1
    
                ####_____draw gene density under query bars_start__________________
    
                if option_dict['-LTR_MYA'] !="0":
                    option_dict['-layer']="0"
    
                    max_position=int(csv_dic[key][0])#(max(gene_position_left))
                            
                    num_slide_windows=int(max_position/int(option_dict['-sliding_win'])) + 1
    
                    ####___parsing gene position according to each step_start____
    
                    stepwise_dic_gene={}
                    windows=0
                    for loop in range(num_slide_windows):
                        stepwise_dic_gene[loop]=[]
                    
                        
                        for position_q in gene_position_left:
                            if int(position_q) >= windows and int(position_q) < windows +int(option_dict['-sliding_win']):
                                stepwise_dic_gene[loop].append(position_q)
                                
                        windows=windows+int(option_dict['-sliding_win'])
                       
                                
                    ####___parsing gene position according to each step_end____
    
    
    
    
                    ####___calculate position value for gene density according to each step_start____
        
                    sliding_position2=-int(option_dict['-sliding_win'])/2
                    sliding_gene_number=[]
    
                    gene_density_for_max=[]
                    for loop2 in range(num_slide_windows):
                        sliding_position2=sliding_position2+int(option_dict['-sliding_win'])
                                
                        gene_density_for_max.append(len(stepwise_dic_gene[loop2]))
    
    
                        sliding_gene_number.append([sliding_position2,len(stepwise_dic_gene[loop2])])
    
                    if option_dict['-max_peak']=="2":
                        defi_max_gene=max(gene_density_for_max)                                                
    
                    ####___calculate position value for gene density according to each step_start____
    
    
                    ####___draw average gene density on the graph_start____
    
                    sliding_gene_number_convert=[]
                    num_position=0
                    for position3 in sliding_gene_number:
                        num_position=num_position+1
                        
                        x_value=float(float(option_dict['-left_space'])+float(position3[0])/float(option_dict['-scale']))
                        y_value=200+space + float(float(option_dict['-height'])*(float(position3[1])/float(defi_max_gene))) +7
    
                        if num_position == 1:
                            
                            temp_y=200+space + 7
                            sliding_gene_number_convert.append((x_value, temp_y))
                        sliding_gene_number_convert.append((x_value,y_value))
    
                        if num_position == len(sliding_gene_number):
                            temp_y=200+space + 7
                            sliding_gene_number_convert.append((x_value, temp_y))
                            
    
    
                    
                    dwg.add(dwg.polygon(points = [position for position in sliding_gene_number_convert],
                                         stroke = svgwrite.rgb(250,250,250),
                                         stroke_width=1,
                                         fill = 'grey'
                                         ))
    
    
                    
                    gene_density_for_max=[]
                    sliding_gene_number=[] 
                    
                    gene_position_left=[]
                    
    
    
        ##________________mark the matched gene regions to query-end__________
            
    
        ##________________mark the matched repeat regions to query-start__________
            if option_dict['-add_q_repeat']!="1":

                extra=0
                if option_dict['-vertical_graph']=='2':
                    extra=40
                
                if key in q_repeat_dic:
                    for q_key, q_position in list(q_repeat_dic[key][1].items()):
                        if 'LTR/' in q_key:
                            mark_color=(0,0,250)
                        elif 'DNA/' in q_key:
                            mark_color=(0,0,0)
                        else:
                            mark_color=(20,80,70)
                            
        
                        mark_color=(0,0,120)################################## ignore repeat type
                        for position in q_position:
                           
                            z=0
                            if (float(float(option_dict['-left_space'])+position[1]/float(option_dict['-scale']))-(float(float(option_dict['-left_space'])+position[2]/float(option_dict['-scale']))))<=0.2:
                                z=float(option_dict['-match_line'])
        
                            dwg.add(dwg.line(
                                (float(float(option_dict['-left_space'])+position[1]/float(option_dict['-scale'])),200+space+float(option_dict['-layer'])*10+extra),
                                (float(float(option_dict['-left_space'])+position[2]/float(option_dict['-scale']))+z, 200+space+float(option_dict['-layer'])*10+extra),
                                stroke=svgwrite.rgb(mark_color[0],mark_color[1],mark_color[2],'%'), stroke_width=float(option_dict['-mark_thick'])
                                )
                                    )
        ##________________mark the matched repeat regions to query-end__________
    
    
    
                ##______________LTR domain graph draw_start_____________
            if option_dict['-LTR_dom'] !="1":
                extra=0
                y_posi1=-15
                y_posi2=-25
                if option_dict['-vertical_graph']=='2':
                    extra=40
                    y_posi1=20
                    y_posi2=30
                
                #option_dict['-layer']="0"
                import shelve
                LTR_dom_dic=shelve.open(option_dict['-LTR_dom'])

                key=">"+key
                
                if key in LTR_dom_dic:
                    
                    num_posi=0
                    for position in LTR_dom_dic[key]:
                        num_posi=num_posi+1
                        if position[2]=='GAG':
                            mark_color=(63,72,62)##################################
                        elif position[2]=='AP':
                            mark_color=(90,45,123)################################## 
                        elif position[2]=='RT':
                            mark_color=(14,80,2)################################## 
                        elif position[2]=='RNaseH':
                            mark_color=(44,76,95)################################## 
                        elif position[2]=='INT':
                            mark_color=(122,67,18)################################## 
                        elif position[2]=='ENV':
                            mark_color=(14,125,117)################################## 
                        else:
                            mark_color=(0,200,200)
                        z=0
                        
                        if (float(float(option_dict['-left_space'])+int(position[0])/float(option_dict['-scale']))-(float(float(option_dict['-left_space'])+int(position[1])/float(option_dict['-scale']))))<=0.2:
                            z=float(option_dict['-match_line'])
                        
                        
                        
                        dwg.add(dwg.line(
                            (float(float(option_dict['-left_space'])+int(position[0])/float(option_dict['-scale'])),200+space+float(option_dict['-layer'])*10+extra),
                            (float(float(option_dict['-left_space'])+int(position[1])/float(option_dict['-scale']))+z, 200+space+float(option_dict['-layer'])*10+extra),
                            stroke=svgwrite.rgb(mark_color[0],mark_color[1],mark_color[2],'%'), stroke_width=float(option_dict['-mark_thick']-2)
                            )
                                )
                        if position[2]=="RNaseH":
                            txt="RH"
                        elif position[2]=="INT":
                            txt="IN"
                        else:
                            txt=position[2]
                        dwg.add(dwg.text(txt,
                                         insert=(float(float(option_dict['-left_space'])+int(position[0])/float(option_dict['-scale'])),200+space+float(option_dict['-layer'])*10+extra+y_posi1),
                                         fill= svgwrite.rgb(mark_color[0],mark_color[1],mark_color[2],'%'),
                                         font_size=11
                                         )
                                )
                        
                        dwg.add(dwg.text(position[3].split('__')[1],
                                         insert=(float(float(option_dict['-left_space'])+int(position[0])/float(option_dict['-scale'])),200+space+float(option_dict['-layer'])*10+extra+y_posi2),
                                         fill= svgwrite.rgb(mark_color[0],mark_color[1],mark_color[2],'%'),
                                         font_size=10                                     
                                         )
                                )
                        
                ##______________LTR domain graph draw_end_____________

    
    
    
            ##______________LTR insertion time graph draw_start_____________
            if option_dict['-LTR_MYA'] !="0":
                option_dict['-layer']="0"
    
                max_MYA=max(MYA_list)
                #max_K2P=max(K2P_list)
                
    
                
                if option_dict['-LTR_density']=='1':
                    if key in MYA_db:
                        for position in MYA_db[key]:
    
                            MYA_y_value=200+space - float(float(option_dict['-height'])*(float(MYA_db[key][position][1])/float(max_MYA)))
                            #K2P_y_value=200+space - float(float(option_dict['-height'])*(float(MYA_db[key][position][0])/float(max_K2P)))
    
                            dwg.add(dwg.line(
                                (float(float(option_dict['-left_space'])+float(position)/float(option_dict['-scale'])), MYA_y_value-6),#previous y value:  200+space-7
                                (float(float(option_dict['-left_space'])+float(position)/float(option_dict['-scale'])), MYA_y_value-7), stroke=svgwrite.rgb(35,35,35,'%'),stroke_width=1))
                        
                ###_______________Average insertion time draw by sliding window_start________________________
    
    
                max_position=float(csv_dic[key][0])
                num_slide_windows=int(max_position/int(option_dict['-sliding_win'])) + 1
    
    #            max_position=max(position_list)
    #            num_slide_windows=max_position/int(option_dict['-sliding_win']) + 1
    
                windows=0
                stepwise_dic={}
    
                ####___parsing MYA value according to each step_start____
                for loop in range(num_slide_windows):
                    stepwise_dic[loop]=[]
                    
                    if key in MYA_db:
                        for position2 in MYA_db[key]:
                            if int(position2) >= windows and int(position2) < windows +int(option_dict['-sliding_win']):
                                stepwise_dic[loop].append(float(MYA_db[key][position2][1]))
                        windows=windows+int(option_dict['-sliding_win'])
                ####___parsing MYA value according to each step_end____
    
    
                ####___calculate average MYA value according to each step_start____
    
                if option_dict['-LTR_density']=='1':
                    sliding_position=-int(option_dict['-sliding_win'])/2
                    average_MYA_position=[]
    
                    
                    for loop2 in range(num_slide_windows):
                        sliding_position=sliding_position+int(option_dict['-sliding_win'])
                        total_sum=0
                        for num in stepwise_dic[loop2]:
                            total_sum=total_sum+num
                        if len(stepwise_dic[loop2]) != 0:
                            average_MYA_position.append([sliding_position,(total_sum/float(len(stepwise_dic[loop2])))])
                        else:
                            average_MYA_position.append([sliding_position, 0])
                ####___calculate LTR density according to each step_start____
                elif option_dict['-LTR_density']!='1':
                    sliding_position=-int(option_dict['-sliding_win'])/2
                    
                    LTR_density=[]
                    
                    for loop3 in range(num_slide_windows):
                        LTR_density.append(len(stepwise_dic[loop3]))
                    max_LTR_density=max(LTR_density)
                    
                    LTR_density_position=[]
                    for density in LTR_density:
                        sliding_position=sliding_position+int(option_dict['-sliding_win'])
                        LTR_density_position.append([sliding_position,density])
                    
                    if option_dict['-max_peak'] =="1":
                        max_LTR_density=defi_max
                        
                            
                        
                ####___calculate average MYA value according to each step_start____
    
                ####___draw LTR density on the graph_start____
                if option_dict['-LTR_density']=='1':
                    average_MYA_convert=[]
                    for position3 in average_MYA_position:
                        x_value=float(float(option_dict['-left_space'])+float(position3[0])/float(option_dict['-scale']))
                        y_value=200+space - float(float(option_dict['-height'])*(float(position3[1])/float(max_MYA))) -7
                        average_MYA_convert.append((x_value,y_value))
    
                    dwg.add(dwg.polyline( points = [position for position in average_MYA_convert],
                                          stroke = svgwrite.rgb(250,0,0),
                                          stroke_width=1,
                                          fill = 'none'
                                          ))
                elif option_dict['-LTR_density']!='1':
                    LTR_density_convert=[]
                    density_num=0
                    for position4 in LTR_density_position:
                        density_num=density_num+1
                        
                        x_value=float(float(option_dict['-left_space'])+float(position4[0])/float(option_dict['-scale']))
                        if max_LTR_density!=0:
                            y_value=200+space - float(float(option_dict['-height'])*(float(position4[1])/float(max_LTR_density))) -7
                        else:
                            y_value=200+space -7
                            
                        if density_num==1:
                            y_temp=200+space -7
                            LTR_density_convert.append((x_value,y_temp))
                        
                        LTR_density_convert.append((x_value,y_value))
    
                        if density_num==len(LTR_density_position):
                            y_temp=200+space -7
                            LTR_density_convert.append((x_value,y_temp))
    
                    if "," in option_dict['-LTR_density']:
                        LTR_density_color=svgwrite.rgb(int(option_dict['-LTR_density'].split(',')[0]),int(option_dict['-LTR_density'].split(',')[1]),int(option_dict['-LTR_density'].split(',')[2]))
                    else:
                        LTR_density_color=option_dict['-LTR_density']
                                                       
                    
                    dwg.add(dwg.polygon( points = [position for position in LTR_density_convert],
                                          stroke = svgwrite.rgb(250,250,250),
                                          stroke_width=1,
                                          fill = LTR_density_color
                                          ))
                    
                ####___calculate average MYA value according to each step_end____
    
    
    
                ###_______________Average insertion time draw by sliding window_end________________________
    
    
            ##______________LTR insertion time graph draw_end_____________                    
            
        
        ##________________mark the matched repeat regions to query-end__________
    
    
    
            
            
            
            
                           
            if option_dict['-layer'] != "0":
    
        #==============================Graph_drawing_Hit==============================
            
        
        ##___________Hit sort by position-start____________
        
                hit_name_sort=[]
                if ">" in key:
                    key=key[1:]
                for key_pre,value_pre in list(csv_dic[key][1].items()):
                    x_query_position=[]
                    for value in value_pre:
                        x_query_position.append(value[1])
                        x_query_position.append(value[2])
                    #x_query_center=float((max(x_query_position)+min(x_query_position))/2)
                    sum_posi=0##
                    for posi in x_query_position:##
                        sum_posi=sum_posi+float(posi)##
                    x_query_center=sum_posi/len(x_query_position)##
               
                    hit_name_sort.append((x_query_center,key_pre))
                
                hit_name_sort.sort()
                
            
        ##___________Hit sort by position-end____________
    
    
        
                for hit_pair in hit_name_sort: #hit individual
                    if ">" in key:
                        key=key[1:]
                    if key in csv_dic:
                        item2=csv_dic[key][1][hit_pair[1]]
                        k=k+1
                        #print item2
                        
                      
            ##____________upper_side_graph_______________
                        if k%2 == 1:
                            m=m+1
                            if m%3 == 1:
                                color=(100,75,0)
                                y_value=200+space+int(option_dict['-height'])+m%int(option_dict['-layer'])*18+int(option_dict['-layer'])*10
                
                                if int(option_dict['-grey_scale'])==1:
                                    color_chart=(0,70,70)
                                
                            if m%3 == 2:
                                color=(35,100,35)
                                y_value=200+space+int(option_dict['-height'])+m%int(option_dict['-layer'])*18+int(option_dict['-layer'])*10
                
                                if int(option_dict['-grey_scale'])==1:
                                    color_chart=(70,70,70)
                                
                            if m%3 == 0:
                                color=(80,50,60)
                                y_value=200+space+int(option_dict['-height'])+m%int(option_dict['-layer'])*18+int(option_dict['-layer'])*10
            
                                if int(option_dict['-grey_scale'])==1:
                                    color_chart=(60,60,200)
            
                            if "Gypsy" in hit_pair[1]:#######
                                color=(0,250,0)##############
                            elif "Copia" in hit_pair[1]:#####
                                color=(250,0,0)##############
                            
                                       
            
            
            
                ##___________Compared pair position calibration-start____________
                            x_query_position=[]
                            x_hit_position=[]
                
                            #print item2
                            for x in item2:
                                x_query_position.append(x[1])
                                x_query_position.append(x[2])
                                x_hit_position.append(x[3])
                                x_hit_position.append(x[4])
                            x_query_posi=0
                            for y in x_query_position:
                                x_query_posi=x_query_posi+float(y)
                            x_query_center=x_query_posi/len(x_query_position)
                            x_hit_posi=0
                            for z in x_hit_position:
                                x_hit_posi=x_hit_posi+float(z)
                            x_hit_center=x_hit_posi/len(x_hit_position)
                                
                            #x_query_center=float((max(x_query_position)+min(x_query_position))/2)
                            #x_hit_center=float((max(x_hit_position)+min(x_hit_position))/2)
                            hit_translocation=x_query_center-x_hit_center
                ##___________Compared pair position calibration-end____________
                 
                            if option_dict['-add_h_repeat']!="1":
                                h_stroke_width=12
                                h_color=(255,30,30)
                            elif option_dict['-add_h_gene']!="1":
                                h_stroke_width=12
                                h_color=(255,30,30)
                            else:
                                h_stroke_width=4
                                h_color=color
            
                            h_color=color####################################################### hit bar color 
                                
                            main_line=dwg.line(  #main_line
                                (float(float(option_dict['-left_space'])+(hit_translocation)/float(option_dict['-scale'])),y_value),
                                (float(float(option_dict['-left_space'])+(hit_translocation+item2[0][0])/float(option_dict['-scale'])),y_value), stroke=svgwrite.rgb(h_color[0],h_color[1],h_color[2],'%'), stroke_width=h_stroke_width)
                            #print item2
        
                            if option_dict['-add_h_repeat']=="1":
                                if option_dict['-add_h_gene']=="1":
            
                                    flanking_line1=dwg.line( #side_vertical_line_left
                                        (float(float(option_dict['-left_space'])+(hit_translocation)/float(option_dict['-scale'])),y_value-3),
                                        (float(float(option_dict['-left_space'])+(hit_translocation)/float(option_dict['-scale'])),y_value+3), stroke='black', stroke_width=1)
            
                                    flanking_line2=dwg.line( #side_vertical_line_right
                                        (float(float(option_dict['-left_space'])+(hit_translocation+item2[0][0])/float(option_dict['-scale'])),y_value-3),
                                        (float(float(option_dict['-left_space'])+(hit_translocation+item2[0][0])/float(option_dict['-scale'])),y_value+3), stroke='black', stroke_width=1)
            
                            #print item2
                            ##______________creat hyperlink_start___________
                            if option_dict['-hyperlink'] != "":
                                main_line_link=svgwrite.container.Hyperlink('%s\\%s.txt' %(path, hit_pair[1]),target="_blank")
                                main_line_link.add(main_line)
                                if option_dict['-add_h_repeat']=="1":
                                    if option_dict['-add_h_gene']=="1":
                                        main_line_link.add(flanking_line1)
                                        main_line_link.add(flanking_line2)
                                dwg.add(main_line_link)
                            ##______________creat hyperlink_end___________
                            else:
                                dwg.add(main_line)
                                if option_dict['-add_h_repeat']=="1":
                                    if option_dict['-add_h_gene']=="1":
                                        dwg.add(flanking_line1)
                                        dwg.add(flanking_line2)
                                
            
            
            
                ##________________mark the matched gene regions to hit-start__________
                            if option_dict['-add_h_gene']!="1":
                                if hit_pair[1] in h_gene_dic:
            
                                    #____________gene color change_start___________
                                    gene_position=[]
                                    x=0
                                    gene_position_sort=[]
                                    for h_key, h_position in list(h_gene_dic[hit_pair[1]][1].items()):
                                        h_list=[]
                                        for h in h_position:
                                            h_list.append(h[1])
                                        gene_position_sort.append([min(h_list),h_key])
                                    gene_position_sort.sort()
                
                                    sorted_key_list=[]
                                    for key2 in gene_position_sort:
                                        sorted_key_list.append(key2[1])
                                        
                                    for key3 in sorted_key_list:
                                        h_position=h_gene_dic[hit_pair[1]][1][key3]
                                    #____________gene color change_end___________
                                        if x%2==1:
                                            mark_color=(251,198,14)
                                        if x%2==0:
                                            mark_color=(0,255,114)
            
                                        gene_color=(80,80,80) ###################### ignore gene color
                                        mark_color=(250,250,250)
            
                                        for h_sub_position in h_position:
                                            gene_position.append([float(h_sub_position[1]),float(h_sub_position[2])])
                        
                                        gene_position.sort()
        
                                        #________________whole gene draw preparation start_____
                                        whole_gene=0
                                        min_gene_posi=min(min(gene_position))###
                                        max_gene_posi=max(max(gene_position))###
                                        #________________whole gene draw preparation end_____
                            
                                        
                                        for g_position in gene_position:
                                        
                                            z=0
                                            if (float(float(option_dict['-left_space'])+(hit_translocation+g_position[0])/float(option_dict['-scale']))-float(float(option_dict['-left_space'])+(hit_translocation+g_position[1])/float(option_dict['-scale'])))<=0.2:
                                                z=float(option_dict['-match_line'])
        
                                            #________________whole gene draw start_____
                                            if whole_gene==0:
                                                dwg.add(dwg.line( 
                                                    (float(float(option_dict['-left_space'])+(hit_translocation+min_gene_posi)/float(option_dict['-scale'])),y_value),
                                                    (float(float(option_dict['-left_space'])+(hit_translocation+max_gene_posi)/float(option_dict['-scale']))+z, y_value),
                                                    stroke=svgwrite.rgb(gene_color[0],gene_color[1],gene_color[2],'%'), stroke_width=8
                                                    ))
                                                whole_gene=1
                                            #________________whole gene draw end_____
                                                            
                                            if option_dict['-exon_depict']==1:
                                                dwg.add(dwg.line( 
                                                    (float(float(option_dict['-left_space'])+(hit_translocation+g_position[0])/float(option_dict['-scale'])),y_value),
                                                    (float(float(option_dict['-left_space'])+(hit_translocation+g_position[1])/float(option_dict['-scale']))+z, y_value),
                                                    stroke=svgwrite.rgb(mark_color[0],mark_color[1],mark_color[2],'%'), stroke_width=8
                                                    ))
                                        gene_position=[]
                                        x=x+1
            
            
            
                ##________________mark the matched gene regions to hit-end__________
            
                
            
            
                #_________mark the matched repeat regions to hit-start__________
                            if option_dict['-add_h_repeat']!="1":
                                if hit_pair[1] in h_repeat_dic:
                                    for h_key, h_position in list(h_repeat_dic[hit_pair[1]][1].items()):
                                        if 'LTR/' in h_key:
                                            mark_color=(0,0,250)
                                        elif 'DNA/' in h_key:
                                            mark_color=(20,80,70)
                                        else:
                                            mark_color=(0,0,0)
            
                                        #mark_color=(0,0,250)################################## ignore repeat type
            
            
                                        for position in h_position:
                                            
                                            z=0
                                            if (float(float(option_dict['-left_space'])+float(hit_translocation+position[1])/float(option_dict['-scale']))-float(float(option_dict['-left_space'])+float(hit_translocation+position[2])/float(option_dict['-scale'])))<=0.2:
                                                z=float(option_dict['-match_line'])
            
                                            dwg.add(dwg.line( 
                                                (float(float(option_dict['-left_space'])+(hit_translocation+position[1])/float(option_dict['-scale'])), y_value),
                                                (float(float(option_dict['-left_space'])+(hit_translocation+position[2])/float(option_dict['-scale']))+z, y_value), stroke=svgwrite.rgb(mark_color[0],mark_color[1],mark_color[2],'%'), stroke_width=8))
            
                    
                                ##______________LTR domain graph draw_start_____________
                            if option_dict['-LTR_dom'] !="1":
                                extra=0
                                import shelve
                                LTR_dom_dic=shelve.open(option_dict['-LTR_dom'])
                                key=">"+hit_pair[1]
                                if key in LTR_dom_dic:
                                    
                                    num_posi=0
                                    for position in LTR_dom_dic[key]:
                                        num_posi=num_posi+1
                                        if position[2]=='GAG':
                                            mark_color=(63,72,62)##################################
                                        elif position[2]=='AP':
                                            mark_color=(90,45,123)################################## 
                                        elif position[2]=='RT':
                                            mark_color=(14,80,2)################################## 
                                        elif position[2]=='RNaseH':
                                            mark_color=(44,76,95)################################## 
                                        elif position[2]=='INT':
                                            mark_color=(122,67,18)################################## 
                                        elif position[2]=='ENV':
                                            mark_color=(14,125,117)################################## 
                                        else:
                                            mark_color=(0,200,200)
                                        z=0
                                        
                                        if (float(float(option_dict['-left_space'])+int(position[0])/float(option_dict['-scale']))-(float(float(option_dict['-left_space'])+int(position[1])/float(option_dict['-scale']))))<=0.2:
                                            z=float(option_dict['-match_line'])
                                        
                                        
                                        
                                        dwg.add(dwg.line(
                                            (float(float(option_dict['-left_space'])+(hit_translocation+int(position[0]))/float(option_dict['-scale'])), y_value),
                                            (float(float(option_dict['-left_space'])+(hit_translocation+int(position[1]))/float(option_dict['-scale']))+z, y_value),
                                            stroke=svgwrite.rgb(mark_color[0],mark_color[1],mark_color[2],'%'), stroke_width=float(option_dict['-mark_thick']-2)
                                            )
                                                )
                                        if position[2]=="RNaseH":
                                            txt="RH"
                                        elif position[2]=="INT":
                                            txt="IN"
                                        else:
                                            txt=position[2]
                                        dwg.add(dwg.text(txt,
                                                         insert=(float(float(option_dict['-left_space'])+(hit_translocation+int(position[0]))/float(option_dict['-scale'])),y_value+20),
                                                         fill= svgwrite.rgb(mark_color[0],mark_color[1],mark_color[2],'%'),
                                                         font_size=11
                                                         )
                                                )
                                        
                                        dwg.add(dwg.text(position[3].split('__')[1],
                                                         insert=(float(float(option_dict['-left_space'])+(hit_translocation+int(position[0]))/float(option_dict['-scale'])),y_value+30),
                                                         fill= svgwrite.rgb(mark_color[0],mark_color[1],mark_color[2],'%'),
                                                         font_size=10                                     
                                                         )
                                                )
                                        
                                ##______________LTR domain graph draw_end_____________
            
                                        
                ##________________mark the matched repeat regions to hit-end__________
                                
            
            
                            #print item2
                            for item3 in item2: #separated hit
                                #print item3
            
                                if int(option_dict['-grey_scale'])==2:
                                    color_chart_key=str(220-int((item3[5]-float(option_dict['-identity']))/(1.0-float(option_dict['-identity']))*(220))) #__color_selection from color chart by identity___
                                    color_chart=grey_chart[color_chart_key]                                                                          #__color_selection from color chart by identity___
            
                                p=0
                                if option_dict['-add_h_repeat']!="1":
                                    p=4
                                if option_dict['-add_h_gene']!="1":
                                    p=4
        
                                match_line=float(option_dict['-match_line'])
                                
                                
                                dwg.add(dwg.polygon(points=[
                                    (float(float(option_dict['-left_space'])+item3[1]/float(option_dict['-scale'])),200+space+float(option_dict['-layer'])*10+7),
                                    (float(float(option_dict['-left_space'])+item3[2]/float(option_dict['-scale'])), 200+space+float(option_dict['-layer'])*10+7),
                                    (float(float(option_dict['-left_space'])+(hit_translocation+item3[4])/float(option_dict['-scale'])),y_value-2-p),
                                    (float(float(option_dict['-left_space'])+(hit_translocation+item3[3])/float(option_dict['-scale'])),y_value-2-p)], stroke=svgwrite.rgb(color_chart[0],color_chart[1],color_chart[2],'%'),stroke_width=match_line, fill=svgwrite.rgb(color_chart[0],color_chart[1],color_chart[2],'%')))
        
                ##________________mark the matched regions to query-start__________
                                if option_dict['-add_q_repeat']=="1":
                                    if option_dict['-add_q_gene']=="1":
            
                                        z=0
                                        if (float(float(option_dict['-left_space'])+item3[1]/float(option_dict['-scale']))-float(float(option_dict['-left_space'])+item3[2]/float(option_dict['-scale'])))<=0.2:
                                            z=float(option_dict['-match_line'])
            
                                        dwg.add(dwg.line( 
                                            (float(float(option_dict['-left_space'])+item3[1]/float(option_dict['-scale'])),200+space+float(option_dict['-layer'])*10),
                                            (float(float(option_dict['-left_space'])+item3[2]/float(option_dict['-scale']))+z, 200+space+float(option_dict['-layer'])*10), stroke='yellow', stroke_width=float(option_dict['-mark_thick'])))
                ##________________mark the matched regions to query-end__________
            
        
            ##___________________downside_graph______________
        
                    if k%2 == 0:
                        n=n+1
                        if n%3 == 1:
                            y_value=200+space-int(option_dict['-height'])-n%int(option_dict['-layer'])*18+int(option_dict['-layer'])*10
                            color=(100,75,0)
                            if int(option_dict['-grey_scale'])==1:
                                color_chart=(0,70,70)
        
                        
                        if n%3 == 2:
                            color=(35,100,35)
                            y_value=200+space-int(option_dict['-height'])-n%int(option_dict['-layer'])*18+int(option_dict['-layer'])*10
            
                            if int(option_dict['-grey_scale'])==1:
                                color_chart=(70,70,70)
        
                        if n%3 == 0:
                            color=(80,50,60)
                            y_value=200+space-int(option_dict['-height'])-n%int(option_dict['-layer'])*18+int(option_dict['-layer'])*10
        
                            if int(option_dict['-grey_scale'])==1:
                                color_chart=(60,60,200)
        
                        if "Gypsy" in hit_pair[1]:#######
                            color=(0,250,0)##############
                        elif "Copia" in hit_pair[1]:#####
                            color=(250,0,0)##############
        
        
        
            ##___________Compared pair position calibration-start___________
                        x_query_position=[]
                        x_hit_position=[]
        
        
                        for y in item2:
                            x_query_position.append(y[1])
                            x_query_position.append(y[2])
                            x_hit_position.append(y[3])
                            x_hit_position.append(y[4])
                        x_query_posi=0
                        for y in x_query_position:
                            x_query_posi=x_query_posi+float(y)
                        x_query_center=x_query_posi/len(x_query_position)
                        x_hit_posi=0
                        for z in x_hit_position:
                            x_hit_posi=x_hit_posi+float(z)
                        x_hit_center=x_hit_posi/len(x_hit_position)
                            
                        #x_query_center=float((max(x_query_position)+min(x_query_position))/2)
                        #x_hit_center=float((max(x_hit_position)+min(x_hit_position))/2)
                        hit_translocation=x_query_center-x_hit_center
        ##___________Compared pair position calibration-end____________
        
                        if option_dict['-add_h_repeat']!="1":
                            h_stroke_width=12
                            h_color=(255,30,30)
                        elif option_dict['-add_h_gene']!="1":
                            h_stroke_width=12
                            h_color=(255,30,30)
                        else:
                            h_stroke_width=4
                            h_color=color
        
                        h_color=color####################################################### hit bar color 
        
                    
                        main_line=dwg.line( #hit_main_line
                            (float(float(option_dict['-left_space'])+(hit_translocation)/float(option_dict['-scale'])),y_value),
                            (float(float(option_dict['-left_space'])+(hit_translocation+item2[0][0])/float(option_dict['-scale'])),y_value), stroke=svgwrite.rgb(h_color[0],h_color[1],h_color[2],'%'), stroke_width=h_stroke_width)
        
                        if option_dict['-add_h_repeat']=="1":
                            if option_dict['-add_h_gene']=="1":
        
                                flanking_line1=dwg.line( #side_vertical_line_left
                                    (float(float(option_dict['-left_space'])+(hit_translocation)/float(option_dict['-scale'])),y_value-3),
                                    (float(float(option_dict['-left_space'])+(hit_translocation)/float(option_dict['-scale'])),y_value+3), stroke='black', stroke_width=1)
        
                                flanking_line2=dwg.line( #side_vertical_line_right
                                    (float(float(option_dict['-left_space'])+(hit_translocation+item2[0][0])/float(option_dict['-scale'])),y_value-3),
                                    (float(float(option_dict['-left_space'])+(hit_translocation+item2[0][0])/float(option_dict['-scale'])),y_value+3), stroke='black', stroke_width=1)
        
        
                        ##______________creat hyperlink_start___________
                        if option_dict['-hyperlink'] != "":
                            main_line_link=svgwrite.container.Hyperlink('%s\\%s.txt' %(path, hit_pair[1]),target="_blank")
                            main_line_link.add(main_line)
                            if option_dict['-add_h_repeat']=="1":
                                if option_dict['-add_h_gene']=="1":
                                    main_line_link.add(flanking_line1)
                                    main_line_link.add(flanking_line2)
        #                    if option_dict['-add_h_repeat']!="1":
        #                        main_line_link.add(repeat_line)
        #                    if option_dict['-add_h_gene']!="1":
        #                        main_line_link.add(gene_line)
                            dwg.add(main_line_link)
                        ##______________creat hyperlink_end___________
                        else:
                            dwg.add(main_line)
                            if option_dict['-add_h_repeat']=="1":
                                if option_dict['-add_h_gene']=="1":
                                    dwg.add(flanking_line1)
                                    dwg.add(flanking_line2)
        
        
    
        
            ##________________mark the matched gene regions to hit-start__________
                        if option_dict['-add_h_gene']!="1":
                            #print hit_pair[1]###################################
                            if hit_pair[1] in h_gene_dic:
                    
                                #____________gene color change_start___________
                                gene_position=[]
                                x=0
                                gene_position_sort=[]
                                for h_key, h_position in list(h_gene_dic[hit_pair[1]][1].items()):
                                    h_list=[]
                                    for h in h_position:
                                        h_list.append(h[1])
                                    gene_position_sort.append([min(h_list),h_key])
                                gene_position_sort.sort()
        
                                sorted_key_list=[]
                                for key2 in gene_position_sort:
                                    sorted_key_list.append(key2[1])
                                    
                                for key3 in sorted_key_list:
                                    h_position=h_gene_dic[hit_pair[1]][1][key3]
                                #____________gene color change_end___________
                                    if x%2==1:
                                        mark_color=(251,198,14)
                                    if x%2==0:
                                        mark_color=(0,255,114)
        
                                    gene_color=(80,80,80) ###################### ignore gene color
                                    mark_color=(250,250,250)
                    
                                    for h_sub_position in h_position:
                                        gene_position.append([float(h_sub_position[1]),float(h_sub_position[2])])
                    
                                    gene_position.sort()
    
    
                                    #________________whole gene draw preparation start_____
                                    whole_gene=0
                                    min_gene_posi=min(min(gene_position))###
                                    max_gene_posi=max(max(gene_position))###
                                    #________________whole gene draw preparation end_____
                        
                                    for g_position in gene_position:
                                    
                                        z=0
                                        if (float(float(option_dict['-left_space'])+(hit_translocation+g_position[0])/float(option_dict['-scale']))-float(float(option_dict['-left_space'])+(hit_translocation+g_position[1])/float(option_dict['-scale'])))<=0.2:
                                            z=float(option_dict['-match_line'])
    
                                            
                                        #________________whole gene draw start_____
                                        if whole_gene==0:
                                            dwg.add(dwg.line( 
                                                (float(float(option_dict['-left_space'])+(hit_translocation+min_gene_posi)/float(option_dict['-scale'])),y_value),
                                                (float(float(option_dict['-left_space'])+(hit_translocation+max_gene_posi)/float(option_dict['-scale']))+z, y_value),
                                                stroke=svgwrite.rgb(gene_color[0],gene_color[1],gene_color[2],'%'), stroke_width=8
                                                ))
                                            whole_gene=1
                                        #________________whole gene draw end_____
                                                        
                                        if option_dict['-exon_depict']==1:
                                            dwg.add(dwg.line( 
                                                (float(float(option_dict['-left_space'])+(hit_translocation+g_position[0])/float(option_dict['-scale'])),y_value),
                                                (float(float(option_dict['-left_space'])+(hit_translocation+g_position[1])/float(option_dict['-scale']))+z, y_value),
                                                stroke=svgwrite.rgb(mark_color[0],mark_color[1],mark_color[2],'%'), stroke_width=8
                                                ))
                                    gene_position=[]
                                    x=x+1
        
            ##________________mark the matched gene regions to hit-end__________
        
        
        
            #_________mark the matched repeat regions to hit-start__________
                        if option_dict['-add_h_repeat']!="1":
                            if hit_pair[1] in h_repeat_dic:
                                
                                for h_key, h_position in list(h_repeat_dic[hit_pair[1]][1].items()):
                                    if 'LTR/' in h_key:
                                        mark_color=(0,0,250)
                                    elif 'DNA/' in h_key:
                                        mark_color=(20,80,70)
                                    else:
                                        mark_color=(0,0,0)
        
                                    #mark_color=(0,0,250)################################## ignore repeat type    
        
                                    for position in h_position:
                                        
                                
                                        z=0
                                        if (float(float(option_dict['-left_space'])+float(hit_translocation+position[1])/float(option_dict['-scale']))-float(float(option_dict['-left_space'])+float(hit_translocation+position[2])/float(option_dict['-scale'])))<=0.2:
                                            z=float(option_dict['-match_line'])
            
                                        dwg.add(dwg.line( 
                                            (float(float(option_dict['-left_space'])+(hit_translocation+position[1])/float(option_dict['-scale'])),y_value),
                                            (float(float(option_dict['-left_space'])+(hit_translocation+position[2])/float(option_dict['-scale']))+z, y_value), stroke=svgwrite.rgb(mark_color[0],mark_color[1],mark_color[2],'%'), stroke_width=8))
            ##________________mark the matched repeat regions to hit-end__________
        
                                    ##______________LTR domain graph draw_start_____________
                        if option_dict['-LTR_dom'] !="1":
                            extra=0
                            import shelve
                            LTR_dom_dic=shelve.open(option_dict['-LTR_dom'])
                            print(list(LTR_dom_dic.keys()))
                            
                            if key in LTR_dom_dic:
                                
                                num_posi=0
                                for position in LTR_dom_dic[key]:
                                    num_posi=num_posi+1
                                    if position[2]=='GAG':
                                        mark_color=(63,72,62)##################################
                                    elif position[2]=='AP':
                                        mark_color=(90,45,123)################################## 
                                    elif position[2]=='RT':
                                        mark_color=(14,80,2)################################## 
                                    elif position[2]=='RNaseH':
                                        mark_color=(44,76,95)################################## 
                                    elif position[2]=='INT':
                                        mark_color=(122,76,18)################################## 
                                    elif position[2]=='ENV':
                                        mark_color=(14,125,117)################################## 
                                    else:
                                        mark_color=(0,200,200)
                                    z=0
                                    
                                    if (float(float(option_dict['-left_space'])+int(position[0])/float(option_dict['-scale']))-(float(float(option_dict['-left_space'])+int(position[1])/float(option_dict['-scale']))))<=0.2:
                                        z=float(option_dict['-match_line'])
                                    
                                    
                                    
                                    dwg.add(dwg.line(
                                        (float(float(option_dict['-left_space'])+(hit_translocation+int(position[0]))/float(option_dict['-scale'])), y_value),
                                        (float(float(option_dict['-left_space'])+(hit_translocation+int(position[1]))/float(option_dict['-scale']))+z, y_value),
                                        stroke=svgwrite.rgb(mark_color[0],mark_color[1],mark_color[2],'%'), stroke_width=float(option_dict['-mark_thick']-2)
                                        )
                                            )
                                    if position[2]=="RNaseH":
                                        txt="RH"
                                    elif position[2]=="INT":
                                        txt="IN"
                                    else:
                                        txt=position[2]
                                    dwg.add(dwg.text(txt,
                                                     insert=(float(float(option_dict['-left_space'])+(hit_translocation+int(position[0]))/float(option_dict['-scale'])),y_value+20),
                                                     fill= svgwrite.rgb(mark_color[0],mark_color[1],mark_color[2],'%'),
                                                     font_size=11
                                                     )
                                            )
                                    
                                    dwg.add(dwg.text(position[3].split('__')[1],
                                                     insert=(float(float(option_dict['-left_space'])+(hit_translocation+int(position[0]))/float(option_dict['-scale'])),y_value+25),
                                                     fill= svgwrite.rgb(mark_color[0],mark_color[1],mark_color[2],'%'),
                                                     font_size=10                                     
                                                     )
                                            )
                                    
                            ##______________LTR domain graph draw_end_____________

        
                    
    
                        for item3 in item2: #separated hit
                            if int(option_dict['-grey_scale'])==2:
                                color_chart_key=str(int(220-(item3[5]-float(option_dict['-identity']))/(1.0-float(option_dict['-identity']))*(220))) #__color_selection from color chart by identity___
                                color_chart=grey_chart[color_chart_key]                                                                             #__color_selection from color chart by identity___
                            p=0
                            if option_dict['-add_h_repeat']!="1":
                                p=4
                            if option_dict['-add_h_gene']!="1":
                                p=4
                                
                            match_line=float(option_dict['-match_line'])
                        
                            dwg.add(dwg.polygon(points=[
                                (float(float(option_dict['-left_space'])+item3[1]/float(option_dict['-scale'])),200+space+float(option_dict['-layer'])*10-7),
                                (float(float(option_dict['-left_space'])+item3[2]/float(option_dict['-scale'])), 200+space+float(option_dict['-layer'])*10-7),
                                (float(float(option_dict['-left_space'])+(hit_translocation+item3[4])/float(option_dict['-scale'])),y_value+2+p),
                                (float(float(option_dict['-left_space'])+(hit_translocation+item3[3])/float(option_dict['-scale'])),y_value+2+p)], stroke=svgwrite.rgb(color_chart[0],color_chart[1],color_chart[2],'%'),stroke_width=match_line, fill=svgwrite.rgb(color_chart[0],color_chart[1],color_chart[2],'%')))
        
            ##________________mark the matched regions to query-start__________
                            if option_dict['-add_q_repeat']=="1":
                                if option_dict['-add_q_gene']=="1":
                                    z=0
                                    if (float(float(option_dict['-left_space'])+item3[1]/float(option_dict['-scale']))-float(float(option_dict['-left_space'])+item3[2]/float(option_dict['-scale'])))<=0.2:
                                        z=float(option_dict['-match_line'])
        
                                    dwg.add(dwg.line( 
                                        (float(float(option_dict['-left_space'])+item3[1]/float(option_dict['-scale'])),200+space+float(option_dict['-layer'])*10),
                                        (float(float(option_dict['-left_space'])+item3[2]/float(option_dict['-scale']))+z, 200+space+float(option_dict['-layer'])*10), stroke='yellow', stroke_width=float(option_dict['-mark_thick'])))
            ##________________mark the matched regions to query-end__________
    
    
        length_list=[] #To clear memory
        length_list_query=[] #To clear memory
    
    
        dwg.save()
    
        #print "\n\nCompleted!!"+str(serial)+"/"+str(separate_num+1)


csv_dic={} # To clear memory
x_query_position=[] # To clear memory
x_hit_position=[] # To clear memory
quit()

