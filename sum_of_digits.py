#prints the sum of the digits of a two digit number
num_char = input ("Enter a number\n")
print ("Number entered is: \n" + num_char)
first_num_str = num_char [0]
second_num_str = num_char [1]
sum = int(first_num_str) + int(second_num_str)
print (sum)