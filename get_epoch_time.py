# %%
#######################################
def get_epoch_time():
    """Returns the present date and time as a float in epoch timestamp format.

    Examples:
        >>> now = get_epoch_time()\n
        >>> now\n
        1636559940.508071
        
        >>> now_as_dt_obj = convertfrom_epoch_time( now )\n
        >>> now_as_dt_obj\n
        datetime.datetime(2021, 11, 10, 7, 59, 0, 508071)
        
        >>> convertto_human_readable_time( now_as_dt_obj )\n
        '2021-11-10 07:59:00.508071'

    Returns:
        float: Returns a float.
    """
    import datetime
    dt_obj = datetime.datetime.now()
    epoch_time = dt_obj.timestamp()
    return epoch_time

