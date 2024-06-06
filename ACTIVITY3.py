
# Add month 'Sep' at the beginning of the spring list
spring.insert(0, 'Sep') #ON this line, the formula spring.insert(0, 'Sep') inserts 'Sep' at the beginning (index 0) of the spring list.

# Create new lists
MonthsISleep = summer[2:] + autumn + winter + spring[1:] #On this line, MonthsISleep is created by concatenating slices and entire lists: summer[2:] slices the summer list to get elements from index 2 onwards ('Feb'), autumn is the whole list,winter is the whole list after removing the excess 'Jul' and spring[1:] slices the spring list to get elements from index 1 onwards (excluding the newly inserted 'Sep').
MonthsIParty = summer[:2] + [spring[0]] #On this line, MonthsIParty is created by concatenating: summer[:2] slices the summer list to get the first two elements ('Dec' and 'Jan'). and [spring[0]] adds 'Sep' from the spring list.

# Display elements from both lists
print("Months I Sleep:") #On this line, print("Months I Sleep:") it will print a header to indicate the next output.
print(MonthsISleep) #On this line, print(MonthsISleep) it will print the elements of the MonthsISleep list.
print("Months I Party:") #On this line, print("Months I Party:") it will print a header to indicate the next output.
print(MonthsIParty) #On this line, print(MonthsIParty) it will print the elements of the MonthsIParty list.

# Display the elements of list summer in reverse order
print("Summer months in reverse order:") #On this line, print("Summer months in reverse order:") it will priint a header to indicate the next output.
print(summer[::-1])  #On this line, print(summer[::-1]) it will print print the summer list reversed.
