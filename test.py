import subprocess

filename = 'test.py'
print('start')
while True:
    text = input(">>: ")
    if (text):
        print('have' + text)
    else:
    # """However, you should be careful with the '.wait()'"""
        p = subprocess.Popen('/usr/bin/python3 '+filename, shell=True).wait()

    # """#if your there is an error from running 'my_python_code_A.py', 
    # the while loop will be repeated, 
    # otherwise the program will break from the loop"""
    # if p != 0:
    #     continue
    # else:
    #     break