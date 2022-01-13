def tutors_for_klasses():


    tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
    klasses = ['9А', '7В', '9Б', '9В', '8Б']

    if len(tutors) > len(klasses):
        for t_k in zip(tutors, klasses):
            yield t_k
        for t_n in range(len(klasses), len(tutors)):
            yield (tutors[t_n], None)
    else:
        for t_k in zip(tutors, klasses):
            yield t_k


timetable = tutors_for_klasses()
print(type(timetable))
print(next(timetable))
print(next(timetable))
print(next(timetable))
print(next(timetable))
print(next(timetable))
print(next(timetable))
print(next(timetable))
print(next(timetable))
