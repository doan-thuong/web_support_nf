
def is_value_in_range(value, min_val=None, max_val=None, auto_swap=False):
    """
    Trả về True nếu value nằm trong khoảng [min_val, max_val].
    Nếu auto_swap=True, tự đảo chiều nếu min_val > max_val.
    """
    if value is None:
        return False

    if min_val is not None and max_val is not None and auto_swap and min_val > max_val:
        min_val, max_val = max_val, min_val  # hoán đổi

    if min_val is not None and value < min_val:
        return False
    if max_val is not None and value > max_val:
        return False

    return True
