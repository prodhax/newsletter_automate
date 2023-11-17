Automated Newsletter Subscription

This Python script automates the process of subscribing to multiple newsletters using the Selenium web driver. The project starts by reading Gmail account details from an Excel file (seedlist.xlsx). It then opens different newsletter subscription pages, including CNN, The Skimm, ProductHunt, Wired, and Charged, and enters the provided Gmail accounts to subscribe. The chromedriver executable is used to interact with the Chrome browser.

Getting Started:

Before running the script, ensure you have Python installed on your machine. Download the ChromeDriver executable and update its path in the code. Clone the repository, navigate to the project directory, and install the required Python packages using the provided requirements.txt file.

Usage:

Place your Gmail account details in the seedlist.xlsx Excel file, and then execute the script (python automated_subscription.py). The script will sequentially open different newsletter subscription pages and subscribe to them using the specified Gmail accounts.

Configuration:

Customize the chromedriver path in the code to match its location on your machine.

Supported Newsletters:

The script supports subscription to various newsletters, including CNN, The Skimm, ProductHunt, Wired, and Charged.

Contributors:

This project is maintained by [Your Name], and contributions are welcome.

## Getting Started

### Prerequisites

- Make sure you have Python installed.
- Download the [ChromeDriver executable](https://sites.google.com/chromium.org/driver/) and update the path in the code.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/automated-newsletter-subscription.git
    ```

2. Navigate to the project directory:

    ```bash
    cd automated-newsletter-subscription
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Place your Excel file (`seedlist.xlsx`) with Gmail account details in the project directory.

2. Run the script:

    ```bash
    python automated_subscription.py
    ```

3. The script will open different newsletter subscription pages and subscribe using the provided Gmail accounts.

## Configuration

- Update `chromedriver` path in the code to match the location on your machine.

## Supported Newsletters

- CNN Newsletters
- The Skimm Newsletters
- ProductHunt Newsletters
- Wired Newsletters
- Charged Newsletters
