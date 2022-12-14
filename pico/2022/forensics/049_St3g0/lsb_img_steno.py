#!/usr/bin/env python3

import numpy as np
from PIL import Image

def encode(src, msg, dst):
    img = Image.open(src, 'r')
    w, h = img.size
    arr = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4

    total_pixels = arr.size//n

    msg += "$t3g0"
    b_msg = ''.join([format(ord(i), "08b") for i in msg])
    req_pixels = len(b_msg)

    if req_pixels > total_pixels:
        print("ERROR: Need larger file size")
    else:
        index = 0
        for p in range(total_pixels):
            for q in range(0, 3):
                if index < req_pixels:
                    arr[p][q] = int(bin(arr[p][q])[2:9] + b_msg[index], 2)
                    index += 1

            arr=arr.reshape(h, w, n)
            enc_img = Image.fromarray(arr.astype('uint8'), img.mode)
            enc_img.save(dst)
            print("Image Encode Successfully")

def decode(src):
    img = Image.open(src, 'r')
    arr = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4

    total_pixels = arr.size//n

    hidden_bits = ""
    for p in range(total_pixels):
        for q in range(0, 3):
            hidden_bits += (bin(arr[p][q])[2:][-1])
    hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]

    msg = ""
    for i in range(len(hidden_bits)):
        if msg[-5:] == "$t3g0":
            break
        else:
            msg += chr(int(hidden_bits[i], 2))
    if "$t3g0" in msg:
        print(msg[:-5])
    else:
        print("No hidden message found.")

def stego():
    print("--Welcome to $t3g0--")
    print("1: Encode")
    print("2: Decode")

    func = input()

    if func == '1':
        print("Enter Source Image Path")
        src = input()
        print("Enter Message to Hide")
        msg = input()
        print("Enter Destination Image Path")
        dst = input()
        print("Encoding...")
        encode(src, msg, dst)

    elif func == '2':
        print("Enter Source Image Path")
        src = input()
        print("Decoding...")
        decode(src)

    else:
        print("ERROR: Invalid option chosen")


if __name__ == '__main__':
    stego()
