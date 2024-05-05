# Homework 2 Feedback Sheet

### Student

**ODIN: nassar**

## Grade (98.4/100)

- [x] Downloaded Linux textbooks
- [x] Completed THM Linux Funadmentals Room Part 1
- [x] Completed THM Linux Modules Room 
##### grep tasks
- [x] All lines that contain the word “password” (case-sensitive)
- [x] All lines that contain “password” (case-insensitive)
- [x] All lines that end with exactly 3 numerical digits - WITH an anchor
- [] All lines that end with exactly 3 numerical digits - WITHOUT an anchor
- [x] All lines that contain exactly 3 numerical digits, in any position (do not have to be adjacent, just 3 total)
##### sed tasks
- [x] Task 5.1
- [x] Task 5.2
- [x] Task 5.3
##### objdump, nm, readelf on /bin/ls
- [x] Task 6, question 1 for all three tools
- [x] Task 6, question 2 for all three tools
- [x] Task 6, question 3 for all three tools
##### virtual environment
- [x] Virtual Environment shell function
##### awk, cut, grep
- [x] Task 8, question 1
- [x] Task 8, question 2 
- [x] Task 8, question 3 
- [x] Task 8, question 4


## Comments
Good work!

-.3 x 2 = -.6 OdinID missing from two screenshots. Screenshots must include OdinID. This can be done with a sticky note app, typing it into the search bar, editing it into your screenshots, etc.

-1 No wihtout-an-anchor regular expression.
The with vs without anchor commands can be done like this:
with an anchor `grep -P '(?<!\d)\d{3}(?!\d)$'`
without an anchor `grep -P '(?<!\d)\d{3}(?!\d)\Z`
They should return the same wc since they perform the same task
All lines that contain exactly 3 numerical digits, in any position (do not have to be adjacent, just 3 total) `grep -P '^(.*\d.*){3}$'`


