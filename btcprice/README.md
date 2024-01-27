# BTCPrice

BTCPrice is a Python command-line tool that fetches the current price of Bitcoin in a specified currency. It's a handy tool for cryptocurrency enthusiasts, traders, and financial analysts.

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/ShyamGadde/python-mini-projects.git
```

Navigate to the project directory:

```bash
cd python-mini-projects/btcprice
```

## Usage

You can use the BTCPrice tool from the command line as follows:

```bash
python btcprice.py --currency EUR 0.5
```

This command will output the current price of 0.5 Bitcoin in Euros.

For more information on the available options, use the -h or --help option:

```bash
$ python btcprice.py -h
usage: btcprice.py [-h] [--currency CURRENCY] [amount]

Get the current price of bitcoin in a given currency (default: USD)

positional arguments:
  amount               the amount of bitcoin to convert to the target currency (default: 1)

options:
  -h, --help           show this help message and exit
  --currency CURRENCY  the target currency to convert to (default: USD)
```
