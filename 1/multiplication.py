# multiply a and b together
def naive (a,b):
    ans = 0
    while a:
        ans += b
        a -= 1
    return ans

# Russian Peasant/Egyptian multiplication
# a*b = a*b + ans, always
# each time there is a 1 in the binary representation of value a, an addition takes place.
# 20 * 7. 20 = 001010 ~ two additions
def russian(a, b):
    ans = 0
    while a:
        # if odd, add to ongoing sum
        if a % 2 == 1:
            ans += b
        a = a >> 1
        b = b << 1
    return ans

def main():
    print naive(4, 5)
    print russian(14, 11) # 154

if __name__ == "__main__":
    main()