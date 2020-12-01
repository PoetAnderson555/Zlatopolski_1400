# 3.1.	 Дано расстояние в сантиметрах. Найти число полных метров в  нем.

def cm_m(cm):
    return f'В {cm} см {cm // 100} полных метров'


# 3.2.	 Дана масса в  килограммах. Найти число полных центнеров в  ней.

def kg_cent(kg):
    return f'В {kg} кг {kg // 100} центнеров'


# 3.3.	 С  некоторого момента прошло 234 дня. Сколько полных
# недель прошло за этот период?

print(f'За этот период прошло {234 // 7} недель')


# 3.4.	 Написать программу, которая решает следующую задачу:
# «N школьников делят k яблок поровну так, чтобы каждому достались только целые яблоки,
# остальные яблоки остаются в  корзинке. Определить, сколько яблок достанется каждому школьнику
# и  сколько яблок останется в корзинке».

def apples(N, k):
    return f'Каждому школьнику достанется {k // N} яблок, а в корзинке останется {k % N}'


# 3.5.	 Дан прямоугольник с  размерами 543×130 мм. Сколько
# квадратов со стороной 130 мм можно отрезать от него?

def otrezh_kvadrat(a=543, b=130, c=130):
    a1 = a // c
    a2 = b // c
    if a < c or b < c:
        return f"Хер ты получишь квадрат со стороной {c}"
    elif a1 >= 1 and a2 >= 1:
        return f'Ты можешь получить {min(a1, a2)} квадратов'


# 3.6.	 В  купейном вагоне имеется 9 купе с  четырьмя местами
# для пассажиров в каждом. Определить номер купе, в котором находится место с  заданным номером
# (нумерация мест сквозная, начинается с 1).

def kupe(mesto):
    if 0 <= mesto <= 36:
        return f'Ваше место находится в {mesto // 4} купе'
    else:
        return 'Твоё место в другом поезде, идиот'


# 3.7.	 В  подъезде № 1 пятиэтажного жилого дома 15 квартир.
# Определить, на каком этаже этого подъезда находится квартира
# с  заданным номером.
import math


def etazh(kvartira):
    if 0 <= kvartira <= 15:
        return f'Ваш этаж - {math.ceil(kvartira / 3)}'
    else:
        return 'Вали с нашей территории'


# 3.8.	 В кинотеатре имеется 20 рядов мест для зрителей, в каждом из которых расположено 15 кресел.
# Билет для зрителей имеет серию АВ и  номер билета, для первого места в  первом ряду
# равного 01643 (далее этот номер увеличивается согласно условному обозначению мест, имеющему вид, показанный в таблице
# ниже):
# 1 2 … 15
# 16 17 … 30
# … … … …
# 286 287 300
# Определить, в  каком ряду находится место, билет на которое
# имеет заданный серийный номер.

n = 20
m = 15
a = [[0] * m for i in range(n)]  # Здесь создаётся пустой массив

k = 1643
for i in range(n):
    for j in range(m):  # Здесь этот массив заполняется номерами билетов
        a[i][j] = k
        k += 1


def row(bilet):
    if 1643 <= bilet < 1943:
        for i in range(n):
            for j in range(m):
                if a[i][j] == bilet:
                    return f'Ваш ряд: {i + 1}'  # Здесь проверяется условие попадание билета в этот зал
    else:
        return f'Вы не в том кинотеатре'


# 3.9.	 С  начала суток прошло n секунд. Определить:
# а) сколько полных часов прошло с  начала суток;
# б) сколько полных минут прошло с начала очередного часа;
# в) сколько полных секунд прошло с начала очередной минуты.

def time(secunds):
    print(f'С начала суток прошло {secunds // 3600} часов')
    print(f'С начала очередного часа прошло {secunds % 3600} минут')
    print(f'С начала очередной минуты прошло {secunds % 3600 % 60} секунд')


# 3.10.	 Дано целое число k (1 ≤ k ≤ 365). Присвоить целочисленной величине n значение 1, 2, ..., 6 или 0
# в  зависимости от того, на какой день недели (понедельник, вторник, ..., субботу или
# воскресенье) приходится k-й день года, в котором 1  января:
# а) понедельник;
# б) вторник;
# в) d-й день недели (если 1 января– понедельник, то d = 1, если
# вторник – d = 2, ..., если воскресенье – d = 7).
nedela = {1: 'понедельник',
          2: 'вторник',
          3: 'среда',
          4: 'четверг',
          5: 'пятница',
          6: 'суббота',
          7: 'воскресенье'}


def den_nedeli(k=1, d=1):
    if k > 365 or k < 1:
        return 'В году 365 дней, идиот'

    if d > 7 or d < 1:
        return "в неделе 7 дней, дурак"
