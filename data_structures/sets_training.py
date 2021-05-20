# used to store multiple items in a single variable

students = {"pasan", "vidura", "gamith", "muditha"}

print(type(students))

# print if gamith is within the set 
for i in students:
    if i=='gamith':
        print(i)
        break

# add kirulu to the set students
students.add("kirulu")
print(students)

# remove pasan from the set
students.remove("pasan")
print(students)

# remove the last added member from the set
students.pop()
print(students)

# empty the set
students.clear()
print(students)

# delete the set


# even and prime numbers less than 10

even_numbers = [2, 4, 6, 8, 10]
prime_numbers = [2, 3, 5, 7]

# join the 2 sets to create a new set named join_set
join_set = even_numbers + prime_numbers
print(join_set)

# print only ones common on both the sets
lists=(set(even_numbers).intersection(prime_numbers))
print(lists)

# keep all but not the duplicates
    #even = set(even_numbers)
    #prime = set(prime_numbers)
    #merge=prime.symmetric_difference_update(even)
    #print(merge)

# print all except for all present in both the sets