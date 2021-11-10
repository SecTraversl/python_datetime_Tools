# %%
#######################################
def convertfrom_epoch_time(epoch_time: "int | float"):
    """Takes a given epoch timestamp int or float and converts it to a datetime object.

    Examples:
        >>> now = get_epoch_time()\n
        >>> now\n
        1636559940.508071
        
        >>> now_as_dt_obj = convertfrom_epoch_time( now )\n
        >>> now_as_dt_obj\n
        datetime.datetime(2021, 11, 10, 7, 59, 0, 508071)
        
        >>> convertto_human_readable_time( now_as_dt_obj )\n
        '2021-11-10 07:59:00.508071'

    Args:
        epoch_time (int | float): Reference an epoch timestamp that is an int or a float.

    Returns:
        datetime.datetime: Returns a datetime object.
    """
    import datetime
    dt_obj = datetime.datetime.fromtimestamp(epoch_time)
    return dt_obj

