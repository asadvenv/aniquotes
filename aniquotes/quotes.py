from random import choice
from typing import Dict, List, Optional

from aniquotes.data import QUOTES

def filter_quotes(
    character: Optional[str] = None,
    show: Optional[str] = None,
    search: Optional[str] = None,
) -> List[Dict[str, str]]:

    if not character and not show and not search:
        return QUOTES

    c_query = character.strip().lower() if character else None
    s_query = show.strip().lower() if show else None
    q_query = search.strip().lower() if search else None

    results = []
    for item in QUOTES:
        if c_query and c_query not in item.get("character", "").lower():
            continue
        if s_query and s_query not in item.get("show", "").lower():
            continue
        if q_query and q_query not in item.get("quote", "").lower():
            continue
        results.append(item)

    return results

def get_quote(
    character: Optional[str] = None,
    show: Optional[str] = None,
    search: Optional[str] = None,
) -> Optional[Dict[str, str]]:
    """Returns a single random anime quote matching the given criteria."""
    matches = filter_quotes(character=character, show=show, search=search)
    return choice(matches) if matches else None

def get_quotes(
    character: Optional[str] = None,
    show: Optional[str] = None,
    search: Optional[str] = None,
    limit: Optional[int] = None,
) -> List[Dict[str, str]]:
    """Returns a list of anime quotes matching the given criteria."""
    matches = filter_quotes(character=character, show=show, search=search)
    if limit is not None and limit > 0:
        return matches[:limit]
    return matches

def get_characters(show: Optional[str] = None) -> List[str]:
    """Returns a sorted list of unique character names."""
    quotes = filter_quotes(show=show)
    return sorted({item["character"] for item in quotes if item.get("character")})

def get_shows() -> List[str]:
    """Returns a sorted list of all unique anime show titles."""
    return sorted({item["show"] for item in QUOTES if item.get("show")})

def get_total_count() -> int:
    """Returns the total number of anime quotes available."""
    return len(QUOTES)