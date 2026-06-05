def get_age_input(fail_message: str):
    try:
        return int(input("Введите ваш возраст: "))
    except ValueError:
        print(fail_message)
        return None

def get_citizen_status(fail_message: str):
    citizen_status = input("Являетесь ли вы гражданином страны (Да/Нет): ").lower()
    if citizen_status in ["да", "нет"]:
        return citizen_status
    else:
        print(fail_message)
        return None

def get_disqualified_status(fail_message: str):
    disqualified_status = input("Были ли вы дисквалифицированы (Да/Нет): ").lower()
    if disqualified_status in ["да", "нет"]:
        return disqualified_status
    else:
        print(fail_message)
        return None

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

    if age >= 18 and is_citizen == "да" and is_disqualified == "нет":
        print("Разрешено участвовать в голосовании.")
    else:
        print("Запрещено участие в голосовании.")


fail_message = "Введено некорректное значение. Завершение работы программы."
check_vote_status(fail_message)
