"""
Homework 'mini zbirka'
"""

from math import sqrt

################################################################


class SimpleTest:
    """ Class for function testing """

    def __init__(
            self,
            skip_test: bool,
            title: str,
            description: str,
            test_function) -> None:

        self.__title = title
        self.__description = description
        self.__test_function = test_function
        self.__skip_test = skip_test

        if self.get_skip_test():
            return
        self.show_title()

    def get_title(self):
        """getter"""
        return self.__title

    def get_description(self):
        """getter"""
        return self.__description

    def get_test_function(self):
        """getter"""
        return self.__test_function

    def get_skip_test(self):
        """getter"""
        return self.__skip_test

    def show_title(self) -> None:
        """show title"""
        print(f'\n\t Test function: {self.get_title()}\n')

    def run(self, args_list: list) -> None:
        """ run tests """
        if self.get_skip_test():
            return

        for arg in args_list:
            print(f'Input: {arg}')
            print(f'{self.get_description()}: {self.get_test_function()(arg)}')


class InputSimpleTest(SimpleTest):

    """Class for function testing with users inputs"""

    def __init__(
            self,
            skip_test: bool,
            title: str,
            description: str,
            test_function,
            times_to_run: int,
            input_prompt: str,
            is_input_string_ok) -> None:

        super().__init__(
            skip_test,
            title,
            description,
            test_function)

        self.__times_to_run = times_to_run
        self.__input_prompt = input_prompt
        self.__is_input_string_ok = is_input_string_ok

    def get_times_to_run(self):
        """getter"""
        return self.__times_to_run

    def get_input_prompt(self):
        """getter"""
        return self.__input_prompt

    def get_is_input_string_ok(self):
        """getter"""
        return self.__is_input_string_ok

    def run(self, args_list: list) -> None:
        """ run tests"""
        if self.get_skip_test():
            return

        input_string = ''
        for _ in range(0, self.get_times_to_run()):

            while True:
                input_string = input('\t'+self.get_input_prompt())
                if not self.get_is_input_string_ok()(input_string):
                    print('Wrong input. Please, input right data.')
                    continue
                break

            super().run([input_string])


################################################################
# to skip some tests
SKIP = False

print("""
1. Napravite program koji će ispisati je li srednja znamenka unesenog 
troznamenkastog broja parna, neparna ili nula""")


def test_middle_digit_in_3digit_number(number: int) -> str:
    """je li srednja znamenka unesenog troznamenkastog broja parna, neparna ili nula"""
    digit = int((number/10) % 10)
    if digit == 0:
        return 'zero'
    if digit % 2 == 0:
        return 'even'
    return 'odd'


SimpleTest(SKIP,
           """test_middle_digit_in_3digit_number""",
           'Middle digit is ',
           test_middle_digit_in_3digit_number
           ).run([183, 312, 501])


print("""
2. Napravite program koji će na zaslon ispisati drugi korijen 
najveće znamenke unesenog troznamenkastog broja
""")


def square_root_from_maximum_digit_in_3digit_number(number: int) -> str:
    """ drugi korijen najveće znamenke unesenog troznamenkastog broja"""
    # find max digit
    temp_list = list(str(number))
    temp_list.sort()
    # return sqrt
    return round(sqrt(int(temp_list[2])), 1)


SimpleTest(SKIP,
           """square_root_from_maximum_digit_in_3digit_number""",
           'Square root is ',
           square_root_from_maximum_digit_in_3digit_number
           ).run([193, 412, 508])


print("""
3. Napravite program koji će od korisnika tražiti unos
troznamenkastog broja. Na zaslon treba ispisati naivjeći mogući
troznamenkasti broj koji se može dobiti kombinacijom znamenki unesenog broja
""")


def find_maximum_number_from_3digits(number: str) -> str:
    """naivjeći mogući troznamenkasti broj koji se može dobiti kombinacijom znamenki unesenog broja"""

    temp_list = list(number)
    temp_list.sort(reverse=True)

    return int(''.join(temp_list))


InputSimpleTest(SKIP,
                """find_maximum_number_from_3digits""",
                'Maximum number is ',
                find_maximum_number_from_3digits,
                3,
                'Input 3 digit number: ',
                lambda s: True if len(s) == 3 and s.isdigit() else False,
                ).run([])


print("""
4. Napravite program kojim ćete pomoći svojoj razrednici (ili razredniku)
u ispisanju svjedodžbi. Omogućite im unos datuma u obliku: dd.mm.ggg.
Upisani datum ispišite na zaslon tako da mjesec umjesto brojem bude ispisan
njegovim nazivom
""")


def convert_month_in_date_to_its_name(date: str) -> str:
    """mjesec umjesto brojem bude ispisan njegovim nazivom"""
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


SimpleTest(False,
           """4. convert_month_in_date_to_its_name""",
           'Date is ',
           convert_month_in_date_to_its_name
           ).run([
               '12. 04. 2006.',
               '24. 03. 2004.',
               '23. 10. 2007.',
           ])
