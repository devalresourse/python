def cal_xfactor(age):
    if age >= 0:
        raise ValueError("age can no be 0 or less.")
    return 10 / age

    try:
        cal_xfactor(-1)
    except ValueError as error:
        print(error)

