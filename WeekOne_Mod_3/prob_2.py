def encypt_func(txt,s):
    result = ''
    for i in range(len(txt)):
        char = txt[i]
        if(char.isupper()):
            result += chr((ord(char)+s-65)%26+65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

test = input('Input a String: ')
s = int(input('Enter a Int: '))
encypt_text = encypt_func(test,s)
print(f'tmr lukano text-> {encypt_text}') 