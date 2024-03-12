
# Qiymeti_AZ

Qiymeti_AZ is a Python package that provides a convenient way to scrape product prices from various Azerbaijani websites. It includes default instances for popular Azerbaijani electronic stores and allows users to easily search for product prices from these stores using a simple interface.

## Installation

You can install Qiymeti_AZ via pip:

```bash
pip install qiymeti-az
```

## Usage

```python
import qiymeti_az

# Search for a product in a specific store
result = qiymeti_az.search(query="iphone 15", target="bytelecom")
print(result)
```

## Supported Stores

Qiymeti_AZ currently supports the following Azerbaijani electronic stores:

- Kontakt Home
- Baku Electronics
- World Telecom
- Irshad
- MG Store
- ByTelecom

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
