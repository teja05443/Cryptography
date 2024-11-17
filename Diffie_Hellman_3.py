def main():
    # Input the prime number p and primitive root alpha
    p = int(input("Enter the prime number P: "))
    alpha = int(input("Enter the primitive root of P: "))

    # Input the private keys of Users A, B, and C
    Xa = int(input("Enter the private key of User A: "))
    Xb = int(input("Enter the private key of User B: "))
    Xc = int(input("Enter the private key of User C: "))

    # Compute the public keys for each user
    Ya = pow(alpha, Xa, p)  # Public key for User A
    Yb = pow(alpha, Xb, p)  # Public key for User B
    Yc = pow(alpha, Xc, p)  # Public key for User C

    print(f"\nPublic key of User A (Ya): {Ya}")
    print(f"Public key of User B (Yb): {Yb}")
    print(f"Public key of User C (Yc): {Yc}")

    # Compute the shared secret key (common to all three users)
    # Each user computes the shared secret key in the following steps:
    Ka = pow(pow(Yb, Xa, p), Xc, p)  # A -> B -> C
    Kb = pow(pow(Yc, Xb, p), Xa, p)  # B -> C -> A
    Kc = pow(pow(Ya, Xc, p), Xb, p)  # C -> A -> B

    print(f"\nShared secret key computed by User A (Ka): {Ka}")
    print(f"Shared secret key computed by User B (Kb): {Kb}")
    print(f"Shared secret key computed by User C (Kc): {Kc}")

    # Verify that all shared keys are the same
    assert Ka == Kb == Kc, "Shared keys do not match!"
    print("\nAll users have successfully computed the same shared secret key.")

if __name__ == "__main__":
    main()
