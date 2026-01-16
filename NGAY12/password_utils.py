# Tạo module password_utils.py:
# is_long_enough(pw)        # >= 8 ký tự
# has_number(pw)
# has_uppercase(pw)
# is_strong_password(pw)    # thỏa cả 3 điều kiện trên
# password_utils.py
def is_long_enough(pw: str, min_len: int = 8) -> bool:
    """Trả về True nếu pw là chuỗi và có độ dài >= min_len."""
    return isinstance(pw, str) and len(pw) >= min_len

def has_number(pw: str) -> bool:
    """Trả về True nếu pw chứa ít nhất một chữ số 0-9."""
    if not isinstance(pw, str):
        return False
    for ch in pw:
        if '0' <= ch <= '9':
            return True
    return False

def has_uppercase(pw: str) -> bool:
    """Trả về True nếu pw chứa ít nhất một chữ cái in hoa A-Z."""
    if not isinstance(pw, str):
        return False
    for ch in pw:
        if 'A' <= ch <= 'Z':
            return True
    return False

def is_strong_password(pw: str, min_len: int = 8) -> bool:
    """Trả về True nếu pw thỏa cả 3 điều kiện: dài, có số, có chữ in hoa."""
    return is_long_enough(pw, min_len) and has_number(pw) and has_uppercase(pw)
