# Print the first 3 elements using slice expression
print("First 3 elements using slice expression:") #on this line, print("First 3 elements using slice expression:") it will print a header for the output.
print(numbers[:3]) #On this line, it will print thesr 3 elements as a list.

# Change the elements to [2, 4, 6, 8, 10]
numbers = [num * 2 for num in numbers] #On this line, the formula [num * 2 for num in numbers] creates a new list by doubling each element in the original numbers list using a list comprehension.
print("List after doubling each element:") #on this line, print("List after doubling each element:") prints a header for the output.
print(numbers) #on this line, it will print the updated list.

# Display the min and max value in the list
min_value = min(numbers) ] #On this line, min(numbers) calculates the minimum value in the list.
max_value = max(numbers) #On this line, min_value & max_value store these results.
print(f"Min value: {min_value}") #On this line and the line below, print(f"Min value: {min_value}") and print(f"Max value: {max_value}") print the minimum and maximum values using f-strings for formatting.
print(f"Max value: {max_value}")
