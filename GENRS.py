class Block:
    a = 0
    b = 0
    c = 0
    ah = 0
    bh = 0
    ch = 0
    key = ""
    pos = 0
    def __init__(self, aa, bb, cc):

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
        if(self.pos == len(self.key)):
            pos = 0
        return int(self.key[self.pos])


    def mult(self):
        self.a = self.a*self.getMultBy()
        self.b = self.b*self.getMultBy()
        self.c = self.c*self.getMultBy()

    def demult(self):
        self.a = self.a/self.getMultBy()
        self.b = self.b/self.getMultBy()
        self.c = self.c/self.getMultBy()


# b = (int.from_bytes(b'\xff', "big"))
# print(b)
# print(b.to_bytes(2,"big"))
# filename = input("file name: ")




bytes = []


filename = "testfile"
# filename = "new"
# filename = "1.jpg"

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
    b = Block(bytes[pos], bytes[pos+1], bytes[pos+2])
    blocks.append(b)
    pos += 2

print(blocks[0].a)


# of = open("new", "wb")
# for b in bytes:
#     of.write(b.to_bytes(1,"big"))
#
# of.close()