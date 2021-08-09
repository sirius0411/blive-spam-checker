import spamcheck, json

checker = spamcheck.SpamChecker()

print(checker.check({
    'uname': '耵埔WPa户',
    'content': '成*人*直*播 网*址 ΡK6.LivΕ'
}))

print(checker.check({
    'uname': 'bili_1173236677',
    'content': '成*人*直*播 网*址 ΡK6.LivΕ'
}))

print(checker.check({
    'uname': '啊啊啊啊啊fff啊啊啊',
    'content': '成*人*直*播 网*址 ΡK6.LivΕ'
}))

print(checker.check({
    'uname': '啊啊啊啊啊fff啊啊啊',
    'content': '17.44'
}))

print(checker.check({
    'uname': '路人甲',
    'content': '哇嘎奶'
}))

print(checker.check({
    'uname': '守护臀部のV型凹位',
    'content': 'No.10是总榜啦'
}))

# with open('30.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)
#     for i in data['full_comments']:
#         if 'text' in i:
#             name = i['username']
#             content = i['text']
#             result = checker.check({
#                 'uname': name,
#                 'content': content
#             })
#             if result['level'] > 0:
#                 print(result['level'], name, result['signature'])
