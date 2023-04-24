# Detect Pangram
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once. - CodeWars

## Initial folder structure
1. 
```bash
mkdir Exes_and_Ohs
cd Exes_and_Ohs

mkdir tests
mkdir xo

New-Item app.py
New-Item ./xo/__init__.py
New-Item ./xo/solution.py

New-Item ./tests/__init__.py
New-Item ./tests/test_xo.py
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