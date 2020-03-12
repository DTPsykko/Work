# Error Handling

while True:
    try:
        age = int(input('What is your age?'))
        10/age
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter a number larger than 0')
    else:
        print('thanks lmao')
        break
    finally:
        print('ok, i am finally done')


# def sum(num1, num2):
#     try:
#         return num1/num2
#     except (TypeError, ZeroDivisionError):
#         print('something ain\'t right boi. enter numbers')


# print(sum(7, 6))
