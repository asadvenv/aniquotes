# aniquotes

A lightweight, zero dependency Python package to generate, search, and filter **13,000+** anime quotes from **3,500+** characters across **1,500+** anime shows.

## Installation

```bash
pip install aniquotes
```

---

## Quickstart

```python
from aniquotes import get_quote

# Get a random anime quote
print(get_quote())
# {
#   'character': 'Bear',
#   'show': '.hack//SIGN',
#   'quote': 'If you want to know the truth, you must have the courage to accept it.'
# }
```

---

## Usage Guide

### 1. Get a Random Quote `get_quote`

```python
from aniquotes import get_quote

# Random quote from the entire database
quote = get_quote()

# Filter by character name
quote = get_quote(character="Luffy")

# Filter by anime show
quote = get_quote(show="Naruto")

# Filter by text within quotes
quote = get_quote(search="courage")

# Combine multiple filters
quote = get_quote(character="Luffy", show="One Piece", search="king")
```

### 2. Retrieve Multiple Quotes `get_quotes`

```python
from aniquotes import get_quotes

# Filter by anime show
death_note_quotes = get_quotes(show="Death Note")

# Filter by character name
luffy_quotes = get_quotes(character="Luffy")

# Filter by text within quotes
dream_quotes = get_quotes(search="dream")

# Limit the number of returned results
first_10_quotes = get_quotes(limit=10)

# Combine multiple filters with a limit
results = get_quotes(character="Goku", show="Dragon Ball", search="power", limit=5)
```

### 3. List Characters & Shows

```python
from aniquotes import get_characters, get_shows, get_total_count

# Total count of quotes in database
print(get_total_count())

# List all unique anime shows
shows = get_shows()

# List all unique characters
all_characters = get_characters()

# List characters from a specific show
naruto_chars = get_characters(show="Naruto")
```

---

## License

This project is licensed under [The Unlicense](LICENSE).