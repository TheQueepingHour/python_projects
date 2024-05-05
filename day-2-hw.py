#Maximum of three numbers
def max_num(num1, num2, num3):
  return max([num1, num2, num3])
print(max_num(233, 42, 50))

#Multiply all numbers in a list
def mult_list(lst):
  product = 1
  for i in lst:
    product *= i
  return product

print(mult_list([2, 3, 4, 5]))

#Reverse string 
def rev_string(string):
  return string[::-1]

print(rev_string(string="Hello"))

#Check whether a number falls in a given range
# def num_within(num):
#   r = range(1,4)
#   return num in r
def num_within(num, min, max):
  return num in range(min, max+1)

print(num_within(3, 2, 4))
print(num_within(3, 1, 3))
print(num_within(10, 2, 5))

#Prints out the first n rows of Pascal's Triangle
def pascal(n):
  values = []
  for i in range(n):
    row = [1]
    if i > 0:
      prev_row = values[i-1]
      for j in range(1, i):
        row.append(prev_row[j-1] + prev_row[j])
    if i > 0:
      row.append(1)
    values.append(row)
  return values

print(pascal(1))
print(pascal(5))