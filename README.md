# Goprox

Goprox is a magical Python module that performs Google searches with superpowers like automatic proxy handling, so you don't have to worry about a thing!

## Installation

1. Download or clone this repository.
2. Copy the `goprox` directory to your project's directory.
3. Install dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Quick Start

```python
from goprox import GoogleSearch

# Let Goprox do its magic!
search = GoogleSearch("your query", num=5, region="us", language="en", proxy=False)

# Perform search with automatic proxy handling
results = search.search()

# Print the magic search results
for result in results:
    print(result)
```

## Features

- Perform Google searches effortlessly with custom parameters.
- Automatic handling of proxies for each search.
- Goprox selects a random user-agent for each request.
- It's super easy to use and makes searching Google a breeze.

## Credits

This project uses the amazing [free-proxy](https://github.com/jundymek/free-proxy) module to fetch and validate proxies.

## License

Goprox is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
