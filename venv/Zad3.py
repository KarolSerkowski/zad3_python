import csv

with open('prezydent_2015_tura1.csv', 'r') as csvfile:
    content = csv.DictReader(csvfile, delimiter=';')

    contentList = []
    for line in content:
        contentList.append(line)

statisticTemplate = {
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
                       'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0,
                       'Marian Janusz Kowalski': 0,
                       'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0,
                       'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
    'warmińsko-mazurskie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0,
                            'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0,
                            'Marian Janusz Kowalski': 0, 'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0,
                            'Janusz Marian Palikot': 0, 'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
    'wielkopolskie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0,
                      'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0,
                      'Marian Janusz Kowalski': 0,
                      'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0, 'Janusz Marian Palikot': 0,
                      'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
    'zachodniopomorskie': {'Grzegorz Michał Braun': 0, 'Andrzej Sebastian Duda': 0, 'Adam Sebastian Jarubas': 0,
                           'Bronisław Maria Komorowski': 0, 'Janusz Ryszard Korwin-Mikke': 0,
                           'Marian Janusz Kowalski': 0, 'Paweł Piotr Kukiz': 0, 'Magdalena Agnieszka Ogórek': 0,
                           'Janusz Marian Palikot': 0, 'Paweł Jan Tanajno': 0, 'Jacek Wilk': 0},
}

class Application:
    statystykiWybory = {}

    def makeStatistic(self, statisticTemplate={}, contentList=[]):

        self.statystykiWybory = statisticTemplate
        for row in contentList:
            indexWojewodztwo = row['Województwo']
            if (self.statystykiWybory[indexWojewodztwo]):
                for prezydent in (self.statystykiWybory[indexWojewodztwo]):
                    self.statystykiWybory[indexWojewodztwo]['%s' % prezydent] += int(row['%s' % prezydent])

        for wypisujeWojewodztwo in self.statystykiWybory:
            print('')
            print(wypisujeWojewodztwo)
            print('')
            for prezydent in self.statystykiWybory['%s' % wypisujeWojewodztwo]:
                print(prezydent)
                self.statystykiWybory['polska'][prezydent] += int(self.statystykiWybory[wypisujeWojewodztwo][prezydent])
                print(self.statystykiWybory[wypisujeWojewodztwo][prezydent])
        self.writeStatsToCsv(self.statystykiWybory)


    def writeStatsToCsv(self, dictWybory):

        with open('gotoweStatystyki.csv', 'w') as f:
            w = csv.DictWriter(f, fieldnames= dictWybory.keys())
            w.writeheader()
            w.writerow(dictWybory)




wyniki = Application()
wyniki.makeStatistic(statisticTemplate, contentList)


