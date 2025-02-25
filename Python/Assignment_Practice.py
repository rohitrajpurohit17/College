# Find the Length of a List in Python
lst = [1, 2, 3, 4, 5]  
print(len(lst))

# Python program to interchange first and last elements in a list
lst = [1, 2, 3, 4, 5]
lst[0], lst[-1] = lst[-1], lst[0]
print(lst)

# To swap two elements in a list
lst = [1, 2, 3, 4, 5]
pos1, pos2 = 1, 3
lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
print(lst)

# To check if element exists in list
lst = [1, 2, 3, 4, 5]
element = 3
print(element in lst)

# Reversing a List
lst = [1, 2, 3, 4, 5]
print(lst[::-1])

# Cloning or Copying a list
lst = [1, 2, 3, 4, 5]
copy_lst = lst[:]
print(copy_lst)

# Count occurrences of an element in a list
lst = [1, 2, 3, 2, 4, 2, 5]
print(lst.count(2))

# Find sum and average of List in Python
lst = [1, 2, 3, 4, 5]
print(sum(lst), sum(lst) / len(lst))

# Sum of number digits in List
lst = [12, 34, 56]
print(sum(sum(int(digit) for digit in str(num)) for num in lst))

# Multiply all numbers in the list
lst = [1, 2, 3, 4, 5]
product = 1
for num in lst:
    product *= num
print(product)

# Find smallest number in a list
lst = [3, 1, 4, 1, 5]
print(min(lst))

# Find largest number in a list
lst = [3, 1, 4, 1, 5]
print(max(lst))

# Find second largest number in a list
lst = [3, 1, 4, 1, 5]
print(sorted(set(lst))[-2])

# Print even numbers in a list
lst = [1, 2, 3, 4, 5]
print([num for num in lst if num % 2 == 0])

# Print odd numbers in a List
lst = [1, 2, 3, 4, 5]
print([num for num in lst if num % 2 != 0])

# To count Even and Odd numbers in a List
lst = [1, 2, 3, 4, 5]
even_count = sum(1 for num in lst if num % 2 == 0)
odd_count = sum(1 for num in lst if num % 2 != 0)
print(even_count, odd_count)

# To print positive numbers in a list
lst = [-1, 2, -3, 4, -5]
print([num for num in lst if num > 0])

# To print negative numbers in a list
lst = [-1, 2, -3, 4, -5]
print([num for num in lst if num < 0])

# To count positive and negative numbers in a list
lst = [-1, 2, -3, 4, -5]
pos_count = sum(1 for num in lst if num > 0)
neg_count = sum(1 for num in lst if num < 0)
print(pos_count, neg_count)

# Remove multiple elements from a list in Python
lst = [1, 2, 3, 4, 5, 6, 7, 8]
remove_lst = {2, 4, 6}
print([num for num in lst if num not in remove_lst])