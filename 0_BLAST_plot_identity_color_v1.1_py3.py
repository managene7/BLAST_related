#________________ option parse _______________________________
import sys 

args = sys.argv[1:]

option_dict={'-identity':0.6, '-width':1000.0,'-height':40.0,'-space':180.0, '-scale_temp':1,'-left_space':400,'-grey_scale':1,'-layer':2, '-mark_thick':1,'-out':'default','-num_graph':50,'-width_basis':1,'-right_space':0,'-hyperlink':"",
             '-add_q_repeat':"1", '-add_q_gene':"1", '-add_h_repeat':"1", '-add_h_gene':"1"}
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
-identity       input identity threshold (ex. 0.99, Default is 0.85)
-mark_thick     thickness of matched region mark. 2~10 (default is 8)
-left_space     space of left side (default is 400)
-out            output file name of output that you want to (option)


_____________________________________________________________________________
""")
                quit()
#        else:
#            print "There maybe an option error!"
#            quit()





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

#____________csv position parsing-end_______________________________________    


#__________query and hit length parsing_start________
query=[]
hit=[]
for key in csv_dic:
    if [key,csv_dic[key][0]] not in query:
        query.append([key,csv_dic[key][0]])
    for key2 in csv_dic[key][1]:
        if [key2,csv_dic[key][1][key2][0][0]] not in hit:
            hit.append([key2,csv_dic[key][1][key2][0][0]])


query.sort()

hit.sort()

hit.reverse()

#__________query and hit length parsing_end________

#__________determine scale______________
query_len_tot=0
name_len_list=[]
for cont in query:
    query_len_tot=query_len_tot+int(cont[1])
    name_len_list.append(len(cont[0]))

max_q_name_len=max(name_len_list)
scale= float(query_len_tot)/float(option_dict['-width'])
#_______________________________________

#___________draw frame__________
hit_len_tot=0
hit_len_list=[]
for cont in hit:
    hit_len_tot=hit_len_tot+int(cont[1])
    hit_len_list.append(len(cont[0]))

max_h_name_len=max(hit_len_list)

pic_file_name=option_dict['-csv'][:-4]+"_blast_plot.svg"

import svgwrite
width = int(option_dict['-width'])+600
height = int(float(hit_len_tot)/scale)+650

dwg=svgwrite.Drawing(pic_file_name,(width,height),profile='tiny',debug=True)

#_____color chart draw start___________
blue_chart={'216': (96, 96, 120), '217': (97, 97, 120), '214': (94, 94, 120), '215': (95, 95, 120), '212': (92, 92, 120), '213': (93, 93, 120), '210': (90, 90, 120), '211': (91, 91, 120), '218': (98, 98, 120), '219': (99, 99, 120), '133': (13, 13, 120), '132': (12, 12, 120), '131': (11, 11, 120), '130': (10, 10, 120), '137': (17, 17, 120), '136': (16, 16, 120), '135': (15, 15, 120), '134': (14, 14, 120), '95': (0, 0, 95), '139': (19, 19, 120), '138': (18, 18, 120), '225': (105, 105, 120), '24': (0, 0, 24), '25': (0, 0, 25), '26': (0, 0, 26), '224': (104, 104, 120), '20': (0, 0, 20), '21': (0, 0, 21), '22': (0, 0, 22), '23': (0, 0, 23), '223': (103, 103, 120), '28': (0, 0, 28), '29': (0, 0, 29), '222': (102, 102, 120), '0': (0, 0, 0), '221': (101, 101, 120), '8': (0, 0, 8), '220': (100, 100, 120), '68': (0, 0, 68), '87': (0, 0, 87), '227': (107, 107, 120), '120': (0, 0, 120), '121': (1, 1, 120), '122': (2, 2, 120), '123': (3, 3, 120), '124': (4, 4, 120), '125': (5, 5, 120), '126': (6, 6, 120), '127': (7, 7, 120), '128': (8, 8, 120), '129': (9, 9, 120), '69': (0, 0, 69), '91': (0, 0, 91), '59': (0, 0, 59), '58': (0, 0, 58), '55': (0, 0, 55), '54': (0, 0, 54), '57': (0, 0, 57), '56': (0, 0, 56), '51': (0, 0, 51), '50': (0, 0, 50), '53': (0, 0, 53), '52': (0, 0, 52), '90': (0, 0, 90), '201': (81, 81, 120), '199': (79, 79, 120), '198': (78, 78, 120), '200': (80, 80, 120), '195': (75, 75, 120), '194': (74, 74, 120), '197': (77, 77, 120), '196': (76, 76, 120), '191': (71, 71, 120), '190': (70, 70, 120), '193': (73, 73, 120), '192': (72, 72, 120), '115': (0, 0, 115), '114': (0, 0, 114), '117': (0, 0, 117), '116': (0, 0, 116), '111': (0, 0, 111), '110': (0, 0, 110), '113': (0, 0, 113), '112': (0, 0, 112), '82': (0, 0, 82), '205': (85, 85, 120), '80': (0, 0, 80), '81': (0, 0, 81), '119': (0, 0, 119), '118': (0, 0, 118), '84': (0, 0, 84), '204': (84, 84, 120), '207': (87, 87, 120), '66': (0, 0, 66), '206': (86, 86, 120), '226': (106, 106, 120), '27': (0, 0, 27), '3': (0, 0, 3), '7': (0, 0, 7), '92': (0, 0, 92), '108': (0, 0, 108), '109': (0, 0, 109), '240': (120, 120, 120), '102': (0, 0, 102), '103': (0, 0, 103), '100': (0, 0, 100), '101': (0, 0, 101), '106': (0, 0, 106), '107': (0, 0, 107), '104': (0, 0, 104), '105': (0, 0, 105), '39': (0, 0, 39), '38': (0, 0, 38), '33': (0, 0, 33), '32': (0, 0, 32), '31': (0, 0, 31), '30': (0, 0, 30), '37': (0, 0, 37), '36': (0, 0, 36), '35': (0, 0, 35), '34': (0, 0, 34), '94': (0, 0, 94), '86': (0, 0, 86), '60': (0, 0, 60), '61': (0, 0, 61), '62': (0, 0, 62), '63': (0, 0, 63), '64': (0, 0, 64), '65': (0, 0, 65), '179': (59, 59, 120), '178': (58, 58, 120), '177': (57, 57, 120), '176': (56, 56, 120), '175': (55, 55, 120), '174': (54, 54, 120), '173': (53, 53, 120), '172': (52, 52, 120), '171': (51, 51, 120), '170': (50, 50, 120), '203': (83, 83, 120), '182': (62, 62, 120), '183': (63, 63, 120), '180': (60, 60, 120), '181': (61, 61, 120), '186': (66, 66, 120), '187': (67, 67, 120), '184': (64, 64, 120), '185': (65, 65, 120), '188': (68, 68, 120), '189': (69, 69, 120), '202': (82, 82, 120), '4': (0, 0, 4), '97': (0, 0, 97), '6': (0, 0, 6), '99': (0, 0, 99), '98': (0, 0, 98), '168': (48, 48, 120), '169': (49, 49, 120), '229': (109, 109, 120), '228': (108, 108, 120), '164': (44, 44, 120), '165': (45, 45, 120), '166': (46, 46, 120), '167': (47, 47, 120), '160': (40, 40, 120), '161': (41, 41, 120), '162': (42, 42, 120), '163': (43, 43, 120), '11': (0, 0, 11), '10': (0, 0, 10), '13': (0, 0, 13), '12': (0, 0, 12), '15': (0, 0, 15), '14': (0, 0, 14), '17': (0, 0, 17), '16': (0, 0, 16), '19': (0, 0, 19), '18': (0, 0, 18), '88': (0, 0, 88), '93': (0, 0, 93), '89': (0, 0, 89), '151': (31, 31, 120), '150': (30, 30, 120), '153': (33, 33, 120), '152': (32, 32, 120), '155': (35, 35, 120), '154': (34, 34, 120), '157': (37, 37, 120), '156': (36, 36, 120), '159': (39, 39, 120), '158': (38, 38, 120), '238': (118, 118, 120), '239': (119, 119, 120), '83': (0, 0, 83), '234': (114, 114, 120), '235': (115, 115, 120), '236': (116, 116, 120), '237': (117, 117, 120), '230': (110, 110, 120), '231': (111, 111, 120), '232': (112, 112, 120), '233': (113, 113, 120), '48': (0, 0, 48), '49': (0, 0, 49), '46': (0, 0, 46), '47': (0, 0, 47), '44': (0, 0, 44), '45': (0, 0, 45), '42': (0, 0, 42), '43': (0, 0, 43), '40': (0, 0, 40), '41': (0, 0, 41), '1': (0, 0, 1), '5': (0, 0, 5), '9': (0, 0, 9), '85': (0, 0, 85), '146': (26, 26, 120), '147': (27, 27, 120), '144': (24, 24, 120), '145': (25, 25, 120), '142': (22, 22, 120), '143': (23, 23, 120), '140': (20, 20, 120), '141': (21, 21, 120), '209': (89, 89, 120), '208': (88, 88, 120), '148': (28, 28, 120), '149': (29, 29, 120), '77': (0, 0, 77), '76': (0, 0, 76), '75': (0, 0, 75), '74': (0, 0, 74), '73': (0, 0, 73), '72': (0, 0, 72), '71': (0, 0, 71), '70': (0, 0, 70), '96': (0, 0, 96), '79': (0, 0, 79), '78': (0, 0, 78), '2': (0, 0, 2), '67': (0, 0, 67)}
red_chart={'216': (120, 96, 96), '217': (120, 97, 97), '214': (120, 94, 94), '215': (120, 95, 95), '212': (120, 92, 92), '213': (120, 93, 93), '210': (120, 90, 90), '211': (120, 91, 91), '218': (120, 98, 98), '219': (120, 99, 99), '133': (120, 13, 13), '132': (120, 12, 12), '131': (120, 11, 11), '130': (120, 10, 10), '137': (120, 17, 17), '136': (120, 16, 16), '135': (120, 15, 15), '134': (120, 14, 14), '139': (120, 19, 19), '138': (120, 18, 18), '166': (120, 46, 46), '24': (24, 0, 0), '25': (25, 0, 0), '26': (26, 0, 0), '224': (120, 104, 104), '20': (20, 0, 0), '21': (21, 0, 0), '22': (22, 0, 0), '23': (23, 0, 0), '160': (120, 40, 40), '28': (28, 0, 0), '29': (29, 0, 0), '222': (120, 102, 102), '0': (0, 0, 0), '4': (4, 0, 0), '8': (8, 0, 0), '220': (120, 100, 100), '87': (87, 0, 0), '227': (120, 107, 107), '3': (3, 0, 0), '120': (120, 0, 0), '121': (120, 1, 1), '122': (120, 2, 2), '123': (120, 3, 3), '124': (120, 4, 4), '125': (120, 5, 5), '126': (120, 6, 6), '127': (120, 7, 7), '128': (120, 8, 8), '129': (120, 9, 9), '69': (69, 0, 0), '59': (59, 0, 0), '58': (58, 0, 0), '55': (55, 0, 0), '54': (54, 0, 0), '57': (57, 0, 0), '56': (56, 0, 0), '51': (51, 0, 0), '50': (50, 0, 0), '53': (53, 0, 0), '52': (52, 0, 0), '90': (90, 0, 0), '164': (120, 44, 44), '201': (120, 81, 81), '199': (120, 79, 79), '198': (120, 78, 78), '147': (120, 27, 27), '195': (120, 75, 75), '194': (120, 74, 74), '197': (120, 77, 77), '196': (120, 76, 76), '191': (120, 71, 71), '190': (120, 70, 70), '193': (120, 73, 73), '192': (120, 72, 72), '115': (115, 0, 0), '114': (114, 0, 0), '88': (88, 0, 0), '116': (116, 0, 0), '111': (111, 0, 0), '110': (110, 0, 0), '113': (113, 0, 0), '112': (112, 0, 0), '82': (82, 0, 0), '205': (120, 85, 85), '80': (80, 0, 0), '81': (81, 0, 0), '86': (86, 0, 0), '118': (118, 0, 0), '84': (84, 0, 0), '204': (120, 84, 84), '207': (120, 87, 87), '141': (120, 21, 21), '226': (120, 106, 106), '27': (27, 0, 0), '179': (120, 59, 59), '177': (120, 57, 57), '7': (7, 0, 0), '92': (92, 0, 0), '225': (120, 105, 105), '108': (108, 0, 0), '109': (109, 0, 0), '102': (102, 0, 0), '103': (103, 0, 0), '100': (100, 0, 0), '101': (101, 0, 0), '106': (106, 0, 0), '107': (107, 0, 0), '104': (104, 0, 0), '105': (105, 0, 0), '39': (39, 0, 0), '38': (38, 0, 0), '33': (33, 0, 0), '32': (32, 0, 0), '31': (31, 0, 0), '30': (30, 0, 0), '37': (37, 0, 0), '36': (36, 0, 0), '35': (35, 0, 0), '34': (34, 0, 0), '94': (94, 0, 0), '223': (120, 103, 103), '60': (60, 0, 0), '61': (61, 0, 0), '62': (62, 0, 0), '63': (63, 0, 0), '64': (64, 0, 0), '65': (65, 0, 0), '66': (66, 0, 0), '178': (120, 58, 58), '68': (68, 0, 0), '176': (120, 56, 56), '175': (120, 55, 55), '174': (120, 54, 54), '173': (120, 53, 53), '172': (120, 52, 52), '171': (120, 51, 51), '170': (120, 50, 50), '203': (120, 83, 83), '145': (120, 25, 25), '182': (120, 62, 62), '183': (120, 63, 63), '180': (120, 60, 60), '181': (120, 61, 61), '162': (120, 42, 42), '187': (120, 67, 67), '184': (120, 64, 64), '185': (120, 65, 65), '186': (120, 66, 66), '188': (120, 68, 68), '189': (120, 69, 69), '221': (120, 101, 101), '6': (6, 0, 0), '99': (99, 0, 0), '98': (98, 0, 0), '168': (120, 48, 48), '169': (120, 49, 49), '229': (120, 109, 109), '228': (120, 108, 108), '91': (91, 0, 0), '165': (120, 45, 45), '93': (93, 0, 0), '167': (120, 47, 47), '95': (95, 0, 0), '161': (120, 41, 41), '97': (97, 0, 0), '163': (120, 43, 43), '11': (11, 0, 0), '10': (10, 0, 0), '13': (13, 0, 0), '12': (12, 0, 0), '15': (15, 0, 0), '14': (14, 0, 0), '17': (17, 0, 0), '16': (16, 0, 0), '19': (19, 0, 0), '18': (18, 0, 0), '117': (117, 0, 0), '89': (89, 0, 0), '151': (120, 31, 31), '150': (120, 30, 30), '153': (120, 33, 33), '152': (120, 32, 32), '155': (120, 35, 35), '154': (120, 34, 34), '157': (120, 37, 37), '156': (120, 36, 36), '159': (120, 39, 39), '158': (120, 38, 38), '238': (120, 118, 118), '239': (120, 119, 119), '83': (83, 0, 0), '234': (120, 114, 114), '235': (120, 115, 115), '236': (120, 116, 116), '237': (120, 117, 117), '230': (120, 110, 110), '231': (120, 111, 111), '232': (120, 112, 112), '233': (120, 113, 113), '48': (48, 0, 0), '49': (49, 0, 0), '46': (46, 0, 0), '119': (119, 0, 0), '44': (44, 0, 0), '45': (45, 0, 0), '42': (42, 0, 0), '43': (43, 0, 0), '40': (40, 0, 0), '41': (41, 0, 0), '1': (1, 0, 0), '5': (5, 0, 0), '9': (9, 0, 0), '85': (85, 0, 0), '146': (120, 26, 26), '200': (120, 80, 80), '144': (120, 24, 24), '202': (120, 82, 82), '142': (120, 22, 22), '143': (120, 23, 23), '140': (120, 20, 20), '206': (120, 86, 86), '209': (120, 89, 89), '208': (120, 88, 88), '148': (120, 28, 28), '149': (120, 29, 29), '77': (77, 0, 0), '76': (76, 0, 0), '75': (75, 0, 0), '74': (74, 0, 0), '73': (73, 0, 0), '72': (72, 0, 0), '71': (71, 0, 0), '70': (70, 0, 0), '96': (96, 0, 0), '79': (79, 0, 0), '78': (78, 0, 0), '2': (2, 0, 0), '47': (47, 0, 0), '67': (67, 0, 0)}


n=30
dwg.add(dwg.text(option_dict['-csv'], insert=(320,100), fill='purple' ))
dwg.add(dwg.text("Similarity", insert=(320,160), fill='purple' ))
dwg.add(dwg.text("100%", insert=(280,190), fill='purple' ))
dwg.add(dwg.text("60%", insert=(420,190), fill='purple' ))
for i in range(190):
    dwg.add(dwg.line((305+float(n)/2,170), (305+float(n)/2,180), stroke=svgwrite.rgb(blue_chart[str(n)][0],blue_chart[str(n)][1],blue_chart[str(n)][2],'%'), stroke_width=0.5))
    dwg.add(dwg.line((305+float(n)/2,190), (305+float(n)/2,200), stroke=svgwrite.rgb(red_chart[str(n)][0],red_chart[str(n)][1],red_chart[str(n)][2],'%'), stroke_width=0.5))
    n=n+1
    
    #svgwrite.rgb(blue_chart[str(n)][0],blue_chart[str(n)][1],blue_chart[str(n)][2])
    #svgwrite.rgb(red_chart[str(n)][0],red_chart[str(n)][1],red_chart[str(n)][2])

#_____color chart draw end___________



#dwg.add(dwg.rect(insert = (max_q_name_len*10,50),
#                 size = (int(float(query_len_tot)/scale), int(float(hit_len_tot)/scale)),
#                 stroke="black",
#                 stroke_width=1,
#                 fill="none"))


print("\n\nScale =",int(float(hit_len_tot)/scale),'\n\n\n')
##_________vertical line____________
interval=0

query_x_axis={} #==> x axis for plotting


left_space=max_h_name_len*10+100
top_space=250


for cont in query:
    query_x_axis[cont[0]]=interval
    
    dwg.add(dwg.line(start = (left_space+interval,top_space),
                     end = (left_space+interval, int(top_space+float(hit_len_tot)/scale)),
                     stroke = "black",
                     stroke_width = 0.5)
            )
    ###__________x-axis name_start___________
    x=left_space+interval+int((float(cont[1])/scale+0.5)/2)
    y=int(top_space+float(hit_len_tot)/scale)+max_q_name_len*10
    dwg.add(dwg.text(cont[0],
                     insert=(10,10),
                     transform='translate(%s,%s) rotate(-90)' % (str(x),str(y))
                    ))
    ###__________x-axis name_end___________
    
    interval=interval+int(float(cont[1])/scale+0.5)
    

dwg.add(dwg.line(start = (left_space+interval,top_space),
                 end = (left_space+interval, top_space+int(float(hit_len_tot)/scale)),
                 stroke = "black",
                 stroke_width = 0.5)
        )
dwg.add(dwg.text("0", insert=(left_space-13,top_space+int(float(hit_len_tot)/scale+16)), fill='black' ))
        
##_________horizontal line____________
interval=0

hit_y_axis={} #==> y axis for plotting

for cont in hit:
    
    
    dwg.add(dwg.line(start = (left_space,top_space+interval),
                     end = (int(left_space + float(query_len_tot)/scale), top_space+interval),
                     stroke = "black",
                     stroke_width = 0.5)
            )
    ###__________x-axis name_start___________
    x=100
    y=top_space+interval+int((float(cont[1])/scale+0.5)/2)
    dwg.add(dwg.text(cont[0],
                     insert=(x,y)                     
                    ))
    ###__________x-axis name_end___________

    
    interval=interval+int(float(cont[1])/scale+0.5)

    hit_y_axis[cont[0]]=interval

dwg.add(dwg.line(start = (left_space,top_space+interval),
                 end = (int(left_space+ float(query_len_tot)/scale), top_space+interval),
                 stroke = "black",
                 font_family = 'arial',
                 font_size=20,
                 stroke_width = 0.5)
        )

##_________plot line____________

for key in csv_dic:
    for key2 in csv_dic[key][1]:
        for sub_list in csv_dic[key][1][key2]:
            q_s_pre=float(sub_list[1])
            q_e_pre=float(sub_list[2])
            h_s_pre=float(sub_list[3])
            h_e_pre=float(sub_list[4])
            identity_pre=float(sub_list[5])
            identity_converted=str(int(505-identity_pre*475))
            

            q_s=left_space+query_x_axis[key] + int(q_s_pre/scale+0.5)
            h_s=top_space+hit_y_axis[key2] - int(h_s_pre/scale+0.5)
            q_e=left_space+query_x_axis[key] + int(q_e_pre/scale+0.5)
            h_e=top_space+hit_y_axis[key2] - int(h_e_pre/scale+0.5)

            if q_s_pre > q_e_pre or h_s_pre > h_e_pre:
                col=(blue_chart[identity_converted][0],blue_chart[identity_converted][1],blue_chart[identity_converted][2])
            else:
                col=(red_chart[identity_converted][0],red_chart[identity_converted][1],red_chart[identity_converted][2])
                

            if (q_s,h_s) != (q_e, h_e):
                dwg.add(dwg.line(start = (q_s,h_s),
                                 end = (q_e, h_e),
                                 stroke = svgwrite.rgb(col[0],col[1],col[2],'%'),
                                 stroke_width = float(option_dict['-mark_thick']))
                        )
            else:
                dwg.add(dwg.ellipse(center=(q_s, h_s),
                                    r=(0.5,0.5),
                                    stroke=svgwrite.rgb(col[0],col[1],col[2],'%'),
                                    stroke_width=0,
                                    fill=svgwrite.rgb(col[0],col[1],col[2],'%')))
                                    



dwg.save()

