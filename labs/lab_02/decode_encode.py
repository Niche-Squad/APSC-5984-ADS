import struct


def float32_to_bin(num):
    # https://stackoverflow.com/questions/16444726/binary-representation-of-float-in-python-bits-not-hex
    return "".join("{:0>8b}".format(c) for c in struct.pack("!f", num))


def float64_to_bin(num):
    # generated by Copilot
    return "".join("{:0>8b}".format(c) for c in struct.pack("!d", num))


def string_to_bin(str):
    # generated by Copilot
    return "".join("{:0>8b}".format(ord(c)) for c in str)


bin(5)  # 0b101
int("101", 2)  # 5
float32_to_bin(5)
string_to_bin("5")  # ASCII code for '5' is 53
