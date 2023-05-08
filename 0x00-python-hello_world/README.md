## 0-run:

Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable $PYFILE

    guillaume@ubuntu:~/py/0x00$ cat main.py 
    #!/usr/bin/python3
    print("Best School")
    
    guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
    guillaume@ubuntu:~/py/0x00$ ./0-run
    Best School
    guillaume@ubuntu:~/py/0x00$
    
    
----------------------------------------------------------------------------------------

## 1-run_inline:

Write a Shell script that runs Python code.

The Python code will be saved in the environment variable $PYCODE

    guillaume@ubuntu:~/py/0x00$ export PYCODE='print(f"Best School: {88+10}")'
    guillaume@ubuntu:~/py/0x00$ ./1-run_inline 
    Best School: 98
    guillaume@ubuntu:~/py/0x00$ 
    
----------------------------------------------------------------------------------------------
