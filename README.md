# Random Password Generator
#### *rpg v0.0.1*

## What is rpg?
**Rpg** stands for **R**andom **P**assword **G**enerator, it's a utility command line tool that allows you to generate random entropic password.


## Installation
1. `pip install random-password-genrator-cli`


## Advice
1. Use rpg to generate random entropic password
2. Check if your password has already been leaked here: [haveibeenpwned](https://haveibeenpwned.com/Passwords)
3. Avoid to use a short password, try to use only passwords with 16+ characters.
4. Do not share your passwords with any one.
5. Do not reuse a password.


## Usage
`rpg [OPTIONS] <pass-length>`

`<pass-length>` it's your desire password length, please note that it MUST BE at lease 12
We do this to ensure to provide a strong password.
In our opinion you should never use a password lower then 16 characters.

`[OPTIONS]` are:

- `-n, --number <pass-number>`: generate `<pass-number>` passwords
- `-o, --output <out-file>`: write generated passwords into `<out-file>`
- `-nL, --no-lower`: remove lower-case charsets 
- `-nU, --no-upper`: remove upper-case charsets
- `-nD, --no-digits`: remove digits charsets
- `-nP, --no-punctuation`: remove punctuation charsets
- `-v, --verbose`: print verbose output
- `-V, --version`: print rpg version
- `-h, --help`: print help text

## Examples
Generate a 16 character password:
```
$ rpg 16
Passwords:
6=L!Sda7~7xU5V@m

The entropy of generated password is: 104.8734216268422
```

Generate a 20 character password without lower-case charsets
```
$ rpg 20

Passwords:
.T(89$!OPT4C{1088LS=

The entropy of generated password is: 121.7492568250068

```

Generate five 20 character passwords without punctuation charsets
```
$ rpg -n 5 20

Passwords:
zW9z4974ciLgkP9hT3CC
grX01Bd6MkQj01Y72dOa
XtPmY88o2X87QaaA54bL
dxhk9EYu7IJ4uS2d6Q66
3Wr04RnOlV4h4c5Fvo6D

The entropy of generated password is: 119.08392620773752
```

Generate five 12 character passwords and save them into pw-out.txt
```
$ rpg -n 5 -o pw-out.txt 12
Passwords:
.HHc'd2sK2\7
Y5=3"da`W9aB
60U">By<Z7db
j9N4W5Tvu;'@
8F,l<Oej6$M6

The entropy of generated password is: 78.65506622013166

```
*pw-out.txt*
```
$ cat pw-out.txt 
Passwords:
.HHc'd2sK2\7
Y5=3"da`W9aB
60U">By<Z7db
j9N4W5Tvu;'@
8F,l<Oej6$M6
Entropy: 78.65506622013166
```
