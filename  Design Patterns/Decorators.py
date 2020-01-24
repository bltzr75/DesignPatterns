import time
def timing_function(external_function):
    def wrapper_function():
        t1=time.time() 
        external_function()
        t2=time.time()
        print("This function took ", (t2-t1), "seconds")
    return wrapper_function

@timing_function
def my_function():
    num_list=[]
    for num in (range(0,1000)):
        num_list.append(num)
    print("The sum of all numbers is :", str(sum(num_list)))   

my_function()