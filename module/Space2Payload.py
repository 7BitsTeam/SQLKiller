from itertools import permutations

def Space2Payload(source):
    rets=[]
    payload = ['%0a','%0b','/**/','/*!*/','/*!44444*/','/*!99999*/']
    for exp in source:
        for i in range(1, len(payload)):
            for j in permutations(payload, i+1):
                st = ''.join(j)
                res = exp.replace(' ',st)
                rets.append(res)

    return rets