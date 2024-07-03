calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search = [words.lower() for words in list_to_search]
    return string in list_to_search


print(string_info('Capibara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cicle', ['recycling', 'cyclic']))
print(calls)
