# %%
#######################################
def convertto_epoch_time(dt_obj: datetime.datetime):
    """Takes a given datetime object and converts it to an epoch timestamp format.

    Examples:
        >>> now = get_datetime()\n
        >>> now\n
        datetime.datetime(2021, 11, 10, 7, 58, 3, 714462)
        
        >>> convertto_epoch_time( now )\n
        1636559883.714462
        
        >>> convertto_human_readable_time( now )\n
        '2021-11-10 07:58:03.714462'

    Args:
        dt_obj (datetime.datetime): Reference an existing datetime object

    Returns:
        float | int: Returns a float or an integer.
    """
    epoch_time = dt_obj.timestamp()
    return epoch_time

