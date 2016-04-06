import sys
import os
from random import shuffle

__version__ = 0.01
__author__ = 'Alex Sanchez\nalex@s1ck.org\n'

arg_help = """

Usage: python3 game.py [options]

Options:
--help, -h\t\tGet help
--version, -v\t\tCheck game version
--author, -c\t\tAuthor information
"""

help_info = """
Приветствуем Вас в игре "Кто хочет стать миллионером"!

Правила игры:
  1. На каждый вопрос может быть только один правильный ответ.
  2. Вы можете выйти из игры в любой момент.
  3. Есть две несгораемые суммы: 5000 и 100000 денег. Т.е. ответив правильно 
     на 5 или 10 вопросов, Вы соответственно гарантируете себе 5000 или 100000
     денег выигрыша, даже если после этого ответите на какой-либо вопрос 
     неверно. 

"""

questions = {

    1: {'prize': 500,
        'question': 'Что растёт в огороде?',
        'answers': ['Лук', 'Пистолет', 'Пулемёт', 'Ракета СС-20'],
        'answer': 'A'},

    2: {'prize': 1000,
        'question': 'Как называют микроавтобусы, совершающие поездки по'
                    ' определённым маршрутам?',
        'answers': ['Рейсовка', 'Путёвка', 'Курсовка', 'Маршрутка'],
        'answer': 'D'},

    3: {'prize': 2000,
        'question': 'О чём писал Грибоедов, отмечая, что он «нам сладок и '
                    'приятен» ?',
        'answers': ['Дым Отечества', 'Дух купечества', 'Дар пророчества',
                    'Пыл девичества'],
        'answer': 'A'},

    4: {'prize': 3000,
        'question': 'Какого персонажа нет в известной считалке «На золотом '
                    'крыльце сидели» ?',
        'answers': ['Сапожника', 'Кузнеца', 'Короля', 'Портного'],
        'answer': 'B'},

    5: {'prize': 5000,
        'question': 'Какой специалист занимается изучением неопознанных '
                    'летающих объектов?',
        'answers': ['Кинолог', 'Уфолог', 'Сексопатолог', 'Психиатр'],
        'answer': 'B'},

    6: {'prize': 10000,
        'question': 'Как называется разновидность воды, в которой атом водорода'
                    ' замещён его изотопом дейтерием?',
        'answers': ['Лёгкая', 'Средняя', 'Тяжёлая', 'Невесомая'],
        'answer': 'C'},

    7: {'prize': 15000,
        'question': 'Что такое десница?',
        'answers': ['Бровь', 'Глаз', 'Шея', 'Рука'],
        'answer': 'D'},

    8: {'prize': 25000,
        'question': 'В какое море впадает река Урал?',
        'answers': ['Азовское', 'Чёрное', 'Средиземное', 'Каспийское'],
        'answer': 'D'},

    9: {'prize': 50000,
        'question': 'На что кладут руку члены английского общества лысых во '
                    'время присяги?',
        'answers': ['Баскетбольный мяч', 'Бильярдный шар', 'Апельсин',
                    'Кокосовый орех'],
        'answer': 'B'},

    10: {'prize': 100000,
         'question': 'Как назывался каменный монолит, на котором установлен '
                     'памятник Петру I в Санкт-Петербурге?',
         'answers': ['Дом-камень', 'Гром-камень', 'Гора-камень',
                     'Разрыв-камень'],
         'answer': 'B'},

    11: {'prize': 200000,
         'question': 'Как Пётр Ильич Чайковский назвал свою серенаду для '
                     'скрипки с оркестром си-бемоль минор?',
         'answers': ['Флегматическая', 'Меланхолическая', 'Холерическая',
                     'Сангвиническая'],
         'answer': 'B'},

    12: {'prize': 400000,
         'question': 'Какого ордена не было у первого советского космонавта '
                     'Юрия Гагарина?',
         'answers': ['«Ожерелье Нила» (Египет)', '«Крест Грюнвальда» (Польша)',
                     '«Плайя Хирон» (Куба)',
                     '«Орден двойного дракона» (Китай)'],
         'answer': 'D'},

    13: {'prize': 800000,
         'question': 'Какое животное имеет второе название — кугуар?',
         'answers': ['Оцелот', 'Леопард', 'Пума', 'Пантера'],
         'answer': 'C'},

    14: {'prize': 1500000,
         'question': 'Что в России 19 века делали в дортуаре?',
         'answers': ['Ели', 'Спали', 'Ездили верхом', 'Купались'],
         'answer': 'B'},

    15: {'prize': 3000000,
         'question': 'Какой химический элемент назван в честь злого подземного '
                     'гнома?',
         'answers': ['Гафний', 'Кобальт', 'Бериллий', 'Теллур'],
         'answer': 'B'}
}


class Game:

    def __init__(self):
        self.fifty_fifty = False
        self.questions = []


class Question:

    def __init__(self, question, prize, answers, answer, _id):
        self.question = question
        self.prize = prize
        self.answer = answer
        self.answers = answers
        self.id = _id

    def fifty_fifty(self, game_obj):
        options = ['a', 'b', 'c', 'd']
        options.remove(self.answer.lower())
        shuffle(options)
        res = [options.pop(1), self.answer.lower()]
        res.sort()
        print('Оставшиеся ответы: ({}) ({})'.format(res[0].upper(),
                                                    res[1].upper()))
        game_obj.fifty_fifty = True


def serve_question(q, game_obj):
    
    os.system('clear')

    print('Вопрос №{} за {} денег. \n\n{}'.format(q.id,
                                                  q.prize,
                                                  q.question))
    print('(A) {:<15} (B) {:<15}\n'
          '(C) {:<15} (D) {:<15}\n'.format(q.answers[0],
                                           q.answers[1],
                                           q.answers[2],
                                           q.answers[3]))
    
    def get_response():
        
        options = ['a', 'b', 'c', 'd', 'q', '1', 'h']

        if game_obj.fifty_fifty:
            options.remove('1')

        print('Опции:\n'
              '{}'
              'h - помощь\n'
              'q - выход'.format('1 - подсказка 50/50\n' 
                                 if not game_obj.fifty_fifty else 
                                 'Подсказка 50/50 использована.\n'))
        ans = input('Ваш ответ: ').lower()
        while ans not in options:
            print('Неверный ввод.')
            return get_response()
        return ans
    
    def validate_response(ans):
        if ans == q.answer.lower():
            print('Правильно! :)\n')
            res = True
        elif ans == 'q':
            confirmation = input('Вы действительно хотите выйти? (y/n): ').lower()
            if confirmation == 'y':
                print('Очень жаль.\n')
                res = False
            else:
                return serve_question(q, game_obj)
        elif ans == '1':
            q.fifty_fifty(game_obj) 
            return validate_response(get_response())
        elif ans == 'h':
            show_help()
            return serve_question(q, game_obj)
        else:
            print('Неправильно :(\n'
                  'Правильный ответ: "{}"\n'.format(q.answer))
            res = False
        return res

    return validate_response(get_response())


def question_lookup(_id):
    try:
        obj = Question(questions[_id]['question'],
                       questions[_id]['prize'],
                       questions[_id]['answers'],
                       questions[_id]['answer'],
                       _id)
        return obj
    except KeyError:
        print('Wrong question ID.')


def play_game():
    
    game = Game()
    game.questions = [question_lookup(i) for i in range(1, 16)]
    
    for q in game.questions:
        if serve_question(q, game):
            if q.id == 15:
                print('Поздравляем, Вы стали миллионером!')
        else:
            if q.id < 5:
                print('Вы проиграли. Выигрыш: 0 денег.\n'
                      'Спасибо за игру!\n')
            elif 5 <= q.id < 10:
                print('Вы проиграли. Выигрыш: {} денег.\n'
                      'Спасибо за игру!\n'.format(game.questions[4].prize))
            else:
                print('Вы проиграли. Выигрыш: {} денег.\n'
                      'Спасибо за игру!\n'.format(game.questions[9].prize))
            break


def show_help():
    print(help_info)
    input('Нажмите ВВОД для продолжения...')


def main():
    
    os.system('clear')
    print('\nДобро пожаловать в "Кто хочет стать миллионером"!\n')
    
    def get_response():
        options = ['n', 'h', 'q']
        ans = input('Выберите опцию: \n'
                    'N - новая игра\n'
                    'H - помощь\n'
                    'Q - выход\n').lower()
        while ans not in options:
            print('Неверный ввод.\n')
            return get_response()
        return ans

    ans = get_response()
    
    if ans == 'n':
        play_game()
    elif ans == 'h':
        show_help()
        main()
    else:
        confirmation = input('Вы действительно хотите выйти? (y/n): ').lower()
        if confirmation == 'y':
            print('До новых встреч.\n')
            sys.exit(0)
        else:
            main()


if len(sys.argv) == 1:
    main()
elif len(sys.argv) == 2:
    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        show_help()
    elif sys.argv[1] == '-v' or sys.argv[1] == '--version':
        print('v{}'.format(__version__))
    elif sys.argv[1] == '-c' or sys.argv[1] == '--author':
        print(__author__)
    else:
        print('\nWrong argument: {}.'.format(sys.argv[1]), arg_help)
              
else:
    print('\nToo many arguments.', arg_help)
