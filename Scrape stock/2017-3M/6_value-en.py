# -*- coding: utf-8 -*-
"""
Created on Sun Dec 04 22:19:23 2016

@author: Home
"""
count_stock = 0
from datetime import datetime
def time_stamp():
    tstamp = datetime.now()
    return tstamp
    
##Steps
# open read file   //
# read content     //
# split content    //
# open write file
# write content
# add header

def read_content(file_read):
    f = open(file_read,'r')
    contents = f.read()
    contents = str(contents)
    f.close()
    return contents


def split_token(start_a,end_a,token):
    split_token = (token.split(start_a))[1].split(end_a)[0]
    split_token = split_token.strip()    
    return split_token
    print split_token
    
def addheader(header,file_data,file_new):
    file_header = 'header.txt'

    f1 = open(file_header,'w')
    for field in header:
        f1.write(field+'\t')
    f1.close()
    
    f1 = open(file_header,'r')
    content = f1.read()
    f1.close()
    
    f1 = open(file_header,'w')
    f1.write(content+'\n')
    f1.close()
               
    filenames = [file_header,file_data]
    with open(file_new, 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
    print '>>> finish >>> Function_add header: '+ file_name

print '=========================== Start record time ==============================' 
tstart = time_stamp()
print tstart

print '=========================== Stock list ==============================' 
######## Select stock name ############
filename = []
stockname = open('004_allstock.txt','r')
for name in stockname:
    name = name.strip()
    print name
    filename.append(name)
print filename
stockname.close()

#filename = ['au','col']
print filename 
print '=========================== value - statement =============================='  
  
f2 = open('value-en.txt','w')
   
for name in filename[0:3]:
    name = name.strip() 
    
    file_read = ('Factsheet_en_'+str(name)+'.txt') 
    count_stock +=1         
    try:
        contents = read_content(file_read)
### 2. Find year ############ 
        token = contents      
        start_a = '<td align="left" class="factsheet-head"><strong>Statement of Comprehensive Income (MB.)</strong></td>'
        end_a = '</tr>'  
        phase = split_token(start_a,end_a,token)         
        lines_year = phase.splitlines()
        year_statement = []       
        for line in lines_year:
            token = line
            start_a = 'nowrap="nowrap"><strong>'
            end_a = '\xc2\xa0<br/>'
            phase = split_token(start_a,end_a,token)
            year_statement.append(phase) 
            print name +' '+phase
    except :
        print name+' no content'           
############ 3.Find value ############       
    topics_b = ['Total Revenues','COGs','SG&amp;A','Net Profit','EPS (B.)'\
#    ,'Cash'\
    ,'Operating Cash Flow                                                                                   '\
    ,'Investing Cash Flow                                                                                   '\
    ,'Financing Cash Flow                                                                                   '\
    ,'D/E (X)','Gross Profit Margin (%)','Net Profit Margin (%)']      
# ****แก้ไข Cash - Not unique >> remove only header 
    for topic in topics_b:
        count = -1                
        try:
            contents = read_content(file_read)
            token = contents
            start_a = topic+'</td>'
            end_a = '</tr>'              
            phase = split_token(start_a,end_a,token)
            lines_value = phase.splitlines()           
            for line in lines_value:                
                token = line
                start_a = 'nowrap="nowrap">'
                end_a = '</td>'               
                count = count+1
                year = year_statement[count]
                phase = split_token(start_a,end_a,token)
                data_b = str(name+'\t'+topic.strip()+'\t'+year+'\t'+phase+'\n')
                f2.write(data_b)            
        except :
            print name+' '+topic +' error no content'        
print '=========================== value - statistic =============================='           
############ 1. import content_stock (part a) year,value ############

for name in filename:
    name = name.strip()
    file_read = ('Factsheet_en_'+str(name)+'.txt') 
      
    try:
        contents = read_content(file_read)      
        token = contents
        start_a = '<td align="left" class="factsheet-head" nowrap="nowrap" width="25%"><strong>Statistics</strong></td>'
        end_a = '</tr>'
        phase_stat = split_token(start_a,end_a,token)       
        year_stat = []         
        lines_year_0 = phase_stat.splitlines()
        print phase_stat
        print '======phase_stat========'
        for line in lines_year_0:
            token = line            
            start_a = 'nowrap="nowrap"><strong>'
            end_a = '</td>'
            phase_year = split_token(start_a,end_a,token)         
            print phase_year
            print '===========phase year============'
            
            if phase_year.startswith('YTD'):
                token = phase_stat
                start_a = '<br/>'
                end_a = '</strong>'                
                phase_YTD = split_token(start_a,end_a,token)
            else:
                token = line
                start_a = 'nowrap="nowrap"><strong>'
                end_a = '<'
                phase_YTD = split_token(start_a,end_a,token)
            year_a = phase_YTD.strip()
            year_stat.append(year_a)
            print year_stat
            print '============year stat=============='            
    except :
        print name + '***error statistic'
############ 3.Find value ############
    topics_a = ['Market Cap (MB.)'\
    ,'Price (B./share)'\
    ,'P/E (X)'\
    ,'Dividend Yield (%)'\
    ]   
    for topic in topics_a:
        count_a = -1
            
        try:
            contents = read_content(file_read)
            token = contents
            start_a = '<td align="left" class="factsheet-head" nowrap="nowrap" width="25%"><strong>Statistics</strong></td>'
            end_a = '<td class="factsheet" nowrap="nowrap">Dividend Policy</td>'
            phase = split_token(start_a,end_a,token)
            token = phase
            start_a = topic+'</td>'
            end_a = '</tr>'
            phase = split_token(start_a,end_a,token)           
            lines_value_a = phase.splitlines()
            for line in lines_value_a:
                count_a = count_a+1
                year_a = year_stat[count_a]
                token = line
                start_a = '">'
                end_a = '</td>'
                phase = split_token(start_a,end_a,token)
                phase = phase[:-2]
                data_a = str(name+'\t'+topic.strip()+'\t'+year_a+'\t'+phase+'\n')
                f2.write(data_a)               
        except :
            print name+'\t'+topic+' = no content'
        print '>>> finish >>> part a: '+ str(count_a) +' '+name                       
f2.close() 
print '===========================end ==============================\n' 
############ Company name (Thai) ############

print '=========================== value - business detail =============================='
############ Function: record business detail ############
f2 = open('Business.txt','w')
def busdetail(name):
    name = name.strip() 
    try:
        f = open('Factsheet_th_'+str(name)+'.txt','r')
        content_stock = f.read()
        content_stock = str(content_stock)
        f.close()
        
        token = content_stock
        start_a = '<td class="factsheet-head"><strong>ลักษณะธุรกิจ</strong></td>'
        end_a = '</table>'

        phase = split_token(start_a,end_a,token)

        token = phase
        start_a = '<td class="factsheet">'
        end_a = '</td>'
        phase = split_token(start_a,end_a,token)
        name = name.upper()
        result_Busdetail = name+'\t'+phase+'\n'

        f2.write(result_Busdetail)

    except :
        print name + ' error Business detail'
    print '>>> finish >>> Function_record business detail: '+name
    
print '=========================== value - div =============================='
############ Function: record นโยบายเงินปันผล ############
f3 = open('dv.txt','w')
def dvdetail(name):
    name = name.strip() 
    try:
        f = open('Factsheet_th_'+str(name)+'.txt','r') 
        content_stock = f.read()
        content_stock = str(content_stock)
        f.close()

        token = content_stock
        start_a = '<td class="factsheet" nowrap="nowrap">นโยบายเงินปันผล</td>'
        end_a = '</table>'  
        phase = split_token(start_a,end_a,token)

        token =phase
        start_a = '<td class="factsheet" colspan="3">'
        end_a = '</td>'
        phase = split_token(start_a,end_a,token)
        name = name.upper()
        result_dvdetail = name+'\t'+phase+'\n'

        f3.write(result_dvdetail)

    except :
        print name + ' error dividen detail'
    print '>>> finish >>> Function_record dv detail: '+name

print '=========================== value - company name =============================='
############ company name ############
f4 = open('Company_name_th.txt','w')
def compname(name):
    name = name.strip() 
    try:
        f = open('Factsheet_th_'+str(name)+'.txt','r') 
        content_stock = f.read()
        content_stock = str(content_stock)
        f.close()

        token = content_stock
        start_a = '<td align="left" class="topic-blue" nowrap="nowrap">สรุปข้อสนเทศบริษัทจดทะเบียน</td>'
        end_a = '<td align="left" class="factsheet-noline" nowrap="nowrap">CG Report:   -    </td>'
        phase = split_token(start_a,end_a,token)

        token = phase   
        start_a = '<td class="factsheet-heading2" valign="bottom">'
        end_a = ' </td>'
        phase = split_token(start_a,end_a,token)
        name = name.upper()
        result_co = name+'\t'+phase+'\n'

        f4.write(result_co)

    except :
        print name + ' error compname'
    print '>>> finish >>> Function_record company name: '+name

print '=========================== value - ind name =============================='    
############ industry name ############

f5 = open('Ind_name_en.txt','w')
def indname(name):
    name = name.strip() 
    try:
        f = open('Factsheet_en_'+str(name)+'.txt','r') 
        content_stock = f.read()
        content_stock = str(content_stock)
        f.close()
      
        token = content_stock
        start_a = '<td align="left" class="topic-blue" nowrap="nowrap">Company Summary</td>'
        end_a = '<td align="left" class="factsheet-noline" nowrap="nowrap">CG Report:   -    </td>'
        phase = split_token(start_a,end_a,token)
        
        token = phase
        start_a = '<td align="left" class="factsheet-noline" nowrap="nowrap">'
        end_a = '    </td>'
        phase = split_token(start_a,end_a,token)

        name = name.upper()
        result_ind = name+'\t'+phase+'\n'
    
        print result_ind
        f5.write(result_ind)

    except :
        print name + ' error ind_name'
    print '>>> finish >>> Function_record industry name: '+name
    
############ 4. import business detail ############
print '=========================== add header =============================='

for name in filename:
    busdetail(name)
    dvdetail(name)
    compname(name)
    indname(name)
    print '==============='
    
f2.close()
f3.close()
f4.close()
f5.close()

############  Add header - statement data ############
header = ['Name','Topic','Year','Value']
file_data = 'value-en.txt'
file_name = 'value-en_header.txt'
addheader(header,file_data,file_name)

############  Add header - business detail ############
header = ['Name','Business_detail']
file_data = 'Business.txt'
file_name = 'Business_header.txt'
addheader(header,file_data,file_name)

############  Add header - dv detail ############
header = ['Name','Divident_detail']
file_data = 'dv.txt'
file_name = 'dv_header.txt'
addheader(header,file_data,file_name)

############  Add header - company name ############
header = ['Name','Company_name']
file_data = 'Company_name_th.txt'
file_name = 'Company_name_th_header.txt'
addheader(header,file_data,file_name)

############  Add header - industry ############
header = ['Name','Ind']
file_data = 'Ind_name_en.txt'
file_name = 'Ind_name_en_header.txt'
addheader(header,file_data,file_name)

### recode start and end time (part2) ###

tend = time_stamp()
print '===========Time stamp==================='
print str(tstart) + ' << start'
print str(tend) + ' << end'
running_time = tend-tstart
print str(running_time) + ' << running'
print count_stock
print '========================================'


