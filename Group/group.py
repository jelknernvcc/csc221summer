import random


students = {
    "Hayfield": [("Abby", 0), ("Ryan", 1), ("Hector R", 2), ("Xavier", 0),
                 ("Travis", 0), ("Lael", 1), ("Aidan", 1)],
    "Robinson": [("Emmanuel", 1), ("Keiry", 1)],
    "Oakton": [("Jakob", 0)],
    "Alexandria City": [("Cristian", 1), ("Nico", 2)],
    "ACC": [("Fikir", 2), ("Johan", 2), ("Anar", 2)],
    "Wakefield": [("Sophia", 1), ("Eliana", 1), ("Alan", 1)],
    "Justice": [("Emma", 0), ("Jamil", 1)],
    "Arlington Community": [("Heydi", 0)],
    "Washington-Liberty": [("Joan", 0), ("Sid", 2)],
    "Yorktown": [("Luis", 2)],
    "James Madison": [("Rami", 2)],
}


def student_names():
    names = []
    for school in students.keys():
        for student in students[school]:
            names.append(student[0])
    return names


def random_groups_of_n(n):
    the_students = student_names()
    groups = []
    while len(the_students) > n:
        group = []
        for i in range(n):
            name = random.choice(the_students)
            group.append(name)
            the_students.remove(name)
        groups.append(group)
    groups.append(the_students)
    return groups


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(random_groups_of_n(6))
