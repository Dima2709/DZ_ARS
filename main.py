import csv
import pandas as pd
import numpy as np
from collections import Counter

#    1) открываем файл

# with open('movie_bd_v5.csv') as file:
#     data = file.read()

#    2) Находим общее, " "tt ", " ;;;;;;; ", в обоих случаях, работают не на весь объем информации.

# data = data.split('"tt')
# data_qwe = []

# for i in data:
#     data_qwe.append(i.split(';;;;;;;'))

#    3) Сплитим по запятым

# d = []
# for i in data_qwe:
#     mass = []
#     for j in i:
#         mass.append(j.split(','))
#     for c in mass:
#         d.append(c)

#   4) убираем пустые массивы

# e = []
# for i in d:
#     if len(i) > 2:
#         e.append(i)

#   5) Проблемная зона, там " ;;;;;;; " стоят между значениями строки

# e_new = []
# for i in e[:84]:
#     e_new.append(i)
# e1 = e[84] + e[85]
# e_new.append(e1)
# for i in e[86:]:
#     e_new.append(i)

#   6) Убираем первые 3 и 3 последних столбца, там проблем не заметил

# qwerty = []
# for i in e_new:
#     mass = []
#     for j in i[3:-3]:
#         mass.append(j)
#     qwerty.append(mass)

#   7) готовим колонки - runtime, genre, production_companies, a = индексы, проблемных зон, там стоят запятые в колонке production_companies.(нужно написать алгоритм по получению этих индексов.

# a = [219, 221, 271,289,372,410,471,489,511,559,592,607,608,673,741,755,862,877,885,971,1015,1100,1258,1452,1522,1541,1567,1686,1709,1731,1792,1831]
# run_genre_comp = []
# for i in range(len(qwerty)):
#     if i in a:
#         q = []
#         q.append(','.join(qwerty[i][-4:-2]))
#         q = q[0].split(',')
#         q.append(' '.join(qwerty[i][-2:]))
#         run_genre_comp. append(q)
#     else:
#         run_genre_comp.append(qwerty[i][-3:])

#   8) Готовим колонки - original_title, cast, director. К сожалению, решение проблемы пока не придумал, в названии стоят запятые, похоже решить можно только вручную и то не понятно, как обнаружить проблему, везде строки.

# tit_cast_dir = []
# for i in qwerty:
#     tit_cast_dir.append(i[:3])

#   9) Готовим первые 3 колонки, надо почистить id, через isdigit()

# first3=[]
# for i in e_new:
#     mass = []
#     for j in i[:3]:
#         mass.append(j)
#     first3.append(mass)

#   10) Готовим последние 3 колонки, до заданий с датой не дошел, может нужно будет мудрить с этой колонкой

# last3 = []
# for i in e_new:
#     mass = []
#     for j in i[-3:]:
#         mass.append(j)
#     last3.append(mass)

#   11) Объединяем все колонки, записываем файл. Без колонок 'tagline', 'overview', в заданиях они не нужны.

# for i in range (len(run_genre_comp)):
#     mass = []
#     for j in  range(len(run_genre_comp[i])):
#         mass.append(run_genre_comp[i][j])
#         mass.append(last3[i][j])
#         mass.append(first3[i][j])
#         mass.append(tit_cast_dir[i][j])
#     with open(f"data1.csv", "a", encoding="utf-8") as file:
#              writer = csv.writer(file,delimiter=",", lineterminator='\n')
#              writer.writerow(mass)

# Класс с методами для выполнения заданий.

class data:

    def __init__(self,df):
        self.df = df

        self.df = pd.read_csv(self.df)

    # Редактирование колонки release_year:

        for i in range(len(self.df['release_year'])):
            mass = []
            for j in self.df['release_year'][i]:
                if j.isdigit():
                    mass.append(j)
            self.df['release_year'][i] = int(''.join(mass))


    # 1. У какого фильма из списка самый большой бюджет?
    # 2. Какой из фильмов самый длительный (в минутах)?

    def max(self, arg):
        self.arg = arg
        for i in range(len(self.df[arg])):
            if self.df[arg][i] == self.df[arg].max():
                print(self.df.iloc[i])

    # 3. Какой из фильмов самый короткий(в минутах)?

    def min(self,arg):
        self.arg = arg
        for i in range(len(self.df[arg])):
            if self.df[arg][i] == self.df[arg].min():
              print(self.df.iloc[i])

    # 4. Какова средняя длительность фильмов?

    def avg(self,arg):
        self.arg = arg
        print(self.df[arg].sum()/self.df[arg].count())

    # 5. Каково медианное значение длительности фильмов?

    def med(self,arg):
        self.arg = arg
        if len(self.df[arg]) % 2 == 0:
            a = self.df[arg].sort_values()
            print((a.iloc[len(a)/2]+a.iloc[len(a)/2-1])/2)
        else:
            a = self.df[arg].sort_values()
            print(a.iloc[int(len(a) / 2 + 1)])

    # 6. Какой самый прибыльный фильм?
    # 7. Какой фильм самый убыточный?

    def profit(self):
        self.df['profit'] = self.df['revenue'] - self.df['budget']

        the.max('profit')

        the.min('profit')

    #8. У скольких фильмов из датасета объем сборов оказался выше бюджета?

    def count_dif(self):
        count = 0
        for i in range(len(self.df['budget'])):
            if self.df['budget'][i] < self.df['revenue'][i]:
                count +=1
        print(count)

    #9. Какой фильм оказался самым кассовым в 2008 году?

    def max_profit_years(self,arg):
        self.arg = arg
        self.df['profit'] = self.df[(self.df.release_year == arg)]['revenue'] - self.df[(self.df.release_year == arg)]['budget']
        for i in range(len(self.df['profit'])):
            if self.df['profit'][i] == self.df['profit'].max():
                print(self.df.iloc[i])

    #10. Самый убыточный фильм за период с 2012 по 2014 г. (включительно)?

    def low_profit_years(self,arg,arg1):
        self.arg = arg
        self.arg1 = arg1
        self.df['profit'] = self.df[(self.df.release_year <= arg1) & (self.df.release_year >= arg)]['revenue'] - self.df[(self.df.release_year <= arg1) & (self.df.release_year >= arg)]['budget']
        for i in range(len(self.df['profit'])):
            if self.df['profit'][i] == self.df['profit'].min():
                print(self.df.iloc[i])

    #11. Какого жанра фильмов больше всего?

    def genre_max(self):
        mass1 = []
        mass2 = []
        for i in self.df['genres']:
            mass1.append(i.split('|'))
        for i in mass1:
            for j in i:
                mass2.append(j)
        count = Counter(mass2)
        print ([i for i in count.keys()][[count[i] for i in count.keys()].index(max(count[i] for i in count.keys()))])

    #12. Фильмы какого жанра чаще всего становятся прибыльными?

    def genre_profit(self):

        self.df['profit'] = self.df['revenue'] - self.df['budget']
        mass1 = []
        mass2 = []
        for l in range(len(self.df['profit'])):
            if self.df['profit'][l] > 0:
                mass1.append(self.df['genres'][l].split('|'))
        for i in mass1:
            for j in i:
                mass2.append(j)
        count = Counter(mass2)
        print([i for i in count.keys()][[count[i] for i in count.keys()].index(max(count[i] for i in count.keys()))])

    #13. У какого режиссера самые большие суммарные кассовые сбооры?

    def dir_win(self):

        self.df['profit'] = self.df['revenue'] - self.df['budget']
        a = {}
        for i in self.df['director'].unique():
            a[i] = []
        for j in list(a.keys()):
            mass = []
            for i in range(len(self.df['director'])):
                if self.df['director'][i] == j:
                    mass.append(self.df['profit'][i])
            a[j].append(sum(mass))

        for i in list(a.keys()):
            if a[i] == max(a.values()):
                print(i, a[i])

    #14. Какой режисер снял больше всего фильмов в стиле Action?

    def dir_genre(self,arg):

        self.arg = arg
        a = {}
        for i in self.df['director'].unique():
            a[i] = 0

        for i in range(len(self.df['genres'])):
            mass1 = []
            mass1.append(self.df['genres'][i].split('|'))
            for j in mass1:
                for l in j:
                    if l == arg:
                        a[self.df['director'][i]] += 1
        for i in list(a.keys()):
            if a[i] == max(a.values()):
                print(i, a[i])

    #15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году?

    def cast_profit(self,arg):

        self.df['profit'] = self.df['revenue'] - self.df['budget']
        a = {}
        mass = []
        mass1 = []
        for i in self.df[(self.df['release_year'] == arg)]['cast']:
            mass.append(i)

        for i in mass:
            for j in i.split('|'):
                mass1.append(j)

        for i in set(mass1):
            a[i] = []
        for i in a.keys():
            mass = []
            for j in range(len(self.df[(self.df['release_year'] == arg)]['cast'])):
                for l in self.df['cast'][j].split('|'):
                    if l == i:
                        mass.append(self.df['profit'][j])
            a[i].append(sum(mass))

        for i in list(a.keys()):
            if a[i] == max(a.values()):
                print(i, a[i])

    #16. Какой актер снялся в большем количестве высокобюджетных фильмов?

    def cast_bud(self):

        mass = []
        mass1 = []
        for i in self.df[(self.df['budget'] > self.df['budget'].sum() / self.df['budget'].count())]['cast']:
            mass.append(i)

        for i in mass:
            for j in i.split('|'):
                mass1.append(j)
        count = Counter(mass1)
        print([i for i in count.keys()][[count[i] for i in count.keys()].index(max(count[i] for i in count.keys()))])

    #17. В фильмах какого жанра больше всего снимался Nicolas Cage?

    def gen_cast(self,arg):
        mass = []
        mass1 = []
        for i in range(len(self.df['cast'])):
            for j in self.df['cast'][i].split('|'):
                if j == arg:
                    mass.append(i)
        for i in mass:
            for j in self.df['genres'][i].split('|'):
                mass1.append(j)
        count = Counter(mass1)
        print([i for i in count.keys()][[count[i] for i in count.keys()].index(max(count[i] for i in count.keys()))])

    #18. Самый убыточный фильм от Paramount Pictures

    def low_profit_com(self,arg):

        mass = []
        mass1 = []
        self.df['profit'] = self.df['revenue'] - self.df['budget']
        for i in range(len(self.df['production_companies'])):
            for j in self.df['production_companies'][i].split('|'):
                if j == 'Paramount Pictures':
                    mass.append(self.df['profit'][i])
                    mass1.append(i)

        a = mass.index(min(mass))
        print(self.df.iloc[mass1[a]])

    #19. Какой год стал самым успешным по суммарным кассовым сборам?

    def years_prof(self):

        a = {}
        self.df['profit'] = self.df['revenue'] - self.df['budget']
        for i in self.df['release_year'].unique():
            a[i] = []

        for i in list(a.keys()):
            mass = []
            for j in range(len(self.df['release_year'])):
                if i == self.df['release_year'][j]:
                    mass.append(self.df['profit'][j])
            a[i].append(sum(mass))
        for i in list(a.keys()):
            if a[i] == max(a.values()):
                print(i,' - ', a[i][0])

    #20. Какой самый прибыльный год для студии Warner Bros?

    def comp_max_year(self,arg):
        a = {}
        self.df['profit'] = self.df['revenue'] - self.df['budget']
        for i in self.df['release_year'].unique():
            a[i] = []
        mass = []
        for i in range(len(self.df['production_companies'])):
            for j in self.df['production_companies'][i].split('|'):
                if j == arg:
                    mass.append(i)
        for i in mass:
            mass1 = []
            a[self.df['release_year'][i]].append(self.df['profit'][i])

        for i in list(a.keys()):
            a[i] = sum(a[i])

        for i in list(a.keys()):
            if a[i] == max(a.values()):
                print(i, ' - ', a[i])

    #21. В каком месяце за все годы суммарно вышло больше всего фильмов?

















the = data('data1.csv')
# the.max('runtime')
# the.min('runtime')
#the.avg('runtime')
#the.med('runtime')
#the.profit()
#the.count_dif()
#the.max_profit_years(2008)
#the.low_profit_years(2012, 2014)
#the.genre_max()
#the.genre_profit()
#the.dir_win()
#the.dir_genre('Action')
#the.cast_profit(2013)
#the.cast_bud()
#the.gen_cast('Nicolas Cage')
#the.low_profit_com('Paramount Pictures')
#the.years_prof()
the.comp_max_year('Warner Bros.')
