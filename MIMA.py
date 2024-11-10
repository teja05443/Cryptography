import random

# Prime number and base for Diffie-Hellman (small for simplicity)
p = 23  # Prime
g = 5   # Base

# Alice's side
alice_private_key = random.randint(1, p-1)
alice_public_key = pow(g, alice_private_key, p)
print(f"Alice's Public Key: {alice_public_key}")

# Bob's side
bob_private_key = random.randint(1, p-1)
bob_public_key = pow(g, bob_private_key, p)
print(f"Bob's Public Key: {bob_public_key}")

# Darth (attacker)
darth_private_key = random.randint(1, p-1)
darth_public_key = pow(g, darth_private_key, p)
print(f"Darth's Public Key: {darth_public_key}")

# Alice thinks she's communicating with Bob, but her shared secret is with Darth
alice_shared_secret_with_darth = pow(darth_public_key, alice_private_key, p)
print(f"Alice's Shared Secret with Darth: {alice_shared_secret_with_darth}")

# Bob thinks he's communicating with Alice, but his shared secret is with Darth
bob_shared_secret_with_darth = pow(darth_public_key, bob_private_key, p)
print(f"Bob's Shared Secret with Darth: {bob_shared_secret_with_darth}")

# Darth calculates shared secrets with both Alice and Bob
darth_shared_secret_with_alice = pow(alice_public_key, darth_private_key, p)
darth_shared_secret_with_bob = pow(bob_public_key, darth_private_key, p)
print(f"Darth's Shared Secret with Alice: {darth_shared_secret_with_alice}")
print(f"Darth's Shared Secret with Bob: {darth_shared_secret_with_bob}")

# Confirm that Alice and Bob's "shared secrets" are actually with Darth
assert alice_shared_secret_with_darth == darth_shared_secret_with_alice, \
    "Mismatch between Alice and Darth's shared secrets!"
assert bob_shared_secret_with_darth == darth_shared_secret_with_bob, \
    "Mismatch between Bob and Darth's shared secrets!"

# Output final shared secrets for inspection
print("=== Final Shared Secrets ===")
print(f"Alice's Shared Secret (with Darth): {alice_shared_secret_with_darth}")
print(f"Bob's Shared Secret (with Darth): {bob_shared_secret_with_darth}")
