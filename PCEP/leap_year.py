def is_leapyear(year):
    """
      >>> is_leapyear(1999)
      False
      >>> is_leapyear(1996)
      True
      >>> is_leapyear(1700)
      False
      >>> is_leapyear(1600)
      True
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
