# TODO Напишите функцию find_common_participants
def find_common_participation(first_group, second_group, argument):
    common_participation = []
    for members_first_group in first_group.split(argument):
        if members_first_group in second_group.split(argument):
            common_participation.append(members_first_group)
    common_participation.sort()
    print(common_participation)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
find_common_participation(participants_first_group, participants_second_group, "|")
