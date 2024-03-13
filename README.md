<p align="center">
  <img src="images/logo" alt="Qiymeti, zmmmdf, azerbaijan cheap price, qiymeti-az's mascot">
</p>

<p align="center">
  <a href="https://github.com/zmmmdf/qiymeti-az/releases"><img src="https://img.shields.io/github/release/zmmmdf/qiymeti-az" alt="GitHub release"></a>
  <a href="https://discord.gg/ZEfWKK8qhv"><img src="https://img.shields.io/discord/1217399848194674778?color=blue" alt="Discord chat"></a>
</p>

<!-- A spacer -->
<div>&nbsp;</div>

Qiymeti_AZ is a Python package that provides a convenient way to scrape product prices from various Azerbaijani websites. It includes default instances for popular Azerbaijani electronic stores and allows users to easily search for product prices from these stores using a simple interface. For more information see [the website](https://zmmmdf.github.io/qiymeti-az).


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
