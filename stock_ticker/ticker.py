"""Get stock ticker info."""
import re
import requests
import vcr  # testing

TICKER_SYMBOL = "NFLX"
FORECASTS_URL = (
    f"https://money.cnn.com/quote/forecast/forecast.html?symb={TICKER_SYMBOL}"
)

REGEX = r"([a-z]+) [a-z]+ of ([0-9]+.[0-9]{2})"


def forcast():
    """Use regular expression to extract the current price as well as the 3 estimated prices (high, medium, low)."""
    ret = {}
    res = requests.get(FORECASTS_URL)
    for match in re.findall(REGEX, res.text):
        ret[match[0]] = match[1]

    return ret


if __name__ == "__main__":
    print(forcast())


# Test


@vcr.use_cassette()
def test_forcast():
    """."""
    calc = forcast()
    print(calc)
    assert {
        "last": "359.73",
        "median": "384.00",
        "high": "440.00",
        "low": "215.00",
    } == calc
