# %%
#######################################
def convert_timestamp(timestamp: float, tenthousandths=False):
    """Takes a given timestamp in epoch time format and converts it to a human-readable string.

    Examples:
        >>> import os\n
        >>> mtime = os.stat('.').st_mtime\n
        >>> mtime\n
        1635892055.433207
        >>> convert_timestamp(mtime)\n
        '2021-11-02 15:27:35'
        >>> convert_timestamp(mtime, tenthousandths=True)\n
        '2021-11-02 15:27:35.433207'

    References:
        https://stackoverflow.com/questions/39359245/from-stat-st-mtime-to-datetime\n
        https://stackoverflow.com/questions/1111317/how-do-i-print-a-datetime-in-the-local-timezone\n

    Args:
        timestamp (float): Refence an epoch-style timestamp
        tenthousandths (bool, optional): Set tenthousandths=True to include the ten-thousandths-of-a-second values. Defaults to False.

    Returns:
        str: Returns a string version of the timestamp.
    """
    from datetime import datetime
    if tenthousandths:
        readable_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S.%f')
    else:
        readable_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    return readable_time

