"""
Recursive mthod contains the base case and inductive step

t = temp var
S = stack
T = temp stack

sort_stack(S)
main() - helper method


base case
    if list is empty, then it's sorted
    return stack, S

inductive step
    you have top element and rest of stack
        t = S.pop()
        assume rest of stack is sorted  (do you always put the recursion at the part where you "assume" something?)

    sortedStack = stack_sort(S)   <-- recursive

    find out where t fits in sortedStack
    while S.peek() > t:
        T.push(S.pop())
    S.push(t)
    while T.peek() != {}:   (I don't know if peek returns anything on empty)
        S.push(T.pop())

    return sortedStack

"""
