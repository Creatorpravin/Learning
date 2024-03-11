a, b, c, d, e, f, g, h, i, j = (82.26,82.17,82.27,82.10,82.26,82.42,82.17,82.14,82.10,82.52)
k = (a + b + c + d + e + f + g + h + i + j) / 10
print("1: {:.5f}".format(k))
l = (b + c + d + e + f + g + h + i + j + k) / 10
print("2:", l)
m = (c + d + e + f + g + h + i + j + k + l) / 10
print("3:", m)
n = (d + e + f + g + h + i + j + k + l + m) / 10
print("4:", n)
o = (e + f + g + h + i + j + k + l + m + n) / 10
print("5:", o)
p = (f + g + h + i + j + k + l + m + n + o) / 10
print("6:", p)
q = (g + h + i + j + k + l + m + n + o + p) / 10
print("7:", q)
r = (h + i + j + k + l + m + n + o + p + q) / 10
print("8:", r)
s = (i + j + k + l + m + n + o + p + q + r) / 10
print("9:", s)
t = (j + k + l + m + n + o + p + q + r + s) / 10
print("10:",t)
def find_max_min(numbers):
    if len(numbers) == 0:
        return None, None  # Return None for both max and min if the list is empty
    else:
        max_value = numbers[0]  # Assume the first element is the maximum
        min_value = numbers[0]  # Assume the first element is the minimum

        for num in numbers:
            if num > max_value:
                max_value = num
            elif num < min_value:
                min_value = num

        return max_value, min_value

# Example usage:
numbers = [k,l,m,n,o,p,q,r,s,t]
max_val, min_val = find_max_min(numbers)
print("Maximum value:{:.5f}".format(max_val))
print("Minimum value:{:.5f}".format(min_val))
def calculate_RSI(closing_prices, num_periods, rsi_period):
    avg_gain = 0
    avg_loss = 0

    for i in range(1, num_periods):
        if closing_prices[i] > closing_prices[i - 1]:
            gain = closing_prices[i] - closing_prices[i - 1]
            avg_gain += gain
        else:
            loss = closing_prices[i - 1] - closing_prices[i]
            avg_loss += loss

    avg_gain /= (num_periods - 1)
    avg_loss /= (num_periods - 1)

    # Calculate Relative Strength (RS)
    rs = avg_gain / avg_loss

    # Calculate RSI
    rsi = 100 - (100 / (1 + rs))

    return rsi


def main():
    closing_prices = [a,b,c,d,e,f,g,h,i,j]  # Predefined closing prices
    num_periods = len(closing_prices)
    rsi_period = 10  # Predefined RSI period

    # Calculate RSI
    rsi = calculate_RSI(closing_prices, num_periods, rsi_period)

    # Indication to buy or sell based on RSI value
    if rsi >= 70:
        print(f"RSI is {rsi:.2f}. Overbought - Suggests selling.")
    elif rsi <= 30:
        print(f"RSI is {rsi:.2f}. Oversold - Suggests buying.")
    else:
        print(f"RSI is {rsi:.2f}. No clear indication.")


if __name__ == "_main_":
    main()

import numpy as np

def calculate_bollinger_bands(prices, window):
    """Calculate Bollinger Bands with factors of 2 and 10"""
    sma = np.mean(prices[-window:])
    std_dev = np.std(prices[-window:])
    
    upper_band_factor_2 = sma + (2 * std_dev)
    lower_band_factor_2 = sma - (2 * std_dev)
    return upper_band_factor_2, lower_band_factor_2

# Example prices data
prices = [a,b,c,d,e,f,g,h,i,j]
window = 10

# Calculate Bollinger Bands
upper_band_factor_2, lower_band_factor_2 = calculate_bollinger_bands(prices, window)

# Print results
print(f"Bollinger Bands (Factor of 2): Upper = {upper_band_factor_2:.5f}, Lower = {lower_band_factor_2:.5f}")



def stochastic_oscillator(closes):
    highest_high = closes[0]
    lowest_low = closes[0]

    # Find highest high and lowest low within the period
    for close in closes[1:]:
        if close > highest_high:
            highest_high = close
        if close < lowest_low:
            lowest_low = close

    # Calculate %K
    stochastic_k = ((closes[-1] - lowest_low) / (highest_high - lowest_low)) * 100
    return stochastic_k

def main():
    # Example closing prices
    closes = [a,b,c,d,e,f,g,h,i,j]

    # Calculate stochastic oscillator
    stochastic_k = stochastic_oscillator(closes)

    # Print result
    print(f"Stochastic Oscillator ({PERIOD}-period): {stochastic_k:.2f}")

    # Check for overbought or oversold condition
    if stochastic_k >= OVERBOUGHT:
        print("Overbought condition detected!: sell")
    elif stochastic_k <= OVERSOLD:
        print("Oversold condition detected!: buy")
    else:
        print("No overbought or oversold condition detected.")

if __name__ == "_main_":
    PERIOD = 10
    OVERBOUGHT = 70
    OVERSOLD = 30
    main()