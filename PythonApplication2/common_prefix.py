def all_startwith_string(words, str):
    """ 
    checks if all items in words list start with str
    """
    all_startwith = True
    for item in words:
        if not item.startswith(str):
            all_startwith = False
            break
    return all_startwith


def find_shortest_string_in_list(words):
    shortest = words[0]
    for i in words:
        if len(i) < len(shortest):
            shortest = i
    return shortest


def find_common_prefix_between(words):
    if '' in words:
        return ''
    shortest = find_shortest_string_in_list(words)
    prefix = ''
    index = 1
    keep_going = True
    while keep_going:
        if index > len(shortest):
            break
        prefix_check = shortest[:index]
        if all_startwith_string(words, prefix_check):
            prefix = prefix_check
            index +=1
        else:
            keep_going = False
    return prefix
