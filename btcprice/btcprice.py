import argparse
import json
import sys
import urllib
from urllib.request import urlopen


def main():
    parser = argparse.ArgumentParser(
        description="Get the current price of bitcoin in a given currency (default: USD)"
    )
    parser.add_argument(
        "amount",
        type=float,
        nargs="?",
        default=1,
        help="the amount of bitcoin to convert to the target currency (default: 1)",
    )
    parser.add_argument(
        "--currency",
        type=str,
        default="USD",
        help="the target currency to convert to (default: USD)",
    )
    args = parser.parse_args()

    # Check if the target currency is supported by the API
    if args.currency not in ["USD", "GBP", "EUR"]:
        print(f"Error: {args.currency} is not supported by the API")
        sys.exit(1)

    try:
        with urlopen("https://api.coindesk.com/v1/bpi/currentprice.json") as response:
            data = json.loads(response.read().decode())
            print(f'${data["bpi"]["USD"]["rate_float"] * args.amount:,.4f}\n')
    except urllib.error.HTTPError as e:
        print(f"Error: Could not connect to the API ({e.code} {e.reason})")
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Error: Could not connect to the API ({e.reason})")
        sys.exit(1)
    except KeyError:
        print(f"Error: {args.currency} is not supported by the API")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
