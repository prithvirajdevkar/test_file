#                                                                                                *Set - C Kudiods Comapny Pvt Ltd*

# 1. write a progeam which ask user to enter the marks in percentage, and raise the custome exception "InvalidMarksException" if user the percentage than 100 % or less than 0%.
# Sample Test Cases:
# I/P: 90
# O/P: You got 90 marks!

# I/P: 101
# O/P: InvalidMarks Exception: Marks must be from 0 to 100

# I/P: -25
# O/P: InvalidMarks Exception: Marks must be from 0 to 100
class InvalidMarksException(Exception):
    def __init__(self, message="Marks must be from 0 to 100"):
        self.message = message
        super().__init__(self.message)

def get_marks():
    try:
        marks = float(input("Enter your marks in percentage: "))
        if marks < 0 or marks > 100:
            raise InvalidMarksException()
        else:
            print(f"You got {marks} marks!")
    except InvalidMarksException as e:
        print(f"InvalidMarks Exception: {e.message}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")


get_marks() 

# 2. write a program  to input a string and print the count of vowels and consonants in the string.
def count_vowels_consonants(input_string):
    vowels = "aeiou"
    consonant = "AEIOU"
    v_count = 0
    c_count = 0

    for char in input_string:
        if char.isalpha():  
            if char in vowels:
                v_count += 1
            else:
                c_count += 1

    return v_count, c_count


input_string = input("Enter a string: ")

vowels, consonants = count_vowels_consonants(input_string)

print(f"Total number of vowels: {vowels}")
print(f"Total number of consonants: {consonants}")

# 3. Write a program to input an array and count how many elements are greater than the average of the array.
# Sample Test Case: 
# Input: [1,2,3,4,5]
# output: 2

# Input:[5,10,15]
# output: 1

# Explanation: The average of the array is . the elemenet greater than 10 is 15

def count_greater_than_average(arr):
    if not arr:
        return 0
    
    average = sum(arr) / len(arr)
    count = sum(1 for x in arr if x > average)
    
    return count

print(count_greater_than_average([1, 2, 3, 4, 5]))  
print(count_greater_than_average([5, 10, 15]))     


