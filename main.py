import random
cont = True

# import random
# for x in range(10):
#   print random.randint(1,101)
while True:
    print random.randint(1,10)
    response = raw_input("Continue? (Y/N): ")
    if response == "N":
        print "done"
        break
