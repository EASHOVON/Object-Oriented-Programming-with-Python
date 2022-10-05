data = "aNtEriOur\n\t>>"

""" Please make it result  => a_e_i_o_u """
newStr = ''
data = data.lower()
for ch in data:
    if(ch=='a') or (ch=='e') or (ch=='i') or (ch=='o') or (ch=='u'):
        if(len(newStr)==8):
            newStr+=ch
        else:
            newStr+=ch+'_'
        
print((newStr))