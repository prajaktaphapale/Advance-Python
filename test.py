def simple_interest(p, n, r):
    """
    This function takes Principle, Number of years and rate of intrest as input
    output simple Intrest with amount
    """
    I = (p*n*r)/100
    A= p + I
    return I ,A

if __name__  == "__main__":
    I1, A1 = simple_interest(p=570000, n=5 ,r=7.5)
    print(f"Simple Interest : {I1:.2f}")
    print(f"Amount : {A1:.2f}")

    