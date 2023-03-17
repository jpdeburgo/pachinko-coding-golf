v={'.':1,'_':0,'/':-1,'\\':1}
def e(s,t=0):
    for p,c in enumerate(s):t+=r(s,p,v[c])if c in'\/'else (r(s,p,1)+r(s,p,-1))/2 if c=='|'else v[c]
    return int((t*100)/len(s))
def r(s,p,d):return 0 if p+d>=len(s)or p+d<0 or s[p+d]in'\/|'else(r(s,p+d,d)if s[p+d]=='_'else 1)