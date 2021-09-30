import math

def digits_amount(num):
    return int(math.log10(num)) + 1

def split_at(num, at):
    num1 = num // 10**(at)
    num0 = num % 10**(at)
    return num1, num0

def karatsuba(x, y):
    if (x < 10) and (y < 10):
        res = x*y
        print(f'karatsuba({x},{y})={res}')
        return res, 1, 0, 1

    digits_x = digits_amount(x)
    digits_y = digits_amount(y)
    m = max(digits_x, digits_y)
    n = m // 2

    x1, x0 = split_at(x, n)
    y1, y0 = split_at(y, n)
    print(f'karatsuba({x},{y}): m:{m} n:{n} x1:{x1} x0:{x0} y1:{y1} y0:{y0} calls karatsuba({x0},{y0}), karatsuba({x1+x0},{y1+y0}), karatsuba({x1},{y1})')
    z0, mults0, sums0, iterations0 = karatsuba(x0, y0)
    z1, mults1, sums1, iterations1 = karatsuba(x1 + x0, y1 + y0)
    z2, mults2, sums2, iterations2 = karatsuba(x1, y1)

    mults = mults0 + mults1 + mults2
    sums = sums0 + sums1 + sums2
    iterations = iterations0 + iterations1 + iterations2
    res = z2*(10**(2*n)) + (z1 - z2 - z0)*(10**n) + z0
    print(f'karatsuba({x},{y})={res}')
    return res, mults, sums + 4, iterations + 1

def digits_list(num):
    digits = [int(n) for n in str(num)]
    return digits[::-1]

def traditional_multiplication(x, y):
    digits_x = digits_list(x)
    digits_y = digits_list(y)

    sums = 0
    mults = 0
    result = [0]*(len(digits_x) + len(digits_y))
    for pos_y in range(len(digits_y)):
        carry = 0
        for pos_x in range(len(digits_x)):
            result[pos_x + pos_y] += carry + digits_x[pos_x] * digits_y[pos_y]
            mults +=1
            sums += 2
            carry = result[pos_x + pos_y] // 10
            result[pos_x + pos_y] = result[pos_x + pos_y] % 10
            
        result[pos_y + len(digits_x)] = carry
    return int("".join(map(str, reversed(result)))), mults, sums, mults



def main():
    result, mults, sums, iterations = karatsuba(73514116, 28986655)
    print(f'Karatsuba: result:{result} multiplications:{mults} sums:{sums} iterations:{iterations}')

    result, mults, sums, iterations = traditional_multiplication(73514116, 28986655)
    print(f'Traditional: result:{result} multiplications:{mults} sums:{sums} iterations:{iterations}')



if __name__ == "__main__":
    main()
