# %%
#######################################
def convert_file_timestamp_strftime(file_time: float):
    """Takes a given file timestamp and converts it to a human-readable format.

    Examples:
        >>> import os\n
        >>> mtime = os.stat('.').st_mtime\n
        >>> mtime\n
        1635892055.433207
        >>> convert_file_timestamp_strftime(mtime)\n
        '2021-11-02 15:27:35.433207'

    References:
        https://stackoverflow.com/questions/39359245/from-stat-st-mtime-to-datetime\n
        https://stackoverflow.com/questions/1111317/how-do-i-print-a-datetime-in-the-local-timezone\n

    Args:
        file_time (float): Reference a file timestamp.

    Returns:
        str: Returns a string version of the timestamp.
    """
    from datetime import datetime
    readable_time = datetime.fromtimestamp(file_time).strftime('%Y-%m-%d %H:%M:%S.%f')
    return readable_time

