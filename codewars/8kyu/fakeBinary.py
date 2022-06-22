def fake_bin(x):
    output = ""
    for i in x:
        if int(i) < 5:
            output += "0"
        else:
            output += "1"
            
    return output

print(fake_bin("0635002098273157"))