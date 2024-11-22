# 3) Remove Duplicates from a List (3 ქულა)
# Create a program that receives a list and removes duplicate elements while maintaining the original order.
# Examples:
# [1, 2, 2, 3, 4, 4, 5] --> [1, 2, 3, 4, 5]
# c --> ['a', 'b', 'c']

def remove_duplicates (list1):
    result = []
    seen = []
    for item in list1:
        if item not in seen:
            seen.append(item)
            result.append (item)
    return result

print (remove_duplicates ([1, 2, 2, 3, 4, 4, 5]))
print (remove_duplicates (['a', 'b', 'a', 'c']))