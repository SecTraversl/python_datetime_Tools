# %%
#######################################
def get_datetime():
    """Returns the present date and time as a datetime object.
    
    Examples:
        >>> now = get_datetime()\n
        >>> now\n
        datetime.datetime(2021, 11, 10, 7, 58, 3, 714462)
        
        >>> convertto_epoch_time( now )\n
        1636559883.714462
        
        >>> convertto_human_readable_time( now )\n
        '2021-11-10 07:58:03.714462'

    Returns:
        datetime.datetime: Returns a datetime object
    """
    import datetime
    dt_obj = datetime.datetime.now()
    return dt_obj

