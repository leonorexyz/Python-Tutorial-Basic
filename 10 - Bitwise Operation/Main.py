# This is how bitwise operations work in Python

a = 9  # In binary: 1001
b = 5  # In binary: 0101 

# bitwise OR (|)
c = a | b  # Result: 1101 (13 in decimal)
print('\n========== Bitwise OR ==========')
print(f"Nilai a = {a} dalam biner: {a:08b}")
print(f"Nilai b = {b} dalam biner: {b:08b}")
print('==================================')
print(f"Nilai c = {c} dalam biner: {c:08b}")
# bitwise AND (&)
c = a & b  # Result: 0001 (1 in decimal)
print('\n========== Bitwise AND ==========')
print(f"Nilai a = {a} dalam biner: {a:08b}")
print(f"Nilai b = {b} dalam biner: {b:08b}")
print('==================================')
print(f"Nilai c = {c} dalam biner: {c:08b}")
# bitwise XOR (^)
c = a ^ b  # Result: 1100 (12 in decimal)
print('\n========== Bitwise XOR ==========')
print(f"Nilai a = {a} dalam biner: {a:08b}")
print(f"Nilai b = {b} dalam biner: {b:08b}")
print('==================================')
print(f"Nilai c = {c} dalam biner: {c:08b}")
# bitwise NOT (~)
c = ~a  # Result: -1010 (-10 in decimal, two's complement)
print('\n========== Bitwise NOT ==========')
print(f"Nilai a = {a} dalam biner: {a:08b}")
print('==================================')
print(f"Nilai c = {c} dalam biner: {c & 0xff:08b}")  # Masking to show last 8 bits

# shifting

# shift right (>>)
c = a >> 1
print('\n========== Bitwise SHIFT RIGHT ==========')
print(f"Nilai a = {a} dalam biner: {a:08b}")
print('==================================')
print(f"Nilai c = {c} dalam biner: {c:08b}")  # Result: 0010 (2 in decimal)
# shift left (<<)
c = a << 1
print('\n========== Bitwise SHIFT LEFT ==========')
print(f"Nilai a = {a} dalam biner: {a:08b}")
print('==================================')
print(f"Nilai c = {c} dalam biner: {c:08b}")  # Result: 0010 (2 in decimal)