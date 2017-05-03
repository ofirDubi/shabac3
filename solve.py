import enchant
class Command:
    commandType = 0
    parameter = 0
    length = 0
    def str(self):
        return ("commandType: " + str(self.commandType) + " parameter: " + str(self.parameter) + " length: " + str(self.length))

    def toByte(self):
        return

def validChar(x):
    return (ord(x)>64 and ord(x) <91) or (ord(x)>96 and ord(x) <123)  or x == '?' or x == '.' or x == ' '

string = []
bytes = []

d = enchant.Dict("en_US")

#def commandToBin(commands):
#    bytes = []
#    for command in command:
#        bytes.append()

with open("EncryptedMessage.bin", "rb") as f:
    byte = f.read(1)
    while byte != b"":
        # Do stuff with byte.
        string.append(chr(int.from_bytes(byte, byteorder="little")  ))
        bytes.append(byte)
        byte = f.read(1)
#print(" bytes" + str(bytes))
#"My mother is the coolest, most amazing person I know."
#The goal is always to do B material in an A fashion.
#I've had the same friends since I was in kindergarten.
#It is a leap of faith doing any serialised storytelling. - 55!!

file = open("testfile.txt", "w")

mod = 7
result = list(map(lambda x: int.from_bytes(x, byteorder='little'), bytes))
result = result[mod:len(result)]

length = len(result)
print("length "+str(length))
changeInLocation =0
possible = []

for commandType in range(3):
    for parameter in range(255):
        for location in range(0, length):
            if (commandType == 0):
                result[location] = result[location] ^ parameter
            if (commandType == 1):
                result[location] = result[location] + parameter
            if (commandType == 2):
                result[location] = result[location] - parameter

            location += changeInLocation
            if (location >= length):
                location -= 1
                changeInLocation = -2
            if (location < 0):
                location += 1
                changeInLocation = 0
        possible.append(list(map(lambda x: chr(x%256),result)))
        result = list(map(lambda x: int.from_bytes(x, byteorder='little'), bytes))
        result = result[mod:len(result)]
        location =0

real_possibles = []
i=0

for sub in possible:
    '''and all((sub.index(x) > 10 or x.isalpha() or ord(x)==('?') or ord(x) == '.' or ord(x)==' ') for x in sub )'''

    if(" "in sub and sub.index(" ") <=10 and all(sub.index(x) > 0 or validChar(x) for x in sub )):
        i+=1
        real_possibles.append(sub)
for i in real_possibles:
    print(i)
    print(len(i))


'''
word = [None]*55
def wow(loc):

    if(loc == len(bytes)):

        hasAbraham()
        return

    #print("init word: ")
    #print(word)
    for i in range(65, 91):
       word[loc] = chr(i)
       wow(loc+1)
    for i in range(97, 123):
        word[loc] = chr(i)
        wow(loc+1)
    word[loc] = '.'
    wow(loc +1)
    word[loc] = ' '
    wow(loc + 1)
    word[loc] = '?'
    #print("final word: ")
    #print(word)
    wow(loc+1)
    return
def hasAbraham():
    #print(word)
    if "JJ abram" in ("".join(word)).lower() and " " in word:
        print(word)
        file.write("".join(word)+ " y")


wow(0)


file.close()
for original, target in (bytes, answer):
    for i in range(256):

        if(int.from_bytes(original, byteorder="little") ^ i == ord(target)):
            options[k].append("xor "+str(i))
            bool = False
        if (int.from_bytes(original, byteorder="little") + i == ord(target)):
            options[k].append("add " + str(i))
            bool = False
        if (int.from_bytes(original, byteorder="little") - i == ord(target)):
            options[k].append("sub " + str(i))
            bool = False
    if (bool):
        options[k].append("none")
    k+=1
print(options)

for i in range(5):
    while(command.length!=0):
        if(command.commandType ==0):
            result[location] =result[location] ^ command.parameter
        if (command.commandType == 1):
            result[location] = result[location] + command.parameter
        if (command.commandType == 2):
            result[location] = result[location] - command.parameter
        command.length -=1
        location += changeInLocation
        if(location >= len(bytes)):
            location -= 1
            changeInLocation = -1
        if(location < 0):
            location+= 1
            changeInLocation = 1
'''