from turtle import title
from pandas import array
from math import sqrt

################################################################
# helpers

# run tests


class simpleTest:

    def __init__(self,
                 title: str,
                 description: str,
                 testFunction,
                 args) -> None:

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
                 title: str,
                 timesToRun: int,
                 inputPrompt: str,
                 isInputStringOk,
                 description: str,
                 testFunction) -> None:

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


simpleTest(
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


simpleTest(
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


inputSimpleTest(
    """3. findMaximumNumberFrom3Digits""",
    3,
    'Input 3 digit number: ',
    lambda s: True if len(s) == 3 and s.isdigit() else False,
    'Maximum number is ',
    findMaximumNumberFrom3Digits)
