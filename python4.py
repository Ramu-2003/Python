# --- Logical Operators ---
p = True
q = False

print(p and q)  # Logical AND: Returns True only if both are True; returns False
print(p or q)  # Logical OR: Returns True if at least one is True; returns True
print(not p)   # Logical NOT: Reverses the state; returns False because p is True

# --- Bitwise Operators ---
# 10 in binary is 1010, 4 in binary is 0100
m = 10
n = 4

print(m & n)   # Bitwise AND (&): Sets bit to 1 if both bits are 1; returns 0
print(m | n)   # Bitwise OR (|): Sets bit to 1 if one of the bits is 1; returns 14
print(m ^ n)   # Bitwise XOR (^): Sets bit to 1 if only one bit is 1; returns 14
print(~m)      # Bitwise NOT (~): Inverts all bits; returns -11
print(m << 2)  # Left Shift (<<): Shifts bits left by 2 positions; returns 40
print(m >> 2)  # Right Shift (>>): Shifts bits right by 2 positions; returns 2
