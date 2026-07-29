def target_sum_subsets(values,target):
    out=[]; n=len(values)
    for mask in range(1<<n):
        subset=[values[i] for i in range(n) if mask>>i&1]
        if sum(subset)==target:out.append(subset)
    return sorted(out,key=lambda x:(len(x),x))
