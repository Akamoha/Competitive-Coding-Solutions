def notequal(a, b):
    return a.lower() != b.lower()

while True:
    A = raw_input()
    if A == "*":
        break
    sentence = A.split()
    firstLetter = sentence[0][0]
    for word in sentence:
        if notequal(word[0],firstLetter):
            print "N"
            break
    else:
        print "Y"
