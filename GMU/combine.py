"""
combine(A, B)  --- recursive method

return list of all valid output lists

list.insert(<index>, <value>)


base case:
    if an array is empty, return the other array

inductive step:
    c1 =
"""
import logging
logging.basicConfig(filename='/Users/jkam/logs/combine.log', level=logging.DEBUG)

def combine(my_listA, my_listB):
    """
    params: listA = list 1
            listB = list 2
    """
    print('------------')

    my_listA = list(listA)
    my_listB = list(listB)
    # print("my_listA: {0}\tmy_listB: {1}".format(my_listA, my_listB))  ##

    # Base Case
    if my_listA == []:
        print('A empty; return [{0}]'.format(my_listB))
        return [ my_listB ]
    if my_listB == []:
        print('B empty; return [{0}]'.format(my_listA))
        return [ my_listA ]


    # Inductive Step
    # elemA = my_listA.pop(0)
    elemA = my_listA[0]
    print("left: combine({0},{1})".format(my_listA[1:], my_listB))  ##
    # left = combine(my_listA[1:], listB)

    #left = [list(elemA) + output_listA for output_listA in combine(my_listA[1:], my_listB)]
    left = combine(my_listA[1:],my_listB)
    print("== END LEFT COMBINE ==")
    # insert first element back
    print("LEFT: {0}".format(left)) ##
    for output_listA in left:
        output_listA.insert(0,elemA)
    print("after inserting back first element, left: {0}".format(left))


    # pop off first element and call recursive method with updated list
    #elemB = my_listB.pop(0)
    print("right: combine({0}, {1})".format(my_listA, my_listB)) ##
    #right = [list(elemB) + output_listB for output_listB in combine(my_listA, my_listB[1:])]
    right = combine(my_listA, my_listB[1:])
    print("== END RIGHT COMBINE ==")
    # insert first elemnt back
    print("RIGHT: {0}".format(right)) ##
    for output_listB in right:
        output_listB.insert(0,my_listB[0])
    print("after inserting back first element, right: {0}".format(right))


    #return left.extend(right)
    return left + right
