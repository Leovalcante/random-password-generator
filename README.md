# Random Password Generator
#### *rpg v1.0.0*

## What is rpg?
**Rpg** stands for **R**andom **P**assword **G**enerator, it's a utility command line tool that allows you to generate random entropic password.

## Requirements
- Python 3+

## Installation
1. `git clone https://github.com/Leovalcante/random-password-generator`
2. `cd random-password-generator`
3. `./run_install.sh`


## Usage
`rpg [OPTIONS] <pass-length>`

`<pass-length>` it's your desire password length, please note that it MUST BE at lease 12
We do this to ensure to provide a strong password.
In our opinion you should never use a password lower then 16 characters.

`[OPTIONS]` are:

- `--help`: to print help text
- `--version`: to print out rpg version
- `-n <int>`: with this option you can generate *n* password

## Examples
Generate a 16 character password:
```
$ rpg 16

5;K6]V%h]ewW8N5i
```

Generate a 20 character password
```
$ rpg 20

:6#T^ioVY9"RaQ7x3i7{
```

Generate five 20 character passwords
```
$ rpg -n 5 20

xb|b8$_03`yZ69T"wRHS
^~|78IRyH]L3jq3fR'h0
w9V>2vd2!%O53|sCy?GM
>01^7%zZx8X*lHb+sEV3
74"2Vd17Z@hNUy__Pt/u
```


## Advice
1. Do not reuse a password.
2. Avoid use of short password, try to use only 16+ character passwords.
3. Do not share your passwords with any one.
4. Check if your password has already been leaked here: [haveibeenpwned](https://haveibeenpwned.com/Passwords)
5. Use rpg to generate random entropic password
