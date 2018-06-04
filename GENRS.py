
class Block:
    a = 0
    b = 0
    c = 0
    ah = 0
    bh = 0
    ch = 0
    key = ""

    def __init__(self, aa, bb, cc):
        pos = 0
        self.a = aa
        self.b = bb
        self.c = cc


    def Rot(self):
        hold = self.a
        self.a = self.b
        self.b = self.c
        self.c = hold

        hold = self.ah
        self.ah = self.bh
        self.bh = self.ch
        self.ch = hold


    def deRot(self):

        hold = self.c
        self.c = self.b
        self.b = self.a
        self.a = hold

        hold = self.ch
        self.ch = self.bh
        self.bh = self.ah
        self.ah = hold

    def Geth(self):
        while(self.a > 255):
            self.a -= 255
            self.ah += 1

        while(self.b > 255):
            self.b -= 255
            self.bh += 1

        while(self.c > 255):
            self.c -= 255
            self.ch += 1

    def Puth(self):
        self.a += 255*self.ah
        self.b += 255*self.bh
        self.c += 255*self.ch

    def getMultBy(self):
        if(Block.pos == len(Block.key)):
            Block.pos = 0
        r = ord(Block.key[Block.pos])
        Block.pos += 1
        return r


    def mult(self):
        self.a = self.a*self.getMultBy()
        self.b = self.b*self.getMultBy()
        self.c = self.c*self.getMultBy()

    def demult(self):
        self.a = self.a/self.getMultBy()
        self.b = self.b/self.getMultBy()
        self.c = self.c/self.getMultBy()

class DBlock(Block):

    def __init__(self, hhaa, aa, hhbb, bb, hhcc ,cc):
        # print(hhaa+" "+ aa+" "+ hhbb+" "+ bb+" "+ hhcc +" "+cc)
        self.ah = int(hhaa)
        self.bh = int(hhbb)
        self.ch = int(hhcc)
        self.a = int(aa)
        self.b = int(bb)
        self.c = int(cc)

def encrypt(bytesarr):
    Block.pos = 0
    for block in bytesarr:
        # print("encryptcalled")
        block.mult()
        # block.Rot()
        block.Geth()
        # print(bytesarr)
    return bytesarr


def decrypt(bytesarr):
    Block.pos = 0
    for dblock in bytesarr:
        dblock.Puth()
        # dblock.deRot()
        dblock.demult()
    return bytesarr



# b = (int.from_bytes(b'\xff', "big"))
# print(b)
# print(b.to_bytes(2,"big"))
# filename = input("file name: ")

key = "a"
dve = "d"
# dve = "e"

blocks = []
bytes = []


# filename = "testfile"
filename = "new"
# filename = "1.jpg"

if dve == "e":
    Block.key = key

    f = open(filename, "rb")
    try:
        byte = f.read(1)
        while byte != b'':
            # Do stuff with byte.
            # byte = int(f.read(1))
            # b = bin(int.from_bytes(byte, "big"))
            bytes.append(int.from_bytes(byte, "big"))
            byte = f.read(1)

    finally:
        f.close()



    if (len(bytes) % 3 != 0):
        bytes.append(32)
    if (len(bytes) % 3 != 0):
        bytes.append(32)

    # print(bytes)

    pos = 0
    for i in range(int(len(bytes) / 3)):
        b = Block(bytes[pos], bytes[pos + 1], bytes[pos + 2])
        blocks.append(b)
        
        pos += 3

    blocks = encrypt(blocks)

    of = open("new", "w")
    for b in blocks:
        of.write(
            (str(b.ah) + " " + str(b.a) + " " + str(b.bh) + " " + str(b.b) + " " + str(b.ch) + " " + str(b.c) + " "))

    of.close()

elif dve == "d":
    Block.key = key

    f = open(filename, "r")
    try:
        byte = f.read(1)
        while byte != '':

            char = ''
            while byte != ' ':
                char += byte
                byte = f.read(1)
            byte = f.read(1)

            char2 = ''
            while byte != ' ':
                char2 += byte
                byte = f.read(1)
            byte = f.read(1)

            char3 = ''
            while byte != ' ':
                char3 += byte
                byte = f.read(1)
            byte = f.read(1)

            char4 = ''
            while byte != ' ':
                char4 += byte
                byte = f.read(1)
            byte = f.read(1)

            char5 = ''
            while byte != ' ':
                char5 += byte
                byte = f.read(1)
            byte = f.read(1)

            char6 = ''
            while byte != ' ':
                char6 += byte
                byte = f.read(1)
            byte = f.read(1)

            b = DBlock(char, char2, char3, char4, char5, char6)
            blocks.append(b)


    finally:
        f.close()


    blocks = decrypt(blocks)

    of = open("new", "wb")
    for b in blocks:
        of.write (int.to_bytes(int(b.a), 1, "big"))
        of.write (int.to_bytes(int(b.b), 1, "big"))
        of.write (int.to_bytes(int(b.c), 1, "big"))

    of.close()