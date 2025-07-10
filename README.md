 🤖 Amizone Feedback Bot

  This project is an automation bot built using Python and Selenium that fills out the Amizone Feedback Portal automatically. It simulates user behavior by randomly selecting ratings using Python’s `randint`        function.

---

  📌 Features

  ✅ Automates checkbox selection in the Amizone Feedback Portal  
  🔢 Uses `random.randint(0, 3)` to assign ratings dynamically  
  🧪 Built using **Selenium WebDriver** to interact with web elements  
  💡 Lightweight, simple, and easy to configure

---

   🛠️ Requirements

  - Python 3.7+
  - Google Chrome (or any supported browser)
  - ChromeDriver compatible with your Chrome version

 Python Libraries

Install dependencies:

```bash
pip install selenium

    Clone The Repository

      git clone https://github.com/yourusername/amizone-feedback-bot.git
      cd amizone-feedback-bot

    Update Credentials Setup

    USERNAME = "your_amizone_username"
    PASSWORD = "your_amizone_password"

This suppose to bet get saved on "pass __init__" the linux command :: OR we suppose to save it into using python function config... :: For most it gets saved as non persistent and hashed  

Run The Bot

python amizone_bot.py

The bot will:

Log into Amizone

Navigate to the feedback section

Randomly select ratings (from 0 to 3) for each question using:

python
Copy
Edit
random.randint(0, 3)

🙋‍♂️ Contributions
Feel free to submit pull requests for enhancements like:

⚠️ Disclaimer
This tool is for educational purposes only.
Use it responsibly and ensure it doesn't violate your institution's terms of service or academic integrity policies.

CAPTCHA handling

GUI interface

Better randomness or selection logic
