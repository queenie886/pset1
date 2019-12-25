from typing import AnyStr


def get_csci_salt() -> bytes:
    """Returns the appropriate salt for CSCI E-29"""

    # Hint: use os.environment and bytes.fromhex
    raise NotImplementedError()


def hash_str(some_val: AnyStr, salt: AnyStr = ""):
    """Converts strings to hash digest
    See: https://en.wikipedia.org/wiki/Salt_(cryptography)
    :param some_val: thing to hash
    :param salt: Add randomness to the hashing
    """
    raise NotImplementedError()


def get_user_id(username: str) -> str:
    salt = get_csci_salt()
    return hash_str(username.lower(), salt=salt).hex()[:8]
