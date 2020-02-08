"""
Given a list of numbers and a number a, return whether any 2 numbers from the list adds up to k.
"""


def AddNum(args, k):
    # Args :
    # list of numbers
    # target number
    # return bool - True when sum of any 2 digits of list is equal to target number
    num_set = set()
    for num in args:
        if (k - num) in num_set:
            return True
        else:
            num_set.add(num)


res = AddNum([1, 2, 3, 4, 5, 6], k=9)
print(res)
