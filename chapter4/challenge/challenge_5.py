def to_float(x):
    """
    文字列を浮動小数点数に変換する。
    :param x: str.
    :return: string converted to int.
    """
    try:
        result = float(x)
    except ValueError:
        print("Invalid Value.")
    else:
        print(result)

to_float("1")