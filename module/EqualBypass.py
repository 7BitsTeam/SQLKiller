import re
def EqualBypass(source):
    rets=[]
    for exp in source:
        output=exp.replace("="," like ")
        output1=exp.replace("=","  regexp '") + "'"
        
        rets.append(output1)
        rets.append(output)
        
        '''
        output2=exp.split("=")
        part1=int(output2[1])
        part2=int(output2[1])+1
        outpu3=output2[0] +" < "+str(part2)
        rets.append(outpu3)
	'''
        
        r=re.findall(r"([\d]+[\s\S]*)=[\s\S]*?([\d]+)",exp)
        part1=r[0][0]
        part2=int(r[0][1]) + 1
        outpu3=part1 + "<" + str(part2)
        rets.append(outpu3)
    return rets


