from itertools import permutations

def UpperCase(source):
    ret=[]
    len_source=len(source)
    
    quantity_to_change_buffer=[]
    for i in range(0,len_source):
        quantity_to_change_buffer.append(i)
    for quantity_to_change in quantity_to_change_buffer:
        index_to_change_buffer=getIndex(quantity_to_change+1,quantity_to_change_buffer)
        for index_list in index_to_change_buffer:
            temp_source=[]
            for c in source:
                temp_source.append(c)
            
            for i in range(0,len_source):
                for index in index_list:
                    if index == i:
                        temp_source[index]=source[index].upper()
            temp_source_str=""
            for c_str in temp_source:
                temp_source_str=temp_source_str+str(c_str)
            ret.append(temp_source_str)
    return list(set(ret))
 

def getIndex(num,buffer):
    indexs=[]
    init_index=0
    for str_tmp in permutations(buffer,num):
        indexs.append(list(str_tmp))
    return indexs
    
def UpperCaseMain(source):
    for exp in source:
        rets=[]
        while_list=["and","union","select","or"]
        for s in while_list:
            if s in exp.lower():
                payloads=UpperCase(s)
                for payload in payloads:
                    #print(payload)
                    ret=exp.lower().replace(s,payload)
                    rets.append(ret)
    return rets

#print(UpperCase("Union Select"))
#print(UpperCaseMain(["and"]))



