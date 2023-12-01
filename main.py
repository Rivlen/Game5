from random import randint


def roll(player_input: str):
    try:
        number_of_rolls = int(player_input.split('D')[0])
        die_type = int(player_input.split('D')[1].split("+")[0])
    except Exception:
        exit('Invalid input')
    try:
        modifier = int(player_input.split('D')[1].split("+")[1])
    except ValueError:
        exit('Invalid input')
    except IndexError:
        pass
    rolls = [randint(1, die_type) for _ in range(number_of_rolls)]
    try:
        return sum(rolls) + modifier
    except NameError:
        return sum(rolls)


if __name__ == '__main__':
    print(roll('12D12+20'))
