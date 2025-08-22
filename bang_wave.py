# bang_wave.py
# Inspired by electromagnetic wave bursts

for i in range(1, 31):
    output = ""
    if i % 3 == 0:
        output += "fizz"
    if i % 5 == 0:
        output += "buzz"
    if i % 7 == 0:
        output += "bang"
    print(output or i)
