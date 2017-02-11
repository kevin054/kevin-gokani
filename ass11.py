def compound(p,t,r):
    A=p*(1+r/100)**t
    return A
p=int(raw_input("please enter the principal amount"))
t=int(raw_input("please enter the time per year"))
r=float(raw_input("please enter the interest in percantage"))
c=compound(p,t,r)
print c
