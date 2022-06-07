def EqualBypass(source):
    rets=[]
    for exp in source:
        output=exp.replace("="," like ")
        rets.append(output)
    return rets