var = "d"
print(var == "e")

fy = open("testfile" , "wb")
fy.write(int.to_bytes(0,1,"big"))
fy.close()