Here's a concise and cleaned-up version of the README file that you can directly upload to GitHub:

```markdown
# Instagram-Unlike-Bot

A Python bot that unlikes Instagram posts one by one, respecting Instagram's algorithm.

## Overview

This bot automates the process of unliking posts on Instagram using **Selenium WebDriver**. It logs into your account, navigates to the "Your Activity > Interactions > Likes" page, and unlikes posts in batches while mimicking human behavior.

## Features

- Logs into Instagram automatically.
- Selects and unlikes posts in small batches.
- Simulates human-like interaction with delays between actions.
- Prompts for manual OTP input during login for added security.

## Requirements

- **Python 3.x**
- **Selenium**: Install via:
  ```bash
  pip install selenium
  ```
- **ChromeDriver**: Download the correct version for your Chrome browser from [here](https://sites.google.com/a/chromium.org/chromedriver/) and update its path in the script.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Instagram-Unlike-Bot.git
   ```
2. Navigate to the project folder:
   ```bash
   cd Instagram-Unlike-Bot
   ```
3. Install dependencies:
   ```bash
   pip install selenium
   ```
4. Download ChromeDriver and place it in a known directory. Update the path in the script as needed.

## Usage

1. Replace your Instagram credentials (`username` and `password`) in the script.
2. Run the bot:
   ```bash
   python unlike_bot.py
   ```
3. Manually input the OTP in the browser when prompted and press Enter to continue.
4. The bot will begin unliking posts in batches of 15, scrolling down to load more posts as needed.

## Limitations

- Manual OTP entry is required during login.
- Updates may be needed if Instagram changes its web structure or algorithms.
- Excessive use may trigger rate limits or account restrictions.

## Disclaimer

This bot is not affiliated with Instagram. Use responsibly and ensure compliance with Instagram's terms of service.
```

