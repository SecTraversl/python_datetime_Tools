# %%
#######################################
def test_epoch_time(epoch_time: "int | float"):
    """Takes a given int or float representation of an epoch-style timestamp and runs some tests to see if that timestamp is in an expected format, while additionally printing output on what a datetime.datetime.fromtimestamp() conversion would look like. Some programs store the timestamps in a millisecond or microsecond format (e.g. Firefox and Chrome), and not the format of using seconds; and for those situations this tool will make a recommendation on the syntax to use along with the expected output.

    Examples:
        >>> test_epoch_time(1636562455)\n
        The command:  print(datetime.datetime.fromtimestamp(1636562455))\n
        The results: 2021-11-10 08:40:55\n
        
        >>> test_epoch_time(1621094493163270)\n
        The number of digits in this integer is greater than 10, which is not usual for a normal representation of an epoch timestamp.  It could be that the timestamp is actually representing milliseconds or microseconds, and not seconds. If this is indeed an epoch-style timestamp in a millisecond/microsecond representation, then the syntax and output below demonstrates a way to get potentially desired results.\n\n

        The command:  print(datetime.datetime.fromtimestamp(1621094493163270 / 1000000))\n
        The results: 2021-05-15 09:01:33.163270\n
        
        >>> test_epoch_time(1636562102.9876)\n
        The command: print(datetime.datetime.fromtimestamp(1636562102.9876))\n
        The results: 2021-11-10 08:35:02.987600\n

    References:
        # Shows an example of an epoch-style timestamp that is in milliseconds and how to handle it:\n
        https://stackoverflow.com/questions/12458595/convert-timestamp-since-epoch-to-datetime-datetime\n
        
        # A reference to Firefox / Chrome storing time in microseconds\n
        https://stackoverflow.com/questions/2193820/convert-chrome-history-date-time-stamp-to-readable-format\n

    Args:
        epoch_time (int | float): Reference an int or float representation of an epoch-style timestamp.
    """
    import datetime
    if isinstance(epoch_time, int):
        digits_in_int = len(str(epoch_time))
        if digits_in_int > 10:
            print('The number of digits in this integer is greater than 10, which is not usual for a normal representation of an epoch timestamp.  It could be that the timestamp is actually representing milliseconds or microseconds, and not seconds. If this is indeed an epoch-style timestamp in a millisecond/microsecond representation, then the syntax and output below demonstrates a way to get potentially desired results.\n')
            thedifference = digits_in_int - 10
            divide_by_this = int( '1' + ('0' * thedifference) )
            results = datetime.datetime.fromtimestamp(epoch_time / divide_by_this)
            print(f'The command:  print(datetime.datetime.fromtimestamp({epoch_time} / {divide_by_this}))')
            print(f'The results: {results}')
        else:
            results = datetime.datetime.fromtimestamp(epoch_time)
            print(f'The command:  print(datetime.datetime.fromtimestamp({epoch_time}))')
            print(f'The results: {results}')
    elif isinstance(epoch_time, float):
        wheres_the_decimal = str(epoch_time).find('.')
        if wheres_the_decimal > 10:
            print('This probably is not a correctly formatted epoch timestamp.')
            results = datetime.datetime.fromtimestamp(epoch_time)
            print(f'Here is what the conversion would be: {results}')
        else:
            results = datetime.datetime.fromtimestamp(epoch_time)
            print(f'The command: print(datetime.datetime.fromtimestamp({epoch_time}))')
            print(f'The results: {results}')
    else:
        print("\nThe argument given to the 'epoch_time' parameter is neither an int or a float.\n")

