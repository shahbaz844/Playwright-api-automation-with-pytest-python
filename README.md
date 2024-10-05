# 🌟 API Project Automation🌟

## Overview

Welcome to the **API Automation Project**! This project leverages the power of [Playwright](https://playwright.dev/) and [pytest](https://docs.pytest.org/en/stable/) to automate the testing of MetaBull APIs. 🚀

## ⭐ Features

✨ **Automated API Testing**: Ensure your APIs work flawlessly with automated tests.
<br>
✨ **Automated UI Testing**: Ensure your UI functions flawlessly with automated tests.
<br>
✨ **Scalable & Maintainable**: Easily add new tests and maintain existing ones.
<br>

## 📦 Installation

Get started quickly by cloning the repository and installing the necessary dependencies:

```bash
git clone https://github.com/your-username/git-repository-name.git
```
```bash
cd project-directory
```
```bash
pip install -r requirements.txt
```

## 🏃‍♂️ Running Test

### Run this command to execute all tests

```bash
pytest
```

### Run this command to execute all tests with keyword in name

```bash
pytest -k keyword-in-name
```

### Run this command to execute tests and log in terminals

```bash
pytest -s
```

## 🏃‍♂️ Running Test To Generate HTML Report

### Run this command to generate an HTML report
#### This command will generate report.html file in root after execution of all tests.
#### You can open this report in any browser.

```bash
pytest --html=report.html
```

### Run this command to generate an Allure report
#### This command will generate a directory name report in root after execution of all tests.

```bash
pytest --alluredir=report
```

### Run this command to serve allure report on allure server

```bash
allure serve report
```

### Happy Testing 🚀
