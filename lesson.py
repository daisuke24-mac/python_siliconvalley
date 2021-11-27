#### 初めに
# print('hello world')

# # control+Rで実行

# a = 'test'
# b = a
# c = b
# print(c)

#### 変数宣言
# num = 1
# # num : int = 1と書いてもいい
# name = 'Mike'
# is_ok = True
#
# print(num, type(num))
# print(name, type(name))
# print(is_ok, type(is_ok))
#
# num = name
# print(type(num))

#### print文
# print('Hi', 'Mike', sep=',', end='.\n')
#
# import math
#
# result = math.sqrt(25)
# print(result)
# print(help(math))
# # help関数でドキュメントを見れる

#### 文字列
# print("I don't know")
# print('I don\'t know')
# print('say "I don\'t know"')
#
# # rと最初に記述すれば\は無視される（生のデータとして扱われる）
# print(r'C:\name\name')
#
# print('#####')
# print("""\
# line1
# line2
# line3\
# """)
# print('#####')
# # 文の最後に\を書くと改行されない(次の行に続くという意味)
# print('Hi' * 3 + 'Mike')
#
# # 2行に渡ってコードを書くことで見やすいコードになる
# s = ('aaaaaaaaaaaaaaaaaaa'
#      'bbbbbbbbbbbbbbbbbbb')
# print(s)
# l = 'cccccccccccccccccccc'\
#     'dddddddddddddddddddd'
# print(l)

#### 文字のインデックス　
# word = 'python'
# print(word[0])
# print(word[-1])
# print(word[0:2])
# print(word[:2])
# print(word[2:])
# print(word[0:-1])
# word = 'j' + word[1:]
# print(word)
# print(word[:])
# n = len(word)
# print(n)

#### 文字のメソッド
# s = 'My name is Mike. Hi Mike.'
# print(s)
# is_start = s.startswith('My')
# print(is_start)
# is_start = s.startswith('X')
# print(is_start)
# print('############################')
# print(s.find('Mike'))
# print(s.rfind('Mike'))
# print(s.count('Mike'))
# print('############################')
# print(s.capitalize())   # 最初だけ大文字
# print(s.title())        # 全ての単語の1文字目だけ大文字
# print(s.upper())
# print(s.lower())
# print(s.replace('Mike', 'Judy'))

#### 文字の代入
# # formatで入れると数字も文字に変換されて扱われる
# print('a is {}'.format('a'))
# print('a is {}{}{}'.format('1', '2', '3'))
# print('a is {2}{1}{0}'.format('1', '2', '3'))
# print('My name is {name} {family}. Watashi ha {family} {name}.'.format(name='Harry', family='Potter'))
# print(str(1))
# # f-strings
# # 上記の新しい書き方としてf-stringsがある
# a = 'a'
# print(f'a is {a}')
# name, family = 'Harry', 'Potter'
# print(f'My name is {name} {family}.')