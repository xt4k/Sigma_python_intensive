import math

from Home_works_common.stack.my_stack_collections import *

print("Let's begin")
aux_stack = create_stack()
dest_stack = create_stack()

size = 3

home_stack = create_stack()
for i in range(size):
    push(home_stack, 3 * size - i * 2)

print("we got stack: ")
show_stack(home_stack)


def TowerOfHanoiOps(power, stack_list):
    for x in range(0, int(math.pow(2, power))):
        pop_from = (x & x - 1) % 3
        push_to = ((x | x - 1) + 1) % 3
        # initial_list = stack_list # - uncomment lines 23, 25 to have more detailed debug info
        stack_list_element_reposition(stack_list, pop_from, push_to)
        # print(f"{x}: {initial_list} -> {stack_list}")
    return stack_list


print("TowerOfHanoiOps ")
stack_list = [home_stack, aux_stack, dest_stack]
print("Before moving:", stack_list)
print("After moving: ", TowerOfHanoiOps(size, [home_stack, aux_stack, dest_stack]))
