# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, splitter=','):
    first_group = participants_first_group.split(splitter)
    second_group = participants_second_group.split(splitter)
    itog_lst = list(set(first_group).intersection(second_group))
    itog_lst.sort()
    return itog_lst



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, splitter='|'))