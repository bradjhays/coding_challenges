# Stock Ticker

## Task
1. This following URL provides stock price forecasts for a given [stock ticker](https://stockanalysis.com/stocks/):
`https://money.cnn.com/quote/forecast/forecast.html?symb=<ticker symbol>`
2. Using the above url, make the https call to retrieve the forecast page.
3. Write a method that uses regular expression to extract the current price as well as the 3 estimated prices (high, medium, low) from the page, and return them as 4 numbers.
4.  Write a unittest for the method.