import hashlib


def hash_text(text: str) -> str:
    """
    Converts plain text into a SHA-256 hash.

    Args:
        text: Plain text to hash.

    Returns:
        SHA-256 hash as a hexadecimal string.
    """

    return hashlib.sha256(text.encode("utf-8")).hexdigest()