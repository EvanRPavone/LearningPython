
def run():
    print("process started running...")
    
def shut_down():
    print("process is shutting down...")
    
def start_task_1():
    print("started task 1")
    
def start_task_2():
    print("started task 2")
    
def email_admin():
    print("violation noted. Emailing admin...")

if __name__ == '__main__':
    """
    python interpreter actually assigns a particular value to this name variable as soon as the script is used
    whether as an import or directly
    When we try to run this file directly, the interpreter actually takes name and it assigns it to the main value
    __name__ - not easy for someone to override it
    """
    run()
    start_task_1()
    start_task_2()
    shut_down()
    # email_admin()
    # this process will not run if we are using it as an import
    # if this file is run directly, the code that is in this if block will be run first