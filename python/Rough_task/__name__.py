def calculate_area( base, height):
    print("__name__:",__name__)
    return 1/2*(base*height)

if __name__ == "__main__":
    print("I am __main__")
    a = calculate_area(10, 20)
    print("area:",a)