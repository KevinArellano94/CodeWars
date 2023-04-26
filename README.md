# Detect Pangram
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once. - CodeWars

## Initial folder structure
1. 
```bash
$assessment_name = "string_to_camelcase"
$function_name = "to_camel_case"

mkdir $assessment_name
cd $assessment_name

mkdir tests
mkdir $function_name
New-Item README.md

New-Item app.py
New-Item ./$function_name/__init__.py
New-Item ./$function_name/solution.py

New-Item ./tests/__init__.py
New-Item ./tests/test_$function_name.py
```

## Installation
1. Clone
```bash
git clone git@github.com:KevinArellano94/CodeWars.git
```

2. CD into project file
```bash
cd detect_pangram
```

## Usage

1. To run
```bash
py .\app.py
```

2. To test
To test run all:
```bash
py -m unittest tests
```

3. To test run specific modules:
```bash
clear; py -m unittest tests.test_is_pangram
```

## Contributing

{ Available }

## Credits
CodeWars and the top 2 solutions.

## License
MIT License