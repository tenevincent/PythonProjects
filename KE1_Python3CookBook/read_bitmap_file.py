
def bytes2int(b):
    res = 0
    for x in b[::-1]:
        res = (res << 8) + x
    return res

with open("lena.bmp", "rb") as file:
    file.seek(18)
    print("Breite:", bytes2int(file.read(4)), "px")
    print("Höhe:", bytes2int(file.read(4)), "px")

    file.seek(2, 1)
    print("Farbtiefe:", bytes2int(file.read(2)), "bpp")


