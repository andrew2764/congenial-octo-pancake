import random
cont = True

while True:
    print random.randint(1,10)
    response = raw_input("Continue? (Y/N): ")
    if response == "N":
        print "done"
        break
