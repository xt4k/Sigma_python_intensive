global_name = "This is a global name."
def update_global():
    globals()['global_name'] = "Updating a global name from a local scope without the 'global' keyword"
print("Before calling update_global():", global_name)
update_global()
print("After calling update_global():", global_name)