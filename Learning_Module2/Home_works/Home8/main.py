import calendar


def short_week_day_names_simple(string_list: list) -> list:
    '''
    string_list - list of any strings,
    in case if element equal to week day name - it will be shortened to first 3 letters
    '''
    new_result = []
    for element in string_list:
        if element in list(calendar.day_name):
            new_result.append(element[0:3])
        else:
            new_result.append(element)
    return new_result


def short_week_day_names(string_list: list) -> list:
    '''
    string_list - list of any strings,
    in case if element equal to week day name - it will be shortened to first 3 letters
    '''
    new_result = []
    for element in string_list:
        new_result.append(element[0:3]) if element in list(calendar.day_name) else new_result.append(element)
    return new_result
