# List of even numbers up to 20
even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] #on this line, I created a list called 'even_numbers' that has all even numbers from 2 to 20, so I can use it in the next steps.

# Display the first 3 elements one by one
print("First 3 elements:") #on this line, I used print to print out the 'First 3 elements', indicating the following output ill show.
for num in even_numbers[:3]: #On this line, Using a for loop, I go through the first three items in the even_numbers list (by slicing even_numbers[:3]). In each pass, I print the current number (num). This shows the first three numbers one at a time.
    print(num) #on this line shows the pcode for the printed outcome.

# Display all numbers in the list using range function
print("All even numbers in the list:") #On this line, I print 'All even numbers in the list', so it indicates the next part of the output.
for i in range(len(even_numbers)): #On this line,I use the 'range(len(even_numbers)) function to create a sequence of indices from - to the length of the list minus one. And then, I use a for loop to iterate over these indices. Therefore, Inside the loop, 'even_numbers[i]' accesses each element in the list by its index, and 'print(even_numbers[i])' it's gonna print every single element.
    print(even_numbers[i]) #on this line, shows the code for the printed outcome.

# Calculate and display the average of the given even numbers in the list
average = sum(even_numbers) / len(even_numbers) #on this line, 'sum(even_numbers)' calculates the sum of all the elements in the 'even_numbers' list, and 'len(even_numbers)' calculates the total number of elements in the list. The average is calculated by dividing the sum by the number of elements and is stored in the variable 'average'.
print(f"Average of even numbers: {average}") #On this line, its gonna print the calculated average using an f-string for formatting, showing a message with the average value.
