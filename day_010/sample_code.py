# Init day 10

# Basic functions with outputs

def format_name(f_name: str, l_name: str) -> str:
    """
    Takes two strings as an input and joins them together
    with a space seperator.
    It then returns the string in Titlecase.
    \n
    Example:\n
    format_name("max", "MUsteR") returns -> "Max Muster"
    """
    return ' '.join([f_name, l_name]).title()


print(format_name("mArCo", "FuCHs"))
