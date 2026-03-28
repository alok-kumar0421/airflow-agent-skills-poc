# skills.py

def run_tests(context="local"):
    """
    Returns the command to run tests based on execution context.
    """
    if context == "local":
        return "pytest tests/"
    elif context == "breeze":
        return "./breeze testing pytest tests/"
    else:
        return "Unknown context"


def run_static_checks(context="local"):
    """
    Returns the command to run static checks.
    """
    if context == "local":
        return "pre-commit run --all-files"
    elif context == "breeze":
        return "./breeze static-checks"
    else:
        return "Unknown context"