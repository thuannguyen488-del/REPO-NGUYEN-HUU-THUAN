# Tạo module password_utils.py:
# is_long_enough(pw)        # >= 8 ký tự
# has_number(pw)
# has_uppercase(pw)
# is_strong_password(pw)    # thỏa cả 3 điều kiện trên
# password_utils.py
def is_long_enough(pw,min_len: int = 8):
    return isinstance(pw,str) and len(pw) >= min_len
def has_number(pw):
    if not isinstance(pw,str):
        return False
    for ch in pw:
        if '0' <= ch <= '9':
            return True
    return False
def has_uppercase(pw):
    if not isinstance(pw, str):
        return False
    for ch in pw:
        if 'A' <= ch <= 'Z':
            return True
    return False
def is_strong_password(pw: str, min_len: int = 8):
    """Trả về True nếu pw thỏa cả 3 điều kiện: dài, có số, có chữ in hoa."""
    return is_long_enough(pw, min_len) and has_number(pw) and has_uppercase(pw)
