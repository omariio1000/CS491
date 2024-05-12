# Homework 3 Feedback Sheet

### Student

**ODIN: nassar**

## Grade (100/100)

#### TryHackMe Crack the Hash Room Using HashCat
##### Level 1
- [x] Cracked Password 1
- [x] Cracked Password 2
- [x] Cracked Password 3
- [x] Cracked Password 4
- [x] Cracked Password 5

##### Level 2
- [x] Cracked Password 1
- [x] Cracked Password 2
- [x] Cracked Password 3
- [x] Cracked Password 4

#### TryHackMe Crack the Hash Room Using John
##### Level 1
- [x] Cracked Password 1
- [x] Cracked Password 2
- [x] Cracked Password 3
- [x] Cracked Password 4
- [x] Cracked Password 5

##### Level 2
- [x] Cracked Password 1
- [x] Cracked Password 2
- [x] Cracked Password 3
- [x] Cracked Password 4 OR Documented that it wasn't possible with all attempted cracking

#### Task 3
- [x] Generate list of 20 random passwords
- [x] Generate list of every 3-word combination of those 20 random passwords
- [x] Generate ssh key passphrase with random 3 password combo - with spaces
- [x] convert hash to be understandable to john
- [x] crack passphrase with list of 3-word combinations


## Comments
Thank you for your thorough documentation and OdinID/name in your screenshots. Great work!

The last one of level two can be cracked with john in this format:
`PASS:$dynamic_24$5d0374a36358da86f4932a598485b546de204908$tryhackme`
dynamic_24 being this john format:
`dynamic_24 [sha1($p.$s) 256/256 AVX2 8x1]`
