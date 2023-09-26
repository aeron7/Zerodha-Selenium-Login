# Zerodha Selenium Login

![GitHub repo size](https://img.shields.io/github/repo-size/aeron7/Zerodha-Selenium-Login)
![GitHub watchers](https://img.shields.io/github/watchers/aeron7/Zerodha-Selenium-Login)
![GitHub](https://img.shields.io/github/repo-size/aeron7/Zerodha-Selenium-Login)
![GitHub last commit](https://img.shields.io/github/last-commit/aeron7/Zerodha-Selenium-Login)
![GitHub stars](https://img.shields.io/github/stars/aeron7/Zerodha-Selenium-Login)
![GitHub forks](https://img.shields.io/github/forks/aeron7/Zerodha-Selenium-Login)
![GitHub watchers](https://img.shields.io/github/watchers/aeron7/Zerodha-Selenium-Login)

Automate the Zerodha login process using Selenium and ChromeDriver.

## About Unofficed Community

This tool has been developed to cater to the needs of the [Unofficed](https://www.unofficed.com/)  community. Unofficed is a vibrant community of traders, developers, and enthusiasts passionate about financial markets and trading strategies.

Visit the [Unofficed Community Chat](https://www.unofficed.com/chat/) to engage in discussions, share insights, and collaborate with fellow members. Join the community to explore a wealth of knowledge and resources related to trading and financial markets.

## Prerequisites

Before running the script, ensure you have the following:

- Python installed on your system.
- ChromeDriver installed and located in the same folder as the script. You can download ChromeDriver from [here](https://chromedriver.chromium.org/downloads).

## Installation

Clone the repository to your local machine:

   ```shell
   git clone https://github.com/yourusername/Zerodha-Selenium-Login.git
   ```

## Zerodha Screenshot Generator 

Update the zerodha_screenshot.py file with your Zerodha credentials:


```python
zerodha_username = "your_username"
zerodha_password = "your_password"
zerodha_totp = "your_totp"
```
###Usage
Run the script to automate the Zerodha login process. The script will perform the following steps:

- Open a headless Chrome browser.
- Navigate to the Zerodha login page.
- Fill in your username and password.
- Enter your TOTP (Time-Based One-Time Password) generated from your authenticator app.
- Capture a screenshot of the Zerodha dashboard and save it as a timestamped PNG file.
  
```shell
python zerodha_screenshot.py
```

## Automating Zerodha Login with Python and Selenium

Automating the login process for your Zerodha account can be efficiently accomplished using Python and Selenium. Below is a step-by-step guide to automate your Zerodha login:

1. **Download Required Files:** Begin by downloading the the `zer_login_exe.zip` file and unzip it.

2. **Update Credentials:** Open the JSON file within the downloaded files and update your Zerodha account credentials, which should include your username and password.

3. **Run the Executable:** Execute the downloaded .exe file. This action will automatically open the Zerodha website and log you into your account.

4. **Optional: Decompilation (for Educational Purposes):** If you're interested in gaining insights into the automation code, you can decompile the .exe file. It's intentionally unprotected to facilitate educational use. Verify if the code within the .exe matches the zer_login.py file.

By following these steps, you can seamlessly automate the login process for your Zerodha account using Python and Selenium. Always remember to use automation responsibly and in accordance with the platform's terms of service.

License
This project is licensed under the MIT License - see the LICENSE file for details.
