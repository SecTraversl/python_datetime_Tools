# %%
#######################################
def convertto_human_readable_time(dt_obj: datetime.datetime):
    """Takes a given datetime object and returns a string representation of that date/time in a easily understood human readable format.

    Examples:
        >>> now = get_datetime()\n
        >>> now\n
        datetime.datetime(2021, 11, 10, 7, 58, 3, 714462)
        
        >>> convertto_epoch_time( now )\n
        1636559883.714462
        
        >>> convertto_human_readable_time( now )\n
        '2021-11-10 07:58:03.714462'

    Args:
        dt_obj (datetime.datetime): Reference an existing datetime object.

    Returns:
        str: Returns a string.
    """
    import datetime
    human_readable_timestamp = str(dt_obj)
    return human_readable_timestamp

