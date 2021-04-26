# exercises based on : https://www.programiz.com/python-programming/exception-handling

# ex-1

try:
    num = int(input("Enter a number: "))
    assert number % 2 == 0
except:
    print("Not an even")
else:
    # runs if the code within try runs without errors
    reciprocal  = 1/num
    print(reciprocal)

# ex-2
try:
    f = open("test-file.txt", encoding = 'utf-8')
    # f = open("test-file1.txt", encoding = 'utf-8')
finally:
    f.close()

# ex-3

import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)

# ex-4

# import sys

# randomList = ['a', 0, 2]

# for entry in randomList:
#     try:
#         print("The entry is", entry)
#         r = 1/int(entry)
#         break
#     except ValueError as e:
#         # handle ValueError exception
#         print(e)
#     except (TypeError, ZeroDivisionError) as e:
#         # handle multiple exceptions
#         # TypeError and ZeroDivisionError
#         print(e)
#     except:
#         # handle all other exceptions
#         print(e)
# print("The reciprocal of", entry, "is", r)