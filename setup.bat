@echo off
echo Installing project dependencies...
poetry install

echo Downloading ChromeDriver...
python -c "import os; from downloadChromeDriver import download_chromedriver; download_chromedriver(os.getcwd())"

echo Activating the Poetry environment...
poetry shell

echo Setup complete.
