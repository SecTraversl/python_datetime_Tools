# %%
#######################################
def convertto_iso_format(dt_obj: datetime.datetime):
    """Takes a given datetime object and returns the timestamp in ISO format as a string.

    Examples:
        >>> now = get_epoch_time()\n
        >>> now\n
        1636559940.508071
        
        >>> now_as_dt_obj = convertfrom_epoch_time( now )\n
        >>> now_as_dt_obj\n
        datetime.datetime(2021, 11, 10, 7, 59, 0, 508071)
        
        >>> convertto_human_readable_time( now_as_dt_obj )\n
        '2021-11-10 07:59:00.508071'
        
        >>> convertto_iso_format( now_as_dt_obj )\n
        '2021-11-10T07:59:00.508071'

    Args:
        dt_obj (datetime.datetime): Reference an existing datetime object.

    Returns:
        str: Returns a string.
    """
    import datetime
    iso_format = dt_obj.isoformat()
    return iso_format

