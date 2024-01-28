import calendar


def get_result(string_list: list):
    new_result = []
    for element in string_list:
        if element in list(calendar.day_name):
            new_result.append(element[0:3])
        else:
            new_result.append(element)
    return new_result
