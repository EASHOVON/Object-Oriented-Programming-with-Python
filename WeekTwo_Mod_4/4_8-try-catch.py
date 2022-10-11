""" 4-8 Try Except Finally And File Handling Read Write
Error handling statement (try-catch) in python is called try-except statement. The syntax is given below with an example: """

try:
   # First, try to execute the statements in this block
   result = 20 / 2
   print(result)
except:
    # Execute this block of code if try block failed to run
    print('something went wrong')
finally:
    # this block always run, it is an indication of the completion of try-except-finally statement
    print('operation completed')

