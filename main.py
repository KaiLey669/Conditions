def get_age_input(fail_message: str):
    try:
        return int(input("Введите ваш возраст: "))
    except ValueError:
        print(fail_message)
        return None

def get_citizen_status(fail_message: str):
    citizen_status = None
    try:
        citizen_status = int(input("Являетесь ли вы гражданином страны (1 - Да, 2 - Нет): "))
        if citizen_status not in [1, 2]:
            return None
        elif citizen_status == 1:
            return True
        else:
            return False
    except ValueError:
        print(fail_message)
    return citizen_status

def get_disqualified_status(fail_message: str):
    disqualified_status = None
    try:
        disqualified_status = int(input("Были ли вы дисквалифицированы (1 - Да, 2 - Нет): "))
        if disqualified_status not in [1, 2]:
            return None
        elif disqualified_status == 1:
            return True
        else:
            return False
    except ValueError:
        print(fail_message)
    return disqualified_status

def check_vote_status(fail_message: str):
    age = get_age_input(fail_message)
    if age is None:
        return

    is_citizen = get_citizen_status(fail_message)
    if is_citizen is None:
        return

    is_disqualified = get_disqualified_status(fail_message)
    if is_disqualified is None:
        return

    if age >= 18 and is_citizen and not is_disqualified:
        print("Разрешено участвовать в голосовании.")
    else:
        print("Запрещено участие в голосовании.")


fail_message = "Введено некорректное значение. Завершение работы программы."
check_vote_status(fail_message)
