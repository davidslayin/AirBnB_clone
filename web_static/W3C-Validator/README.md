W3C validator for Holberton School
For HTML, CSS and SVG files

Based on 1 API:

Markup Validator Web Service API
Requirements
Python 3
Requests: HTTP for Humans™
Quickstart
Clone this repo
git clone https://github.com/holbertonschool/W3C-Validator.git
Run the validator command from within
Single file:

./w3c_validator.py index.html
./w3c_validator.py css/styles.css
Multiple files:

./w3c_validator.py index.html article.html css/styles.css
All errors are printed in STDERR; Exit status = # of errors (0 on success)

Troubleshooting
Error: bad interpreter: No such file or directory If you get this error you might not have Python installed correctly; or the system PATH might not be updated to reflect the installed Python version.
Assuming that Python 3 is indeed installed, you can try to run it like so:

python3 w3c_validator.py index.html
