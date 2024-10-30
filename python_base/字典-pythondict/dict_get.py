#coding:utf-8

user_info = {
    'id': 1,
    'username': 'dewei',
    'password': 'abcdefg',
    'created_time': '2020-01-01 11:11:11',
    'birthday': None
}

values = []
id = user_info['id']

values.append(id)
values.append(user_info['username'])
values.append(user_info['password'])
#values.append(user_info['created_time'])
values.append(user_info.get('created_time', '2020-02-02'))
# values.append(user_info['birthday'])
values.append(user_info.get('birthday', '2020-03-03'))

print(values)
# values.append(user_info['birthday'])

# values.append(user_info.get('birthday', '1986-01-01'))
# print(values)
