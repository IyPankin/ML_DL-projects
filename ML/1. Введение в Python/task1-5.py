from typing import List


def hello(name: str = None) -> str:
    if name == "" or not name:
        return "Hello!"
    else:
        return f"Hello, {name}!"


def int_to_roman(num: int) -> str:
    roman_nums = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    roman = ''
    for value, symbol in roman_nums.items():
        while num >= value:
            roman += symbol
            num -= value

    return roman


def longest_common_prefix(strs_input: List[str]) -> str:
    if not strs_input:
        return ""
    cur_pref = strs_input[0].strip()
    if len(strs_input) == 1:
        return cur_pref

    for i in range(1, len(strs_input)):
        cur_str = strs_input[i].strip()
        tmp = ""
        for j in range(min(len(cur_str), len(cur_pref))):
            if cur_str[j] != cur_pref[j]:
                break
            else:
                tmp += cur_pref[j]
        cur_pref = tmp
        if cur_pref == "":
            return ""
    return cur_pref


def primes() -> int:
    yield 2
    number = 3
    while True:
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            yield number
        number += 2


class BankCard:
    def __init__(self, total_sum: int, balance_limit: int = None):
        self.total_sum = total_sum
        self.balance_limit = balance_limit

    def __call__(self, sum_spent):
        if sum_spent > self.total_sum:
            print("Not enough money to spend {} dollars.".format(sum_spent))
            raise ValueError()
        self.total_sum -= sum_spent
        print("You spent {} dollars.".format(sum_spent))

    def __str__(self):
        return "To learn the balance call balance."

    def put(self, sum_put):
        self.total_sum += sum_put
        print("You put {} dollars.".format(sum_put))

    @property
    def balance(self):
        if self.balance_limit is None:
            return self.total_sum
        elif self.balance_limit > 0:
            self.balance_limit -= 1
            return self.total_sum
        else:
            print("Balance check limits exceeded.")
            raise ValueError()

    def __add__(self, other):
        ans = self.total_sum + other.total_sum
        if self.balance_limit is not None and other.balance_limit is not None:
            tot = max(self.balance_limit, other.balance_limit)
        else:
            tot = None
        return BankCard(ans, tot)