import math

from Home_works_common.stack.my_stack_collections import *

print("Let's go")
aux_stack = create_stack()
dest_stack = create_stack()

# print("Let's define the stack size")
# size = int(input("enter stack size: "))
size = 3

home_stack = create_stack()
# print("we got stack: ")
# show_stack(home_stack)

# print("Let's fill stack by values")
# print(range(size))
for i in range(size):
    # print(f"enter stack element {i}: ")
    # stack_element = int(input(f"enter stack element `{i}`: "))
    # push(home_stack, stack_element)
    push(home_stack, 7 - i * 2)

print("we got stack: ")
show_stack(home_stack)

# Recursive Python function to solve the tower of hanoi
#
# def TowerOfHanoi(n, source, destination, auxiliary):
#     if n == 0:
#         return
#
#     TowerOfHanoi(n - 1, source, auxiliary, destination)
#     print("Move last disk from source", source, "to destination", destination)
#     TowerOfHanoi(n - 1, auxiliary, destination, source)
#     shows(source,auxiliary,destination)

#
# def TowerOfHanoiStack(source_stack, aux_stack, destination_stack):
#     print("initial")
#     shows(source_stack, aux_stack, destination_stack)
#
#     # doMove(source_stack,aux_stack,destination_stack)
#     print("1. A->C")
#     #  shows(source_stack, aux_stack, destination_stack)
#     taken = pop(source_stack)
#     push(destination_stack, taken)
#     shows(source_stack, aux_stack, destination_stack)
#     print("------------")
#
#     print("2. A->B")
#     # shows(source_stack, aux_stack, destination_stack)
#     taken = pop(source_stack)
#     push(aux_stack, taken)
#     shows(source_stack, aux_stack, destination_stack)
#     print("------------")
#
#     print("3. Move disk: C->B")
#     # shows(source_stack, aux_stack, destination_stack)
#     taken = pop(destination_stack)
#     push(aux_stack, taken)
#     shows(source_stack, aux_stack, destination_stack)
#     print("------------")
#
#     print("4. Move disk: A->C")
#     taken = pop(source_stack)
#     push(destination_stack, taken)
#     shows(source_stack, aux_stack, destination_stack)
#     print("------------")
#
#     print("5. Move disk: B->A")
#     taken = pop(aux_stack)
#     push(source_stack, taken)
#     shows(source_stack, aux_stack, destination_stack)
#     print("------------")
#
#     print("6. Move disk: B->C")
#     taken = pop(aux_stack)
#     push(destination_stack, taken)
#     shows(source_stack, aux_stack, destination_stack)
#     print("------------")
#
#     print("7. Move disk: A->C")
#     taken = pop(source_stack)
#     push(destination_stack, taken)
#     shows(source_stack, aux_stack, destination_stack)
#     print("------------")
#
#     print("final")
#     shows(source_stack, aux_stack, destination_stack)

# def TowerOfHanoi33(N):
#     #list_stack = [source, auxiliary, destination]
#     list_stack_names = ["source", "auxiliary", "destination"]
#
#     for x in range(1, int(math.pow(2, N))):
#         print(f" step:`{x}; Move from Rod `{list_stack_names[(x & x - 1) % 3 ]}`->`{list_stack_names[((x| x - 1) + 1) % 3 ]}`")
#   #      print("x= ", x, ";Move from Rod ", ((x & x - 1) % 3 + 1), " to Rod ", (((x | x - 1) + 1) % 3 + 1))
#
#
# # Driver Code
# TowerOfHanoi33(3)

def TowerOfHanoi44(N, stack_list):
    # list_stack = [source, auxiliary, destination]
    list_stack_names = ["source", "auxiliary", "destination"]

    for x in range(1, int(math.pow(2, N))):
        pop_from = (x & x - 1) % 3
        push_to = ((x | x - 1) + 1) % 3
        # print(f"pop_from:{pop_from}, push_to: {push_to}")
        # print(f" step:`{x}; Move from Rod `{list_stack_names[(x & x - 1) % 3 ]}`->`{list_stack_names[((x| x - 1) + 1) % 3 ]}`")
        print("stack_list before reposition", stack_list)
        stack_list_element_reposition(stack_list, pop_from, push_to)
        # stack_list = lambda stack_list[pop_from], stack_list[push_to]: pop_push(stack_list[pop], stack_list[push])
        print("stack_list after reposition", stack_list)

    return stack_list


print("han44:----- ")
shows(home_stack, aux_stack, dest_stack)
stack_list = [home_stack, aux_stack, dest_stack]

print("han44: ", TowerOfHanoi44(3, [home_stack, aux_stack, dest_stack]))
