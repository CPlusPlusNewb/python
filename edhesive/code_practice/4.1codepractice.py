# your code goes here
def main():
    name = input("Please enter a name: (Nope to end) ")
    if (name == "Nope"):
        exit()
    else:
        print("Nice to meet you %s" % name)
        main()

main()