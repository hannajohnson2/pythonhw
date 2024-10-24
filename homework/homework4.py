#Question 2

#2.1

numbers_list = []

for i in range(21):
    numbers_list.append(i)

print(numbers_list)

#2.2
def squaring(list):
    new_list = []
    for number in list:
        squared = number ** 2
        new_list.append(squared)
    return new_list

#I originally forgot a return statement

#2.3 

def slicing(list):
   return list[0 : 15]

print(slicing(squaring(numbers_list)))
#I forgot a print statement

#2.4

def every_fifth_element(list):
    return list[4 : len(list): 5]

print(every_fifth_element(squaring(numbers_list)))
#did len(list) - 1 before realizing that it excludes 20 and started at 0

#2.5

def slice_stride(list):
    slice = list[-30::]
    stride = slice[::-3]
    return stride

#3

#3.1

def create_2d_list():
    rows = 5
    col = 5

    array = []

    count = 1

    for row in range(rows):
        row_list = []
        for column in range(col):
            row_list.append(count)
            count += 1
        array.append(row_list)
            
    return array

print(create_2d_list())
matrix = create_2d_list()

#3.2

def modified_2d_list(mat):
    for row in range(len(mat)):
        for col in range(len(mat[row])):
            if mat[row][col] % 3 == 0:
                mat[row][col] = "?"
    return mat

new_matrix = (modified_2d_list(matrix))
print(new_matrix)

# #3.3
#print(matrix)
#new_matrix = modified_2d_list(matrix)

def sum_non_question_elements(m):
    count = 0 
    for row in range(len(m)):
        for col in range(len(m[row])):
            if m[row][col] != "?":
                count += m[row][col]
    return count



    