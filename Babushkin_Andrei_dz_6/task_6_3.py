user_list = ['Иванов,Иван,Иванович', 'Петров,Петр,Петрович']
with open('users.csv', 'w+') as users:
    for user in user_list:
        users.write(user + '\n')

hobby_list = ['скалолазание,охота', 'горные лыжи', 'рыбалка']
with open('hobby.csv', 'w+') as hobby:
    for hob in hobby_list:
        hobby.write(hob + '\n')

with open('users.csv', 'r') as users:
    user = users.read()
with open('hobby.csv', 'r') as hobby:
    hob = hobby.read()

FILENAME = 'users_hobby.txt'

users_list = []
hobby_list = []

for use in user.split('\n'):
    users_list.append(use)
for h in hob.split('\n'):
    hobby_list.append(h)

if len(users_list) > len(hobby_list):
    user_hobby = dict.fromkeys(users_list[:-1])
    user_hobby.update(zip(users_list[:-1], hobby_list[:-1]))
elif len(users_list) < len(hobby_list):
    exit(1)
else:
    user_hobby = dict(zip(users_list[:-1], hobby_list))

with open(FILENAME, 'w+') as u_h:
    u_h.write(str(user_hobby))
with open(FILENAME, 'r') as u_h:
    print(u_h.read())