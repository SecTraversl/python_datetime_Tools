# %%
#######################################
def convert_file_timestamp(file_time: float, utc=False):
    """Takes a given file timestamp and converts it to a human-readable format.

    Examples:
        >>> import os\n
        >>> os.stat('.').st_mtime\n
        1635892055.433207
        >>> mtime = os.stat('.').st_mtime\n

        >>> convert_file_timestamp(mtime)\n
        '2021-11-02 15:27:35.433207'
        >>> convert_file_timestamp(mtime, utc=True)\n
        '2021-11-02 22:27:35.433207+00:00'

    References:
        https://stackoverflow.com/questions/39359245/from-stat-st-mtime-to-datetime\n
        https://stackoverflow.com/questions/1111317/how-do-i-print-a-datetime-in-the-local-timezone\n

    Args:
        file_time (float): Reference a file timestamp.
        utc (bool, optional): Set utc=True to get the returned timestamp in UTC. Defaults to False.

    Returns:
        str: Returns a string version of the timestamp.
    """
    from datetime import datetime, timezone
    if utc:
        dt_obj = datetime.fromtimestamp(file_time, tz=timezone.utc)
    else:
        dt_obj = datetime.fromtimestamp(file_time)
    readable_time = str(dt_obj)
    return readable_time

