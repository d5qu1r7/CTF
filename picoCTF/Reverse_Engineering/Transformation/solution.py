randomtext = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ"
flag = ""

for i in range(0, len(randomtext)):
    first_char = ord(randomtext[i]) >> 8
    second_char = ord(randomtext[i]) & 0xFF
    flag += chr(first_char)
    flag += chr(second_char)

print(flag)