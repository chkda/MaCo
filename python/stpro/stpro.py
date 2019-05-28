import torch as tc 

def fact(n):
    ## input must be a torch tensor
    ## output is the factorial of given input
    pi = tc.tensor(3.142,dtype=tc.float32) ##pi
    n_fact = tc.pow((2*pi),0.5) * n * tc.pow(n,(n+0.5)) * tc.exp((-n)) ##Stirling Formula
    return tc.ceil(n_fact)

x = fact(tc.tensor([2],dtype=tc.float32))
print(x)