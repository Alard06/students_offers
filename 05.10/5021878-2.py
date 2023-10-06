def calculate_interest_scheme(P, t, jm):
    if P < 0 or t < 0 or jm < 0:
        print("Ошибка: значения должны быть неотрицательными")
        return

    schemes = ["ЕЖЕГОДНО", "ЕЖЕКВАРТАЛЬНО", "ЕЖЕМЕСЯЧНО"]
    max_interest = 0
    max_scheme = ""

    for m in [1, 4, 12]:
        if m > len(schemes):
            continue

        S = P * (1 + jm / m) ** (m * t)
        I = S - P

        if I > max_interest:
            max_interest = I
            max_scheme = schemes[m - 1]

    print(f"Наиболее выгодная схема: {max_scheme}")
    cop = 0
    for i in range(len(str(max_interest))):
        if str(max_interest)[i] == '.':
            cop = f'{str(max_interest)[i+1]}{str(max_interest)[i+2]}'
            break
    print(f"Величина начисленных процентов равна {int(max_interest)} руб. "
          f"{cop} коп.")


P = float(input("Введите текущую стоимость: "))
t = float(input("Введите время (в годах): "))
jm = float(input("Введите годовую номинальную ставку наращения (в процентах годовых): ")) / 100

calculate_interest_scheme(P, t, jm)


