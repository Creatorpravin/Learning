def sqrt(x):
    guess = x
    i = 0
    while guess * guess != x and i<20:
        guess = (guess + x / guess) / 2.0
        i +=1
    return guess

def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))#generate the error
    except ZeroDivisionError:#catch and print it
        print("cannot compute square root for negative")
    finally:
        print("I am the finally block always executed")


if __name__ == '__main__':
    main()