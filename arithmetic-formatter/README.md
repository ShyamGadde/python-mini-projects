# Arithmetic Formatter

Arithmetic Formatter is a command-line tool that formats arithmetic problems for better readability. It takes a list of arithmetic problems and optionally displays their answers. This tool is perfect for teachers, students, and anyone who needs to format multiple arithmetic problems quickly and efficiently.

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/ShyamGadde/python-mini-projects.git
```

Navigate to the project directory:

```bash
cd python-mini-projects/arithmetic-formatter
```

## Usage

You can use the Arithmetic Formatter tool from the command line as follows:

```bash
python arithmetic_formatter.py '32 + 698' '3801 - 2' '45 + 43' '123 + 49' --display_answer
```

This command will output:

```bash
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
  730      3799      88      172
```

For more information on the available options, use the `-h` or `--help` option:

```bash
$ python arithmetic_formatter.py -h
usage: arithmetic_formatter.py [-h] [-d] problems [problems ...]

This tool formats arithmetic problems for better readability. It takes a list of arithmetic problems and optionally displays their answers.

positional arguments:
  problems              Arithmetic problems to be formatted.

options:
  -h, --help            show this help message and exit
  -d, --display_answer  Display the answers of the problems.
```
