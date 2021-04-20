def strStr(haystack, needle):
    L, n = len(needle), len(haystack)
    if L > n:
        return -1

    # base value for the rolling hash function
    a = 26
    # modulus value for the rolling hash function to avoid overflow
    modulus = 2 ** 31

    # lambda-function to convert character to integer
    h_to_int = lambda i: ord(haystack[i]) - ord('a')
    needle_to_int = lambda i: ord(needle[i]) - ord('a')

    # compute the hash of strings haystack[:L], needle[:L]
    h = ref_h = 0
    for i in range(L):
        h = (h * a + h_to_int(i)) % modulus
        ref_h = (ref_h * a + needle_to_int(i)) % modulus
    if h == ref_h:
        return 0

    # const value to be used often : a**L % modulus
    aL = pow(a, L, modulus)
    for start in range(1, n - L + 1):
        # compute rolling hash in O(1) time
        h = (h * a - h_to_int(start - 1) * aL + h_to_int(start + L - 1)) % modulus
        if h == ref_h:
            return start

    return -1


heystack = input()
num = int(input())
ls = []
for i in range(num):
    ls.append(input())

i = 0
needle = ls[i]
terminal = 0
while True:
    start = strStr(heystack, needle)
    if start == -1:
        terminal += 1
        if terminal == len(ls):
            print(heystack)
            break
        else:
            i = (i + 1) % len(ls)
            needle = ls[i]
    else:
        terminal = 0
        heystack = heystack[:start] + heystack[start + len(needle):]
        print(needle)





