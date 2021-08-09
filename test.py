import spamcheck

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