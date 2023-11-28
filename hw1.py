
def printStar(nLayer):
    for j in range(0, nLayer*2-1):
        print("*",end="")

def printSpace(nLayer):
    for i in range(0, nLayer):
        print(" ",end="")

def printLeaves(nLayer, addSpace=True):
    for i in range(0, nLayer):
        start = i + 1;
        if addSpace:
            printSpace(nLayer - start)
        printStar(start)
        print(end="\n")

def readInt(msg):
    while True:
        try:
            # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
            inputData = int(input(msg))
            return inputData
        except ValueError:
            print("Sorry, I didn't understand that.")
            #better try again... Return to the start of the loop
            continue
        else:
            #age was successfully parsed!
            #we're ready to exit the loop.
            break

def printTrunk(h ,w ,limit):
    for i in range(0, h):
        numSpace = int((limit - w) / 2)
        for j in range(0,numSpace):
            print(" ",end="")
        for j in range(0, w):
            print("|",end="")
        print("")

def case1():
    print("case 1")
    layerNum = int(readInt("輸入層數 : "))
    printLeaves(layerNum, addSpace=False)
    print("================================\n")

def case2():
    print("case 2")
    layerNum = int(readInt("輸入層數 : "))
    printLeaves(layerNum, addSpace=True)
    print("================================\n")

def case3():
    print("case 3")
    layerNum = int(readInt("輸入層數 : "))
    trunkHeight = int(readInt("樹幹高度 : "))
    trunkWidth = int(readInt("樹幹寬度(奇數) : "))
    limit = layerNum * 2 - 1

    if limit < trunkWidth :
        print("Error input, the width of the trunk is too large")
    elif trunkWidth % 2 == 0 :
        print("Error input, the trunk width should be odd")
    else: 
        printLeaves(layerNum)
        printTrunk(trunkHeight, trunkWidth, limit)
    print("================================\n")

case1()
case2()
case3()

