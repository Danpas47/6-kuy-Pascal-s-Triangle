def count_bits(n):
     return sum(b == '1' for b in bin(n))
