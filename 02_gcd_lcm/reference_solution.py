from math import gcd

def synchronisation_plan(periods):
    sync=1
    for p in periods: sync=(sync//gcd(sync,p))*p
    return sync,[sync//p for p in periods]
