def power(a,b,p):
    return pow(a,b,p)

def main():
    p = int(input("Enter the prime number P"))
    alpha = int(input("Enter the primitive root of p"))
    
    # Choosing the private keys of Xa and Xb
    Xa = int(input("Enter the private key of user A"))
    Xb = int(input("Enter the private key of user B"))

    # Computing the Public keys of each user
    Ya = power(alpha,Xa,p)
    print("The public key of user A is:",Ya)
    Yb = power(alpha,Xb,p)
    print("The public key of user B is:",Yb)

    # Sharing the publlic keys and then Computing the common secret key
    Ka = power(Yb,Xa,p)
    Kb = power(Ya,Xb,p)
    print("The secret key of A is:",Ka)
    print("The secret key of user B is:",Kb)

if __name__ == "__main__":
    main()