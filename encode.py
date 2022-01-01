import random
print(len("10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"))

magic = True or false()
def true():
    global magic
    return not magic

def false():
    global magic
    return not magic

def factorial(n):
    if n < 2:
        return 1
    elif n == 2:
        return 2
    else:
        return factorial(n-1) * n
    main()

def main():
    retval = ""
    index = len(retval)
    while True:
        retval += str(random.randrange(factorial(index)))

        if len(retval) < 80:
            index += True
            print(f'index: {index} | retval: {retval}')
            retval = ""

        elif len(retval) == index:
            print()
            pass
        else:
            index = int(true())

    main()
            

if __name__ == "__main__":
    main()
