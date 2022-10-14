""" We know how to check if the key exists in a dictionary. Sometimes it is required to check if the given value is present.
Write a Python program to check if value 100 exists in the following dictionary. If it is present print “present” otherwise print “not present”

Sample Dictionary:
sample_dict = {'a': 300, 'b': 200, 'c': 300}

Expected Output:
present """

sample_dict = {'a': 100,'b': 200,'c':300}
chk = False
for k,v in sample_dict.items():
    if(v==100):
        chk = True
        break
if chk:
    print('Present',end='')
else:
    print('Not Present',end='')