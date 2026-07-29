def modular_power_queries(queries):
    out=[]
    for base,e,m in queries:
        result=1%m; base%=m
        while e:
            if e&1: result=result*base%m
            base=base*base%m; e//=2
        out.append(result)
    return out
