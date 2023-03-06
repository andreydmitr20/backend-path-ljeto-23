from imghdr import tests
from turtle import title
from pandas import array
from math import sqrt

################################################################
# helpers

# run tests


class simpleTest:

    def __init__(self,
                 skip: bool,
                 title: str,
                 description: str,
                 testFunction,
                 args) -> None:
        if not skip:
            self.showTitle(title)
            self.run(
                description,
                testFunction,
                args)

    # show title
    def showTitle(self, title: str) -> None:
        print(f'\n\t Test function: {title}\n')

    # run tests
    def run(self,
            description: str,
            testFunction,
            args) -> None:

        for arg in args:
            print(f'Input: {arg}')
            print(f'{description}: {testFunction(arg)}')


# run tests with user input
class inputSimpleTest(simpleTest):

    def __init__(self,
                 skip: bool,
                 title: str,
                 timesToRun: int,
                 inputPrompt: str,
                 isInputStringOk,
                 description: str,
                 testFunction) -> None:
        if not skip:
            self.showTitle(title)
            self.run(timesToRun,
                     inputPrompt,
                     isInputStringOk,
                     description,
                     testFunction)

    # run tests

    def run(self,
            timesToRun: int,
            inputPrompt: str,
            isInputStringOk,
            description: str,
            testFunction) -> None:

        input_string = ''
        for i in range(0, timesToRun):

            while (True):
                input_string = input('\t'+inputPrompt)
                if not isInputStringOk(input_string):
                    print('Wrong input. Please, input right data.')
                    continue
                break

            super().run(
                description,
                testFunction,
                [input_string])


################################################################
# to skip some tests
skip = True

"""


1. Napravite program koji će ispisati je li srednja znamenka unesenog 
troznamenkastog broja parna, neparna ili nula"""


def testMiddleDigitIn3DigitNumber(number: int) -> str:
    digit = int((number/10) % 10)
    if digit == 0:
        return 'zero'
    if digit % 2 == 0:
        return 'even'
    return 'odd'


simpleTest(skip,
           """1. testMiddleDigitIn3DigitNumber""",
           'Middle digit is ',
           testMiddleDigitIn3DigitNumber,
           [183, 312, 501])


"""


2. Napravite program koji će na zaslon ispisati drugi korijen 
najveće znamenke unesenog troznamenkastog broja"""


def squareRootFromMaximumDigitIn3DigitNumber(number: int) -> str:
    # find max digit
    temp_list = list(str(number))
    temp_list.sort()
    # return sqrt
    return round(sqrt(int(temp_list[2])), 1)


simpleTest(skip,
           """2. squareRootFromMaximumDigitIn3DigitNumber""",
           'Square root is ',
           squareRootFromMaximumDigitIn3DigitNumber,
           [193, 412, 508])


"""


3. Napravite program koji će od korisnika tražiti unos
troznamenkastog broja. Na zaslon treba ispisati naivjeći mogući
troznamenkasti broj koji se može dobiti kombinacijom znamenki unesenog broja"""


def findMaximumNumberFrom3Digits(number: str) -> str:

    temp_list = list(number)
    temp_list.sort(reverse=True)

    return int(''.join(temp_list))


inputSimpleTest(skip,
                """3. findMaximumNumberFrom3Digits""",
                3,
                'Input 3 digit number: ',
                lambda s: True if len(s) == 3 and s.isdigit() else False,
                'Maximum number is ',
                findMaximumNumberFrom3Digits)


"""


3. Napravite program kojim ćete pomoći svojoj razrednici (ili razredniku)
u ispisanju svjedodžbi. Omogućite im unos datuma u obliku: dd.mm.ggg.
Upisani datum ispišite na zaslon tako da mjesec umjesto brojem bude ispisan
njegovim nazivom"""


def convertMonthInDateToItsName(date: str) -> str:
    months = [
        'siječnja',  # 1
        'veljače',  # 2
        'ožujka',  # 3
        'travnja',  # 4
        'svibnja',  # 5
        'lipnja',  # 6
        'srpnja',  # 7
        'kolovoza',  # 8
        'rujna',  # 9
        'listopada',  # 10
        'studeni',  # 11
        'prosinca',  # 12

    ]

    return date[0: 3] + ' ' + months[int(date[4: 6])-1]+' '+date[8:]


simpleTest(False,
           """4. convertMonthInDateToItsName""",
           'Date is ',
           convertMonthInDateToItsName,
           [
               '12. 04. 2006.',
               '24. 03. 2004.',
               '23. 10. 2007.',
           ])
