'''
Приклад організації стеку з використанням метода deque з модуля collections -
реалізує спеціалізовані типи даних контейнерів
По суті - здійснено трансформація правил черги до рівня стека.
https://docs.python.org/uk/3/library/collections.html#module-collections

Створити стек - означає встановити взаємодію елементів та операцій над ними
push(a) – Вставляє елемент «a» у верхній частині стека
pop() – видаляє найвищий елемент стеку
empty() – Повертає, чи стек порожній
full() : перевірити, чи заповнений стек
peek() – повертає посилання на найвищий елемент стека

'''

from collections import deque


def create_stack():
    stack = deque()
    return stack


def push(stack, item):
    stack.append(item)


def pop(stack):
    if (stack):
        top_element = stack.pop()
        # print(f'Element:{top_element} was pop from stack:')
        return top_element
    else:
        print('Stack is empty')

def show(name, stack):
    return f'`{name}` content:`{stack}`'

def show_stack(stack):
    print(f'`{stack}`')

def shows(stack_a, stack_b, stack_c):
    print("A", show("(src)", stack_a))
    print("B", show("(aux)", stack_b))
    print("C", show("(dest)", stack_c))

def pop_push(stack_from, stack_to):
    taken = pop(stack_from)
    push(stack_to, taken)
    return stack_from, stack_to


def stack_list_element_reposition(stack_list, pop, push):
    stack_list0 = lambda stack_list: pop_push(stack_list[pop], stack_list[push])
    return stack_list0


def stack_list_element_reposition00(stack_list, pop, push):
    stack_list[pop], stack_list[push] = pop_push(stack_list[pop], stack_list[push])
    return
