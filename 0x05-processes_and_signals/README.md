# Processes and signals
# Bash scripts

- ##### 0-what-is-my-pid
A Bash script that displays its own PID.

- ##### 1-list_your_processes
A Bash script that displays a list of currently running processes.

- ##### 2-show_your_bash_pid
A Bash script that displays lines containing the bash word, thus allowing you to
 easily get the PID of your Bash process.

- ##### 3-show_your_bash_pid_made_easy
A Bash script that displays the PID, along with the process name, of processes
 whose name contain the word bash.

- ##### 4-to_infinity_and_beyond
A Bash script that displays To infinity and beyond indefinitely.

- ##### 5-dont_stop_me_now
A Bash script that stops 4-to_infinity_and_beyond process.

- ##### 6-stop_me_if_you_can
A Bash script that stops 4-to_infinity_and_beyond process.

- ##### 7-highlander
A Bash script that displays:
  - `To infinity and beyond` indefinitely
  - With a `sleep 2` in between each iteration
  - `I am invincible!!!` when receiving a SIGTERM signal
A copy of `6-stop_me_if_you_can` script named `67-stop_me_if_you_can`, kills the
`7-highlander` process instead of the `4-to_infinity_and_beyond` one.

- ##### 8-beheaded_process
A Bash script that kills the process 7-highlander.
