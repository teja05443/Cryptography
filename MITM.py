def main():
    # Input the prime number p and primitive root alpha
    p = int(input("Enter the prime number P: "))
    alpha = int(input("Enter the primitive root of P: "))

    # Input the private keys of Users A, B, and Darth (the attacker)
    Xa = int(input("Enter the private key of User A: "))
    Xb = int(input("Enter the private key of User B: "))
    Xc = int(input("Enter the private key of Darth (attacker): "))

    # Compute the public keys of User A and User B
    Ya = pow(alpha, Xa, p)  # Public key for User A
    Yb = pow(alpha, Xb, p)  # Public key for User B

    print(f"\nPublic key of User A (Ya): {Ya}")
    print(f"Public key of User B (Yb): {Yb}")

    # Darth (the attacker) computes his own public keys
    Yc_to_A = pow(alpha, Xc, p)  # Public key sent to Alice
    Yc_to_B = pow(alpha, Xc, p)  # Public key sent to Bob

    print(f"\nDarth's public key sent to User A (Yc_to_A): {Yc_to_A}")
    print(f"Darth's public key sent to User B (Yc_to_B): {Yc_to_B}")

    # Alice computes her shared secret key (thinking it's with Bob)
    Ka_darth = pow(Yc_to_A, Xa, p)  # Shared key between Alice and Darth
    print(f"\nAlice's secret key with Darth (Ka_darth): {Ka_darth}")

    # Bob computes his shared secret key (thinking it's with Alice)
    Kb_darth = pow(Yc_to_B, Xb, p)  # Shared key between Bob and Darth
    print(f"Bob's secret key with Darth (Kb_darth): {Kb_darth}")

if __name__ == "__main__":
    main()
