for num in range(5):
    x=1
    print("loop:: num: ", num, "; x: ", x)

print("num: ",num)
print("x: ",x)
print("locals: ",locals())

print("==============================1")
global_name = "This is a global name."
print("globals_global name: ",globals()['global_name'])
globals()['global_name'] = "globals() support updating its dictionary"

print("after update: ",globals()['global_name'])

print("==============================2")

global_name = "This is a global name."
def update_global():
    globals()['global_name'] = "Updating a global name from a local scope without the 'global' keyword"
print("Before calling update_global():", global_name)
update_global()
print("After calling update_global():", global_name)

print("==============================3")
def update_globals():
    globals()['new_global_from_local'] = "Updating a global name from a local scope without the 'global' keyword"
print(globals().keys())
update_globals()
print(globals().keys())

print("==============================4")

global_inside_test2 = "A global name inside the test2.py module"
print("module:   ",globals().keys())
def print_msg():
    print("function: ",globals().keys())

print_msg()
print("==============================5")
#import test2
global_outside_test2 = 5
#test2.print_msg()
