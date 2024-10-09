# Напишите функцию, которая принимает на вход список строк и возвращает новый список, 
# в котором каждая строка заменяется на её обратную, но только если длина строки больше 3 символов.


# ['aefe', 'ifjeoa', 'ab'] > 

def revert_string(orig_list: list) -> list:
    temp_list = []
    for s in orig_list:
        if len(s) > 3:
            s = s[::-1]
        temp_list.append(s)
    return temp_list


if __name__ == "__main__":
    original_list = ['aefe', 'ifjeoa', 'ab']
    result = revert_string(original_list)
    print(result)
