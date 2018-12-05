# class AnalysisCsv:
import csv
with open('prezydent_2015_tura1.csv', 'r') as csvfile:
    content = csv.DictReader(csvfile, delimiter=';')

    contentList = []
    for line in content:
        contentList.append(line)

    len(contentList)
    # print(list(contentList))


statisticTemplate={
        'polska': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0,
                'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0,
               'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0,
               'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
        'dolnośląskie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0,
                         'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0,
                         'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0,
                         'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
        'kujawsko-pomorskie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0,
                               'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0,
                               'Marian Janusz Kowalski': 0, 'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0,
                               'Janusz Marian Palikot': 0, 'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
        'lubelskie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0,
                      'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0,
                      'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0,
                      'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
        'lubuskie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0,
                     'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0,
                     'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0,
                     'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
        'łódzkie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0,
                    'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0,
                    'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0,
                    'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
        'małopolskie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0,
                        'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0,
                        'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0,
                        'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
        'mazowieckie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0,
                        'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0,
                        'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0,
                        'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
        'opolskie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0,
                     'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0,
                     'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0,
                     'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
        'podkarpackie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0,
                         'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0,
                         'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0,
                         'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
        'podlaskie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0,
                      'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0,
                      'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0,
                      'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
        'pomorskie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0,
                      'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0,
                      'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0,
                      'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
        'śląskie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0,
                    'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0,
                    'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0,
                    'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
        'świętokrzyskie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0,
                           'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0,
                           'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0,
                           'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
        'warmińsko-mazurskie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0,
                                'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0,
                                'Marian Janusz Kowalski': 0, 'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0,
                                'Janusz Marian Palikot': 0, 'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
        'wielkopolskie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0,
                          'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0, 'Marian Janusz Kowalski': 0,
                          'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0,
                          'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
        'zachodniopomorskie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0,
                               'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0,
                               'Marian Janusz Kowalski': 0, 'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0,
                               'Janusz Marian Palikot': 0, 'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
    }



def makeStatistic(statisticTemplate = {}, contentList = []):
    for row in contentList:
        if(statisticTemplate[row['Województwo']]):
            for x in (statisticTemplate[row['Województwo']]):
                print(x)




makeStatistic(statisticTemplate,contentList)






    #
    # sumator = []
    # i = 0
    # for row in contentList:
    #     # jesli i<= 39 (liczba kolumn) zapetlaj całego if-a, moze dopisywac do tablicy asocjacyjnej aby nie nadpisywało watosci
    #     while (i <= 39):
    #         print(i)
    #
    #         if sumator[i] == row[0]:
    #             sumator[7] += row[7]
    #             print (sumator[i])
    #             # i += 1
    #
    #         else:
    #             sumator[len(sumator + 1)] = row[0]
    #             sumator[7] += row[7]
    #             # i=i+1
    #
    #         i += 1
    #         print(i)




# i+=1

# print(row[0])
# print(row[7])
# i+=1

# with open('prezydent_2015_tura1.csv', 'r') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=';')
#
#
#     for row in csvreader:
#         print(row[0]) # wartość kolumny 1 z tego wiersza
#         print(row[1]) # analogicznie - 2 kolumna
#         print(row[2]) # 3cia
#
#     def

# with open('prezydent_2015_tura1.csv', 'r') as csvfile:
#     csvreader = csv.DictReader(csvfile, delimiter=';')
    # print(csvreader.fieldnames)

    # print(list(csvreader))

    # for row in d:
    #
    #     print(row[Gmina]) # wartość kolumny 1 z tego wiersza
    #     print(row[1]) # analogicznie - 2 kolumna
    #     print(row[2]) # 3cia


    # for row in csvreader:
    #     print(row['Gmina'])
#         # print(row['Andrzej Sebastian Duda'])
