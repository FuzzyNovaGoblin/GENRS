
class Block:
    a = 0
    b = 0
    c = 0
    ah = 0
    bh = 0
    ch = 0
    key = ""

    def __init__(self, aa, bb, cc, k):
        pos = 0
        self.a = aa
        self.b = bb
        self.c = cc
        self.key = k

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
        if(Block.pos == len(self.key)):
            Block.pos = 0
        r = ord(self.key[Block.pos])
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

def encrypt(bytesarr):
    Block.pos = 0
    for block in bytesarr:
        block.Rot()
        block.mult()
        block.Geth()
    return bytesarr


def decrypt(bytesarr):
    Block.pos = 0
    for block in bytesarr:
        block.putH()
        block.demult()
        block.deRot()
    return bytesarr



# b = (int.from_bytes(b'\xff', "big"))
# print(b)
# print(b.to_bytes(2,"big"))
# filename = input("file name: ")

key = "Pizza"



bytes = []


filename = "testfile"
# filename = "new"
# filename = "1.jpg"

# f = open(filename, "rb")
# try:
#     byte = f.read(1)
#     while byte != b'':
#         # Do stuff with byte.
#         # byte = int(f.read(1))
#         # b = bin(int.from_bytes(byte, "big"))
#         bytes.append(int.from_bytes(byte, "big"))
#         byte = f.read(1)
#
# finally:
#     f.close()


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



print(bytes)
if(len(bytes)%3!=0):
    bytes.append(0)
if(len(bytes)%3!=0):
    bytes.append(0)




blocks = []
pos = 0
for i in range(int(len(bytes)/3)):
    b = Block(bytes[pos], bytes[pos+1], bytes[pos+2], key)
    blocks.append(b)
    pos += 2




blocks = encrypt(blocks)

of = open("new", "w")
for b in blocks:
    of.write((str(b.ah)+" "+str(b.a)+" "+str(b.bh)+" "+str(b.b)+" "+str(b.ch)+" "+str(b.c)+" "))

of.close()
