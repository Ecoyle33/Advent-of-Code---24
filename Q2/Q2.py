list1 = []

with open("Q2\input.txt", "r") as f:

    for line in f:

        entry = line.strip().split()
        entry = [int(x) for x in entry]
        list1.append(entry)

num_safe_lists = 0
unsafe_lists = []

for array in list1:

    diff_list = []
    # Iterate over each element in list
    for i in range(len(array) - 1):
        diff = array[i + 1] - array[i]
        diff_list.append(diff)

    # If all elements are increasing:
    if all(x > 0 for x in diff_list):

        j = 0
        for i in range(len(diff_list)):

            if (diff_list[i] > 0) and (diff_list[i] <= 3):
                j += 1

        if j == len(diff_list):
            num_safe_lists += 1

        # Add unsafe lists into a separate list for Part 2
        else:
            unsafe_lists.append(array)

    # If all elements are decreasing
    elif all(x < 0 for x in diff_list):

        j = 0
        abs_diff = [abs(x) for x in diff_list]

        for i in range(len(abs_diff)):

            if (abs_diff[i] > 0) and (abs_diff[i] <= 3):
                j += 1

        if j == len(abs_diff):
            num_safe_lists += 1
        # Add unsafe lists into a separate list for Part 2
        else:
            unsafe_lists.append(array)

    # If the elements stay the same:
    else:
        unsafe_lists.append(array)

# print(num_safe_lists)

# ---- Part 2 -----

# If array has more than one 'unsafe' element (unsafe meaning diff value is
# 0 or opposite sign to others), delete array from list, can't be fixed.

# abs_diff always has one less element than its corresponding array
# Find index of unsafe element, add one, remove the element with that value
# for its index

# Test to see if new list is safe, and if so, add one to num_safe_lists
