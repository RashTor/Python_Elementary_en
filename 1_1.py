import random

def main():
    r_int = random.randint(1,100)

    us_int=101

    while us_int != r_int:
        us_int=int(input("Input int: "))
        if us_int > r_int:
            print("Greater")
        elif us_int < r_int:
            print("Less")
    
        else:
            print("GG")

if __name__ == "__main__":
    main()