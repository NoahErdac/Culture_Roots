import re

def sanitize_text(text: str) -> str:
    """Strips basic HTML tags to prevent simple XSS injections."""
    if not text:
        return text
    clean_text = re.sub(r'<[^>]*?>', '', text)
    return clean_text.strip()