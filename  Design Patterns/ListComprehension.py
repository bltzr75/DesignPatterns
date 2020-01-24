list=[1,2,3]
for x in list:
    print(x)
iter = list.__iter__()
iter
iter.__next__()
iter.__next__()
iter.__next__()
numbers=[1,2,3,4]
numbers_again=[n for n in numbers]
numbers_again
even_numbers= [n for n in numbers if n%2==0]
even_numbers
odd_square=[n**2 for n in numbers if n%2!=0]
odd_square
matrix = [[1,2,3],[4,5,6], [7,8,9]]
flat = [n for row in matrix for n in row] #List Comprehension: for inside a for
flat