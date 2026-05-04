def is_armstrong_number(number):
    list1 = list(str(number))
    x = len(list1)
    list2 = [int(i) ** x for i in list1]
    final_number = sum(list2)
    return final_number == number
    pass
