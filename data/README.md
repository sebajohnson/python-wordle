# Word dictionaries

The dictionaries in this directory are generated from the Spanish and English
frequency lists provided by `wordfreq` 3.1.1.

They contain normalized five-letter entries using the language-specific
alphabets defined by the project.

Regenerate them with:

```bash
python -m scripts.build_dictionary --idioma es
python -m scripts.build_dictionary --idioma en