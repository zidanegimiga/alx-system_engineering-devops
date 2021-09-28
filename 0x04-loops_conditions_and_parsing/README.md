## Loops, conditions and parsing

During this project, i learnt:

How to create SSH keys
What is the advantage of using #!/usr/bin/env bash over #!/bin/bash
How to use while, until and for loops
How to use if, else, elif and case condition statements
How to use the cut command
What are files and other comparison operators, and how to use them

I also learnt how to get my scripts pass the shellcheck


# Shell

- ##### 0-RSA_public_key.pub
Contains my public key

- ##### 1-for_holberton_school
A Bash script that displays Holberton School 10 times using the for loop.

- ##### 2-while_holberton_school
A Bash script that displays Holberton School 10 times using the while loop.

- ##### 3-until_holberton_school
A Bash script that displays Holberton School 10 times using the until loop.

- ##### 4-if_9_say_hi
A  Bash script that displays Holberton School 10 times, but for the 9th
 iteration, displays Holberton School and then Hi on a new line.

- ##### 5-4_bad_luck_8_is_your_chance
A  Bash script that loops from 1 to 10 and:
   - displays bad luck for the 4th loop iteration
   - displays good luck for the 8th loop iteration
   - displays Holberton School for the other iterations
Using while loop, if,elif,else

- ##### 6-superstitious_numbers
A Bash script that displays numbers from 1 to 20 and:
  - displays 4 and then bad luck from China for the 4th loop iteration
  - displays 9 and then bad luck from Japan for the 9th loop iteration
  - displays 17 and then bad luck from Italy for the 17th loop iteration
Using the while loop and case statement

- ##### 7-clock
A Bash script that displays the time for 12 hours and 59 minutes:
  - display hours from 0 to 12
  - display minutes from 1 to 59
Using the while loop.

- ##### 8-for_ls
A Bash script that displays:
  - The content of the current directory
  - In a list format
  - Where only the part of the name after the first dash is displayed
   (refer to the example)
Using the for loop
Not displaying hidden files

- ##### 9-to_file_or_not_to_file
A Bash script that gives you information about the holbertonschool file.
  - checks if the file exists and prints:
    - if the file exists: holbertonschool file exists
    - if the file does not exist: holbertonschool file does not exist
  - if the file exists, print:
    - if the file is empty: holbertonschool file is empty
    - if the file is not empty: holbertonschool file is not empty
    - if the file is a regular file: holbertonschool is a regular file
    - if the file is not a regular file: (nothing)

- ##### 10-fizzbuzz
A Bash script that displays numbers from 1 to 100.
- Requirements:<br>
	- Displays `FizzBuzz` when the number is a multiple of 3 and 5<br>
	- Displays `Fizz` when the number is multiple of 3<br>
	- Displays `Buzz` when the number is a multiple of 5<br>
	- Otherwise, displays the number<br>
	- In a list format
