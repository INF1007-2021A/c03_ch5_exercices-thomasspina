from typing import List
import math

def convert_to_absolute(number: float) -> float:
    if number > 0:
        return number
    return number * -1


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    names = []

    for char in prefixes:
        names.append(char + suffixe)
    
    return names


def prime_integer_summation() -> int:
    prime_nums = [2, 3]

    curr_num = 3
    while len(prime_nums) != 100:
        curr_num += 2
        is_prime = True

        for i in range(3, (int(math.sqrt(curr_num)) + 1), 2):
            if curr_num % i == 0 and i != curr_num:
                is_prime = False
                break
        
        if is_prime:
            prime_nums.append(curr_num)

    return sum(prime_nums)


def factorial(number: int) -> int:
    for i in range(1, number):
        number *= i

    return number


def use_continue() -> None:
    for i in range(1, 11):
        if i == 5:
            continue
        print(i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    acceptable_groups = []

    for group in groups:
        if len(group) > 10 or len(group) <= 3:
            acceptable_groups.append(False)
            continue

        has_70, has_50, group_validity = False, False, True
        for age in group:
            if age == 50:
                has_50 = True
            if age > 70:
                has_70 = True

            if (has_70 and has_50) or age < 18:
                group_validity = False
                
            if age == 25:
                group_validity = True
                break 
        
        acceptable_groups.append(group_validity)

    return acceptable_groups


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
