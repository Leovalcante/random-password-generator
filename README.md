# Random Password Generator

[![version](https://img.shields.io/badge/version-1.0.1-brightgreen.svg)](https://github.com/Leovalcante/random-password-generator/releases/tag/v1.0.0)
[![python required](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)

## What is rpg?
**Rpg** stands for **R**andom **P**assword **G**enerator, it's a utility command line tool that allows you to generate random entropic and safe password. 
Rpg check by default every single password that generates into [Have I Been Pwned Passwords](https://haveibeenpwned.com/Passwords) leaks database.


## Installation
`pip3 install random-password-genrator-cli`


## Usage
`rpg [OPTIONS] <pass-length>`

`<pass-length>` it's your desire password length, please note that it MUST BE between 12 and 90 characters
We do this to ensure to provide strong passwords.
In our opinion you should never use a password lower then 16 characters.

`[OPTIONS]` are:

- `-n, --number <pass-number>`: generate `<pass-number>` passwords
- `-o, --output <out-file>`: write generated passwords into `<out-file>`
- `--exclude-charsets [l,u,d,p]`: remove **l**owercase, **u**ppercase, **d**igits or **p**unctuation charsets *
- `--no-safe`:  don't check passwords validity in [Have I Been Pwned Passwords](https://haveibeenpwned.com/Passwords)  *
- `-v, --verbose`: print verbose output
- `-V, --version`: print rpg version
- `-h, --help`: print help text

*: Using this option will print a warning message. The execution will then proceed as defined by the user.


## Examples
Generate a 20 character password:
```
$ rpg 20
Passwords:
y2-1Uf/XAR5K<2[2x~gb

The entropy of generated password is: 131.09177703355275
```

Generate five 20 character passwords
```
$ rpg -n 5 20
Generating passwords  [####################################]  5/5
Passwords:
87VuRR4{O1?5=ngBzm(-
$.G9D-t7~8Y2M0mk>uZw
AL74H2tM-8a|0(D'z{gf
4[+WfS9\6u3FeP"Gzf%6
"Blox37j8`\^T3h2ALH)

The entropy of generated password is: 131.09177703355275
```

Generate a 20 character password without lower-case charsets:
```
$ rpg --exclude-charsets l 20
You are going to generate passwords without one or more of default charsets!
RPG cares a lot for your security, it's recommended to avoid this practice if possible!

Passwords:
>C1#8A`7D7V|]]95RB\7

The entropy of generated password is: 121.7492568250068
```
*You can see here the warning message*

Generate five 20 character passwords and save them into pw-out.txt
```
$ rpg -n 5 -o pw_out.txt 20
Generating passwords  [####################################]  5/5
```
*pw-out.txt*
```
$ cat pw_out.txt 
Passwords:
8YvW(8m5Gy'\i1G_U!2e
l64@%`V27kOE^rCyG2o]
El_0@19$#reG2ncLK^O4
WAAP;7`8=f{3gy4He8x&
4Y<zl2-4Xi*e*X11(VTz

Entropy: 131.09177703355275

Password strength is determined with this chart:
< 28 bits       = Very Weak; might keep out family members
28 - 35 bits    = Weak; should keep out most people, often good for desktop login passwords
36 - 59 bits    = Reasonable; fairly secure passwords for network and company passwords
60 - 127 bits   = Strong; can be good for guarding financial information
128+ bits       = Very Strong; often overkill
```


## Advice
1. Use *rpg* to generate random entropic password
1. Avoid to use a short password, try to use only passwords with 16+ characters.
1. Do not share your passwords with any one.
1. Do not reuse a password.
