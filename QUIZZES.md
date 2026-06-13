# Phase 0 — Self-test Question Banks

100 questions per foundation lesson. Click a question to reveal its answer. These also appear inside each lesson in the [tracker app](https://sergeiosipov.github.io/data-architect-roadmap/).


## Phase 0 · 0.1 Linux, the command line & shell — 100 self-test questions

<details><summary><b>1.</b> What is WSL2 and why would a Windows-based data engineer use it?</summary>

WSL2 (Windows Subsystem for Linux 2) runs a real Linux kernel in a lightweight VM on Windows, letting you run Ubuntu and Linux tooling natively; it lets you develop in the same Linux environment your production fund-data pipelines will run on.

</details>

<details><summary><b>2.</b> What command installs Ubuntu under WSL2 from a fresh Windows machine?</summary>

`wsl --install` (optionally `wsl --install -d Ubuntu`) installs WSL2 with Ubuntu as the default distribution.

</details>

<details><summary><b>3.</b> How do you check which WSL version a distribution is using?</summary>

Run `wsl -l -v` (list verbose) in PowerShell; the `VERSION` column shows `1` or `2` for each installed distribution.

</details>

<details><summary><b>4.</b> Inside WSL2, where do you find your Windows `C:` drive?</summary>

It is mounted under `/mnt/c`, so `C:\Users\senio` is `/mnt/c/Users/senio` from the Linux side.

</details>

<details><summary><b>5.</b> Why is it faster to keep project files in the Linux filesystem (`/home`) rather than `/mnt/c` under WSL2?</summary>

Cross-filesystem access between the Linux VM and Windows (`/mnt/c`) has high I/O overhead, so reading/writing many files (e.g. a folder of EMT files) is much slower than working under the native Linux ext4 filesystem.

</details>

<details><summary><b>6.</b> What does the Linux filesystem hierarchy directory `/etc` hold?</summary>

System-wide configuration files (e.g. `/etc/passwd`, `/etc/crontab`, `/etc/hosts`); it is for config, not user data or binaries.

</details>

<details><summary><b>7.</b> What is stored under `/home`?</summary>

Per-user home directories, e.g. `/home/senio`, holding that user's personal files and dotfile configuration; `~` is shorthand for the current user's home.

</details>

<details><summary><b>8.</b> What kind of data lives under `/var`?</summary>

Variable data that changes at runtime — logs (`/var/log`), spool/queue files, caches, and mail; you would check `/var/log` to troubleshoot a failed nightly NAV job.

</details>

<details><summary><b>9.</b> What is `/tmp` used for and what is its key caveat?</summary>

`/tmp` is for temporary files; it is world-writable and is typically cleared on reboot, so never store anything you need to keep there.

</details>

<details><summary><b>10.</b> In `ls -l` output, what do the three triplets of `rwx` represent?</summary>

The permission bits for owner, group, and others respectively, each showing read (`r`), write (`w`), and execute (`x`) permissions.

</details>

<details><summary><b>11.</b> In `-rw-r--r--`, what is the leading `-` and what are the permissions?</summary>

The leading `-` means it is a regular file (a `d` would mean directory); owner has read+write, group has read, others have read.

</details>

<details><summary><b>12.</b> What does the execute (`x`) bit mean on a directory versus a file?</summary>

On a file `x` means it can be run as a program; on a directory `x` means you can enter it (`cd` into it) and access files within by name.

</details>

<details><summary><b>13.</b> What is the numeric (octal) value of permissions `rwxr-xr--`?</summary>

`754` — owner `rwx`=7, group `r-x`=5, others `r--`=4.

</details>

<details><summary><b>14.</b> How would you make a script `load_nav.sh` executable for everyone?</summary>

`chmod +x load_nav.sh`, or explicitly `chmod 755 load_nav.sh`.

</details>

<details><summary><b>15.</b> What does `chmod 600 id_rsa` accomplish and why does it matter for SSH?</summary>

It gives the owner read+write and no one else any access; SSH refuses to use a private key file that is readable by group or others.

</details>

<details><summary><b>16.</b> What does `chown` do and what is the syntax to change both owner and group?</summary>

`chown` changes file ownership; `chown user:group file` sets owner and group, e.g. `chown senio:dataeng nav.csv`.

</details>

<details><summary><b>17.</b> When do you typically need `sudo`?</summary>

When performing actions requiring root/administrator privileges, such as installing packages, editing files under `/etc`, or writing outside your home directory.

</details>

<details><summary><b>18.</b> Why is running everything as root (or blanket `sudo`) discouraged?</summary>

It removes the safety net of permission checks, so a typo or malicious script can damage the whole system; least-privilege limits blast radius.

</details>

<details><summary><b>19.</b> What does `chmod -R 755 reports/` do?</summary>

Recursively sets `755` permissions on `reports/` and everything inside it; `-R` means recurse into subdirectories.

</details>

<details><summary><b>20.</b> What does `pwd` print?</summary>

The present working directory — the absolute path of the directory you are currently in.

</details>

<details><summary><b>21.</b> What is the difference between an absolute path and a relative path?</summary>

An absolute path starts from root `/` (e.g. `/home/senio/data`); a relative path is interpreted from the current directory (e.g. `data/nav.csv`).

</details>

<details><summary><b>22.</b> What do `.` and `..` refer to?</summary>

`.` is the current directory and `..` is the parent directory; `cd ..` moves up one level.

</details>

<details><summary><b>23.</b> What does `cd` with no arguments do?</summary>

It returns you to your home directory (`$HOME`), equivalent to `cd ~`.

</details>

<details><summary><b>24.</b> What does `cd -` do?</summary>

It switches to the previous working directory you were in (the value of `$OLDPWD`).

</details>

<details><summary><b>25.</b> What does `ls -la` show that plain `ls` does not?</summary>

`-l` gives the long format (permissions, owner, size, date); `-a` includes hidden dotfiles like `.bashrc`.

</details>

<details><summary><b>26.</b> How do you list files sorted by modification time, newest first?</summary>

`ls -lt` (add `-r` to reverse to oldest first); useful for finding the latest delivered EMT file in a drop folder.

</details>

<details><summary><b>27.</b> What does the `|` (pipe) operator do?</summary>

It connects the standard output of one command to the standard input of the next, e.g. `cat nav.csv | grep LU` filters lines containing `LU`.

</details>

<details><summary><b>28.</b> What is the difference between `>` and `>>`?</summary>

`>` redirects stdout to a file, overwriting it; `>>` appends to the file, preserving existing contents.

</details>

<details><summary><b>29.</b> What does `2>` redirect?</summary>

File descriptor 2, standard error (stderr); e.g. `./job.sh 2> errors.log` sends only error output to the file.

</details>

<details><summary><b>30.</b> How do you redirect both stdout and stderr to the same file?</summary>

`command > out.log 2>&1` (or in bash `command &> out.log`); the `2>&1` sends stderr to wherever stdout currently points.

</details>

<details><summary><b>31.</b> What does the order matter in `command 2>&1 > file` versus `command > file 2>&1`?</summary>

`> file 2>&1` sends both to the file; `2>&1 > file` sends stderr to the terminal (stdout's original target) and only stdout to the file, because redirections are applied left to right.

</details>

<details><summary><b>32.</b> What is `/dev/null` and a common use for it?</summary>

A special device that discards everything written to it; `command 2>/dev/null` suppresses error messages, and `> /dev/null 2>&1` discards all output.

</details>

<details><summary><b>33.</b> What are the three standard file descriptors and their numbers?</summary>

stdin (0), stdout (1), and stderr (2).

</details>

<details><summary><b>34.</b> What does `tee` do in a pipeline?</summary>

It reads stdin and writes to both stdout and one or more files, e.g. `./job.sh | tee run.log` shows output on screen and saves it.

</details>

<details><summary><b>35.</b> What does `grep "LU" isin_list.txt` do?</summary>

It prints every line of `isin_list.txt` containing the substring `LU` (e.g. Luxembourg-domiciled ISINs).

</details>

<details><summary><b>36.</b> What does `grep -i` do?</summary>

Case-insensitive matching, so `grep -i nav` matches `NAV`, `nav`, and `Nav`.

</details>

<details><summary><b>37.</b> How do you grep recursively through a directory of files?</summary>

`grep -r "ISIN" data/` searches all files under `data/`; add `-l` to print only the names of matching files.

</details>

<details><summary><b>38.</b> How would you count how many lines in `holdings.csv` contain a Luxembourg ISIN (prefix `LU`)?</summary>

`grep -c "^LU" holdings.csv` if the ISIN starts the line, or `grep -c "LU" holdings.csv` to count any line containing `LU`.

</details>

<details><summary><b>39.</b> What does the `-E` flag give `grep`?</summary>

Extended regular expressions, allowing `+`, `?`, `|`, and `()` without backslash escaping, e.g. `grep -E "NAV|TNA"`.

</details>

<details><summary><b>40.</b> What does `sed 's/old/new/'` do?</summary>

It performs a substitution, replacing the first occurrence of `old` with `new` on each line; output goes to stdout by default.

</details>

<details><summary><b>41.</b> How do you make `sed` replace all occurrences on each line, not just the first?</summary>

Add the global flag: `sed 's/old/new/g'`.

</details>

<details><summary><b>42.</b> How do you edit a file in place with `sed`?</summary>

`sed -i 's/;/,/g' emt.csv` modifies the file directly; on GNU sed `-i` works, and a backup can be kept with `-i.bak`.

</details>

<details><summary><b>43.</b> How would you convert a semicolon-delimited EMT file to comma-delimited with `sed`?</summary>

`sed 's/;/,/g' emt.csv > emt_comma.csv` (assuming no semicolons appear inside quoted fields).

</details>

<details><summary><b>44.</b> What does `awk '{print $2}'` do?</summary>

It prints the second whitespace-separated field of each line; `$0` is the whole line, `$1` the first field, etc.

</details>

<details><summary><b>45.</b> How do you tell `awk` the fields are separated by commas?</summary>

Use `-F,` (or `-F','`), e.g. `awk -F, '{print $1}' nav.csv` prints the first comma-separated column.

</details>

<details><summary><b>46.</b> How would you use `awk` to print the ISIN and NAV columns (say fields 1 and 4) of a CSV?</summary>

`awk -F, '{print $1, $4}' nav.csv`; the comma in `print` inserts the output field separator (a space by default).

</details>

<details><summary><b>47.</b> How do you filter rows in `awk` where the NAV (field 4) exceeds 100?</summary>

`awk -F, '$4 > 100' nav.csv` prints rows whose fourth field is numerically greater than 100.

</details>

<details><summary><b>48.</b> How would you sum a numeric column with `awk`?</summary>

`awk -F, '{sum += $4} END {print sum}' nav.csv` accumulates field 4 and prints the total after the last line.

</details>

<details><summary><b>49.</b> What is the difference between `grep`, `sed`, and `awk` at a high level?</summary>

`grep` finds/filters lines by pattern, `sed` does stream edits like search-and-replace, and `awk` is a small language for field-based extraction and computation.

</details>

<details><summary><b>50.</b> What does the `$PATH` environment variable control?</summary>

The ordered list of directories the shell searches for an executable when you type a command; "command not found" means the binary is in none of those directories.

</details>

<details><summary><b>51.</b> How do you print the value of an environment variable?</summary>

`echo $VAR` (e.g. `echo $PATH`) or `printenv VAR`.

</details>

<details><summary><b>52.</b> How do you set an environment variable for the current shell session only?</summary>

`export VAR=value`, e.g. `export DB_HOST=localhost`; it persists for the session and child processes but not after closing the shell.

</details>

<details><summary><b>53.</b> What is the difference between `VAR=value` and `export VAR=value`?</summary>

Plain `VAR=value` sets a shell variable visible only to the current shell; `export` marks it for inheritance by child processes (it becomes an environment variable).

</details>

<details><summary><b>54.</b> How do you append a directory to `$PATH` without losing the existing entries?</summary>

`export PATH="$PATH:/new/dir"` (or prepend with `export PATH="/new/dir:$PATH"` to give it priority).

</details>

<details><summary><b>55.</b> Where would you put `export` lines so they apply to every new interactive shell?</summary>

In your shell startup file, typically `~/.bashrc` (or `~/.profile`/`~/.bash_profile` for login shells).

</details>

<details><summary><b>56.</b> After editing `~/.bashrc`, how do you apply the changes without logging out?</summary>

Run `source ~/.bashrc` (or `. ~/.bashrc`) to re-read the file into the current shell.

</details>

<details><summary><b>57.</b> How do you find which executable will run for a given command name?</summary>

`which command` (or `type command`) shows the full path of the binary that would be executed based on `$PATH`.

</details>

<details><summary><b>58.</b> How do you unset an environment variable?</summary>

`unset VAR` removes it from the current shell environment.

</details>

<details><summary><b>59.</b> What is SSH and what is it used for?</summary>

Secure Shell — an encrypted protocol for logging into and running commands on remote machines, and for secure file transfer (scp/sftp) and tunneling.

</details>

<details><summary><b>60.</b> What is the difference between an SSH public key and private key?</summary>

The private key (e.g. `~/.ssh/id_ed25519`) stays secret on your machine; the public key (`.pub`) is copied to servers, which use it to verify you hold the matching private key.

</details>

<details><summary><b>61.</b> What command generates a modern SSH key pair?</summary>

`ssh-keygen -t ed25519 -C "you@example.com"` creates an Ed25519 key pair, recommended over older RSA.

</details>

<details><summary><b>62.</b> How do you copy your public key to a remote server's authorized keys?</summary>

`ssh-copy-id user@host` appends your public key to the server's `~/.ssh/authorized_keys`; otherwise paste it there manually.

</details>

<details><summary><b>63.</b> What is the SSH agent and why use it?</summary>

`ssh-agent` is a background process that holds your decrypted private keys in memory so you enter your passphrase once per session instead of on every connection.

</details>

<details><summary><b>64.</b> How do you add a key to the running SSH agent?</summary>

`ssh-add ~/.ssh/id_ed25519` (start the agent first with `eval "$(ssh-agent -s)"` if it is not running).

</details>

<details><summary><b>65.</b> What is the purpose of the `~/.ssh/config` file?</summary>

It stores per-host connection settings (hostname, user, port, identity file) so you can connect with a short alias, e.g. `ssh prod-sftp`.

</details>

<details><summary><b>66.</b> What does a "Permissions 0644 for 'id_ed25519' are too open" SSH error mean and how do you fix it?</summary>

SSH refuses to use a private key that others can read; fix with `chmod 600 ~/.ssh/id_ed25519`.

</details>

<details><summary><b>67.</b> What is `known_hosts` and why does SSH warn about a changed host key?</summary>

`~/.ssh/known_hosts` records server fingerprints; a changed key triggers a warning because it could indicate a man-in-the-middle attack (or a legitimately rebuilt server).

</details>

<details><summary><b>68.</b> What does a shebang line like `#!/usr/bin/env bash` do?</summary>

It tells the OS which interpreter to run the script with; using `env bash` finds bash via `$PATH` rather than hardcoding `/bin/bash`.

</details>

<details><summary><b>69.</b> Why must the shebang be the very first line of a script?</summary>

The kernel only checks the first two bytes (`#!`) of the file to choose the interpreter; if anything precedes it, the shebang is ignored.

</details>

<details><summary><b>70.</b> In a bash script, what do `$1`, `$2`, etc. mean?</summary>

They are positional parameters — the first, second, etc. command-line arguments passed to the script.

</details>

<details><summary><b>71.</b> What is the difference between `$@` and `$*`?</summary>

Both expand to all positional arguments, but `"$@"` expands each argument as a separate quoted word (correct for preserving spaces), while `"$*"` joins them into a single word.

</details>

<details><summary><b>72.</b> What does `$#` give you in a script?</summary>

The number of positional arguments passed to the script.

</details>

<details><summary><b>73.</b> What is an exit code and what does `0` conventionally mean?</summary>

An exit code is the integer a command returns on completion; `0` means success and any non-zero value (1–255) signals an error.

</details>

<details><summary><b>74.</b> How do you check the exit code of the command you just ran?</summary>

Inspect `$?`, e.g. `echo $?` prints the exit status of the last command.

</details>

<details><summary><b>75.</b> How do you make a script exit with a specific failure code?</summary>

Use `exit N`, e.g. `exit 1` to signal a generic error to the caller (such as a cron job or orchestrator).

</details>

<details><summary><b>76.</b> What does `set -e` do in a bash script?</summary>

It makes the script exit immediately if any command returns a non-zero status, so failures do not silently continue.

</details>

<details><summary><b>77.</b> What does `set -u` do?</summary>

It treats the use of any unset variable as an error and exits, catching typos like `$INPTU_FILE` instead of `$INPUT_FILE`.

</details>

<details><summary><b>78.</b> What does `set -o pipefail` do?</summary>

It makes a pipeline return the exit status of the first failing command rather than only the last command's status, so `grep x file | sort` fails if `grep` fails.

</details>

<details><summary><b>79.</b> Why is `set -euo pipefail` a recommended header for production bash scripts?</summary>

Together they make the script fail fast on errors (`-e`), unset variables (`-u`), and broken pipelines (`pipefail`), which prevents a partially-failed NAV load from looking successful.

</details>

<details><summary><b>80.</b> What is the basic syntax of an `if` statement in bash?</summary>

`if condition; then ...; fi`, e.g. `if [ -f nav.csv ]; then echo found; fi`; optional `elif` and `else` branches are allowed.

</details>

<details><summary><b>81.</b> What is the difference between `[` and `[[` in bash conditionals?</summary>

`[` is the older POSIX `test` command; `[[ ]]` is a bash keyword with safer behavior — it supports `&&`, `||`, pattern matching, and avoids word-splitting pitfalls.

</details>

<details><summary><b>82.</b> How do you write a `for` loop over files in bash?</summary>

`for f in *.csv; do echo "$f"; done` iterates over each matching filename; always quote `"$f"` to handle spaces.

</details>

<details><summary><b>83.</b> How would you loop over each EMT file in a folder and run a load script on it?</summary>

`for f in emt/*.csv; do ./load_emt.sh "$f"; done` runs `load_emt.sh` once per file.

</details>

<details><summary><b>84.</b> Why should you quote variables like `"$f"` in scripts?</summary>

Unquoted variables undergo word-splitting and glob expansion, so a filename with spaces or special characters would break into multiple arguments; quoting preserves it as one value.

</details>

<details><summary><b>85.</b> What is command substitution and how do you write it?</summary>

It captures a command's output into a value using `$(command)` (preferred) or backticks, e.g. `today=$(date +%F)`.

</details>

<details><summary><b>86.</b> How do you provide a default value for a possibly-unset variable?</summary>

Parameter expansion `${VAR:-default}` yields `default` if `VAR` is unset or empty, e.g. `dir=${DATA_DIR:-/data}`.

</details>

<details><summary><b>87.</b> What does `apt update` do versus `apt upgrade`?</summary>

`apt update` refreshes the local package index from the repositories; `apt upgrade` actually installs newer versions of already-installed packages.

</details>

<details><summary><b>88.</b> Why must you usually prefix `apt` commands with `sudo`?</summary>

Installing, upgrading, or removing system packages modifies system directories and the package database, which requires root privileges.

</details>

<details><summary><b>89.</b> How do you install a package with `apt`?</summary>

`sudo apt install <package>`, e.g. `sudo apt install jq` to install the JSON-processing tool.

</details>

<details><summary><b>90.</b> How do you search for an available package and inspect one?</summary>

`apt search <term>` lists matching packages and `apt show <package>` displays details like version and dependencies.

</details>

<details><summary><b>91.</b> How do you remove a package, and what is the difference between `remove` and `purge`?</summary>

`sudo apt remove <package>` deletes the package but keeps its config files; `sudo apt purge <package>` removes the package and its system config files too.

</details>

<details><summary><b>92.</b> What is the difference between `apt` and `dpkg`?</summary>

`dpkg` is the low-level tool that installs individual `.deb` files without resolving dependencies; `apt` is the high-level front end that fetches packages and resolves dependencies from repositories.

</details>

<details><summary><b>93.</b> What is cron used for?</summary>

Scheduling commands or scripts to run automatically at fixed times or intervals, e.g. a nightly job that ingests NAV files at 02:00.

</details>

<details><summary><b>94.</b> How do you edit your personal crontab?</summary>

`crontab -e` opens your user crontab in an editor; `crontab -l` lists current entries and `crontab -r` removes them all.

</details>

<details><summary><b>95.</b> What do the five time fields of a crontab entry represent, in order?</summary>

Minute (0–59), hour (0–23), day of month (1–31), month (1–12), and day of week (0–7, where both 0 and 7 are Sunday).

</details>

<details><summary><b>96.</b> What schedule does the cron line `0 2 * * 1-5` represent?</summary>

02:00 every Monday through Friday — useful for a NAV load that only runs on EU business days.

</details>

<details><summary><b>97.</b> What does `*/15 * * * *` mean in cron?</summary>

Run every 15 minutes (at minutes 0, 15, 30, 45 of every hour).

</details>

<details><summary><b>98.</b> Why do cron jobs often fail with "command not found" even when the script works in your terminal?</summary>

Cron runs with a minimal environment and a very limited `$PATH`, so you must use absolute paths to binaries or set `PATH` explicitly inside the crontab or script.

</details>

<details><summary><b>99.</b> How do you capture the output and errors of a cron job for troubleshooting?</summary>

Redirect in the crontab line, e.g. `0 2 * * * /opt/jobs/load_nav.sh >> /var/log/nav.log 2>&1`, so both stdout and stderr are appended to a log.

</details>

<details><summary><b>100.</b> A nightly cron job that loads transfer-agency files silently produces no data — what should you check first?</summary>

Check the job's log/output and exit code, then verify cron's environment: confirm absolute paths, the `$PATH`, file permissions on the input directory, and that the script is executable.

</details>


## Phase 0 · 0.2 Programming from zero: Python — 100 self-test questions

<details><summary><b>1.</b> What is a Python variable, and how do you create one?</summary>

A variable is a name bound to a value; you create it by assignment, e.g. `nav = 12.34`, with no separate declaration or type annotation required.

</details>

<details><summary><b>2.</b> Name Python's four most common built-in scalar types and a value of each.</summary>

`int` (e.g. `42`), `float` (e.g. `12.34`), `str` (e.g. `"ISIN"`), and `bool` (`True`/`False`).

</details>

<details><summary><b>3.</b> What does the `type()` function return, and why is it useful when debugging?</summary>

It returns the class/type of an object, e.g. `type(nav)` -> `<class 'float'>`; it's useful to confirm a value isn't a string when arithmetic misbehaves.

</details>

<details><summary><b>4.</b> What is the difference between `==` and `is` in Python?</summary>

`==` compares values for equality, while `is` checks whether two names refer to the exact same object in memory; use `==` for value comparisons and `is` mainly for `is None`.

</details>

<details><summary><b>5.</b> Why should you write `if x is None:` rather than `if x == None:`?</summary>

`None` is a singleton, so identity (`is`) is the correct and faster check, and it avoids surprises from objects that override `__eq__`.

</details>

<details><summary><b>6.</b> What is the difference between `5 / 2` and `5 // 2` in Python 3?</summary>

`5 / 2` is true division giving `2.5` (a `float`), while `5 // 2` is floor division giving `2` (an `int`).

</details>

<details><summary><b>7.</b> What does `int("0012")` return, and what does `int("12.0")` do?</summary>

`int("0012")` returns `12`, but `int("12.0")` raises `ValueError` because `int()` won't parse a decimal-point string directly.

</details>

<details><summary><b>8.</b> Why can converting a NAV string like `"1,234.56"` to a number fail, and how do you handle it?</summary>

`float("1,234.56")` raises `ValueError` because of the thousands separator; strip or replace separators first (e.g. `value.replace(",", "")`) before converting.

</details>

<details><summary><b>9.</b> What is an f-string and why is it preferred for building messages?</summary>

An f-string is a string literal prefixed with `f` that interpolates expressions in braces, e.g. `f"Fund {isin} NAV {nav:.4f}"`; it's concise, readable, and supports format specs.

</details>

<details><summary><b>10.</b> What does the format spec `:.4f` do inside an f-string?</summary>

It formats a number as a fixed-point decimal with exactly 4 digits after the point, which suits NAV values commonly quoted to 4 decimals.

</details>

<details><summary><b>11.</b> What is the difference between mutable and immutable types, with one example each?</summary>

Mutable objects can be changed in place (e.g. `list`, `dict`, `set`); immutable objects cannot (e.g. `int`, `str`, `tuple`), so "changing" them creates a new object.

</details>

<details><summary><b>12.</b> What value does an empty string, empty list, `0`, and `None` have in a boolean context?</summary>

They are all falsy, so `if not value:` is true for each; use this carefully because `0` and `""` are valid data that may not mean "missing".

</details>

<details><summary><b>13.</b> Write an `if/elif/else` that classifies a currency as `"EUR"`, `"USD"`, or `"other"`.</summary>

`if ccy == "EUR": ... elif ccy == "USD": ... else: ...`, where each branch handles one case and `else` catches the rest.

</details>

<details><summary><b>14.</b> How does Python delimit a code block instead of using braces?</summary>

By indentation; a consistent indent (conventionally 4 spaces) defines the block, and mixing tabs and spaces raises an error.

</details>

<details><summary><b>15.</b> What does a `for` loop iterate over, and how do you loop over a list of ISINs?</summary>

A `for` loop iterates over any iterable; `for isin in isins:` binds each element of the list to `isin` in turn.

</details>

<details><summary><b>16.</b> How do you get both the index and the value while looping over a list?</summary>

Use `enumerate`, e.g. `for i, row in enumerate(rows):`, optionally `enumerate(rows, start=1)` to count from 1 (handy for human-readable row numbers).

</details>

<details><summary><b>17.</b> What is the difference between `break` and `continue`?</summary>

`break` exits the enclosing loop entirely, while `continue` skips to the next iteration without running the rest of the current loop body.

</details>

<details><summary><b>18.</b> When would you use a `while` loop instead of a `for` loop?</summary>

When you don't know the iteration count in advance and loop until a condition changes, e.g. paging through an API until no more results are returned.

</details>

<details><summary><b>19.</b> What is a list comprehension, and rewrite `[x for x in navs if x > 0]` in words?</summary>

A concise expression that builds a list; this one collects each `x` from `navs` keeping only the positive values.

</details>

<details><summary><b>20.</b> How do you define a function that takes a row and returns a parsed fund record?</summary>

Use `def parse_row(row):` followed by an indented body that ends in `return record`; the function name and parameters describe its single job.

</details>

<details><summary><b>21.</b> What is the difference between a positional argument and a keyword argument?</summary>

Positional arguments are matched by order, keyword arguments by name (e.g. `f(2, ccy="EUR")`); keywords improve readability and let you skip optional parameters.

</details>

<details><summary><b>22.</b> What is a default parameter value, and what is the classic mutable-default pitfall?</summary>

A default is used when the caller omits the argument; using a mutable default like `def f(items=[])` is a trap because the same list persists across calls — use `None` and create inside instead.

</details>

<details><summary><b>23.</b> What does a function return if it has no `return` statement?</summary>

It returns `None` implicitly, so calling it for a value gives `None` rather than an error.

</details>

<details><summary><b>24.</b> What is the difference between `print()` and `return` in a function?</summary>

`print()` writes to stdout for humans, while `return` hands a value back to the caller for further use; a function meant to be composed should return, not print.

</details>

<details><summary><b>25.</b> Why does the plan favour small composable functions (parse, filter, summarize, write) over one big script blob?</summary>

Small single-purpose functions are independently readable, reusable, and unit-testable, and they make failures easier to localize than a monolithic script.

</details>

<details><summary><b>26.</b> What is variable scope, and can a function see variables defined outside it?</summary>

Scope is the region where a name is visible; a function can read enclosing/global names but assigning to a name inside makes it local unless declared `global` or `nonlocal`.

</details>

<details><summary><b>27.</b> What is a module in Python?</summary>

A module is a `.py` file whose top-level names (functions, classes, variables) can be imported and reused by other files.

</details>

<details><summary><b>28.</b> What is the difference between `import json` and `from json import dumps`?</summary>

`import json` binds the module so you call `json.dumps(...)`, while `from json import dumps` binds the name directly so you call `dumps(...)`; the first keeps the namespace explicit.

</details>

<details><summary><b>29.</b> What does `if __name__ == "__main__":` do?</summary>

It guards code so it runs only when the file is executed directly, not when it's imported as a module, keeping importable functions free of side effects.

</details>

<details><summary><b>30.</b> What is the standard library, and name two modules you'd use building a CSV loader.</summary>

It's the batteries-included set of modules shipped with Python; `csv` for parsing rows and `json` for writing the summary are typical choices.

</details>

<details><summary><b>31.</b> What does the `csv` module's `csv.DictReader` give you per row?</summary>

A dict keyed by the header column names, so you access fields like `row["ISIN"]` instead of by numeric index, which is more robust to column reordering.

</details>

<details><summary><b>32.</b> What is the difference between a list and a tuple?</summary>

Both are ordered sequences, but lists are mutable (`[]`) and tuples are immutable (`()`); use a tuple for fixed records and as dict keys.

</details>

<details><summary><b>33.</b> What does list slicing `rows[1:]` return for a CSV that includes a header row?</summary>

All rows except the first, a common idiom for skipping a header when you've read the file into a list of lines.

</details>

<details><summary><b>34.</b> What is a dict, and why is it the natural fit for a funds-by-ISIN lookup?</summary>

A dict maps keys to values with average O(1) lookup; keying funds by their unique ISIN gives instant retrieval of a fund record by its identifier.

</details>

<details><summary><b>35.</b> What's the difference between `d["ISIN"]` and `d.get("ISIN")` when the key is missing?</summary>

`d["ISIN"]` raises `KeyError`, while `d.get("ISIN")` returns `None` (or a supplied default), which is safer when a field may be absent.

</details>

<details><summary><b>36.</b> What does `dict.setdefault(key, [])` do, and how does it help build a counts structure?</summary>

It returns the existing value or inserts and returns the default if the key is missing, letting you append to per-key lists without a separate existence check.

</details>

<details><summary><b>37.</b> What is `collections.Counter` good for in this loader?</summary>

It counts hashable items efficiently, so `Counter(currencies)` directly yields counts per currency for the summary JSON.

</details>

<details><summary><b>38.</b> What is a set, and what two properties make it distinct from a list?</summary>

A set is an unordered collection of unique, hashable elements; it removes duplicates automatically and offers fast membership tests.

</details>

<details><summary><b>39.</b> How would you find ISINs present in file A but not in file B using sets?</summary>

Convert both to sets and subtract: `set(a) - set(b)` yields the ISINs only in A.

</details>

<details><summary><b>40.</b> Why is checking `isin in my_set` faster than `isin in my_list` for large data?</summary>

Set membership is average O(1) via hashing, whereas list membership is O(n) because it scans element by element.

</details>

<details><summary><b>41.</b> Can a list be a dict key or a set element? Why or why not?</summary>

No — lists are unhashable because they're mutable; use a tuple instead, which is hashable and can serve as a key or set element.

</details>

<details><summary><b>42.</b> What does the `with open(path) as f:` pattern guarantee?</summary>

It opens the file in a context manager that automatically closes it when the block exits, even if an exception is raised.

</details>

<details><summary><b>43.</b> Why prefer `with open(...)` over a bare `open()` plus manual `close()`?</summary>

The context manager closes the file deterministically, preventing leaked file handles and partially written files when errors occur.

</details>

<details><summary><b>44.</b> Why should you pass `encoding="utf-8"` when opening text files?</summary>

It makes decoding explicit and portable; relying on the platform default can corrupt non-ASCII fund names or fail differently on Windows vs Linux.

</details>

<details><summary><b>45.</b> What does iterating directly over a file object yield?</summary>

One line at a time (including the trailing newline), which lets you process a large CSV line by line without loading it all into memory.

</details>

<details><summary><b>46.</b> What is an exception, and name two common ones a CSV loader might hit.</summary>

An exception is a runtime error object that interrupts normal flow; `FileNotFoundError` (missing input) and `ValueError` (bad number conversion) are typical.

</details>

<details><summary><b>47.</b> Write the shape of a `try/except` that catches a bad number and reports the row.</summary>

`try: nav = float(row["nav"]) except ValueError: raise ValueError(f"bad NAV on row {n}: {row['nav']!r}")`, turning a vague error into a located one.

</details>

<details><summary><b>48.</b> Why is `except Exception:` (or bare `except:`) usually a bad idea?</summary>

It swallows every error including bugs and `KeyboardInterrupt`-adjacent issues, hiding the real problem; catch the specific exceptions you can actually handle.

</details>

<details><summary><b>49.</b> What does the `finally` clause guarantee?</summary>

It runs whether or not an exception occurred, used for cleanup; with `with`, much of this need disappears.

</details>

<details><summary><b>50.</b> How do you re-raise the current exception after logging it?</summary>

Use a bare `raise` inside the `except` block, which preserves the original traceback rather than masking it.

</details>

<details><summary><b>51.</b> What does `raise ValueError("malformed row 42")` accomplish in the loader spec?</summary>

It fails loudly with a precise message including the row number, so a malformed transfer-agency row is diagnosable instead of silently skipped.

</details>

<details><summary><b>52.</b> How do you make a CLI exit non-zero with a clean one-line message instead of a raw traceback?</summary>

Catch the expected error at the top level, print a short message to stderr, and call `sys.exit(1)` (or `raise SystemExit("message")`).

</details>

<details><summary><b>53.</b> What does `raise ... from err` do?</summary>

It chains exceptions, showing the original cause in the traceback ("The above exception was the direct cause..."), preserving the debugging trail.

</details>

<details><summary><b>54.</b> What is `uv` and what role does it play in this plan?</summary>

`uv` is a fast Python package and project manager (from Astral) that handles environments, dependencies, and running code; it's the only sanctioned way Python runs here.

</details>

<details><summary><b>55.</b> What does `uv init fundcli` create?</summary>

A new project directory scaffold with a `pyproject.toml`, a starter source file, and version-control metadata, ready for dependencies and `uv run`.

</details>

<details><summary><b>56.</b> What does `uv add httpx` do?</summary>

It adds `httpx` as a project dependency, resolves and installs it into the project environment, and records it in `pyproject.toml` and the lockfile.

</details>

<details><summary><b>57.</b> What does `uv run fundcli.py --help` do that bare `python fundcli.py` does not?</summary>

It ensures the project's locked environment exists and is in sync first, then runs the script inside it — no manual venv activation needed.

</details>

<details><summary><b>58.</b> What is the `uv.lock` file and why does it matter?</summary>

It's the lockfile pinning exact resolved versions (and hashes) of all dependencies, so every machine reproduces the identical environment.

</details>

<details><summary><b>59.</b> Why is bare `pip install` banned in this plan?</summary>

Bare `pip` mutates whatever environment is active, isn't reproducible or lock-tracked, and easily corrupts the system Python; `uv` gives reproducible, isolated, fast installs instead.

</details>

<details><summary><b>60.</b> Should you commit `uv.lock` to git? Why?</summary>

Yes — committing the lockfile is how teammates and CI get byte-for-byte reproducible environments; it's the source of truth for versions.

</details>

<details><summary><b>61.</b> What is the difference between `pyproject.toml` and `uv.lock`?</summary>

`pyproject.toml` declares your intended dependencies and constraints, while `uv.lock` records the exact resolved versions that satisfy them.

</details>

<details><summary><b>62.</b> What does `uv sync` do?</summary>

It makes the project environment match the lockfile exactly, installing or removing packages as needed; `uv run` does this implicitly before running.

</details>

<details><summary><b>63.</b> How do you add a tool you only need for development, like ruff, without shipping it as a runtime dependency?</summary>

Add it to a dev dependency group, e.g. `uv add --dev ruff`, so it's available locally and in CI but not required by consumers.

</details>

<details><summary><b>64.</b> A traceback is many lines long — where is the actual error, and which line names the cause?</summary>

Read it bottom-up: the last line names the exception type and message, and the frames above show the call path that led there.

</details>

<details><summary><b>65.</b> In a traceback, what do "File ..., line N, in func" entries represent?</summary>

Each is a stack frame — a function call in progress — listed from outermost call at the top down to the line that actually raised at the bottom.

</details>

<details><summary><b>66.</b> What does `TypeError: unsupported operand type(s) for +: 'int' and 'str'` tell you?</summary>

You tried to add a number and a string; likely a value read from CSV is still text and needs `int()`/`float()` before arithmetic.

</details>

<details><summary><b>67.</b> What does `KeyError: 'ISIN'` during CSV processing usually indicate?</summary>

The dict (often a CSV row) has no `'ISIN'` key — commonly a header typo, wrong delimiter, or a column-name mismatch like `isin` vs `ISIN`.

</details>

<details><summary><b>68.</b> What does `IndentationError` mean and what's the usual cause?</summary>

The code's indentation is inconsistent or unexpected; common causes are mixing tabs and spaces or misaligning a block.

</details>

<details><summary><b>69.</b> What is the recommended first step when debugging a failure you don't understand?</summary>

Reproduce it minimally — strip the input and code down to the smallest example that still fails — then read the traceback bottom-up before changing anything.

</details>

<details><summary><b>70.</b> How can `print()` or the `breakpoint()` builtin help during debugging?</summary>

`print()` reveals intermediate values quickly, while `breakpoint()` drops you into an interactive debugger (`pdb`) at that line to inspect state and step through.

</details>

<details><summary><b>71.</b> What is the difference between a syntax error and a runtime exception?</summary>

A syntax error is caught before any code runs (the file won't parse), while a runtime exception occurs during execution on a particular input.

</details>

<details><summary><b>72.</b> What does `NameError: name 'navs' is not defined` typically mean?</summary>

You referenced a name that was never assigned in scope — often a typo, a variable defined in another function, or used before assignment.

</details>

<details><summary><b>73.</b> What does `AttributeError: 'NoneType' object has no attribute 'strip'` usually reveal?</summary>

A value you expected to be a string is actually `None` — frequently a function returned `None` or a `.get()` missed a key.

</details>

<details><summary><b>74.</b> What is an HTTP status code, and what does the 2xx range mean?</summary>

It's a three-digit number summarizing a request's outcome; 2xx (e.g. `200 OK`, `201 Created`) means the request succeeded.

</details>

<details><summary><b>75.</b> What do the 4xx and 5xx status-code ranges mean, with one example each?</summary>

4xx is a client error (e.g. `404 Not Found`, `401 Unauthorized`), 5xx is a server error (e.g. `500 Internal Server Error`, `503 Service Unavailable`).

</details>

<details><summary><b>76.</b> What does `429 Too Many Requests` mean and how should a client respond?</summary>

You've been rate-limited; back off and retry after a delay, ideally honoring the `Retry-After` header rather than hammering the endpoint.

</details>

<details><summary><b>77.</b> Why must you always set a timeout on an HTTP request?</summary>

Without a timeout a hung server can block your program indefinitely; a timeout makes the call fail fast so your loader can retry or report cleanly.

</details>

<details><summary><b>78.</b> After `resp = requests.get(url)`, how do you turn a 4xx/5xx into an exception?</summary>

Call `resp.raise_for_status()`, which raises an `HTTPError` for error status codes instead of letting you silently process a failed response.

</details>

<details><summary><b>79.</b> How do you parse a JSON response body into Python objects?</summary>

Call `resp.json()` (or `json.loads(resp.text)`), which converts the JSON into dicts, lists, strings, numbers, and booleans.

</details>

<details><summary><b>80.</b> What is the difference between `json.loads` and `json.load`?</summary>

`json.loads` parses a JSON string in memory, while `json.load` reads and parses from a file object; the `s` stands for "string".

</details>

<details><summary><b>81.</b> How does JSON map onto Python types when you parse it?</summary>

Object -> `dict`, array -> `list`, string -> `str`, number -> `int`/`float`, `true`/`false` -> `bool`, `null` -> `None`.

</details>

<details><summary><b>82.</b> Why should you check `resp.status_code` (or call `raise_for_status`) before calling `resp.json()`?</summary>

An error response often returns HTML or an error JSON, so parsing it as your expected payload yields a confusing `KeyError` or decode error downstream.

</details>

<details><summary><b>83.</b> What does `json.dumps(data, indent=2)` produce versus `json.dumps(data)`?</summary>

`indent=2` pretty-prints with newlines and indentation for human reading, while the plain form produces compact single-line JSON.

</details>

<details><summary><b>84.</b> When writing JSON for fund names with accents, what argument keeps them readable?</summary>

Pass `ensure_ascii=False` to `json.dumps` so non-ASCII characters are written as themselves rather than `\uXXXX` escapes.

</details>

<details><summary><b>85.</b> A NAV feed sometimes returns `200` with an empty body — why is `resp.json()` risky there?</summary>

An empty body isn't valid JSON, so `resp.json()` raises a `JSONDecodeError`; guard by checking the body or content length before parsing.

</details>

<details><summary><b>86.</b> How would you safely retry a transient `503` from a pricing API?</summary>

Wrap the call in a loop with a bounded number of attempts and an increasing (exponential) backoff delay, only retrying idempotent requests and surfacing a clear error if all attempts fail.

</details>

<details><summary><b>87.</b> What is `argparse` and why use it instead of reading `sys.argv` directly?</summary>

`argparse` is the standard library's command-line parser; it gives you typed flags, defaults, validation, usage errors, and `--help` for free instead of hand-parsing `sys.argv`.

</details>

<details><summary><b>88.</b> How do you add a `--currency` flag to an `ArgumentParser`?</summary>

`parser.add_argument("--currency")`, optionally with `help=...`, `default=...`, and `choices=[...]` to constrain and document it.

</details>

<details><summary><b>89.</b> How do you make argparse treat a flag as a boolean switch like `--verbose`?</summary>

Use `action="store_true"`, so the flag's value is `True` when present and `False` (the default) when absent.

</details>

<details><summary><b>90.</b> Where does `--help` text come from, and why does the plan require good help?</summary>

It's generated from the parser's `description` and each argument's `help=`; good help lets someone run `fundcli` correctly without reading the source.

</details>

<details><summary><b>91.</b> What is an exit code, and what do `0` and non-zero mean to a calling shell or pipeline?</summary>

It's the integer a process returns on exit; `0` means success and any non-zero value means failure, which scripts and CI use to decide whether to continue.

</details>

<details><summary><b>92.</b> How do you set a specific exit code from your Python CLI?</summary>

Call `sys.exit(2)` (or return that code from `main` to a caller that exits), or `raise SystemExit("message")` to print and exit non-zero.

</details>

<details><summary><b>93.</b> How do you restrict `--currency` to a known set of values in argparse?</summary>

Pass `choices=["EUR", "USD", "GBP"]`; argparse rejects anything else with a usage error and exit code `2`.

</details>

<details><summary><b>94.</b> Why print error messages to stderr rather than stdout in a CLI?</summary>

stdout carries the program's real output (e.g. the JSON summary) for piping, while stderr carries diagnostics, so errors don't pollute the data stream.

</details>

<details><summary><b>95.</b> What is ruff and what does it do?</summary>

ruff is a fast Python linter and formatter (from Astral) that flags style issues, likely bugs, and unused imports, and can auto-format code.

</details>

<details><summary><b>96.</b> What does `ruff check .` do versus `ruff format .`?</summary>

`ruff check .` lints and reports (and with `--fix` auto-corrects) rule violations, while `ruff format .` reformats code to a consistent style.

</details>

<details><summary><b>97.</b> Why wire ruff into the editor to run on every save from day one?</summary>

Continuous linting catches mistakes and enforces consistent style immediately, so issues never accumulate and reviews focus on logic, not formatting.

</details>

<details><summary><b>98.</b> A teammate runs `python fundcli.py` and gets `ModuleNotFoundError` for a dependency you added — what's the likely fix?</summary>

They ran bare `python` outside the project environment; running `uv run fundcli.py` (after `uv sync`) uses the locked environment where the dependency is installed.

</details>

<details><summary><b>99.</b> Your loader prints `currency` counts as all `1` even with duplicates — first thing to check?</summary>

Check whether you're counting unique values (e.g. accidentally building a set or using a dict keyed by currency overwriting counts) instead of incrementing a `Counter`.

</details>

<details><summary><b>100.</b> `uv run fundcli.py funds.csv` exits 0 but writes no JSON for a malformed file — what's wrong with the design?</summary>

Errors are being swallowed instead of raised; a malformed row should raise with its row number and the process should exit non-zero, per the loader's "fail loudly" spec.

</details>


## Phase 0 · 0.3 SQL from zero — 100 self-test questions

<details><summary><b>1.</b> What is the basic purpose of a `SELECT` statement?</summary>

It reads (queries) rows from one or more tables and returns a result set; it does not change the stored data.

</details>

<details><summary><b>2.</b> In `SELECT fund_name, nav FROM funds;`, what does the part between `SELECT` and `FROM` specify?</summary>

The column list (projection) — exactly which columns appear in the output and in what order; `fund_name` then `nav`.

</details>

<details><summary><b>3.</b> What does `SELECT *` return and why is it discouraged in production code?</summary>

It returns every column of the table; it is fragile because added/reordered columns silently change results and it pulls more data than needed.

</details>

<details><summary><b>4.</b> How do you return every row of a table with no filtering?</summary>

Omit the `WHERE` clause entirely, e.g. `SELECT * FROM funds;`.

</details>

<details><summary><b>5.</b> What does the `WHERE` clause do?</summary>

It filters rows, keeping only those for which its condition evaluates to `TRUE` (rows that are `FALSE` or `UNKNOWN` are excluded).

</details>

<details><summary><b>6.</b> Write a condition that selects funds with a NAV above 100.</summary>

`WHERE nav > 100` — comparison operators like `>`, `<`, `>=`, `<=`, `=`, `<>` filter on the column value.

</details>

<details><summary><b>7.</b> How do you match a range of NAV values inclusively between 90 and 110?</summary>

`WHERE nav BETWEEN 90 AND 110`, which is inclusive of both endpoints (equivalent to `nav >= 90 AND nav <= 110`).

</details>

<details><summary><b>8.</b> What does `WHERE currency IN ('EUR','USD','GBP')` do?</summary>

It keeps rows whose `currency` equals any value in the list — a concise alternative to several `OR` comparisons.

</details>

<details><summary><b>9.</b> What does the `LIKE` operator do and what do `%` and `_` mean?</summary>

`LIKE` does pattern matching on text; `%` matches any sequence of characters (including none) and `_` matches exactly one character.

</details>

<details><summary><b>10.</b> Write a filter for ISINs that start with `LU` (Luxembourg-domiciled).</summary>

`WHERE isin LIKE 'LU%'` — the `%` allows any characters after the `LU` prefix.

</details>

<details><summary><b>11.</b> How does `ORDER BY` change a result set?</summary>

It sorts the returned rows; without it the row order is not guaranteed by SQL even if it looks consistent.

</details>

<details><summary><b>12.</b> What is the default sort direction of `ORDER BY`, and how do you reverse it?</summary>

Ascending (`ASC`) is the default; add `DESC` for descending, e.g. `ORDER BY nav DESC`.

</details>

<details><summary><b>13.</b> How do you sort by multiple columns, e.g. currency then NAV descending?</summary>

`ORDER BY currency ASC, nav DESC` — rows are sorted by the first key, ties broken by the next.

</details>

<details><summary><b>14.</b> Can `ORDER BY` reference a column alias or output column number?</summary>

Yes; because `ORDER BY` runs after the `SELECT` list is computed, you can use an alias (`ORDER BY total`) or position (`ORDER BY 2`), though aliases are clearer.

</details>

<details><summary><b>15.</b> What does `LIMIT 10` (or `FETCH FIRST 10 ROWS ONLY`) do, and why pair it with `ORDER BY`?</summary>

It caps the result to 10 rows; without `ORDER BY` the "top 10" is arbitrary because row order is undefined.

</details>

<details><summary><b>16.</b> In what logical order are `FROM`, `WHERE`, `GROUP BY`, `HAVING`, `SELECT`, and `ORDER BY` evaluated?</summary>

`FROM` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `ORDER BY`; this explains why `WHERE` can't see aggregates and `ORDER BY` can see `SELECT` aliases.

</details>

<details><summary><b>17.</b> What is a `JOIN` used for?</summary>

To combine rows from two or more tables based on a related column (the join condition), producing a wider result set.

</details>

<details><summary><b>18.</b> What does an `INNER JOIN` return?</summary>

Only the rows where the join condition matches in both tables; unmatched rows from either side are dropped.

</details>

<details><summary><b>19.</b> What does a `LEFT JOIN` (LEFT OUTER JOIN) return?</summary>

All rows from the left table plus matching right-table columns; where there is no match, the right-side columns are `NULL`.

</details>

<details><summary><b>20.</b> A fund has no holdings yet. With `funds LEFT JOIN holdings`, what happens to that fund?</summary>

It still appears once, with all `holdings` columns as `NULL`; an `INNER JOIN` would have dropped it.

</details>

<details><summary><b>21.</b> What is the join key in `funds f JOIN nav_history n ON f.fund_id = n.fund_id`?</summary>

`fund_id` — the `ON` condition specifies which columns must match to pair rows from the two tables.

</details>

<details><summary><b>22.</b> Why can a join make the row count multiply (a "fan-out")?</summary>

If one left row matches many right rows, the left row is repeated once per match, so the output can be larger than either input table.

</details>

<details><summary><b>23.</b> One fund has 30 daily NAV rows; you join `funds` to `nav_history`. How many rows for that fund?</summary>

30 — the single fund row is duplicated once for each matching NAV row.

</details>

<details><summary><b>24.</b> A many-to-many join unexpectedly returns far too many rows. What is the likely cause?</summary>

A row on one side matches multiple rows on the other (and vice versa), so counts multiply; check whether the join key is unique on at least one side.

</details>

<details><summary><b>25.</b> How do you avoid double-counting NAV when joining a 1-to-many relationship before aggregating?</summary>

Aggregate the "many" side first (e.g. in a subquery/CTE) so each left row matches exactly one pre-aggregated row, then join.

</details>

<details><summary><b>26.</b> What does a `CROSS JOIN` produce?</summary>

The Cartesian product — every row of the left table paired with every row of the right (rows = left_count × right_count), with no join condition.

</details>

<details><summary><b>27.</b> What accidental SQL pattern silently produces a Cartesian product?</summary>

Listing tables comma-separated in `FROM` without a join condition in `WHERE`, e.g. `FROM funds, holdings` — every combination is returned.

</details>

<details><summary><b>28.</b> What is the difference between filtering in the `ON` clause vs the `WHERE` clause of a `LEFT JOIN`?</summary>

A condition in `ON` only affects which right rows match (left rows are still kept); the same condition in `WHERE` runs after the join and can drop the unmatched left rows.

</details>

<details><summary><b>29.</b> Putting `WHERE h.quantity > 0` after a `LEFT JOIN` — what unintended effect can it have?</summary>

It turns the `LEFT JOIN` into an effective `INNER JOIN`, because rows with no match have `NULL` quantity, and `NULL > 0` is `UNKNOWN`, so they are filtered out.

</details>

<details><summary><b>30.</b> What is a self-join and give a fund example?</summary>

A table joined to itself with table aliases; e.g. joining `nav_history` to itself to compare each day's NAV with the prior day's row.

</details>

<details><summary><b>31.</b> How do you find funds in table A that have no matching row in table B using a `LEFT JOIN`?</summary>

`A LEFT JOIN B ON ... WHERE b.key IS NULL` — the anti-join keeps only left rows whose right side never matched.

</details>

<details><summary><b>32.</b> What does `GROUP BY currency` do conceptually?</summary>

It collapses rows into one output row per distinct `currency`, so aggregate functions compute per group.

</details>

<details><summary><b>33.</b> Name four common aggregate functions and what they return.</summary>

`COUNT()` counts rows, `SUM()` totals, `AVG()` averages, `MIN()`/`MAX()` return the smallest/largest value in the group.

</details>

<details><summary><b>34.</b> What is the difference between `COUNT(*)` and `COUNT(column)`?</summary>

`COUNT(*)` counts all rows in the group; `COUNT(column)` counts only rows where that column is not `NULL`.

</details>

<details><summary><b>35.</b> What does `COUNT(DISTINCT isin)` return?</summary>

The number of distinct non-`NULL` ISIN values in the group, eliminating duplicates before counting.

</details>

<details><summary><b>36.</b> Which columns may appear unaggregated in the `SELECT` list when using `GROUP BY`?</summary>

Only the columns listed in `GROUP BY`; every other selected column must be inside an aggregate function (in standard SQL).

</details>

<details><summary><b>37.</b> Why does `SELECT currency, fund_name, SUM(nav) ... GROUP BY currency` raise an error?</summary>

`fund_name` is neither grouped nor aggregated, so the database cannot pick a single value per currency group.

</details>

<details><summary><b>38.</b> What is the difference between `WHERE` and `HAVING`?</summary>

`WHERE` filters individual rows before grouping; `HAVING` filters whole groups after aggregation and can reference aggregate functions.

</details>

<details><summary><b>39.</b> Write a query for currencies whose total NAV exceeds 1,000,000.</summary>

`SELECT currency, SUM(nav) FROM funds GROUP BY currency HAVING SUM(nav) > 1000000;` — the group-level filter belongs in `HAVING`.

</details>

<details><summary><b>40.</b> Can you put an aggregate like `SUM(nav) > 100` in a `WHERE` clause?</summary>

No; `WHERE` runs before grouping so aggregates aren't available there — use `HAVING` instead.

</details>

<details><summary><b>41.</b> To count holdings per fund and keep only funds with more than 50 holdings, what clauses do you use?</summary>

`GROUP BY fund_id` with `HAVING COUNT(*) > 50` — group then filter the groups.

</details>

<details><summary><b>42.</b> What does a subquery (nested query) mean?</summary>

A `SELECT` embedded inside another statement, used to produce a value, a list, or a derived table that the outer query consumes.

</details>

<details><summary><b>43.</b> What is a scalar subquery?</summary>

A subquery that returns exactly one row and one column, usable wherever a single value is expected, e.g. `WHERE nav > (SELECT AVG(nav) FROM funds)`.

</details>

<details><summary><b>44.</b> What does `WHERE isin IN (SELECT isin FROM blacklist)` do?</summary>

It keeps rows whose `isin` appears in the set of values returned by the subquery — a membership test against a list.

</details>

<details><summary><b>45.</b> What is the difference between a correlated and a non-correlated subquery?</summary>

A non-correlated subquery runs once independently; a correlated subquery references the outer row and is conceptually re-evaluated per outer row.

</details>

<details><summary><b>46.</b> What does `EXISTS (SELECT 1 FROM holdings h WHERE h.fund_id = f.fund_id)` test?</summary>

Whether at least one matching holding row exists for the current fund; `EXISTS` returns `TRUE`/`FALSE` and stops at the first match.

</details>

<details><summary><b>47.</b> What is a CTE (Common Table Expression) and how is it written?</summary>

A named temporary result defined with `WITH name AS (SELECT ...)` that you can reference later in the query, improving readability over nested subqueries.

</details>

<details><summary><b>48.</b> Give one advantage of a CTE over a nested subquery.</summary>

Readability and reuse — a CTE is named, can be referenced multiple times in the main query, and reads top-to-bottom instead of inside-out.

</details>

<details><summary><b>49.</b> How do you chain multiple CTEs?</summary>

Separate them with commas after one `WITH`, e.g. `WITH a AS (...), b AS (SELECT ... FROM a) SELECT ... FROM b;`.

</details>

<details><summary><b>50.</b> What is a recursive CTE typically used for?</summary>

Hierarchical/iterative data such as fund-of-funds ownership chains or org trees, using `WITH RECURSIVE` and a `UNION ALL` between an anchor and a recursive member.

</details>

<details><summary><b>51.</b> What is `NULL` in SQL?</summary>

A marker for unknown or missing data — it is not zero, not an empty string, and not equal to anything (including another `NULL`).

</details>

<details><summary><b>52.</b> Why does `WHERE nav = NULL` return no rows?</summary>

Comparing anything to `NULL` with `=` yields `UNKNOWN`, never `TRUE`, so no row passes the filter; you must use `IS NULL`.

</details>

<details><summary><b>53.</b> How do you correctly test for missing values?</summary>

Use `IS NULL` and `IS NOT NULL`, which are the only operators that return `TRUE`/`FALSE` for `NULL`.

</details>

<details><summary><b>54.</b> What are the three truth values in SQL's logic?</summary>

`TRUE`, `FALSE`, and `UNKNOWN` — three-valued logic, where comparisons involving `NULL` produce `UNKNOWN`.

</details>

<details><summary><b>55.</b> What does `NULL = NULL` evaluate to?</summary>

`UNKNOWN`, not `TRUE` — two unknown values cannot be asserted equal.

</details>

<details><summary><b>56.</b> What does `NOT IN (subquery)` do if the subquery contains a `NULL`?</summary>

It can wrongly return no rows, because a comparison with the `NULL` yields `UNKNOWN`; prefer `NOT EXISTS` to avoid this trap.

</details>

<details><summary><b>57.</b> How does `NULL` behave in arithmetic, e.g. `100 + NULL`?</summary>

The result is `NULL` — any arithmetic with `NULL` propagates to `NULL`.

</details>

<details><summary><b>58.</b> Does `SUM(nav)` count `NULL` NAV values?</summary>

No; aggregate functions (except `COUNT(*)`) ignore `NULL` inputs, so `SUM`/`AVG` skip them.

</details>

<details><summary><b>59.</b> How can ignoring `NULL` in `AVG()` mislead you?</summary>

`AVG` divides by the count of non-`NULL` values, so missing data is excluded rather than treated as zero, which can inflate the average.

</details>

<details><summary><b>60.</b> How do you substitute a default value for `NULL`?</summary>

Use `COALESCE(nav, 0)` (or `IFNULL`/`ISNULL` in some dialects), which returns the first non-`NULL` argument.

</details>

<details><summary><b>61.</b> What does `COALESCE(a, b, c)` return?</summary>

The first of `a`, `b`, `c` that is not `NULL`; if all are `NULL`, it returns `NULL`.

</details>

<details><summary><b>62.</b> How does `ORDER BY` handle `NULL` values?</summary>

Dialect-dependent — they sort either first or last; control it explicitly with `NULLS FIRST` / `NULLS LAST` where supported.

</details>

<details><summary><b>63.</b> What is a window function?</summary>

A function that computes a value across a set of rows related to the current row (the "window") without collapsing them, unlike `GROUP BY` which reduces rows.

</details>

<details><summary><b>64.</b> What is the key behavioural difference between an aggregate with `GROUP BY` and a window function?</summary>

`GROUP BY` returns one row per group; a window function returns one value per input row, so every original row is retained.

</details>

<details><summary><b>65.</b> What does the `OVER ()` clause do?</summary>

It defines the window for the function; an empty `OVER ()` treats all rows as one partition, e.g. `SUM(nav) OVER ()` gives the grand total on every row.

</details>

<details><summary><b>66.</b> What does `PARTITION BY` do inside `OVER`?</summary>

It splits rows into groups; the window function restarts independently within each partition, e.g. running totals per fund.

</details>

<details><summary><b>67.</b> What does `ROW_NUMBER() OVER (ORDER BY nav DESC)` produce?</summary>

A unique sequential integer per row in the specified order (1, 2, 3, …), with no ties.

</details>

<details><summary><b>68.</b> How do you get the latest NAV row per fund using `ROW_NUMBER`?</summary>

`ROW_NUMBER() OVER (PARTITION BY fund_id ORDER BY nav_date DESC)` then filter the outer query to `WHERE rn = 1`.

</details>

<details><summary><b>69.</b> What is the difference between `RANK()` and `DENSE_RANK()`?</summary>

Both give ties the same rank; `RANK()` then skips numbers (1,1,3) while `DENSE_RANK()` does not (1,1,2).

</details>

<details><summary><b>70.</b> What does `LAG(nav) OVER (PARTITION BY fund_id ORDER BY nav_date)` return?</summary>

The previous day's NAV for the same fund; the first row of each partition has no predecessor, so it returns `NULL`.

</details>

<details><summary><b>71.</b> How do you compute the daily NAV change per fund using `LAG`?</summary>

`nav - LAG(nav) OVER (PARTITION BY fund_id ORDER BY nav_date)` gives the difference from the prior NAV in date order.

</details>

<details><summary><b>72.</b> What does `LEAD()` do compared to `LAG()`?</summary>

`LEAD()` looks forward to a following row, while `LAG()` looks back to a preceding row, both within the ordered window.

</details>

<details><summary><b>73.</b> How do you give `LAG`/`LEAD` a default for missing neighbours?</summary>

Pass the offset and default, e.g. `LAG(nav, 1, 0)` returns 0 instead of `NULL` when there is no prior row.

</details>

<details><summary><b>74.</b> Write a running total of subscriptions per fund over time.</summary>

`SUM(amount) OVER (PARTITION BY fund_id ORDER BY trade_date)` — adding `ORDER BY` turns the window into a cumulative (running) sum.

</details>

<details><summary><b>75.</b> Why does adding `ORDER BY` inside `OVER` change `SUM` from a total to a running total?</summary>

With `ORDER BY` the default frame becomes `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`, so it sums from the start up to the current row.

</details>

<details><summary><b>76.</b> What does the frame clause `ROWS BETWEEN 2 PRECEDING AND CURRENT ROW` do?</summary>

It defines a sliding window of the current row plus the two before it — useful for a 3-row moving average of NAV.

</details>

<details><summary><b>77.</b> Can you use a window function in a `WHERE` clause?</summary>

No; window functions are computed after `WHERE`, so you must wrap the query in a subquery/CTE and filter on the result (e.g. `WHERE rn = 1`).

</details>

<details><summary><b>78.</b> What does the `INSERT` statement do?</summary>

It adds new rows to a table.

</details>

<details><summary><b>79.</b> Write an `INSERT` adding one fund with id, name, and currency.</summary>

`INSERT INTO funds (fund_id, fund_name, currency) VALUES (1, 'EU Equity', 'EUR');` — name the columns then supply matching values.

</details>

<details><summary><b>80.</b> Why should you list column names explicitly in `INSERT`?</summary>

So the statement keeps working if columns are added or reordered, and so it is clear which value maps to which column.

</details>

<details><summary><b>81.</b> How do you copy rows from one table into another in a single statement?</summary>

`INSERT INTO archive (...) SELECT ... FROM source WHERE ...;` — the `SELECT` supplies the rows to insert.

</details>

<details><summary><b>82.</b> What does `UPDATE funds SET currency = 'EUR' WHERE fund_id = 1;` do?</summary>

It changes the `currency` to `EUR` for the single row whose `fund_id` is 1.

</details>

<details><summary><b>83.</b> What is the danger of `UPDATE funds SET currency = 'EUR';` with no `WHERE`?</summary>

It overwrites the currency of every row in the table, not just the intended one — a classic destructive mistake.

</details>

<details><summary><b>84.</b> What does `DELETE FROM holdings WHERE fund_id = 1;` do?</summary>

It removes only the holding rows belonging to fund 1.

</details>

<details><summary><b>85.</b> What happens with `DELETE FROM holdings;` (no `WHERE`)?</summary>

It deletes every row in the table; the table remains but is emptied.

</details>

<details><summary><b>86.</b> How can you preview which rows an `UPDATE`/`DELETE` will affect before running it?</summary>

Run the same `WHERE` clause inside a `SELECT` first (e.g. `SELECT * FROM funds WHERE ...`) to confirm the row set.

</details>

<details><summary><b>87.</b> What is a transaction and how do `COMMIT` and `ROLLBACK` relate?</summary>

A transaction groups statements into an all-or-nothing unit; `COMMIT` makes changes permanent and `ROLLBACK` undoes them since the transaction began.

</details>

<details><summary><b>88.</b> How can transactions protect you from a mistaken mass `UPDATE`?</summary>

Run inside `BEGIN`/`START TRANSACTION`, check the row count or results, and `ROLLBACK` if wrong instead of `COMMIT`.

</details>

<details><summary><b>89.</b> What does `UPSERT` (e.g. `INSERT ... ON CONFLICT DO UPDATE`) achieve for daily NAV loads?</summary>

It inserts a new NAV row or, if the key already exists, updates it instead — idempotent loading without duplicate-key errors.

</details>

<details><summary><b>90.</b> What is a database index, in one sentence?</summary>

An auxiliary data structure (often a B-tree) that lets the engine locate rows by key quickly without scanning the whole table.

</details>

<details><summary><b>91.</b> Which operations does an index typically speed up?</summary>

Lookups and range scans in `WHERE`, join matching on the indexed column, and sometimes `ORDER BY`/`GROUP BY` by avoiding a sort.

</details>

<details><summary><b>92.</b> What is the main cost of adding an index?</summary>

Extra storage and slower writes (`INSERT`/`UPDATE`/`DELETE`), because the index must be maintained on every data change.

</details>

<details><summary><b>93.</b> Why does a primary key usually come with an index automatically?</summary>

The database needs to enforce uniqueness efficiently, so it builds a unique index on the primary-key column(s).

</details>

<details><summary><b>94.</b> Why does `WHERE UPPER(isin) = 'LU123'` often fail to use an index on `isin`?</summary>

Wrapping the column in a function prevents the engine from matching it to the plain-column index, forcing a full scan unless a matching function/expression index exists.

</details>

<details><summary><b>95.</b> For a query filtering `fund_id` and ordering by `nav_date`, what kind of index helps most?</summary>

A composite index on `(fund_id, nav_date)`, so the engine can seek by fund and read rows already in date order.

</details>

<details><summary><b>96.</b> How do you check whether a query actually uses an index?</summary>

Run `EXPLAIN` (or `EXPLAIN ANALYZE`) and look for an index scan/seek versus a sequential/full table scan in the plan.

</details>

<details><summary><b>97.</b> What is `information_schema`?</summary>

A standard set of read-only views describing the database's own metadata — its tables, columns, data types, constraints, and more.

</details>

<details><summary><b>98.</b> How do you list all columns and their data types for a `funds` table via `information_schema`?</summary>

`SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'funds';`.

</details>

<details><summary><b>99.</b> How would you find every table in the database using `information_schema`?</summary>

`SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';` (adjust the schema filter to your database).

</details>

<details><summary><b>100.</b> An EMT file load fails because a column is missing — how can `information_schema` help diagnose it fast?</summary>

Query `information_schema.columns` for the target table to confirm the exact column names, types, and nullability before re-checking the file mapping.

</details>


## Phase 0 · 0.4 Git & GitHub (version control from zero) — 100 self-test questions

<details><summary><b>1.</b> What is version control, in one sentence?</summary>

A system that records changes to files over time so you can recall specific versions later, see who changed what, and collaborate without overwriting each other's work.

</details>

<details><summary><b>2.</b> What is Git?</summary>

A distributed version control system that tracks file changes as a series of snapshots (commits), where every clone contains the full history rather than depending on a central server.

</details>

<details><summary><b>3.</b> What is the difference between Git and GitHub?</summary>

Git is the version control tool that runs locally on your machine; GitHub is a web service that hosts Git repositories remotely and adds collaboration features like pull requests, issues, and access control.

</details>

<details><summary><b>4.</b> What are Git's "three states" a file can be in?</summary>

Modified (changed but not staged), staged/indexed (marked to go into the next commit), and committed (safely stored in the local history/database).

</details>

<details><summary><b>5.</b> What are the three corresponding areas in a Git project?</summary>

The working tree (the files you edit), the staging area/index (the snapshot you're preparing), and the `.git` directory (the repository where committed history lives).

</details>

<details><summary><b>6.</b> What is the working tree?</summary>

The directory of actual files you can see and edit on disk — a single checked-out version of the project that Git compares against the index and history.

</details>

<details><summary><b>7.</b> What is the staging area (index)?</summary>

An intermediate area that holds the exact set of changes you've selected for the next commit, letting you craft a commit from a subset of your working-tree changes.

</details>

<details><summary><b>8.</b> What does `git init` do?</summary>

It creates a new, empty Git repository in the current directory by making a `.git` subfolder, after which Git starts tracking changes there.

</details>

<details><summary><b>9.</b> What does `git clone <url>` do?</summary>

It downloads a full copy of an existing remote repository, including all history and branches, and sets up a remote named `origin` pointing back to the source.

</details>

<details><summary><b>10.</b> What does `git status` show?</summary>

Which branch you're on, which files are staged, which are modified but unstaged, which are untracked, and whether your branch is ahead of or behind its remote.

</details>

<details><summary><b>11.</b> How do you stage a single file called `nav_loader.py`?</summary>

Run `git add nav_loader.py`, which copies that file's current content into the staging area for the next commit.

</details>

<details><summary><b>12.</b> How do you stage all changes in the current directory and below?</summary>

Run `git add .` (or `git add -A` to also catch deletions across the whole repo) to stage everything modified, new, or removed.

</details>

<details><summary><b>13.</b> What does `git commit` do?</summary>

It permanently records the staged snapshot into the repository's history as a new commit, along with a message, author, and timestamp.

</details>

<details><summary><b>14.</b> What is `git commit -m "message"` for?</summary>

It commits the staged changes and supplies the commit message inline, avoiding the editor that would otherwise open.

</details>

<details><summary><b>15.</b> What does `git commit -a -m "message"` do, and what's the catch?</summary>

It stages and commits all tracked files that are modified in one step; the catch is it does NOT include new untracked files, which must still be added with `git add`.

</details>

<details><summary><b>16.</b> What makes a good commit message for a fund-data ETL repo?</summary>

A concise imperative summary line under ~50 characters (e.g. `Fix ISIN validation for null tickers`) optionally followed by a blank line and a body explaining the why.

</details>

<details><summary><b>17.</b> What is a commit hash (SHA)?</summary>

A 40-character SHA-1 (or SHA-256) checksum that uniquely identifies a commit based on its content, parent, author, and message; you can usually abbreviate it to the first 7 characters.

</details>

<details><summary><b>18.</b> What does `git log` do?</summary>

It lists the commit history of the current branch in reverse chronological order, showing each commit's hash, author, date, and message.

</details>

<details><summary><b>19.</b> How do you get a compact one-line-per-commit history?</summary>

Run `git log --oneline`, which shows the abbreviated hash and the first line of each commit message.

</details>

<details><summary><b>20.</b> What does `git log --oneline --graph --all` show?</summary>

A compact ASCII graph of all branches and their merge structure, useful for visualising how branches diverged and came back together.

</details>

<details><summary><b>21.</b> What does `git diff` (with no arguments) show?</summary>

The differences between your working tree and the staging area — i.e. the changes you have made but not yet staged.

</details>

<details><summary><b>22.</b> What does `git diff --staged` (or `--cached`) show?</summary>

The differences between the staging area and the last commit — i.e. exactly what will be recorded if you commit now.

</details>

<details><summary><b>23.</b> How do you see what changed in a specific commit?</summary>

Run `git show <commit-hash>`, which displays that commit's metadata and the diff it introduced.

</details>

<details><summary><b>24.</b> How do you compare two branches?</summary>

Run `git diff branchA..branchB` to see the changes that differ between them, or `git diff main` while on a feature branch.

</details>

<details><summary><b>25.</b> In a unified diff, what do lines starting with `+` and `-` mean?</summary>

`+` lines were added in the newer version and `-` lines were removed from the older version; context lines without a sign are unchanged.

</details>

<details><summary><b>26.</b> What is a branch in Git?</summary>

A lightweight, movable pointer to a specific commit; creating a branch just makes a new pointer, so it's cheap and fast.

</details>

<details><summary><b>27.</b> What is HEAD?</summary>

A pointer to the commit you currently have checked out, usually by pointing at the current branch, which in turn points at its latest commit.

</details>

<details><summary><b>28.</b> How do you create a new branch called `feature/emt-parser`?</summary>

Run `git branch feature/emt-parser` to create it, or `git switch -c feature/emt-parser` to create and switch to it in one step.

</details>

<details><summary><b>29.</b> What is the modern command to switch branches, and the older one?</summary>

The modern command is `git switch <branch>`; the older, multi-purpose command is `git checkout <branch>`.

</details>

<details><summary><b>30.</b> How do you list all local branches and see which one you're on?</summary>

Run `git branch`; the current branch is marked with an asterisk (`*`).

</details>

<details><summary><b>31.</b> How do you delete a fully merged local branch?</summary>

Run `git branch -d <branch>`; Git refuses if it isn't merged, in which case `git branch -D <branch>` force-deletes it.

</details>

<details><summary><b>32.</b> What does `git merge <branch>` do?</summary>

It integrates the changes from `<branch>` into your current branch, creating either a fast-forward or a new merge commit depending on the history.

</details>

<details><summary><b>33.</b> What is a fast-forward merge?</summary>

When the current branch has no new commits since the other branch diverged, Git simply moves the branch pointer forward to the other branch's tip — no new commit is created.

</details>

<details><summary><b>34.</b> When does Git create a merge commit instead of fast-forwarding?</summary>

When both branches have new commits since they diverged, Git must combine the two histories with a new commit that has two parents.

</details>

<details><summary><b>35.</b> How can you force a merge commit even when a fast-forward is possible?</summary>

Use `git merge --no-ff <branch>`, which always creates a merge commit to preserve the fact that a branch existed.

</details>

<details><summary><b>36.</b> What is a merge conflict?</summary>

A situation where the same lines (or a delete-vs-edit) changed differently on both branches, so Git can't automatically combine them and asks you to resolve it.

</details>

<details><summary><b>37.</b> What do the conflict markers `<<<<<<<`, `=======`, and `>>>>>>>` mean?</summary>

`<<<<<<<` to `=======` is your current branch's version (HEAD), `=======` to `>>>>>>>` is the incoming branch's version, and you edit the file to keep the correct result.

</details>

<details><summary><b>38.</b> How do you finish resolving a merge conflict?</summary>

Edit the files to the desired final content, remove all conflict markers, `git add` the resolved files, then run `git commit` to complete the merge.

</details>

<details><summary><b>39.</b> How do you abort a merge that has conflicts you don't want to resolve right now?</summary>

Run `git merge --abort`, which restores the branch to the state it was in before you started the merge.

</details>

<details><summary><b>40.</b> A merge conflict appears in `etl/load_nav.py` — what's the safe first step?</summary>

Run `git status` to list which files are conflicted, then open each one and look for the `<<<<<<<` markers to see both versions before deciding what to keep.

</details>

<details><summary><b>41.</b> What is a remote in Git?</summary>

A named reference to another copy of the repository, typically hosted elsewhere (like on GitHub), that you push to and pull from.

</details>

<details><summary><b>42.</b> What is `origin`?</summary>

The conventional default name Git gives to the remote you cloned from; it's just a name, not a special keyword.

</details>

<details><summary><b>43.</b> How do you list your configured remotes and their URLs?</summary>

Run `git remote -v`, which prints each remote name with its fetch and push URLs.

</details>

<details><summary><b>44.</b> What does `git push` do?</summary>

It uploads your local commits on the current branch to the corresponding branch on the remote, updating the remote's history.

</details>

<details><summary><b>45.</b> What does `git push -u origin main` do, and why the `-u`?</summary>

It pushes `main` to `origin` and the `-u` (`--set-upstream`) records the tracking relationship so future `git push`/`git pull` need no arguments.

</details>

<details><summary><b>46.</b> What does `git fetch` do?</summary>

It downloads new commits and branch updates from the remote into your local remote-tracking branches (like `origin/main`) without changing your working tree or local branches.

</details>

<details><summary><b>47.</b> What does `git pull` do, and how does it relate to fetch?</summary>

It runs `git fetch` followed by a merge (or rebase) of the upstream branch into your current branch — i.e. it downloads and integrates remote changes in one step.

</details>

<details><summary><b>48.</b> What is the difference between `git fetch` and `git pull` in terms of safety?</summary>

`git fetch` is non-destructive and just updates your view of the remote, letting you inspect before integrating; `git pull` immediately changes your working branch, which can cause unexpected merges.

</details>

<details><summary><b>49.</b> What is a remote-tracking branch like `origin/main`?</summary>

A local read-only pointer that records where the remote's `main` branch was the last time you fetched or pulled; it's how Git knows whether you're ahead or behind.

</details>

<details><summary><b>50.</b> Your `git push` is rejected as "non-fast-forward" — what does that mean and what do you do?</summary>

The remote has commits you don't have locally, so pushing would lose them; run `git pull` (fetch + integrate) to incorporate them, resolve any conflicts, then push again.

</details>

<details><summary><b>51.</b> What is `.gitignore`?</summary>

A file listing path patterns that Git should not track, used to keep generated files, secrets, and local clutter out of the repository.

</details>

<details><summary><b>52.</b> Give three things you'd typically put in `.gitignore` for a Python fund-data project.</summary>

Virtual environments and caches (`.venv/`, `__pycache__/`), secrets/config (`.env`, credentials), and large data or output files (`*.csv`, `data/raw/`).

</details>

<details><summary><b>53.</b> Why must credentials for the transfer-agency API never be committed?</summary>

Once committed they live in history forever and anyone with repo access (or a leaked clone) can read them; they must be ignored via `.gitignore` and stored in environment variables or a secrets manager.

</details>

<details><summary><b>54.</b> A file is already tracked but you just added it to `.gitignore` — why is it still showing changes?</summary>

`.gitignore` only affects untracked files; you must run `git rm --cached <file>` to stop tracking it, then commit, after which the ignore rule takes effect.

</details>

<details><summary><b>55.</b> What does a pattern like `data/raw/` (with trailing slash) match in `.gitignore`?</summary>

It matches the directory named `data/raw` and everything inside it, ignoring the whole folder's contents.

</details>

<details><summary><b>56.</b> What does `*.csv` in `.gitignore` do, and how do you keep one exception?</summary>

It ignores all files ending in `.csv`; to keep a specific one, add a negation line like `!schema_sample.csv` after it.

</details>

<details><summary><b>57.</b> What is GitHub Flow?</summary>

A lightweight workflow: create a branch off `main` for each change, commit to it, open a pull request, get review/CI, then merge to `main` and deploy — keeping `main` always deployable.

</details>

<details><summary><b>58.</b> What is a pull request (PR)?</summary>

A GitHub feature that proposes merging one branch into another, providing a place for discussion, code review, automated checks, and a record of the change before it's merged.

</details>

<details><summary><b>59.</b> What is the typical lifecycle of a PR?</summary>

Push a feature branch, open a PR against `main`, address review comments and failing checks with new commits, get an approval, then merge and delete the branch.

</details>

<details><summary><b>60.</b> What are the common PR merge strategies on GitHub?</summary>

"Create a merge commit" (preserves all commits plus a merge commit), "squash and merge" (combines the branch into one commit), and "rebase and merge" (replays commits onto `main` with no merge commit).

</details>

<details><summary><b>61.</b> Why is squash-and-merge popular for feature branches?</summary>

It collapses messy work-in-progress commits into a single, clean commit on `main`, keeping the main history readable while preserving the full detail in the PR.

</details>

<details><summary><b>62.</b> What is a "draft" pull request used for?</summary>

To open a PR early for visibility or to run CI while signalling it isn't ready for review or merge yet.

</details>

<details><summary><b>63.</b> What is a fork on GitHub?</summary>

Your own server-side copy of someone else's repository, which lets you push changes and open pull requests back to the original when you lack write access.

</details>

<details><summary><b>64.</b> What is the difference between `git restore` and `git revert`?</summary>

`git restore` discards changes in the working tree or unstages files (it doesn't make a commit); `git revert` creates a new commit that undoes a previous commit, preserving history.

</details>

<details><summary><b>65.</b> How do you discard unstaged changes to a single file `report.sql`?</summary>

Run `git restore report.sql`, which overwrites it with the version from the index (or last commit), losing your unsaved edits to it.

</details>

<details><summary><b>66.</b> How do you unstage a file you accidentally `git add`-ed?</summary>

Run `git restore --staged <file>` (or the older `git reset HEAD <file>`), which removes it from the index but keeps your working-tree changes.

</details>

<details><summary><b>67.</b> What does `git revert <commit>` do?</summary>

It creates a brand-new commit that applies the inverse of the specified commit, undoing its effect while leaving the original commit in history.

</details>

<details><summary><b>68.</b> Why is `git revert` the safe way to undo a commit that's already pushed/shared?</summary>

Because it adds a new commit rather than rewriting history, so collaborators' clones stay consistent and nobody's work is dropped underneath them.

</details>

<details><summary><b>69.</b> What are the three modes of `git reset`?</summary>

`--soft` moves the branch pointer but keeps changes staged; `--mixed` (default) moves the pointer and unstages changes but keeps them in the working tree; `--hard` moves the pointer and discards all changes.

</details>

<details><summary><b>70.</b> What does `git reset --hard HEAD~1` do, and why is it dangerous?</summary>

It moves the current branch back one commit and discards that commit's changes from the index and working tree; it's dangerous because uncommitted work is permanently lost and it rewrites history.

</details>

<details><summary><b>71.</b> What does `HEAD~1` (or `HEAD~3`) mean?</summary>

`HEAD~1` is the commit one step before HEAD (its parent), and `HEAD~3` is three commits back along the first-parent line.

</details>

<details><summary><b>72.</b> Why should you never `git reset` (rewrite) commits that others have already pulled?</summary>

Rewriting shared history changes commit hashes, so collaborators' branches diverge and pulling becomes a tangle of conflicts and duplicated commits; use `git revert` instead.

</details>

<details><summary><b>73.</b> What is `git push --force` and when is it risky?</summary>

It overwrites the remote branch with your local version, discarding remote commits; it's risky on shared branches because it can erase teammates' pushed work.

</details>

<details><summary><b>74.</b> What safer alternative to `--force` should you prefer?</summary>

`git push --force-with-lease`, which refuses to overwrite if the remote has commits you haven't seen, protecting against clobbering someone else's recent push.

</details>

<details><summary><b>75.</b> What is `git reflog` and why is it a lifesaver?</summary>

It logs where HEAD and branch tips have pointed recently, including "lost" commits after a bad reset, so you can recover them with `git reset` or `git checkout` to the recorded hash.

</details>

<details><summary><b>76.</b> You ran `git reset --hard` and lost a commit — how do you try to recover it?</summary>

Run `git reflog` to find the commit's hash from before the reset, then `git checkout <hash>` or `git reset --hard <hash>` (or branch from it) to restore it.

</details>

<details><summary><b>77.</b> What is `git stash`?</summary>

A command that shelves your uncommitted working-tree and staged changes onto a stack and reverts your tree to a clean state, so you can switch tasks without committing.

</details>

<details><summary><b>78.</b> How do you get stashed changes back?</summary>

Run `git stash pop` to reapply the most recent stash and remove it from the stack, or `git stash apply` to reapply without removing it.

</details>

<details><summary><b>79.</b> What does `git rm <file>` do versus deleting the file in your file manager?</summary>

`git rm` removes the file from disk and stages the deletion in one step; deleting it manually only changes the working tree and still requires `git add`/`git rm` to stage the removal.

</details>

<details><summary><b>80.</b> What is the difference between a tracked, untracked, and ignored file?</summary>

A tracked file is one Git already knows about from a prior commit or staging; untracked is a new file Git sees but isn't tracking; ignored is an untracked file matched by `.gitignore` so Git hides it.

</details>

<details><summary><b>81.</b> How do you tell Git your name and email for commit authorship?</summary>

Run `git config --global user.name "Your Name"` and `git config --global user.email "you@example.com"`; the `--global` flag applies it to all your repos.

</details>

<details><summary><b>82.</b> What's the difference between `--global`, `--local`, and `--system` config?</summary>

`--system` applies to all users on the machine, `--global` to all repos for your user, and `--local` (the default) only to the current repository, with local overriding global overriding system.

</details>

<details><summary><b>83.</b> What is a detached HEAD state?</summary>

When HEAD points directly at a commit instead of a branch (e.g. after `git checkout <hash>`); new commits there belong to no branch and can be lost unless you create one.

</details>

<details><summary><b>84.</b> How do you save work made in a detached HEAD?</summary>

Create a branch at the current position with `git switch -c <new-branch>` (or `git branch <name>`) before switching away, so the commits are anchored.

</details>

<details><summary><b>85.</b> What does `git log --oneline origin/main..main` tell you?</summary>

It lists the commits you have on local `main` that haven't been pushed to `origin/main` yet — i.e. what a push would upload.

</details>

<details><summary><b>86.</b> What does "your branch is ahead of 'origin/main' by 2 commits" mean?</summary>

You have made 2 local commits that aren't on the remote yet; running `git push` will send them.

</details>

<details><summary><b>87.</b> What does "your branch is behind 'origin/main' by 3 commits" mean?</summary>

The remote has 3 commits you don't have locally; running `git pull` will bring them in.

</details>

<details><summary><b>88.</b> What does "your branch and 'origin/main' have diverged" mean?</summary>

Both your local branch and the remote have commits the other lacks, so you'll need to merge or rebase to reconcile them before pushing.

</details>

<details><summary><b>89.</b> What is `git rebase` at a high level?</summary>

It replays your branch's commits on top of another base commit, producing a linear history as if you'd started your work from the newer base.

</details>

<details><summary><b>90.</b> Why prefer rebase over merge for keeping a feature branch up to date locally?</summary>

Rebase avoids extra merge commits and yields a clean, linear history; but it rewrites your branch's commits, so you shouldn't rebase commits that others have already based work on.

</details>

<details><summary><b>91.</b> What is the golden rule of rebasing?</summary>

Never rebase (or otherwise rewrite) commits that have been pushed to a shared branch others rely on; only rebase local, unshared commits.

</details>

<details><summary><b>92.</b> What is a tag in Git, and when would a fund-data team use one?</summary>

A tag is a named pointer to a specific commit, typically used to mark releases (e.g. `v2025.06` for the NAV pipeline version that went to production).

</details>

<details><summary><b>93.</b> What's the difference between a lightweight tag and an annotated tag?</summary>

A lightweight tag is just a name pointing at a commit; an annotated tag (`git tag -a v1.0 -m "..."`) is a full object with tagger, date, and message, and is preferred for releases.

</details>

<details><summary><b>94.</b> How do you create a repository on GitHub from existing local code?</summary>

Create an empty repo on GitHub, then run `git remote add origin <url>` locally and `git push -u origin main` to upload your existing history.

</details>

<details><summary><b>95.</b> What is the role of CI checks on a pull request?</summary>

Automated workflows (e.g. GitHub Actions) run tests, linters, and builds on the PR's commits so reviewers and authors see whether the change is safe before merging.

</details>

<details><summary><b>96.</b> What is a `CODEOWNERS` file?</summary>

A file that maps paths in the repo to people or teams who are automatically requested for review when those paths change in a PR.

</details>

<details><summary><b>97.</b> What does "protected branch" mean on GitHub?</summary>

A branch (often `main`) configured with rules such as required reviews, passing checks, and no force-pushes, to prevent unreviewed or destructive changes.

</details>

<details><summary><b>98.</b> A teammate force-pushed and rewrote `main`; your local `main` won't pull cleanly — what's the recovery?</summary>

Use `git reflog`/`git fetch` to inspect, then reset your local branch to the new remote with `git reset --hard origin/main` after backing up any local-only commits to a separate branch.

</details>

<details><summary><b>99.</b> Why commit early and often in small, logical units?</summary>

Small commits make history easy to read, reviews easier, reverts surgical, and conflicts smaller — far better than one giant commit mixing the EMT parser, NAV loader, and config edits.

</details>

<details><summary><b>100.</b> What's the first thing to check if `git push` asks repeatedly for a password or fails to authenticate?</summary>

Verify your remote URL and credentials — GitHub no longer accepts account passwords over HTTPS, so use a personal access token or set up SSH keys, and confirm `git remote -v` points to the right place.

</details>


## Phase 0 · 0.5 Docker & containers from zero — 100 self-test questions

<details><summary><b>1.</b> In one sentence, what is a container?</summary>

A container is an isolated process running on the host kernel with its own filesystem, network, and process namespace, packaged from an image so it runs the same way anywhere Docker runs.

</details>

<details><summary><b>2.</b> What is a Docker image?</summary>

An image is a read-only, layered template (a filesystem snapshot plus metadata like the default command) from which containers are created; it is the build artifact, not the running thing.

</details>

<details><summary><b>3.</b> What is the core difference between an image and a container?</summary>

An image is a static, read-only template stored on disk; a container is a running (or stopped) instance of that image with a thin writable layer on top.

</details>

<details><summary><b>4.</b> Why can you run many containers from a single image at the same time?</summary>

Each container gets its own writable layer and isolated namespaces while sharing the image's read-only layers, so they are independent processes that do not collide.

</details>

<details><summary><b>5.</b> What command lists running containers, and what flag also shows stopped ones?</summary>

`docker ps` lists running containers; `docker ps -a` lists all containers including stopped/exited ones.

</details>

<details><summary><b>6.</b> What does an image tag like `python:3.12-slim` mean?</summary>

`python` is the repository name and `3.12-slim` is the tag identifying a specific variant/version; if you omit the tag Docker defaults to `latest`.

</details>

<details><summary><b>7.</b> Why is relying on the `latest` tag risky in a fund-data pipeline?</summary>

`latest` is a moving pointer, so a rebuild can silently pull a different version and break reproducibility; pin an explicit tag or digest so a NAV-calculation image is deterministic.

</details>

<details><summary><b>8.</b> What is an image digest and why prefer it for reproducibility?</summary>

A digest is a content-addressable SHA256 hash (e.g. `image@sha256:...`) that always points to the exact same bytes, so pinning by digest guarantees the identical image regardless of tag movement.

</details>

<details><summary><b>9.</b> What does `docker run` do at a high level?</summary>

It creates a new container from an image and starts it, optionally pulling the image first if it is not present locally.

</details>

<details><summary><b>10.</b> What are image layers?</summary>

Layers are stacked, read-only filesystem diffs; each Dockerfile instruction that changes the filesystem typically creates one layer, and the final image is the union of all layers.

</details>

<details><summary><b>11.</b> What is the build cache?</summary>

During `docker build`, Docker reuses the result of a previous identical instruction (same instruction plus same inputs) instead of re-executing it, which makes rebuilds fast.

</details>

<details><summary><b>12.</b> When does a layer's build cache get invalidated?</summary>

When the instruction text changes or its inputs change (e.g. a `COPY`ed file's contents differ); once a layer is invalidated, every layer after it is rebuilt too.

</details>

<details><summary><b>13.</b> Why should you `COPY` your dependency manifest and install deps before copying the rest of the source?</summary>

So that editing application code does not invalidate the dependency-install layer; the expensive install stays cached and only the cheap code-copy layer rebuilds.

</details>

<details><summary><b>14.</b> In a Python project, what is the cache-friendly order for installing requirements?</summary>

`COPY requirements.txt .` then `RUN pip install -r requirements.txt`, and only afterwards `COPY . .`, so source edits do not bust the install cache.

</details>

<details><summary><b>15.</b> What does the port flag `-p 8080:80` mean?</summary>

It publishes container port `80` to host port `8080`; the format is `-p HOST:CONTAINER`, so traffic to `localhost:8080` reaches the service on `80` inside the container.

</details>

<details><summary><b>16.</b> If you run `-p 5432:5432` for Postgres but get "port is already allocated", what is the first thing to check?</summary>

Whether something else (often a locally installed Postgres or another container) already binds host port `5432`; either stop it or map a different host port like `-p 5433:5432`.

</details>

<details><summary><b>17.</b> How do you load many environment variables from a file at run time?</summary>

With `--env-file path/to/.env`, which reads `KEY=VALUE` lines and injects them into the container's environment.

</details>

<details><summary><b>18.</b> Why pass secrets like a transfer-agency DB password via env vars or secrets rather than baking them into the image?</summary>

Anything baked into an image is stored in a layer and visible via `docker history`, so credentials in the image leak to anyone who can pull it; runtime env/secrets keep them out of the artifact.

</details>

<details><summary><b>19.</b> What is a bind mount?</summary>

A bind mount maps a specific host directory or file into a container path, so the container sees and edits the live host files directly.

</details>

<details><summary><b>20.</b> What is a named volume?</summary>

A named volume is Docker-managed storage with a name (e.g. `pgdata`) that persists independently of any container and lives under Docker's storage area, not a host path you pick.

</details>

<details><summary><b>21.</b> What is the key practical difference between a bind mount and a named volume?</summary>

A bind mount points at an exact host path you control (great for live source code), while a named volume is managed by Docker and portable (great for persistent data like a database).

</details>

<details><summary><b>22.</b> Which mount type would you use to persist a Postgres data directory, and why?</summary>

A named volume (e.g. `-v pgdata:/var/lib/postgresql/data`) because it is Docker-managed, survives container removal, and avoids host-path permission and portability issues.

</details>

<details><summary><b>23.</b> Which mount type would you use to live-edit a NAV-loading script during development?</summary>

A bind mount of your source directory (e.g. `-v ${PWD}:/app`) so edits on the host are immediately visible inside the container without rebuilding.

</details>

<details><summary><b>24.</b> On Windows PowerShell, how do you bind-mount the current directory into `/app`?</summary>

Use `-v ${PWD}:/app` in PowerShell (or `-v "$(pwd):/app"` in bash); `${PWD}` expands to the current path.

</details>

<details><summary><b>25.</b> What happens to data written inside a container's writable layer (not a volume) when the container is removed?</summary>

It is destroyed with the container; only data in a volume or bind mount survives container removal.

</details>

<details><summary><b>26.</b> What is a Dockerfile?</summary>

A Dockerfile is a text file of instructions that `docker build` executes top-to-bottom to assemble an image layer by layer.

</details>

<details><summary><b>27.</b> What does the `FROM` instruction do?</summary>

It sets the base image the build starts from (e.g. `FROM python:3.12-slim`) and must usually be the first instruction.

</details>

<details><summary><b>28.</b> Why might you choose a `-slim` or `alpine` base image?</summary>

To get a smaller image with fewer packages, reducing size, attack surface, and pull time; `alpine` is smallest but uses musl libc which can cause compatibility issues for some Python wheels.

</details>

<details><summary><b>29.</b> What is the build context?</summary>

The build context is the set of files sent to the Docker daemon for the build, normally the directory passed to `docker build` (e.g. `.`); `COPY`/`ADD` can only use files inside it.

</details>

<details><summary><b>30.</b> What is a `.dockerignore` file and why does it matter?</summary>

It lists patterns to exclude from the build context (e.g. `.git`, `__pycache__`, `data/`), which shrinks the context, speeds builds, and avoids copying secrets or huge data files.

</details>

<details><summary><b>31.</b> What is the difference between `RUN` and `CMD`?</summary>

`RUN` executes at build time to construct the image; `CMD` specifies the default command that runs when a container starts from the image.

</details>

<details><summary><b>32.</b> What does the `CMD` instruction do, and how do you override it at run time?</summary>

`CMD` sets the default command for containers started from the image; you override it by appending a command after the image name, e.g. `docker run myimage python other.py`.

</details>

<details><summary><b>33.</b> What is the difference between `CMD` and `ENTRYPOINT`?</summary>

`ENTRYPOINT` defines the fixed executable that always runs; `CMD` provides default arguments to it; with both set, `docker run` arguments replace `CMD` but keep `ENTRYPOINT`.

</details>

<details><summary><b>34.</b> What does the `ENV` instruction do?</summary>

It sets environment variables baked into the image, available at build time for later instructions and at run time inside containers, unless overridden by `-e`.

</details>

<details><summary><b>35.</b> What is the difference between `ENV` in a Dockerfile and `-e` at run time?</summary>

`ENV` sets a default value persisted in the image; `-e` (or `--env-file`) overrides or supplements it for a specific container run without changing the image.

</details>

<details><summary><b>36.</b> What is the difference between exec form and shell form for `CMD`/`RUN`?</summary>

Exec form is a JSON array like `["python", "app.py"]` and runs the binary directly (no shell); shell form like `python app.py` runs via `/bin/sh -c`, enabling shell features but adding a shell process and affecting signal handling.

</details>

<details><summary><b>37.</b> Why is exec-form `CMD` preferred for the main process?</summary>

Because the process runs as PID 1 directly and receives signals like `SIGTERM`, allowing graceful shutdown, whereas shell form wraps it in `sh -c` which can swallow signals.

</details>

<details><summary><b>38.</b> How do you build an image and tag it?</summary>

`docker build -t myimage:1.0 .` builds from the Dockerfile in the current directory (the context `.`) and tags the result `myimage:1.0`.

</details>

<details><summary><b>39.</b> What is a multi-stage build and why use it?</summary>

It uses multiple `FROM` stages so you can build/compile in a heavy stage and `COPY --from=builder` only the artifacts into a slim final image, drastically reducing final image size.

</details>

<details><summary><b>40.</b> Why combine related commands in a single `RUN` with `&&`?</summary>

Each `RUN` creates a layer, so combining them (and cleaning caches in the same `RUN`) reduces layer count and image size, since deleting files in a later layer does not shrink earlier ones.

</details>

<details><summary><b>41.</b> What is Docker Compose?</summary>

Docker Compose is a tool that defines and runs multi-container applications declaratively from a `compose.yaml` file, so one command can start a whole stack.

</details>

<details><summary><b>42.</b> What command starts a Compose stack, and how do you run it in the background?</summary>

`docker compose up` starts it in the foreground; add `-d` (`docker compose up -d`) to run detached.

</details>

<details><summary><b>43.</b> What does `docker compose down` do, and how do you also delete volumes?</summary>

It stops and removes the project's containers and networks; add `-v` (`docker compose down -v`) to also delete named volumes declared in the file.

</details>

<details><summary><b>44.</b> How do containers in the same Compose project reach each other?</summary>

Compose puts them on a shared default network and they resolve each other by service name as a hostname (e.g. the app connects to `db:5432`).

</details>

<details><summary><b>45.</b> In Compose, what hostname would an app use to reach a service named `postgres` on port `5432`?</summary>

`postgres:5432` — the service name resolves via Docker's internal DNS on the project network, with no host port mapping required.

</details>

<details><summary><b>46.</b> What does `depends_on` do in Compose?</summary>

It controls startup order so a service starts after the ones it lists, but by default it only waits for the container to start, not for the app inside to be ready.

</details>

<details><summary><b>47.</b> Why is plain `depends_on` insufficient to guarantee a database is ready?</summary>

Because it only waits until the dependency's container has started, not until the database accepts connections; you need a `healthcheck` plus `depends_on: condition: service_healthy` for true readiness.

</details>

<details><summary><b>48.</b> How do you make `depends_on` wait until a dependency is actually healthy?</summary>

Use the long form `depends_on: { db: { condition: service_healthy } }` combined with a `healthcheck` on the `db` service.

</details>

<details><summary><b>49.</b> What is a healthcheck in Compose/Docker?</summary>

A periodic command run inside the container to decide if the service is healthy; its exit code (0 = healthy) sets the container's health status shown in `docker ps`.

</details>

<details><summary><b>50.</b> What does a Postgres healthcheck typically use?</summary>

A command like `pg_isready -U postgres` with `interval`, `timeout`, `retries`, and often `start_period`, so the container is marked healthy only once Postgres accepts connections.

</details>

<details><summary><b>51.</b> What do `interval`, `timeout`, `retries`, and `start_period` mean in a healthcheck?</summary>

`interval` is time between checks, `timeout` is how long each check may run, `retries` is consecutive failures before marking unhealthy, and `start_period` is an initial grace window where failures do not count.

</details>

<details><summary><b>52.</b> How do you define a named volume in a Compose file?</summary>

List it under a top-level `volumes:` key (e.g. `volumes: { pgdata: {} }`) and reference it in a service with `volumes: ["pgdata:/var/lib/postgresql/data"]`.

</details>

<details><summary><b>53.</b> What is the difference between `ports:` and `expose:` in Compose?</summary>

`ports:` publishes to the host (`HOST:CONTAINER`), while `expose:` only makes the port reachable to other services on the network without binding it on the host.

</details>

<details><summary><b>54.</b> How do you tell a Compose service to build from a Dockerfile instead of pulling an image?</summary>

Use `build:` (e.g. `build: .` or `build: { context: ., dockerfile: Dockerfile.dev }`) instead of, or alongside, an `image:` name.

</details>

<details><summary><b>55.</b> After changing the Dockerfile, why might `docker compose up` not reflect changes?</summary>

Because Compose reuses the existing image unless you rebuild; run `docker compose up --build` (or `docker compose build`) to force a rebuild.

</details>

<details><summary><b>56.</b> What does `docker logs <container>` show?</summary>

It shows whatever the container's main process wrote to STDOUT and STDERR, the primary way to see application output and errors.

</details>

<details><summary><b>57.</b> Why should a containerized app log to STDOUT/STDERR instead of a file?</summary>

Because Docker captures STDOUT/STDERR for `docker logs` and log drivers; writing to a file inside the container hides logs and can fill the writable layer.

</details>

<details><summary><b>58.</b> Why might `docker exec -it <container> bash` fail with "executable file not found"?</summary>

Because minimal images (like `slim`/`alpine`) may not include `bash`; try `sh` instead: `docker exec -it <container> sh`.

</details>

<details><summary><b>59.</b> Your container keeps showing status `Exited (0)` immediately — what does that mean?</summary>

The main process finished successfully and nothing kept PID 1 alive; a container only runs as long as its foreground process does, so a script that completes will exit cleanly.

</details>

<details><summary><b>60.</b> A container shows `Exited (1)` — how do you investigate?</summary>

Run `docker logs <container>` to read the error output; exit code 1 indicates the main process errored, and the logs usually show the traceback or message.

</details>

<details><summary><b>61.</b> A container shows `Exited (137)` — what does that usually indicate?</summary>

Exit code 137 means the process received `SIGKILL` (128 + 9), commonly the OOM killer terminating it for exceeding its memory limit, or a forced `docker kill`.

</details>

<details><summary><b>62.</b> Why can't you `docker exec` into an exited container?</summary>

`docker exec` needs a running process to attach to; an exited container has no running PID 1, so inspect it with `docker logs`, `docker inspect`, or restart/recreate it.

</details>

<details><summary><b>63.</b> What is the difference between `docker stop` and `docker kill`?</summary>

`docker stop` sends `SIGTERM` then `SIGKILL` after a grace period (default 10s) for a graceful shutdown; `docker kill` sends `SIGKILL` immediately.

</details>

<details><summary><b>64.</b> What does `docker system df` show?</summary>

It reports disk usage broken down by images, containers, local volumes, and build cache, including how much is reclaimable.

</details>

<details><summary><b>65.</b> What does `docker system prune` remove by default?</summary>

It removes stopped containers, unused networks, dangling images, and (in recent versions) build cache, but not named volumes unless you add `--volumes`.

</details>

<details><summary><b>66.</b> What is the danger of `docker system prune -a --volumes`?</summary>

`-a` also deletes all images not used by a running container, and `--volumes` deletes unused named volumes — including persistent data like a Postgres volume — so it can wipe important data.

</details>

<details><summary><b>67.</b> After many rebuilds your disk is full of `<none>` images and old cache — what cleanup sequence is reasonable?</summary>

Run `docker system df` to see usage, then `docker image prune`, `docker builder prune`, and `docker container prune`, reserving `-a`/`--volumes` for when you are sure nothing needed will be lost.

</details>

<details><summary><b>68.</b> Your bind-mounted code changes are not appearing in the container — first thing to check?</summary>

Verify the mount path is correct and actually applied (`docker inspect` mounts), that you mounted over the right container directory, and on Windows/WSL that file sharing for that drive is enabled.

</details>

<details><summary><b>69.</b> A Python app in a container can't find a package you installed — common cause?</summary>

The image was not rebuilt after editing `requirements.txt`/`Dockerfile`, so the old layer without the package is still in use; rebuild with `docker compose up --build` or `docker build`.

</details>

<details><summary><b>70.</b> Your app can't connect to the database using `localhost` inside the container — why?</summary>

Inside a container `localhost` refers to that container itself, not the host or another container; use the database service/container name (e.g. `db`) on the Docker network instead.

</details>

<details><summary><b>71.</b> From inside a container, how do you reach a service running on the host machine?</summary>

Use the special DNS name `host.docker.internal` (supported on Docker Desktop for Windows/Mac and configurable on Linux) to reach host-bound services.

</details>

<details><summary><b>72.</b> A Compose `web` service starts before `db` is ready and crashes on connect — robust fix?</summary>

Add a `healthcheck` to `db` and make `web` use `depends_on: { db: { condition: service_healthy } }`, and ideally have the app retry the connection on startup.

</details>

<details><summary><b>73.</b> You changed a `.env` value but the container still uses the old value — why?</summary>

Environment variables are read at container creation; you must recreate the container (`docker compose up -d` recreates, or `docker run` again), since `docker restart` alone keeps the old environment.

</details>

<details><summary><b>74.</b> A pulled image is `linux/amd64` but won't run well on your Apple Silicon Mac — what is happening?</summary>

An architecture mismatch; the image runs under emulation (slow) or fails, so prefer multi-arch images or build/pull for your platform with `--platform linux/arm64` as appropriate.

</details>

<details><summary><b>75.</b> How would you containerize a daily NAV-loading Python job that reads EMT files from a host folder and writes to Postgres?</summary>

Build an image with the script and deps, run Postgres in a service with a named volume for data, bind-mount the EMT input folder read-only into the job container, and pass DB credentials via env/secrets.

</details>

<details><summary><b>76.</b> For that NAV job, why mount the EMT input folder as read-only?</summary>

To guarantee the pipeline can read source EMT files but cannot accidentally modify or delete the authoritative inputs, protecting data integrity during the load.

</details>

<details><summary><b>77.</b> Why run a one-off ISIN-validation script with `docker run --rm`?</summary>

So the container is automatically cleaned up after the script finishes, avoiding a pile of exited containers from repeated ad-hoc runs.

</details>

<details><summary><b>78.</b> A transfer-agency batch container is OOM-killed (`Exited 137`) at month-end volumes — what do you adjust?</summary>

Increase the container/Compose memory limit (e.g. `mem_limit` or `deploy.resources`), and/or optimize the job to stream/batch records instead of loading everything into memory at once.

</details>

<details><summary><b>79.</b> Why keep the Postgres data on a named volume rather than the writable layer in a fund-data stack?</summary>

So the NAV/holdings data survives container recreation, upgrades, and `docker compose down`, since the writable layer is destroyed on `docker rm` but the named volume persists.

</details>

<details><summary><b>80.</b> How do you run database migrations as a separate step before the app starts in Compose?</summary>

Define a one-off `migrate` service (or command) that `depends_on` the healthy `db`, run it to completion (e.g. `docker compose run --rm migrate`), then start the app.

</details>

<details><summary><b>81.</b> What does `docker compose run` do differently from `docker compose up`?</summary>

`docker compose run` starts a one-off container for a single service with the command you give (good for migrations or a shell), instead of bringing up the whole defined stack.

</details>

<details><summary><b>82.</b> Why should you avoid running the container process as root when possible?</summary>

Running as root increases blast radius if the container is compromised and can create root-owned files on bind mounts; use a `USER` instruction to drop to a non-root user.

</details>

<details><summary><b>83.</b> What is the difference between `ARG` and `ENV`?</summary>

`ARG` defines a build-time variable available only during `docker build` (passed with `--build-arg`); `ENV` sets a variable persisted into the image and present at run time.

</details>

<details><summary><b>84.</b> Why might `docker build` send a huge context and take long even for a small image?</summary>

Because the build context includes everything in the directory (e.g. a multi-GB `data/` folder) unless excluded; add a `.dockerignore` to keep large/irrelevant files out of the context.

</details>

<details><summary><b>85.</b> What does the `HEALTHCHECK` instruction in a Dockerfile do versus a Compose healthcheck?</summary>

`HEALTHCHECK` bakes a default health probe into the image; a Compose `healthcheck` overrides/defines it per service, and both set the container's reported health status.

</details>

<details><summary><b>86.</b> What does `docker history <image>` show and why is it useful?</summary>

It lists the layers of an image with the instruction that created each and its size, helping you spot bloated steps and accidentally embedded secrets or data.

</details>

<details><summary><b>87.</b> Why do containers start almost instantly compared to virtual machines?</summary>

Containers share the host kernel and just start a process with isolation, whereas a VM must boot a full guest OS and kernel, which is far heavier.

</details>

<details><summary><b>88.</b> How do containers differ from virtual machines in terms of isolation?</summary>

VMs virtualize hardware and run separate kernels via a hypervisor (stronger isolation, more overhead); containers share the host kernel using namespaces and cgroups (lighter, faster, weaker isolation).

</details>

<details><summary><b>89.</b> On Windows, what actually runs your Linux containers under Docker Desktop?</summary>

A lightweight Linux VM (typically via WSL 2) hosts the Docker engine and Linux kernel, since Linux containers need a Linux kernel that Windows does not natively provide.

</details>

<details><summary><b>90.</b> What is the recommended way to handle secrets in Compose beyond plain env vars?</summary>

Use Compose `secrets:` to mount secret files into containers (e.g. at `/run/secrets/...`) instead of putting them in environment variables or the image, reducing exposure.

</details>

<details><summary><b>91.</b> What does the `--no-cache` flag on `docker build` do, and when would you use it?</summary>

It rebuilds every layer ignoring the cache, useful when a cached `RUN` (e.g. `apt-get update`) fetched stale data or you suspect a poisoned cache.

</details>

<details><summary><b>92.</b> What is the typical pattern to keep apt-based images small in a single `RUN`?</summary>

`RUN apt-get update && apt-get install -y --no-install-recommends pkg && rm -rf /var/lib/apt/lists/*` so the package index cache is removed in the same layer.

</details>

<details><summary><b>93.</b> Why is it dangerous to bind-mount a host directory over a container path that the image expects to be populated?</summary>

A bind mount shadows whatever the image put at that path with the (possibly empty) host directory, so files baked into the image at that location disappear inside the container.

</details>

<details><summary><b>94.</b> What happens to a named volume the first time it is mounted into a fresh Postgres container?</summary>

If the volume is empty, Postgres initializes a new data directory into it; if it already has data, Postgres reuses it, which is why a stale volume can keep old credentials/schema.

</details>

<details><summary><b>95.</b> You changed `POSTGRES_PASSWORD` but the DB still rejects the new password — likely cause?</summary>

The password is only applied when the data directory is first initialized; an existing named volume keeps the original password, so reset it in-db or recreate with a fresh volume.

</details>

<details><summary><b>96.</b> How do you completely reset a Compose Postgres to re-run its init with new settings?</summary>

`docker compose down -v` to remove the data volume, then `docker compose up`, which forces a fresh database initialization (destroying existing data, so back up first).

</details>

<details><summary><b>97.</b> What is the difference between `docker rm` and `docker rmi`?</summary>

`docker rm` removes containers; `docker rmi` removes images — a common beginner mix-up.

</details>

<details><summary><b>98.</b> Why might `docker run myimage` exit immediately with no output even though the build succeeded?</summary>

The image likely has no long-running foreground process or its `CMD` finished instantly; check the `CMD`/`ENTRYPOINT` and run `docker logs` or run it with a shell to investigate.

</details>

<details><summary><b>99.</b> What is the single most useful first command when any container "doesn't work"?</summary>

`docker logs <container>` (or `docker compose logs <service>`), because the application's STDOUT/STDERR usually contains the exact error explaining the failure.

</details>

<details><summary><b>100.</b> Why keep images small for a fund-data deployment beyond just disk savings?</summary>

Smaller images pull and start faster, have a smaller attack surface (fewer packages/CVEs), and are easier to audit, which matters for regulated EU fund-data environments.

</details>


## Phase 0 · 0.6 Networking & how the web works — 100 self-test questions

<details><summary><b>1.</b> What is an IP address, in one sentence?</summary>

An IP address is a numeric label assigned to a network interface that identifies a host on a network so packets can be routed to it (e.g. `192.0.2.10` for IPv4).

</details>

<details><summary><b>2.</b> What is the difference between IPv4 and IPv6 addresses?</summary>

IPv4 uses 32-bit addresses written as four dotted decimals like `192.0.2.10`, while IPv6 uses 128-bit addresses written in hex groups like `2001:db8::1`, giving a vastly larger address space.

</details>

<details><summary><b>3.</b> What is a port number and why is it needed?</summary>

A port is a 16-bit number (0–65535) that identifies a specific service or socket on a host, so one IP address can run many services at once (e.g. web on `443`, SSH on `22`).

</details>

<details><summary><b>4.</b> What is the range of valid port numbers?</summary>

Ports range from `0` to `65535`; ports `0–1023` are the well-known/privileged ports, `1024–49151` are registered, and `49152–65535` are dynamic/ephemeral.

</details>

<details><summary><b>5.</b> Which port does HTTPS use by default, and which does plain HTTP use?</summary>

HTTPS defaults to port `443` and plain HTTP defaults to port `80`.

</details>

<details><summary><b>6.</b> What does "binding to a port" mean for a server?</summary>

It means the server process claims a specific port on an interface so the OS delivers incoming traffic for that port to it; only one process can bind a given IP/port/protocol at a time.

</details>

<details><summary><b>7.</b> Why might starting a server give "address already in use"?</summary>

Another process is already bound to that IP and port (or the port is in `TIME_WAIT`); you must stop the other process or choose a different port.

</details>

<details><summary><b>8.</b> What are the two main transport protocols on the internet?</summary>

TCP (Transmission Control Protocol) and UDP (User Datagram Protocol).

</details>

<details><summary><b>9.</b> What does TCP guarantee that UDP does not?</summary>

TCP provides a reliable, ordered, connection-oriented byte stream with retransmission, acknowledgements, and flow/congestion control; UDP is connectionless and offers none of those guarantees.

</details>

<details><summary><b>10.</b> When would you prefer UDP over TCP?</summary>

When low latency matters more than reliability and occasional loss is acceptable, such as live video/voice, DNS queries, or gaming.

</details>

<details><summary><b>11.</b> What are the three steps of the TCP three-way handshake?</summary>

The client sends `SYN`, the server replies `SYN-ACK`, and the client responds `ACK`; after that the connection is established.

</details>

<details><summary><b>12.</b> Is HTTP built on TCP or UDP (for HTTP/1.1 and HTTP/2)?</summary>

HTTP/1.1 and HTTP/2 run over TCP; HTTP/3 is the exception, running over QUIC which is built on UDP.

</details>

<details><summary><b>13.</b> What does "connection refused" usually mean?</summary>

The host was reachable and actively rejected the connection because nothing is listening on that port (or a firewall sent a reset), so you got an immediate rejection.

</details>

<details><summary><b>14.</b> What does a connection "timeout" usually mean?</summary>

No response came back at all within the allotted time, typically because packets are being silently dropped by a firewall, the host is down/unreachable, or the address is wrong.

</details>

<details><summary><b>15.</b> "Connection refused" vs "timeout" — which points to a firewall dropping packets?</summary>

A timeout points to silent dropping (often a firewall using DROP) or an unreachable host; "connection refused" means the host replied with an active rejection.

</details>

<details><summary><b>16.</b> Your script can't reach a NAV-publishing API and returns "connection refused" within milliseconds — what's the first thing to check?</summary>

That a service is actually listening on the target port (right port number, service running); a fast refusal means the host is reachable but nothing accepted the connection there.

</details>

<details><summary><b>17.</b> Your script hangs for 30 seconds then times out connecting to a transfer-agency endpoint — what's the likely cause?</summary>

Packets are being silently dropped — usually a firewall rule, a wrong/unroutable IP, or the host being down — rather than an active rejection.

</details>

<details><summary><b>18.</b> What is DNS, in one sentence?</summary>

DNS (Domain Name System) is the distributed system that translates human-readable domain names like `api.example.com` into IP addresses.

</details>

<details><summary><b>19.</b> What is a DNS resolver?</summary>

A resolver is the client-side service (often your ISP's or a public one like `8.8.8.8`) that takes a name query and does the recursive lookup work to return an answer.

</details>

<details><summary><b>20.</b> What is the role of the DNS root servers?</summary>

Root servers sit at the top of the DNS hierarchy and tell the resolver which TLD servers are authoritative for a given top-level domain like `.com` or `.lu`.

</details>

<details><summary><b>21.</b> What is a TLD server in DNS?</summary>

A TLD (top-level domain) server is authoritative for a domain suffix such as `.com`, `.org`, or `.lu`, and points the resolver to the authoritative name server for the specific domain.

</details>

<details><summary><b>22.</b> What is an authoritative name server?</summary>

It is the server that holds the actual DNS records for a domain and gives the definitive answer for names within that zone.

</details>

<details><summary><b>23.</b> Put the DNS resolution chain in order for `app.fund.lu`.</summary>

Resolver → root server (for `.lu`) → TLD server for `.lu` → authoritative server for `fund.lu` → returns the IP for `app.fund.lu`.

</details>

<details><summary><b>24.</b> What is a DNS recursive query vs an iterative query?</summary>

In a recursive query the resolver does all the work and returns a final answer to the client; in iterative queries each server returns a referral and the resolver chases the chain itself.

</details>

<details><summary><b>25.</b> What is DNS TTL?</summary>

TTL (time to live) is the number of seconds a DNS record may be cached before it must be looked up again.

</details>

<details><summary><b>26.</b> Why does DNS caching exist?</summary>

To reduce latency and load on the DNS hierarchy by reusing answers locally instead of walking the root/TLD/authoritative chain every time.

</details>

<details><summary><b>27.</b> You changed a DNS record but clients still hit the old IP — what's the likely reason?</summary>

The old record is still cached somewhere (resolver, OS, or browser cache) until its TTL expires; lowering TTL before a change reduces this window.

</details>

<details><summary><b>28.</b> What does an `A` record map?</summary>

An `A` record maps a hostname to an IPv4 address.

</details>

<details><summary><b>29.</b> What does an `AAAA` record map?</summary>

An `AAAA` record maps a hostname to an IPv6 address.

</details>

<details><summary><b>30.</b> What does a `CNAME` record do?</summary>

A `CNAME` is an alias that points one name to another canonical name, which is then resolved to find the IP.

</details>

<details><summary><b>31.</b> What is a `TXT` record commonly used for?</summary>

For arbitrary text data, often domain verification, SPF/DKIM email authentication, and similar policy entries.

</details>

<details><summary><b>32.</b> What does the command `nslookup api.example.com` or `dig api.example.com` do?</summary>

It queries DNS to resolve the name and shows the returned records (and `dig` shows TTL, the answering server, and query timing).

</details>

<details><summary><b>33.</b> Where is the local hosts file on Windows, and what is it for?</summary>

`C:\Windows\System32\drivers\etc\hosts`; it lets you statically map hostnames to IPs locally, overriding DNS for testing.

</details>

<details><summary><b>34.</b> What is HTTP, briefly?</summary>

HTTP (HyperText Transfer Protocol) is a stateless request/response protocol used by clients and servers to exchange resources over the web.

</details>

<details><summary><b>35.</b> Name the common HTTP methods and their typical meaning.</summary>

`GET` reads a resource, `POST` creates/submits data, `PUT` replaces a resource, `PATCH` partially updates it, and `DELETE` removes it.

</details>

<details><summary><b>36.</b> Which HTTP methods are considered "safe"?</summary>

Safe methods do not modify server state — primarily `GET` and `HEAD` (also `OPTIONS`).

</details>

<details><summary><b>37.</b> What does "idempotent" mean for an HTTP method, and which methods are idempotent?</summary>

Idempotent means repeating the same request has the same effect as making it once; `GET`, `PUT`, `DELETE`, and `HEAD` are idempotent, while `POST` generally is not.

</details>

<details><summary><b>38.</b> What does `HEAD` do compared to `GET`?</summary>

`HEAD` requests only the response headers without the body, useful for checking existence, size, or last-modified metadata cheaply.

</details>

<details><summary><b>39.</b> What does the `OPTIONS` method do?</summary>

It asks the server which methods/capabilities are allowed for a resource and is used in CORS preflight requests.

</details>

<details><summary><b>40.</b> What do HTTP status codes in the 2xx range mean?</summary>

Success — the request was received, understood, and processed (e.g. `200 OK`, `201 Created`, `204 No Content`).

</details>

<details><summary><b>41.</b> What does `201 Created` indicate?</summary>

The request succeeded and a new resource was created, typically with its location in the `Location` header.

</details>

<details><summary><b>42.</b> What does `204 No Content` indicate?</summary>

The request succeeded but there is no response body to return (common for successful `DELETE` or `PUT`).

</details>

<details><summary><b>43.</b> What do 3xx status codes mean?</summary>

Redirection — further action (usually following a `Location` header) is needed, e.g. `301 Moved Permanently` or `302 Found`.

</details>

<details><summary><b>44.</b> What is the difference between `301` and `302`?</summary>

`301 Moved Permanently` signals a permanent redirect that clients should cache/update bookmarks; `302 Found` is a temporary redirect.

</details>

<details><summary><b>45.</b> What do 4xx status codes mean?</summary>

Client errors — the request was malformed or not allowed (e.g. `400`, `401`, `403`, `404`, `429`).

</details>

<details><summary><b>46.</b> What is the difference between `401 Unauthorized` and `403 Forbidden`?</summary>

`401` means you are not authenticated (no/invalid credentials), while `403` means you are authenticated but not allowed to access that resource.

</details>

<details><summary><b>47.</b> What does `400 Bad Request` mean?</summary>

The server could not process the request due to a client error such as malformed syntax, invalid parameters, or a bad payload.

</details>

<details><summary><b>48.</b> What does `404 Not Found` mean?</summary>

The requested resource does not exist at that URL (or the server will not reveal that it does).

</details>

<details><summary><b>49.</b> What does `429 Too Many Requests` mean and how do you handle it?</summary>

You hit a rate limit; back off and retry later, ideally honoring the `Retry-After` header with exponential backoff.

</details>

<details><summary><b>50.</b> What do 5xx status codes mean?</summary>

Server errors — the server failed to fulfill a valid request (e.g. `500`, `502`, `503`, `504`).

</details>

<details><summary><b>51.</b> What is the difference between `502`, `503`, and `504`?</summary>

`502 Bad Gateway` means an upstream gave an invalid response, `503 Service Unavailable` means the server is overloaded or down, and `504 Gateway Timeout` means an upstream did not respond in time.

</details>

<details><summary><b>52.</b> A NAV-feed API intermittently returns `503` — is retrying reasonable?</summary>

Yes; `503` is typically transient, so retry with exponential backoff and respect any `Retry-After` header rather than hammering it.

</details>

<details><summary><b>53.</b> What is an HTTP header, generally?</summary>

A header is a key/value metadata field sent in the request or response that describes the message, the content, caching, authentication, or the connection.

</details>

<details><summary><b>54.</b> What does the `Content-Type` header specify?</summary>

It specifies the media type of the body, e.g. `application/json`, `text/csv`, or `application/xml`, so the receiver knows how to parse it.

</details>

<details><summary><b>55.</b> What does the `Accept` request header do?</summary>

It tells the server which response media types the client can handle, enabling content negotiation (e.g. `Accept: application/json`).

</details>

<details><summary><b>56.</b> What is the `Authorization` header used for?</summary>

To carry credentials, such as `Authorization: Bearer <token>` for tokens or `Authorization: Basic <base64>` for basic auth.

</details>

<details><summary><b>57.</b> What is the purpose of the `Cache-Control` header?</summary>

It defines caching rules for the response, such as `no-store`, `no-cache`, `max-age=3600`, or `private`/`public`.

</details>

<details><summary><b>58.</b> What is an `ETag` and how is it used?</summary>

An `ETag` is a version identifier for a resource; clients can send it back via `If-None-Match` so the server can reply `304 Not Modified` if nothing changed.

</details>

<details><summary><b>59.</b> What is the `Location` header used for?</summary>

It tells the client where to go next — the new URL in a redirect (3xx) or the URL of a newly created resource (`201`).

</details>

<details><summary><b>60.</b> What does the `Host` header do in an HTTP request?</summary>

It names the target virtual host, letting one server/IP serve multiple domains by selecting the right site from the requested hostname.

</details>

<details><summary><b>61.</b> What is REST, in one sentence?</summary>

REST (Representational State Transfer) is an architectural style for web APIs that models resources addressable by URLs and manipulated with standard HTTP methods.

</details>

<details><summary><b>62.</b> In REST, how do you typically read a single resource vs a collection?</summary>

Read a collection with `GET /funds` and a single resource with `GET /funds/{id}`.

</details>

<details><summary><b>63.</b> How would a RESTful API model "create a new fund record"?</summary>

`POST /funds` with the new record in the request body, returning `201 Created` and the new resource's URL.

</details>

<details><summary><b>64.</b> How would a RESTful API model "delete fund 42"?</summary>

`DELETE /funds/42`, typically returning `204 No Content` on success.

</details>

<details><summary><b>65.</b> What does it mean that REST is "stateless"?</summary>

Each request must carry all information needed to process it (e.g. auth token, parameters); the server does not rely on stored client session state between requests.

</details>

<details><summary><b>66.</b> What does a typical REST API return for malformed JSON in a `POST` body?</summary>

A `400 Bad Request` (sometimes `422 Unprocessable Entity`) indicating the payload could not be parsed or validated.

</details>

<details><summary><b>67.</b> Why are query parameters (e.g. `?date=2026-06-13&isin=LU0000000001`) useful in REST?</summary>

They filter, sort, or paginate a collection without changing the resource path, e.g. fetching NAVs for a given ISIN and date.

</details>

<details><summary><b>68.</b> What is TLS and what was it formerly called?</summary>

TLS (Transport Layer Security) is the protocol that encrypts and authenticates network connections; it is the successor to SSL.

</details>

<details><summary><b>69.</b> What three guarantees does TLS provide?</summary>

Confidentiality (encryption), integrity (tamper detection), and authentication of the server's identity (and optionally the client's).

</details>

<details><summary><b>70.</b> Does TLS by itself guarantee the server is "trustworthy" or just that it is who it claims?</summary>

It guarantees the server controls a certificate for that hostname issued by a trusted CA; it does not vouch for the operator's honesty or the data's correctness.

</details>

<details><summary><b>71.</b> What is a TLS/SSL certificate?</summary>

A digitally signed document binding a public key to a hostname (and identity), issued by a Certificate Authority so clients can verify the server.

</details>

<details><summary><b>72.</b> What is a Certificate Authority (CA)?</summary>

A trusted third party that verifies identity and issues signed certificates; operating systems and browsers ship with a list of trusted root CAs.

</details>

<details><summary><b>73.</b> What is the "chain of trust" in certificates?</summary>

A leaf certificate is signed by an intermediate CA, which is signed (transitively) by a trusted root CA; the client validates the whole chain up to a root it trusts.

</details>

<details><summary><b>74.</b> Why might you see "certificate verify failed" when calling an HTTPS API?</summary>

The certificate is expired, self-signed, for the wrong hostname, missing intermediates, or signed by a CA not in your trust store (common behind corporate proxies).

</details>

<details><summary><b>75.</b> What does the certificate's "Common Name"/"Subject Alternative Name" have to match?</summary>

The hostname you connected to; a mismatch (e.g. cert for `a.com` used on `b.com`) causes a verification failure.

</details>

<details><summary><b>76.</b> Why is it risky to disable certificate verification (e.g. `curl -k`) for a fund-data API?</summary>

It removes protection against man-in-the-middle attacks, so an attacker could intercept or alter NAV/ISIN data; only use it for trusted local debugging, never in production.

</details>

<details><summary><b>77.</b> What is the difference between encryption and authentication in TLS?</summary>

Encryption hides the data from eavesdroppers; authentication (via the certificate) proves you are actually talking to the intended server, not an impostor.

</details>

<details><summary><b>78.</b> What is mutual TLS (mTLS)?</summary>

A TLS mode where both the server and the client present certificates, so each authenticates the other — common for B2B fund-data integrations.

</details>

<details><summary><b>79.</b> What is `localhost` and what IP does it map to?</summary>

`localhost` is the loopback hostname for your own machine, resolving to `127.0.0.1` (IPv4) or `::1` (IPv6).

</details>

<details><summary><b>80.</b> What is the difference between binding a server to `127.0.0.1` vs `0.0.0.0`?</summary>

Binding to `127.0.0.1` accepts only local connections, while `0.0.0.0` binds all interfaces so other machines on the network can reach it.

</details>

<details><summary><b>81.</b> You can hit your API at `localhost:8000` but a colleague on the LAN cannot — likely cause?</summary>

The server is bound to `127.0.0.1` (loopback only); bind to `0.0.0.0` (and open the firewall) so it accepts LAN connections.

</details>

<details><summary><b>82.</b> What is a LAN versus the internet?</summary>

A LAN (local area network) is a private network in one location (home/office) using private IP ranges; the internet is the global network of interconnected networks reached via public IPs.

</details>

<details><summary><b>83.</b> What are the private IPv4 address ranges?</summary>

`10.0.0.0/8`, `172.16.0.0/12`, and `192.168.0.0/16`; these are not routable on the public internet.

</details>

<details><summary><b>84.</b> What is NAT (Network Address Translation)?</summary>

NAT lets many devices on a private network share one public IP by rewriting addresses/ports at the router, which is why internal hosts aren't directly reachable from the internet.

</details>

<details><summary><b>85.</b> Why can't someone on the internet usually connect directly to your laptop on a home LAN?</summary>

Your laptop has a private IP behind NAT/a firewall, so inbound connections aren't routed to it unless a port is explicitly forwarded.

</details>

<details><summary><b>86.</b> What is a firewall?</summary>

A firewall is a system that allows or blocks network traffic based on rules (source/destination IP, port, protocol, direction).

</details>

<details><summary><b>87.</b> What is the difference between a firewall that DROPs vs REJECTs a packet?</summary>

DROP discards it silently (causing the client to time out), while REJECT sends back an error (often producing a "connection refused").

</details>

<details><summary><b>88.</b> What is a forward proxy?</summary>

A forward proxy sits between clients and the internet, forwarding their outbound requests (often for filtering, caching, or logging) on the client's behalf.

</details>

<details><summary><b>89.</b> What is a reverse proxy?</summary>

A reverse proxy sits in front of servers and forwards inbound client requests to backends, often handling TLS termination, load balancing, and caching (e.g. nginx).

</details>

<details><summary><b>90.</b> What do the `HTTP_PROXY` / `HTTPS_PROXY` environment variables do?</summary>

They tell many CLI tools and libraries (like `curl`, `requests`) to route outbound HTTP/HTTPS traffic through the specified proxy.

</details>

<details><summary><b>91.</b> You're behind a corporate proxy and TLS calls fail with an unknown-CA error — what's typically happening?</summary>

The proxy is doing TLS interception with its own CA; you must trust the corporate CA certificate in your trust store (or configure your client to use it).

</details>

<details><summary><b>92.</b> What does `curl -v` add to a request?</summary>

Verbose mode, printing the connection steps, the request headers sent (`>`), the response headers received (`<`), and TLS handshake details.

</details>

<details><summary><b>93.</b> In `curl -v` output, what do lines starting with `>` and `<` represent?</summary>

`>` lines are headers/data curl is sending to the server (the request); `<` lines are what the server is sending back (the response).

</details>

<details><summary><b>94.</b> In `curl -v`, what does a line like `* Trying 203.0.113.5:443...` tell you?</summary>

That DNS resolved the hostname and curl is attempting a TCP connection to that IP and port — useful for confirming which IP you actually reached.

</details>

<details><summary><b>95.</b> In `curl -v`, what do the `* SSL connection using TLSv1.3` and certificate lines tell you?</summary>

That the TLS handshake succeeded, which protocol/cipher was negotiated, and details of the server certificate that was validated.

</details>

<details><summary><b>96.</b> How do you make `curl` show only response headers without the body?</summary>

Use `curl -I <url>` (a `HEAD` request) or `curl -sS -D - -o NUL <url>` to dump headers while discarding the body.

</details>

<details><summary><b>97.</b> How do you send a JSON `POST` with curl to a fund API?</summary>

`curl -X POST -H "Content-Type: application/json" -d '{"isin":"LU0000000001"}' https://api.example.com/navs`.

</details>

<details><summary><b>98.</b> How do you add a bearer token to a curl request?</summary>

`curl -H "Authorization: Bearer <token>" https://api.example.com/navs`.

</details>

<details><summary><b>99.</b> A daily EMT-file download via curl returns HTML instead of the file — what should you inspect first?</summary>

The status code and headers (`curl -v` or `-I`): you may be getting a redirect to a login page (`302`) or an error page, so check `Location`, status, and `Content-Type`.

</details>

<details><summary><b>100.</b> A scheduled job resolving `feed.partner.lu` suddenly fails with NXDOMAIN — what does that mean and what do you check?</summary>

NXDOMAIN means DNS has no record for that name; check the hostname spelling, whether the record was removed/changed, the TTL/cache, and which resolver you're using.

</details>


## Phase 0 · 0.7 What data physically is — 100 self-test questions

<details><summary><b>1.</b> At the lowest level, what is any file on disk physically made of?</summary>

A sequence of bytes — each byte is 8 bits, an integer from 0 to 255 — and nothing in the bytes themselves says whether they mean text, an image, or a number; that meaning comes only from how a program chooses to interpret them.

</details>

<details><summary><b>2.</b> What is the difference between "bytes" and "text"?</summary>

Bytes are raw numeric values stored on disk; text is what you get when those bytes are decoded using a character encoding that maps byte values to characters, so the same bytes can become different text under different encodings.

</details>

<details><summary><b>3.</b> What is a character encoding?</summary>

A defined mapping between characters (letters, digits, symbols) and the byte sequences that represent them, e.g. UTF-8 or `ISO-8859-1`, used to turn text into bytes (encode) and bytes back into text (decode).

</details>

<details><summary><b>4.</b> What is the difference between a character set and an encoding?</summary>

A character set (like Unicode) is the catalogue of characters and their code points; an encoding (like UTF-8) is the rule for turning those code points into actual bytes — one character set can have several encodings.

</details>

<details><summary><b>5.</b> What is Unicode?</summary>

A universal character set that assigns a unique number (code point, written like `U+00E9`) to virtually every character in every writing system, plus symbols and emoji, so text is not tied to one language's legacy encoding.

</details>

<details><summary><b>6.</b> What is a Unicode code point?</summary>

The abstract number assigned to a character in Unicode, written as `U+` followed by hex, e.g. `U+20AC` is the euro sign `€`; it is independent of how that character is stored as bytes.

</details>

<details><summary><b>7.</b> What is UTF-8 and why is it the default choice today?</summary>

UTF-8 is a variable-length encoding of Unicode using 1 to 4 bytes per character; it is ASCII-compatible for the first 128 characters, space-efficient for Latin text, and the de facto standard for files, web, and APIs.

</details>

<details><summary><b>8.</b> How many bytes does UTF-8 use for a plain ASCII character like `A`?</summary>

Exactly one byte, with the same value as ASCII (`A` is byte `0x41`/65), which is why valid ASCII text is also valid UTF-8.

</details>

<details><summary><b>9.</b> Why can a single accented character like `é` take more than one byte in UTF-8?</summary>

Because any code point above `U+007F` falls outside the single-byte ASCII range, so UTF-8 encodes it across 2 to 4 bytes; `é` (`U+00E9`) is two bytes (`0xC3 0xA9`).

</details>

<details><summary><b>10.</b> What is ASCII?</summary>

A 7-bit encoding defining 128 characters (English letters, digits, punctuation, control codes); it covers no accented or non-Latin characters, which is why broader encodings like UTF-8 exist.

</details>

<details><summary><b>11.</b> What is `ISO-8859-1` (Latin-1)?</summary>

A single-byte legacy encoding covering ASCII plus 128 extra Western-European characters; every byte 0–255 maps to exactly one character, so it never errors on decode but happily produces wrong characters for non-Latin-1 data.

</details>

<details><summary><b>12.</b> What is "Windows-1252" and why does it matter for legacy fund files?</summary>

A single-byte Microsoft encoding very similar to Latin-1 but using the 0x80–0x9F range for characters like curly quotes and the euro sign; old Windows-exported CSVs often use it, so decoding them as UTF-8 can fail or mangle those symbols.

</details>

<details><summary><b>13.</b> What is UTF-16?</summary>

A Unicode encoding using 2 or 4 bytes per character (16-bit code units); it is common inside Windows and Java internally but uncommon for interchange files, and it is not ASCII-compatible at the byte level.

</details>

<details><summary><b>14.</b> What does it mean that UTF-8 is "self-synchronizing"?</summary>

The leading bits of each byte indicate whether it starts a character or continues one, so a decoder can find character boundaries even after starting mid-stream — a property single-byte legacy encodings lack.

</details>

<details><summary><b>15.</b> What is mojibake?</summary>

Garbled text that appears when bytes are decoded with the wrong encoding, e.g. `é` showing up as `Ã©` because UTF-8 bytes were read as Latin-1; the data is intact but mis-interpreted.

</details>

<details><summary><b>16.</b> You open a CSV and see "Société Générale" instead of "Société Générale" — what happened?</summary>

The file is UTF-8 but was decoded as Latin-1/Windows-1252, so each multi-byte UTF-8 sequence was shown as separate single-byte characters; re-open it declaring the correct UTF-8 encoding.

</details>

<details><summary><b>17.</b> Mojibake shows `Ã©` where you expected `é`. Which direction was the encoding mistake?</summary>

The producer wrote UTF-8 and the reader decoded it as Latin-1/Windows-1252; `Ã©` is exactly the two UTF-8 bytes of `é` interpreted as two single-byte characters.

</details>

<details><summary><b>18.</b> What is a BOM?</summary>

A Byte Order Mark — a special character (`U+FEFF`) optionally placed at the start of a file to signal its encoding/byte order; in UTF-8 it appears as the three bytes `0xEF 0xBB 0xBF`.

</details>

<details><summary><b>19.</b> Why does a UTF-8 BOM cause trouble in CSV files?</summary>

Many parsers do not strip it, so the BOM bytes get attached to the first column name (e.g. header becomes `﻿ISIN` instead of `ISIN`), breaking column lookups and joins.

</details>

<details><summary><b>20.</b> How do you read a BOM-prefixed UTF-8 CSV correctly in Python?</summary>

Open it with encoding `utf-8-sig`, which recognises and discards a leading UTF-8 BOM if present and otherwise behaves like plain UTF-8.

</details>

<details><summary><b>21.</b> Why does Excel sometimes add a BOM when you "Save As CSV UTF-8"?</summary>

Excel writes the UTF-8 BOM so that it can itself later detect the file as UTF-8 on re-open; this helps Excel but can surprise downstream tools that don't expect the BOM.

</details>

<details><summary><b>22.</b> How can you check whether a file starts with a UTF-8 BOM from the command line?</summary>

Inspect the first bytes with a hex viewer such as `xxd file.csv | head -1` or `hexdump -C file.csv | head -1` and look for `ef bb bf` at offset 0.

</details>

<details><summary><b>23.</b> Why should encoding always be specified explicitly when reading files in a pipeline?</summary>

Because the default encoding varies by OS, locale, and tool (Windows may default to a code page, Linux to UTF-8), so relying on the default makes the same code produce mojibake or crashes on a different machine.

</details>

<details><summary><b>24.</b> What is the safest general rule for encodings in a new data pipeline?</summary>

Standardise on UTF-8 everywhere, declare it explicitly on every read and write, and convert legacy inputs to UTF-8 at the ingestion boundary rather than letting unknown encodings propagate.

</details>

<details><summary><b>25.</b> What error does Python raise when it cannot decode bytes with the chosen encoding?</summary>

A `UnicodeDecodeError`, naming the codec and the byte position that failed — a strong signal that the file's real encoding differs from the one you assumed.

</details>

<details><summary><b>26.</b> Why does decoding never "fail" with Latin-1 even on non-Latin-1 data?</summary>

Because Latin-1 maps all 256 possible byte values to a character, so it always succeeds at the byte level but silently yields wrong characters — making it dangerous as a fallback that hides encoding bugs.

</details>

<details><summary><b>27.</b> What is CSV?</summary>

Comma-Separated Values — a plain-text tabular format where rows are lines and fields are separated by a delimiter; it is simple and ubiquitous but has no formal standard, so dialects vary.

</details>

<details><summary><b>28.</b> Why is "CSV has no schema" an important caveat?</summary>

Because the file carries no declared data types, lengths, or constraints — every field is just text, so the meaning (date format, decimal, ISIN vs free text) lives only in convention and downstream parsing code.

</details>

<details><summary><b>29.</b> What is a CSV "dialect"?</summary>

The specific combination of delimiter, quote character, escape rules, line terminator, and quoting policy a particular CSV file uses; mismatching the dialect on read produces misaligned columns.

</details>

<details><summary><b>30.</b> Why are European CSV files often semicolon-delimited?</summary>

Because many European locales use the comma as the decimal separator (e.g. `1.234,56`), so spreadsheets default to `;` as the field delimiter to avoid clashing with decimals.

</details>

<details><summary><b>31.</b> A NAV file from a Luxembourg system uses `;` but your parser assumes `,` — what symptom do you see?</summary>

The whole row lands in a single column (or columns are wildly misaligned), because the parser found no commas to split on; set the delimiter explicitly to `;`.

</details>

<details><summary><b>32.</b> How does CSV handle a field value that itself contains the delimiter?</summary>

The field is wrapped in quote characters (usually `"`), so `"Paris, France"` is one field; a parser that ignores quoting would wrongly split it into two.

</details>

<details><summary><b>33.</b> How is a literal quote character represented inside a quoted CSV field?</summary>

By doubling it, so `"He said ""hi"""` decodes to the value `He said "hi"`; some dialects instead use a backslash escape, which is a dialect difference to watch for.

</details>

<details><summary><b>34.</b> How can a single CSV field legitimately contain a line break?</summary>

When the field is quoted, a newline inside the quotes is part of the value, not a row separator — so a "row" can span multiple physical lines, which naive line-by-line splitting breaks.

</details>

<details><summary><b>35.</b> Why is splitting a CSV on newlines and commas with simple string operations risky?</summary>

Because it ignores quoting, embedded delimiters, embedded newlines, and escaped quotes, so any field containing those characters corrupts the parse; use a real CSV parser instead.

</details>

<details><summary><b>36.</b> What is the safe way to parse CSV in Python?</summary>

Use the standard-library `csv` module (or `pandas.read_csv`), specifying delimiter, quotechar, and encoding, so quoting and embedded newlines are handled per the dialect.

</details>

<details><summary><b>37.</b> What line-ending difference between Windows and Unix can affect CSV reading?</summary>

Windows uses `\r\n` (CRLF) and Unix uses `\n` (LF); a parser or tool expecting one may leave stray `\r` characters on field values or mis-count lines if it expects the other.

</details>

<details><summary><b>38.</b> How do you detect a stray trailing `\r` on the last column of each row?</summary>

Values look fine in print but comparisons/joins fail; inspect with a hex view or check `repr()` of the value to reveal a hidden `\r`, then normalise line endings or set the parser to universal newlines.

</details>

<details><summary><b>39.</b> Why can leading zeros disappear from an ISIN or account number opened in Excel?</summary>

Excel auto-detects the column as numeric and drops leading zeros (and can switch to scientific notation), so `0001234` becomes `1234`; import the column as text or avoid editing identifiers in Excel.

</details>

<details><summary><b>40.</b> Why might `DE000` style identifiers turn into `4.5E+11` in a spreadsheet?</summary>

The spreadsheet guessed the field was a number and reformatted it in scientific notation; this is a data-typing trap of opening text files in spreadsheet apps, and it can silently corrupt identifiers.

</details>

<details><summary><b>41.</b> What does it mean that CSV is "untyped"?</summary>

Every value is text on disk; whether `2026-06-13`, `42`, or `True` is a date, integer, or boolean is decided entirely by the reader, so the same column can be parsed differently by different tools.

</details>

<details><summary><b>42.</b> How do you tell a CSV reader to treat a column as text to preserve identifiers?</summary>

In `pandas.read_csv`, pass `dtype={"ISIN": str}` (and consider `keep_default_na=False`) so the column is not coerced to numbers or NaN, preserving leading zeros and codes.

</details>

<details><summary><b>43.</b> Why can a CSV with a thousands separator like `1,234.56` break a comma-delimited parse?</summary>

The embedded comma is read as a field delimiter unless the value is quoted, splitting one number into two columns; this is a classic reason numeric exports must be quoted or use a different delimiter.

</details>

<details><summary><b>44.</b> What is a header row and why is its presence ambiguous in CSV?</summary>

The first row often holds column names, but CSV has no flag declaring this, so a tool must be told whether row 1 is a header or data — guessing wrong shifts every column or loses a record.

</details>

<details><summary><b>45.</b> Two CSV exports of the same NAV report have different column orders — why is that a CSV-specific risk?</summary>

Because CSV columns are positional with no enforced schema, so code that relies on column position rather than header name breaks when the order changes; always select by header name.

</details>

<details><summary><b>46.</b> What is JSON?</summary>

JavaScript Object Notation — a text format for structured data built from objects (key/value maps), arrays (ordered lists), strings, numbers, booleans, and null; widely used in APIs and config.

</details>

<details><summary><b>47.</b> What are the two container types in JSON?</summary>

Objects, written with `{ }` as unordered collections of string-keyed values, and arrays, written with `[ ]` as ordered lists of values; values can nest arbitrarily.

</details>

<details><summary><b>48.</b> What primitive value types does JSON natively support?</summary>

Strings, numbers, booleans (`true`/`false`), and `null` — and that's all; there is no native date, time, decimal, or binary type.

</details>

<details><summary><b>49.</b> Why is the lack of a native date type in JSON a problem?</summary>

Because dates must be smuggled as strings (e.g. ISO-8601 `"2026-06-13"`) or numbers (epoch), with no guarantee of format, so producers and consumers must agree on a convention or dates parse wrongly.

</details>

<details><summary><b>50.</b> Why are JSON numbers risky for monetary or NAV values?</summary>

JSON numbers are typically read as IEEE-754 floats, which cannot represent many decimals exactly (e.g. `0.1`), so amounts can lose precision; transmit money as strings or scaled integers to preserve exactness.

</details>

<details><summary><b>51.</b> How are large identifiers like big integers a hazard in JSON?</summary>

Many parsers map JSON numbers to 64-bit floats, which lose precision beyond 2^53, so a long numeric ID can be silently rounded; send such IDs as strings.

</details>

<details><summary><b>52.</b> Are JSON object keys ordered?</summary>

The JSON spec treats object members as unordered, so code must not rely on key order (though many parsers preserve insertion order in practice); arrays, by contrast, are ordered.

</details>

<details><summary><b>53.</b> Can JSON object keys be duplicated, and what happens?</summary>

The spec doesn't forbid duplicate keys but says behaviour is undefined; most parsers keep the last value, so duplicates can silently drop data — treat them as a malformed input.

</details>

<details><summary><b>54.</b> What is the difference between JSON and JSON Lines (NDJSON)?</summary>

Plain JSON is usually one document (often a big array); JSON Lines stores one independent JSON object per line, which streams better and lets you process huge datasets record-by-record without loading everything.

</details>

<details><summary><b>55.</b> Why must strings in JSON use double quotes?</summary>

The JSON spec only allows double-quoted strings; single quotes (valid in JavaScript) make the document invalid JSON, a common cause of parse errors when hand-editing.

</details>

<details><summary><b>56.</b> How are special characters escaped in JSON strings?</summary>

With backslash escapes such as `\"`, `\\`, `\n`, `\t`, and `\uXXXX` for arbitrary code points; an unescaped control character or lone backslash makes the JSON invalid.

</details>

<details><summary><b>57.</b> Does JSON allow comments or trailing commas?</summary>

No — standard JSON forbids both, so a trailing comma after the last array/object element or a `//` comment causes a parse error; relaxed variants like JSON5 allow them but aren't standard JSON.

</details>

<details><summary><b>58.</b> What encoding should JSON be in?</summary>

JSON text is exchanged as Unicode and UTF-8 is the standard and assumed default; a BOM is not recommended, and many strict parsers reject a leading BOM.

</details>

<details><summary><b>59.</b> What is XML?</summary>

eXtensible Markup Language — a verbose, tag-based text format for hierarchical data, using nested elements and attributes; it predates JSON and remains common in finance, including EMT/EPT fund-data files.

</details>

<details><summary><b>60.</b> What is the difference between an XML element and an attribute?</summary>

An element is a tagged node like `<price>100</price>` that can contain text and child elements; an attribute is a name/value pair inside a start tag like `<price currency="EUR">100</price>` and cannot itself contain child elements.

</details>

<details><summary><b>61.</b> When should data be an element vs an attribute in XML?</summary>

Convention favours elements for substantive, possibly repeating or structured data and attributes for simple metadata about an element; but XML doesn't enforce this, so consumers must read both.

</details>

<details><summary><b>62.</b> What is an XML namespace and why does it exist?</summary>

A namespace qualifies element/attribute names with a URI to avoid name collisions when documents combine vocabularies, declared via `xmlns`; e.g. two schemas can both define `<id>` without clashing.

</details>

<details><summary><b>63.</b> Why do XML namespaces complicate parsing and XPath queries?</summary>

Because elements become qualified names (prefix maps to a URI), so an XPath like `//id` may match nothing unless you register the namespace and query the fully qualified name; ignoring namespaces is a frequent XML bug.

</details>

<details><summary><b>64.</b> What is the difference between a well-formed and a valid XML document?</summary>

Well-formed means it obeys XML syntax rules (proper nesting, closed tags, quoted attributes); valid means it additionally conforms to a declared schema (DTD/XSD) defining allowed elements, types, and structure.

</details>

<details><summary><b>65.</b> What is an XSD?</summary>

An XML Schema Definition — itself an XML document that formally defines the structure, element/attribute names, data types, cardinality, and constraints a conforming XML file must satisfy; it gives XML a real schema.

</details>

<details><summary><b>66.</b> What is CDATA in XML?</summary>

A `<![CDATA[ ... ]]>` section that holds text verbatim without the parser interpreting `<`, `>`, or `&`, useful for embedding markup or raw content without escaping each character.

</details>

<details><summary><b>67.</b> How are reserved characters like `<` and `&` represented in normal XML text?</summary>

As entity references — `&lt;` for `<`, `&gt;` for `>`, `&amp;` for `&`, `&quot;` and `&apos;` for quotes — because the raw characters would otherwise be parsed as markup.

</details>

<details><summary><b>68.</b> What is the XML prolog/declaration and what does it tell you?</summary>

The optional first line like `<?xml version="1.0" encoding="UTF-8"?>` declaring the XML version and the character encoding of the document, which parsers use to decode the bytes correctly.

</details>

<details><summary><b>69.</b> In fund data, what is an EMT file and what format is it typically?</summary>

The European MiFID Template, a standardised file of product cost/target-market data exchanged between asset managers and distributors; it is commonly distributed as CSV but the data model is schema-defined, with newer versions also available as XML.

</details>

<details><summary><b>70.</b> Why does a schema-defined format like EMT reduce data-exchange errors compared with ad-hoc CSV?</summary>

Because the agreed schema fixes field names, order, types, and allowed values, so producers and consumers interpret each column identically rather than relying on undocumented local conventions.

</details>

<details><summary><b>71.</b> What does "schema" mean in data engineering?</summary>

The formal definition of a dataset's structure — its fields, their data types, constraints, relationships, and sometimes order — that tells any program how to interpret and validate the data.

</details>

<details><summary><b>72.</b> What is the difference between "schema-on-write" and "schema-on-read"?</summary>

Schema-on-write enforces structure when data is stored (as in a relational database), rejecting bad data up front; schema-on-read applies structure only when the data is queried (as with raw files in a data lake), accepting anything and validating later.

</details>

<details><summary><b>73.</b> Which formats are schema-on-write and which are schema-on-read?</summary>

A relational table is schema-on-write; raw CSV/JSON/XML files dropped into storage are schema-on-read because nothing enforces structure until something parses them.

</details>

<details><summary><b>74.</b> What does it mean for data to be "structured"?</summary>

It conforms to a fixed, predefined schema of rows and typed columns — the classic relational table or a well-defined fixed-format file — so its shape is known before you read it.

</details>

<details><summary><b>75.</b> What does "semi-structured" data mean?</summary>

Data with organisational markers (tags, keys, nesting) but no rigid fixed schema, so structure can vary record-to-record; JSON and XML are the canonical examples.

</details>

<details><summary><b>76.</b> What does "unstructured" data mean?</summary>

Data with no predefined data model or field structure, such as free-text documents, PDFs, emails, images, and audio; meaning must be extracted rather than read off a schema.

</details>

<details><summary><b>77.</b> Where does CSV sit on the structured/semi-structured spectrum?</summary>

It is tabular and looks structured, but because it carries no enforced schema or types it behaves like semi-structured/loosely-structured text; the structure is convention, not guarantee.

</details>

<details><summary><b>78.</b> Why does the structured/semi/unstructured distinction matter for storage choices?</summary>

Because structured data fits relational databases and columnar formats, semi-structured fits document stores or flexible columns, and unstructured fits object storage with separate indexing — picking wrong makes querying painful.

</details>

<details><summary><b>79.</b> What is the core difference between a spreadsheet and a database?</summary>

A spreadsheet is a single-user, visual, free-form grid where formatting and formulas mix with data and types are loose; a database enforces a schema, types, and constraints, supports concurrent multi-user access, and scales to large, queryable datasets.

</details>

<details><summary><b>80.</b> Why are spreadsheets risky as a "system of record" for fund data?</summary>

Because they silently coerce types (dropping leading zeros, reformatting dates/IDs), lack enforced constraints and audit trails, allow manual overwrites, and don't scale or support reliable concurrent updates, leading to errors that are hard to trace.

</details>

<details><summary><b>81.</b> What is a key reliability advantage of a database over a spreadsheet?</summary>

A database enforces a schema and constraints (types, keys, not-null, uniqueness) and provides transactions, so invalid data is rejected and concurrent changes stay consistent — guarantees a spreadsheet cannot give.

</details>

<details><summary><b>82.</b> Why does a database give you typed columns while CSV does not?</summary>

Because a database column has a declared type (e.g. `DECIMAL`, `DATE`) enforced on write, whereas CSV stores everything as text and leaves typing to whatever reads it.

</details>

<details><summary><b>83.</b> How does a database handle concurrent edits that a spreadsheet cannot?</summary>

Through transactions and locking/MVCC that isolate concurrent changes and keep data consistent, whereas a shared spreadsheet typically forces last-writer-wins or file conflicts.

</details>

<details><summary><b>84.</b> For a daily NAV feed consumed by many systems, why prefer a database or schema-defined file over an emailed spreadsheet?</summary>

Because the schema-defined source enforces consistent types and structure, supports automated validation and access control, and avoids the silent corruption and version chaos of manually edited spreadsheets.

</details>

<details><summary><b>85.</b> What is a fixed-width (fixed-position) file?</summary>

A text file where each field occupies a fixed number of character columns rather than being delimiter-separated; common in legacy banking/fund feeds, and parsed by column offsets defined in an accompanying spec.

</details>

<details><summary><b>86.</b> Why is a fixed-width file fragile if the spec is wrong by even one column?</summary>

Because parsing is purely positional, an off-by-one in any field's start/length shifts every subsequent field on the line, silently corrupting all downstream values without raising an error.

</details>

<details><summary><b>87.</b> What is TSV and when is it preferable to CSV?</summary>

Tab-Separated Values uses a tab delimiter; it's handy when fields commonly contain commas (so a comma delimiter would need heavy quoting), though tabs inside values still require care.

</details>

<details><summary><b>88.</b> What is Parquet and how does it differ from CSV?</summary>

Parquet is a binary, columnar, schema-carrying file format with compression and typed columns; unlike text CSV it stores its own schema and types, is far more space- and query-efficient, but isn't human-readable.

</details>

<details><summary><b>89.</b> Why is a self-describing format like Parquet or Avro safer than CSV for data interchange?</summary>

Because the schema and types travel with the data, so consumers don't have to guess delimiters, encodings, or types — eliminating a whole class of CSV/encoding ambiguity bugs.

</details>

<details><summary><b>90.</b> A CSV import puts all data in one column — what is the first thing to check?</summary>

The delimiter: the file likely uses `;` or a tab while the parser assumed `,` (or vice versa); confirm by viewing raw bytes and set the delimiter to match the actual file.

</details>

<details><summary><b>91.</b> A CSV has more parsed fields in some rows than the header has columns — what's the likely cause?</summary>

A delimiter character appears unquoted inside a field (e.g. a comma in a name or a decimal), so that field was split; the fix is correct quoting in the source or a parser that honours the file's quoting.

</details>

<details><summary><b>92.</b> Rows in a CSV "disappear" or merge — what trap should you suspect?</summary>

Embedded newlines inside quoted fields being treated as row breaks by a tool that doesn't respect quoting, splitting one record into two or merging text; use a quoting-aware parser.

</details>

<details><summary><b>93.</b> A date column reads as `13/06/2026` in one file and `06/13/2026` in another — what's the underlying issue?</summary>

CSV has no date type, so date format is just a textual convention that varies by locale; you must know and specify the format on parse or risk swapping day and month silently.

</details>

<details><summary><b>94.</b> Numbers like `1.234,56` are misread as `1.234` — what's wrong?</summary>

The file uses European decimal notation (comma decimal, dot thousands) but the parser assumes US notation; set the decimal and thousands separators (e.g. pandas `decimal=","` `thousands="."`) to match the locale.

</details>

<details><summary><b>95.</b> An API returns `"amount": 0.1 + 0.2` style values that don't add up — what concept explains it?</summary>

Floating-point representation: JSON numbers parsed as IEEE-754 floats can't store many decimals exactly, so sums drift; use decimal types or string-encoded amounts for money.

</details>

<details><summary><b>96.</b> A JSON parse fails with "Expecting property name enclosed in double quotes" — what's the likely mistake?</summary>

The JSON uses single quotes, has a trailing comma, or includes a comment — all invalid in standard JSON; fix the source to strict JSON or use a tolerant variant deliberately.

</details>

<details><summary><b>97.</b> Your XPath query against a valid XML file returns nothing despite the element existing — what's the usual culprit?</summary>

An unhandled namespace: the elements are namespace-qualified, so you must register the namespace prefix/URI and query the qualified name rather than the bare local name.

</details>

<details><summary><b>98.</b> A column of identifiers loaded from CSV lost its leading zeros — what should you have done on read?</summary>

Forced the column to a string/text type on import (e.g. `dtype=str` in pandas, or "Text" column type in Excel's import wizard) so numeric coercion never strips the zeros.

</details>

<details><summary><b>99.</b> Bytes look correct in a hex dump but the displayed text is garbled — bytes problem or interpretation problem?</summary>

An interpretation problem: the data on disk is fine but is being decoded with the wrong encoding, so choose the correct encoding rather than trying to "repair" the bytes.

</details>

<details><summary><b>100.</b> As a Data Architect, what is the single most reliable defence against the whole family of "what data physically is" bugs?</summary>

Make structure explicit at boundaries — pin the encoding (UTF-8), the dialect/delimiter, and a declared schema on every interface, validate on ingestion, and prefer self-describing typed formats over guessing from untyped text.

</details>


## Phase 0 · 0.8 Batch processing & OLTP vs OLAP — 100 self-test questions

<details><summary><b>1.</b> What does OLTP stand for, and what kind of work is it for?</summary>

Online Transaction Processing; it handles many small, frequent reads and writes that capture the day-to-day operations of a business, like a transfer agency recording subscription and redemption orders.

</details>

<details><summary><b>2.</b> What does OLAP stand for, and what kind of work is it for?</summary>

Online Analytical Processing; it answers analytical questions by scanning and aggregating large amounts of data, like computing average NAV per fund per month across years of history.

</details>

<details><summary><b>3.</b> In one phrase, what is the shape of a typical OLTP read?</summary>

A small, indexed lookup that touches very few rows, e.g. fetch one investor's current holding by primary key.

</details>

<details><summary><b>4.</b> In one phrase, what is the shape of a typical OLAP read?</summary>

A big scan that reads many rows across few columns and aggregates them, e.g. `SUM`/`AVG` over millions of NAV records.

</details>

<details><summary><b>5.</b> OLTP is described as "latency-bound" — what does that mean?</summary>

The thing you care about is how fast a single small operation completes (milliseconds per query), because users or systems are waiting on each transaction.

</details>

<details><summary><b>6.</b> OLAP is described as "throughput-bound" — what does that mean?</summary>

The thing you care about is how much data you can crunch per unit time, because the query touches huge volumes and you optimise bytes-scanned-per-second rather than per-row latency.

</details>

<details><summary><b>7.</b> Why is response time the key OLTP metric while data volume processed is the key OLAP metric?</summary>

OLTP serves interactive operations where each must feel instant, so per-operation latency dominates; OLAP serves bulk analysis where total work is enormous, so sustained throughput dominates.

</details>

<details><summary><b>8.</b> Give a fund-industry example of an OLTP operation.</summary>

Recording a single subscription order into the transfer-agency order book, or looking up one investor's account balance by ID.

</details>

<details><summary><b>9.</b> Give a fund-industry example of an OLAP operation.</summary>

Month-end analysis computing average NAV, total assets under management, or flow trends per fund across all share classes and dates.

</details>

<details><summary><b>10.</b> Roughly how many rows does a healthy OLTP query touch versus an OLAP query?</summary>

OLTP touches a handful (often one) row via an index; OLAP touches thousands to millions of rows in a scan.

</details>

<details><summary><b>11.</b> Why do OLTP systems lean heavily on indexes?</summary>

Indexes let the engine jump straight to the few rows a transaction needs without scanning the whole table, keeping each operation low-latency.

</details>

<details><summary><b>12.</b> Why are indexes less central to pure OLAP scans?</summary>

Analytical queries read most of a table anyway, so a full sequential scan is often cheaper than walking an index for nearly every row.

</details>

<details><summary><b>13.</b> What is the "access pattern" difference between OLTP and OLAP in one sentence?</summary>

OLTP does point/small-range access on rows; OLAP does wide scans over columns.

</details>

<details><summary><b>14.</b> Why does mixing heavy OLAP queries onto your OLTP database hurt operations?</summary>

A big analytical scan consumes CPU, memory, and I/O and can contend for locks/cache, slowing the small latency-sensitive transactions, e.g. orders crawling at the subscription cutoff.

</details>

<details><summary><b>15.</b> An architect runs month-end reporting directly on the order-capture database and operations complain subscriptions slowed at cutoff — what happened?</summary>

The throughput-hungry OLAP scan saturated the resources the latency-bound OLTP workload needed, so transactional queries queued behind the analytics.

</details>

<details><summary><b>16.</b> What is the standard architectural fix for the "analytics is slowing my transactions" problem?</summary>

Separate the workloads — keep transactions on the OLTP system and copy/extract data into a separate analytical store (warehouse/columnar engine) for OLAP.

</details>

<details><summary><b>17.</b> Why does "one database to rule them all" rarely serve both OLTP and OLAP well?</summary>

The two workloads want opposite physical layouts and tuning — row storage and indexes for small writes/lookups versus columnar storage for wide scans — so optimising for one penalises the other.

</details>

<details><summary><b>18.</b> What is row-oriented storage?</summary>

A layout that stores all the values of one row contiguously on disk, so a whole record is fetched together.

</details>

<details><summary><b>19.</b> What is column-oriented (columnar) storage?</summary>

A layout that stores all the values of one column contiguously, so a single field across many rows is fetched together.

</details>

<details><summary><b>20.</b> What does row storage make cheap?</summary>

Reading or writing an entire single record at once — ideal for OLTP point lookups and inserts/updates of whole rows.

</details>

<details><summary><b>21.</b> What does column storage make cheap?</summary>

Reading just a few columns across many rows for aggregation, since you only touch the bytes you need — ideal for OLAP scans.

</details>

<details><summary><b>22.</b> Why is a row store inefficient for `SELECT AVG(nav) FROM prices` over a wide table?</summary>

It must read every row's full record off disk just to extract one column, wasting I/O on the columns you didn't ask for.

</details>

<details><summary><b>23.</b> Why is a column store inefficient for "fetch this one investor's whole record"?</summary>

The investor's fields are scattered across many separate column files, so assembling one row means reading from many places instead of one contiguous block.

</details>

<details><summary><b>24.</b> How does columnar storage enable better compression?</summary>

Values in a single column are the same type and often similar, so run-length, dictionary, and delta encodings compress far better than mixed-type rows.

</details>

<details><summary><b>25.</b> What is dictionary encoding and why does it help columnar stores?</summary>

It replaces repeated column values (like ISINs or fund names) with small integer codes referencing a value dictionary, shrinking storage and speeding scans.

</details>

<details><summary><b>26.</b> What is run-length encoding and where does it shine in column storage?</summary>

It stores a value plus how many times it repeats consecutively; it shines on sorted or low-cardinality columns like a currency or share-class field.

</details>

<details><summary><b>27.</b> Why does better compression directly speed up OLAP queries?</summary>

Less data on disk means fewer bytes to read into memory per scan, and I/O is usually the bottleneck for analytics, so smaller equals faster.

</details>

<details><summary><b>28.</b> What is "column pruning" and which storage layout benefits from it?</summary>

Reading only the columns a query references and skipping the rest; columnar storage benefits because columns are physically separate.

</details>

<details><summary><b>29.</b> What is vectorized execution?</summary>

Processing data in batches of column values at a time rather than row-by-row, so CPU caches and SIMD instructions are used efficiently — a hallmark of analytical engines.

</details>

<details><summary><b>30.</b> Why is row-by-row processing slower than vectorized column processing for analytics?</summary>

Per-row processing pays interpreter/function-call overhead on every row; vectorized engines amortise that over a whole batch of values, hitting CPU caches well.

</details>

<details><summary><b>31.</b> Which storage layout is better for frequent single-row `UPDATE` statements, and why?</summary>

Row storage, because the whole record sits together so updating it touches one place instead of rewriting many separate column segments.

</details>

<details><summary><b>32.</b> Why are columnar stores often append-mostly rather than update-heavy?</summary>

Updating one row means touching every column segment, so columnar engines favour bulk appends and treat updates as expensive or rewrite-based.

</details>

<details><summary><b>33.</b> Is Postgres a row store or a column store by default?</summary>

Row store — it stores tuples (rows) together, which suits its OLTP heritage.

</details>

<details><summary><b>34.</b> Is DuckDB a row store or a column store?</summary>

Column store with vectorized execution, purpose-built for analytical (OLAP) queries.

</details>

<details><summary><b>35.</b> In one line, when would you reach for Postgres over DuckDB?</summary>

When you need concurrent transactional reads/writes, point lookups, constraints, and many clients — the OLTP shape.

</details>

<details><summary><b>36.</b> In one line, when would you reach for DuckDB over Postgres?</summary>

When you need fast single-node analytics — big scans and aggregations over files like Parquet — without standing up a server.

</details>

<details><summary><b>37.</b> What does it mean that DuckDB is "in-process" / embedded?</summary>

It runs inside your application or REPL as a library with no separate server to install, connect to, or manage — like SQLite but for analytics.

</details>

<details><summary><b>38.</b> Postgres uses a client-server model — what does that imply operationally?</summary>

You run a long-lived server process that clients connect to over a socket/network, giving shared concurrent access, authentication, and durability guarantees.

</details>

<details><summary><b>39.</b> Why is DuckDB often called "the SQLite of analytics"?</summary>

It's a single-file, zero-dependency, embedded SQL engine like SQLite, but columnar and tuned for OLAP scans instead of OLTP transactions.

</details>

<details><summary><b>40.</b> Can DuckDB query a Parquet file directly without importing it first?</summary>

Yes — e.g. `SELECT * FROM 'prices.parquet'`, it reads the file in place using its columnar layout.

</details>

<details><summary><b>41.</b> Why is Parquet a natural pairing with DuckDB?</summary>

Parquet is itself a columnar, compressed file format, so DuckDB can prune columns and read only what a query needs without loading everything.

</details>

<details><summary><b>42.</b> Why might `SELECT AVG(nav) ...` be much faster on DuckDB-over-Parquet than on Postgres for 1M rows?</summary>

DuckDB reads only the `nav` column (and any filter columns) in compressed vectorized batches, while Postgres reads full rows and processes them one at a time.

</details>

<details><summary><b>43.</b> Why might a single-row lookup by fund key be faster on Postgres than on DuckDB?</summary>

Postgres can use a B-tree index to jump straight to the row, while a columnar scan engine may scan to find one row and pay column-reassembly cost.

</details>

<details><summary><b>44.</b> After timing both engines you see the winner reverses between the scan and the point lookup — what does that prove?</summary>

That neither engine is "faster" in the abstract; storage layout matches workload — columnar wins scans, row+index wins point lookups.

</details>

<details><summary><b>45.</b> A teammate says "DuckDB is just fast" — give the real reason it wins an aggregation.</summary>

Columnar layout lets it read only needed columns, compression shrinks I/O, and vectorized execution processes batches efficiently — it's layout and execution, not magic.

</details>

<details><summary><b>46.</b> What is a batch processing job, in one sentence?</summary>

A job that processes a bounded, finite set of data on a schedule and publishes a result, rather than reacting to events continuously.

</details>

<details><summary><b>47.</b> Name the three-part rhythm of a batch job taught in this lesson.</summary>

Schedule, then process a bounded slice of data, then publish the result.

</details>

<details><summary><b>48.</b> What does "bounded data" mean for a batch job?</summary>

The input has a known, finite extent — e.g. "all trades for 2026-06-12" — so the job has a clear start and end, unlike an unbounded stream.

</details>

<details><summary><b>49.</b> How does batch processing differ from stream processing?</summary>

Batch processes a finite dataset all at once on a schedule; streaming processes unbounded events continuously as they arrive.

</details>

<details><summary><b>50.</b> Why is batch the "default rhythm" of the fund industry?</summary>

Core outputs like the daily NAV are produced once per valuation cycle on bounded end-of-day data, which maps naturally onto a scheduled batch.

</details>

<details><summary><b>51.</b> Describe the daily-NAV cycle as a batch job.</summary>

On a schedule (after market close/cutoff), take the bounded set of that day's prices and positions, compute each fund's NAV, then publish it to downstream consumers.

</details>

<details><summary><b>52.</b> What is a "cutoff" in fund operations and why does it matter for batch boundaries?</summary>

A cutoff is the deadline after which the day's orders/prices are fixed; it defines the bounded input for that day's NAV batch so the job knows exactly what to process.

</details>

<details><summary><b>53.</b> What is a scheduler's role in batch processing?</summary>

It triggers the job at the right time or on the right dependency (e.g. daily after cutoff) so the job runs reliably without manual kicks.

</details>

<details><summary><b>54.</b> Give two ways a batch job might be scheduled.</summary>

By the clock (e.g. cron at a fixed time) or by an event/dependency (e.g. "run when the upstream price file lands").

</details>

<details><summary><b>55.</b> What does "publish" mean as the final step of a batch job?</summary>

Making the computed result available to downstream consumers — writing it to a table, file, or feed that others read, ideally only once it's complete and correct.

</details>

<details><summary><b>56.</b> Why should a batch job publish results atomically (all-or-nothing) rather than incrementally visible?</summary>

So downstream consumers never read a half-finished result; they should see either the previous complete output or the new complete one.

</details>

<details><summary><b>57.</b> What is idempotency for a batch job?</summary>

The property that running the job again with the same input produces the same end state — running it twice is safe and leaves no duplicates or drift.

</details>

<details><summary><b>58.</b> Why does this lesson insist that "run it twice must be safe"?</summary>

Batch jobs fail and get retried (crashes, partial runs, manual reruns); if a rerun double-counts or corrupts data, every failure becomes a data-quality incident.

</details>

<details><summary><b>59.</b> Give a concrete way a NON-idempotent NAV job goes wrong on rerun.</summary>

If it blindly `INSERT`s each day's NAVs, a rerun adds a second set of rows for the same day, so downstream `SUM`/`AVG` double-counts.

</details>

<details><summary><b>60.</b> Name one technique to make a batch load idempotent.</summary>

Use upsert/merge keyed on the natural key (e.g. fund + date), or delete-then-insert the target partition, so a rerun overwrites rather than appends.

</details>

<details><summary><b>61.</b> What is "delete-then-insert by partition" and why is it idempotent?</summary>

Before writing a slice (say one date), you delete any existing rows for that slice and then insert fresh ones, so the result is identical no matter how many times you run it.

</details>

<details><summary><b>62.</b> What is an `UPSERT` (e.g. `INSERT ... ON CONFLICT ... DO UPDATE` in Postgres) and how does it help idempotency?</summary>

It inserts a row or updates the existing one on key conflict, so re-running with the same keys overwrites instead of duplicating.

</details>

<details><summary><b>63.</b> Why is a "natural key" important for idempotent fund-data writes?</summary>

A stable key like (ISIN or fund id, valuation date) lets the job recognise and replace the prior version of a row instead of appending a duplicate.

</details>

<details><summary><b>64.</b> How does idempotency relate to retries and failure recovery?</summary>

Because reruns are safe, you can retry a failed or half-completed job freely without manual cleanup, which makes the whole pipeline robust.

</details>

<details><summary><b>65.</b> Is appending rows to a log table idempotent by default? Why or why not?</summary>

No — a plain append adds new rows every run, so a rerun produces duplicates unless you dedupe by key or guard with an insert-if-not-exists.

</details>

<details><summary><b>66.</b> What is a "partition" in the context of a batch job?</summary>

A logical slice of the data, typically by date, that the job processes and can publish/replace independently — e.g. one day's NAVs.

</details>

<details><summary><b>67.</b> Sort these into OLTP/OLAP/batch: "insert one redemption order".</summary>

OLTP — a single small write.

</details>

<details><summary><b>68.</b> Sort into OLTP/OLAP/batch: "compute AUM per fund family for the year".</summary>

OLAP — a large scan-and-aggregate analytical query.

</details>

<details><summary><b>69.</b> Sort into OLTP/OLAP/batch: "every night at 22:00, recompute and publish all funds' NAV".</summary>

Batch (whose internal computation is OLAP-shaped) — scheduled processing of bounded daily data.

</details>

<details><summary><b>70.</b> Sort into OLTP/OLAP/batch: "look up an investor's current balance for the call-centre screen".</summary>

OLTP — a latency-bound point read.

</details>

<details><summary><b>71.</b> Sort into OLTP/OLAP/batch: "month-end report of average NAV per fund per month".</summary>

OLAP — aggregation over a large historical scan.

</details>

<details><summary><b>72.</b> Sort into OLTP/OLAP/batch: "update a single fund's management fee field".</summary>

OLTP — a small single-row write.

</details>

<details><summary><b>73.</b> Where on the OLTP/OLAP split does the daily-NAV batch sit, and what does that imply for where it runs?</summary>

Its computation is OLAP-shaped (scan positions and prices, aggregate per fund), so it should run against an analytical/columnar store or extract, not on the live transactional order book.

</details>

<details><summary><b>74.</b> Why should the daily-NAV calculation generally not run on the transactional order-capture database?</summary>

Its big scans are throughput-bound and would contend with latency-bound order processing; it belongs on a separate analytical copy.

</details>

<details><summary><b>75.</b> An EMT (European MiFID Template) file is a periodic vendor feed of product data — is loading it a batch or a stream job?</summary>

Batch — it arrives as a bounded file on a schedule, so you load and publish it as a scheduled batch.

</details>

<details><summary><b>76.</b> Why must an EMT-file load be idempotent if the vendor can resend a corrected file?</summary>

A resend or rerun must replace the prior version for that period rather than create duplicate product rows, so the load should upsert/replace by key.

</details>

<details><summary><b>77.</b> What natural key would make an ISIN-keyed reference load idempotent?</summary>

The ISIN (plus an effective date or version) — so reloading the same file overwrites each instrument's row instead of appending a copy.

</details>

<details><summary><b>78.</b> Why is an ISIN a good candidate key for instrument reference data?</summary>

It is a standardised, unique 12-character identifier per security, so it stably identifies the same instrument across reloads and sources.

</details>

<details><summary><b>79.</b> For "show one fund's latest NAV on a web page" which engine/layout fits, and why?</summary>

A row store with an index (e.g. Postgres) — it's a latency-bound point lookup, exactly what row+index storage makes cheap.

</details>

<details><summary><b>80.</b> For "chart 5 years of monthly average NAV across all funds" which engine/layout fits, and why?</summary>

A columnar engine (e.g. DuckDB over Parquet) — it's a throughput-bound scan/aggregation, exactly what columnar storage makes cheap.

</details>

<details><summary><b>81.</b> Your "average NAV per fund per month" query is slow on Postgres over 1M rows — what is the first layout-level thing to suspect?</summary>

Row storage is reading full rows to get a couple of columns; the workload is OLAP-shaped and would suit a columnar engine or at least a covering/columnar approach.

</details>

<details><summary><b>82.</b> A point lookup that was fast on Postgres is slow on DuckDB — first thing to check?</summary>

That you actually need a point lookup here; DuckDB scans rather than seeks, so for single-key lookups a row store with an index is the right tool.

</details>

<details><summary><b>83.</b> Your nightly NAV batch produced double the expected rows for today — first thing to check?</summary>

Whether the job ran twice (or was retried) and is not idempotent — i.e. it appends instead of upserting/replacing the day's partition.

</details>

<details><summary><b>84.</b> A batch job "succeeded" but downstream sees yesterday's numbers — first thing to check?</summary>

Whether publish was atomic and pointed at the new partition/date, and whether the schedule actually triggered today's run on the right bounded input.

</details>

<details><summary><b>85.</b> A rerun of a batch job for a single bad day corrupted other days too — what design flaw does this reveal?</summary>

The job isn't partition-scoped; it should delete/replace only the targeted day's slice, not touch the whole dataset.

</details>

<details><summary><b>86.</b> Why is "cold vs warm" timing worth recording when benchmarking Postgres vs DuckDB?</summary>

The first (cold) run reads from disk while a warm run hits cache; comparing both separates I/O cost from CPU/execution cost so you don't misattribute speed.

</details>

<details><summary><b>87.</b> What does a big cold-vs-warm gap on a scan query usually indicate?</summary>

That the query is I/O-bound — most of the cold time is reading bytes from disk, which caching then removes on the warm run.

</details>

<details><summary><b>88.</b> Why does columnar compression matter most on the cold run?</summary>

Compression reduces bytes read from disk, which is exactly the cost dominating a cold, I/O-bound scan.

</details>

<details><summary><b>89.</b> Two engines give identical query results but very different timings — is the slower one "wrong"?</summary>

No — correctness is the same; the difference is performance driven by storage layout and execution model for that workload.

</details>

<details><summary><b>90.</b> Why generate ~1M synthetic NAV rows for this exercise instead of using 100 rows?</summary>

Storage-layout effects (scan I/O, compression, vectorization) only become visible at scale; tiny tables fit in cache and hide the difference.

</details>

<details><summary><b>91.</b> What is a "covering index" and which workload does it help?</summary>

An index that includes all columns a query needs so the engine answers from the index alone; it helps OLTP-ish reads but doesn't turn a row store into a columnar scanner.

</details>

<details><summary><b>92.</b> Why won't simply adding indexes make Postgres beat DuckDB on a full-table aggregation?</summary>

An aggregation scans most rows anyway, so an index adds overhead without avoiding the scan; the win comes from columnar layout, not indexing.

</details>

<details><summary><b>93.</b> What is a materialized view and how does it relate to batch + OLAP?</summary>

A precomputed, stored query result refreshed on a schedule; it's effectively a batch job that publishes an OLAP aggregate for fast reads.

</details>

<details><summary><b>94.</b> Why might you precompute (materialize) "monthly average NAV per fund" rather than query it live each time?</summary>

The aggregation is expensive to recompute repeatedly; a scheduled batch materializes it once so many readers get fast, consistent results.

</details>

<details><summary><b>95.</b> What is the trade-off of materializing aggregates?</summary>

You gain read speed and consistency but add staleness (results lag the refresh) and the cost/complexity of keeping the materialization current.

</details>

<details><summary><b>96.</b> How does the OLTP-vs-OLAP split motivate the classic "extract from the source database" step?</summary>

You copy operational data out of the latency-bound OLTP system into an analytical store so heavy scans never touch live transactions.

</details>

<details><summary><b>97.</b> What does "throughput vs latency" tuning mean you optimise differently for each system?</summary>

For OLTP you minimise per-query latency (indexes, small transactions, caching hot rows); for OLAP you maximise bytes-scanned-per-second (columnar layout, compression, parallel scans).

</details>

<details><summary><b>98.</b> Why are write amplification and lock contention bigger concerns for OLTP than OLAP?</summary>

OLTP has many concurrent small writes competing for the same rows/pages, so locking and write overhead per transaction matter; OLAP is mostly read-heavy bulk scans.

</details>

<details><summary><b>99.</b> Postgres vs DuckDB: which would you expect to handle 500 concurrent writing clients, and why?</summary>

Postgres — its client-server, transactional, row-store design supports high-concurrency reads/writes, which an embedded single-process analytical engine is not built for.

</details>

<details><summary><b>100.</b> Summarise the core lesson of 0.8 in one sentence.</summary>

Match the system to the workload — row stores and indexes for latency-bound OLTP, columnar engines for throughput-bound OLAP — and run analytics on bounded, idempotent batch jobs off a separate copy, as the daily NAV does.

</details>


## Phase 0 · 0.9 pandas & JupyterLab — 100 self-test questions

<details><summary><b>1.</b> What is JupyterLab?</summary>

A browser-based interactive development environment for notebooks, code, and data, where you run Python in cells and see output (text, tables, charts) inline beneath each cell.

</details>

<details><summary><b>2.</b> What is a Jupyter notebook cell?</summary>

An individually executable unit of a notebook; a code cell runs Python and shows its output below, while a Markdown cell renders formatted text.

</details>

<details><summary><b>3.</b> How do you run the current cell and move to the next one in JupyterLab?</summary>

Press `Shift+Enter`; `Ctrl+Enter` runs the cell but keeps focus on it, and `Alt+Enter` runs it and inserts a new cell below.

</details>

<details><summary><b>4.</b> What does the number in `In [5]:` next to a cell mean?</summary>

It is the execution count, showing the order in which cells were run during the current kernel session; a cell run later has a higher number regardless of its position in the notebook.

</details>

<details><summary><b>5.</b> What does `In [*]:` indicate?</summary>

The cell is currently running (or queued) and the kernel has not yet finished executing it.

</details>

<details><summary><b>6.</b> What is the "kernel" in a Jupyter notebook?</summary>

The separate Python process that actually executes your cell code and holds all variables and imports in memory; the notebook UI just sends code to it and displays results.

</details>

<details><summary><b>7.</b> What is notebook "hidden state"?</summary>

Variables, imports, and definitions that still live in the kernel's memory from cells you ran earlier (possibly out of order or since deleted), so the notebook's behaviour no longer matches the code you can see top-to-bottom.

</details>

<details><summary><b>8.</b> Why is running cells out of order dangerous?</summary>

Later cells may depend on state created by cells run in a different order, so the notebook works for you but is not reproducible; re-running top-to-bottom on a fresh kernel can fail or give different results.

</details>

<details><summary><b>9.</b> What does "Restart Kernel and Run All Cells" do and why is it important?</summary>

It clears all in-memory state and executes every cell from top to bottom in order; it is the gold-standard check that your notebook is reproducible and free of hidden-state surprises.

</details>

<details><summary><b>10.</b> You deleted a cell that defined `nav_df`, but later cells still use `nav_df` without error — why?</summary>

The variable is still in the kernel's memory from when the deleted cell ran; restart-and-run-all would expose the now-missing definition as a `NameError`.

</details>

<details><summary><b>11.</b> How do you import pandas by convention?</summary>

`import pandas as pd`.

</details>

<details><summary><b>12.</b> What is a pandas `DataFrame`?</summary>

A 2-D labelled table with rows (indexed) and named columns, where each column is a `Series` and can have its own dtype.

</details>

<details><summary><b>13.</b> What is a pandas `Series`?</summary>

A 1-D labelled array (one column or one row of data) with an index, holding values of a single dtype.

</details>

<details><summary><b>14.</b> What is the DataFrame "index"?</summary>

The row labels of the DataFrame; by default a `RangeIndex` (0, 1, 2, …) but it can be set to a meaningful column such as an ISIN or a date.

</details>

<details><summary><b>15.</b> How do you read a CSV file into a DataFrame?</summary>

`pd.read_csv("file.csv")`.

</details>

<details><summary><b>16.</b> How do you read a Parquet file into a DataFrame?</summary>

`pd.read_parquet("file.parquet")`.

</details>

<details><summary><b>17.</b> What is Parquet and why prefer it over CSV for data pipelines?</summary>

Parquet is a columnar, compressed binary file format that stores dtypes and is far faster and smaller to read/write than CSV, which is plain text with no type information.

</details>

<details><summary><b>18.</b> When you `read_csv`, why might a numeric column come in as `object` (string) dtype?</summary>

The CSV is text, so values like `"1,234.56"`, thousands separators, currency symbols, or stray non-numeric entries force pandas to fall back to `object`; you must clean or specify the dtype.

</details>

<details><summary><b>19.</b> What does the `dtype` of a column tell you?</summary>

The data type of its values, e.g. `int64`, `float64`, `object` (usually strings), `bool`, `datetime64[ns]`, or `category`.

</details>

<details><summary><b>20.</b> How do you inspect the dtype of every column at once?</summary>

`df.dtypes`, or `df.info()` for dtypes plus non-null counts and memory usage.

</details>

<details><summary><b>21.</b> Why does Parquet preserve dtypes but CSV does not?</summary>

Parquet stores the schema (column types) in the file metadata, whereas CSV is just text and pandas must re-infer types on every read.

</details>

<details><summary><b>22.</b> How do you tell `read_csv` to parse a column as dates?</summary>

Pass `parse_dates=["trade_date"]` (a list of column names) so those columns come in as `datetime64[ns]` instead of strings.

</details>

<details><summary><b>23.</b> Why parse dates at read time rather than leaving them as strings?</summary>

A real `datetime64` dtype enables date arithmetic, sorting, filtering by range, resampling, and `.dt` accessors; string dates sort lexicographically and cannot do any of that.

</details>

<details><summary><b>24.</b> An EMT file's `NAV_Date` column reads in as `object` even though it looks like dates — what is the likely cause and fix?</summary>

The date format was not recognised (e.g. `DD/MM/YYYY`); use `pd.to_datetime(df["NAV_Date"], format="%d/%m/%Y")` or pass an explicit `date_format`/`format` to `read_csv`.

</details>

<details><summary><b>25.</b> What does `df.shape` return?</summary>

A tuple `(n_rows, n_columns)` giving the dimensions of the DataFrame.

</details>

<details><summary><b>26.</b> What is the difference between `df.loc[]` and `df.iloc[]`?</summary>

`loc` selects by label (row/column names, inclusive of the end label), while `iloc` selects by integer position (0-based, end-exclusive like normal Python slicing).

</details>

<details><summary><b>27.</b> How do you select the column `nav` as a Series?</summary>

`df["nav"]` or `df.loc[:, "nav"]`.

</details>

<details><summary><b>28.</b> How do you select multiple columns as a DataFrame?</summary>

Pass a list: `df[["isin", "nav", "nav_date"]]`.

</details>

<details><summary><b>29.</b> How do you select the row labelled `LU0123456789` and the `nav` column with `loc`?</summary>

`df.loc["LU0123456789", "nav"]` (assuming the ISIN is the index).

</details>

<details><summary><b>30.</b> How do you select the first 3 rows and first 2 columns by position?</summary>

`df.iloc[0:3, 0:2]`.

</details>

<details><summary><b>31.</b> With `df.loc["2026-01-01":"2026-01-31"]`, is the end label included?</summary>

Yes — `loc` slicing is inclusive of both endpoints, unlike `iloc` and normal Python slicing which exclude the stop.

</details>

<details><summary><b>32.</b> What is a boolean mask in pandas?</summary>

A boolean Series (one `True`/`False` per row) used to filter rows; `df[mask]` keeps only rows where the mask is `True`.

</details>

<details><summary><b>33.</b> How do you filter rows where `nav` is greater than 100?</summary>

`df[df["nav"] > 100]`, or equivalently `df.loc[df["nav"] > 100]`.

</details>

<details><summary><b>34.</b> How do you combine two conditions in a boolean mask?</summary>

Use `&` (and), `|` (or), `~` (not) with each condition in parentheses, e.g. `df[(df["nav"] > 100) & (df["currency"] == "EUR")]`.

</details>

<details><summary><b>35.</b> Why must you use `&`/`|` instead of `and`/`or` in pandas masks?</summary>

`&`/`|` are element-wise operators on Series, while Python's `and`/`or` try to evaluate the whole Series as a single boolean and raise `ValueError: The truth value of a Series is ambiguous`.

</details>

<details><summary><b>36.</b> Why are parentheses required around each condition when combining masks?</summary>

Because `&` and `|` have higher operator precedence than comparison operators, so without parentheses pandas evaluates the bitwise op first and errors or gives wrong results.

</details>

<details><summary><b>37.</b> How do you select rows whose `currency` is in a set of values?</summary>

`df[df["currency"].isin(["EUR", "USD", "GBP"])]`.

</details>

<details><summary><b>38.</b> What is the "chained assignment" / `SettingWithCopyWarning` problem?</summary>

When you write `df[mask]["col"] = value`, pandas may assign to a temporary copy rather than the original DataFrame, so the change silently does not stick and you get a warning.

</details>

<details><summary><b>39.</b> What is the correct way to set values on filtered rows?</summary>

Use a single `loc` call: `df.loc[mask, "col"] = value`, which assigns in place on the original DataFrame.

</details>

<details><summary><b>40.</b> How do you set the `status` column to `"stale"` for all rows where `nav_date` is older than a cutoff?</summary>

`df.loc[df["nav_date"] < cutoff, "status"] = "stale"`.

</details>

<details><summary><b>41.</b> When you slice a DataFrame, how do you guarantee an independent copy you can safely modify?</summary>

Call `.copy()`, e.g. `sub = df[df["currency"] == "EUR"].copy()`, so later assignments don't trigger `SettingWithCopyWarning` and don't touch the original.

</details>

<details><summary><b>42.</b> What is the split-apply-combine pattern?</summary>

A three-step workflow: split rows into groups by some key, apply an aggregation/transformation to each group, then combine the results into a new structure — implemented by `groupby`.

</details>

<details><summary><b>43.</b> How do you compute the mean `nav` per `currency`?</summary>

`df.groupby("currency")["nav"].mean()`.

</details>

<details><summary><b>44.</b> How do you group by more than one column?</summary>

Pass a list of keys: `df.groupby(["fund_id", "currency"])`, which produces a `MultiIndex` on the result.

</details>

<details><summary><b>45.</b> How do you apply different aggregations to different columns in one call?</summary>

Use `.agg()` with a dict, e.g. `df.groupby("fund_id").agg({"nav": "mean", "shares": "sum"})`.

</details>

<details><summary><b>46.</b> How do you produce named aggregation columns with `groupby`?</summary>

Use named aggregation: `df.groupby("fund_id").agg(avg_nav=("nav", "mean"), total_shares=("shares", "sum"))`.

</details>

<details><summary><b>47.</b> After `df.groupby("currency")["nav"].mean()`, what is the index of the result?</summary>

The unique `currency` values become the index of the resulting Series.

</details>

<details><summary><b>48.</b> How do you turn a `groupby` result's group keys back into regular columns?</summary>

Call `.reset_index()`, or pass `as_index=False` to `groupby`.

</details>

<details><summary><b>49.</b> How do you count the number of rows in each group?</summary>

`df.groupby("fund_id").size()`, which counts all rows including NaNs, unlike `.count()` which counts non-null values per column.

</details>

<details><summary><b>50.</b> What is the difference between `size()` and `count()` on a groupby?</summary>

`size()` returns the total number of rows per group (including NaN), while `count()` returns the number of non-null values per column per group.

</details>

<details><summary><b>51.</b> How would you find, per fund, the latest NAV date?</summary>

`df.groupby("fund_id")["nav_date"].max()`.

</details>

<details><summary><b>52.</b> What does `df.merge(other, on="isin")` do?</summary>

Joins the two DataFrames on matching `isin` values, combining columns from both where the keys match (an inner join by default).

</details>

<details><summary><b>53.</b> What are the `how` options for `merge` and what do they mean?</summary>

`inner` (only matching keys), `left` (all left rows), `right` (all right rows), `outer` (all keys from both); the default is `inner`.

</details>

<details><summary><b>54.</b> What is "row multiplication" (fan-out) in a merge?</summary>

If a key matches multiple rows in the other table, each left row is duplicated once per match, so the result can have more rows than either input — a common cause of inflated sums.

</details>

<details><summary><b>55.</b> You merged transactions to a fund reference table and your total share count doubled — what likely happened?</summary>

The reference table had duplicate keys (e.g. two rows per ISIN), causing a many-to-many fan-out that duplicated transaction rows; deduplicate the reference or check for duplicate keys first.

</details>

<details><summary><b>56.</b> How can `merge` help you catch unexpected fan-out or missing matches?</summary>

Pass `validate="one_to_one"` / `"one_to_many"` to assert the key relationship (it raises if violated), and `indicator=True` to add a `_merge` column showing `left_only`/`right_only`/`both`.

</details>

<details><summary><b>57.</b> What does `indicator=True` add to a merge result?</summary>

A categorical `_merge` column labelling each row as `left_only`, `right_only`, or `both`, useful for auditing which keys matched.

</details>

<details><summary><b>58.</b> How do you merge when the key columns have different names in each table?</summary>

Use `left_on` and `right_on`, e.g. `df.merge(other, left_on="security_id", right_on="isin")`.

</details>

<details><summary><b>59.</b> What is the difference between `merge` and `concat`?</summary>

`merge` joins tables horizontally on key values (like a SQL join), while `pd.concat` stacks DataFrames vertically (more rows) or horizontally by index alignment without matching on a key.

</details>

<details><summary><b>60.</b> How do you stack two DataFrames with the same columns into one?</summary>

`pd.concat([df1, df2], ignore_index=True)` to append rows and renumber the index.

</details>

<details><summary><b>61.</b> What does `df["nav_date"].dt.year` give you?</summary>

A Series of the year extracted from each datetime value, via the `.dt` accessor (similarly `.dt.month`, `.dt.day`, `.dt.dayofweek`).

</details>

<details><summary><b>62.</b> What must a column's dtype be before you can use the `.dt` accessor?</summary>

It must be a datetime type (`datetime64[ns]`); on an `object`/string column `.dt` raises an `AttributeError`.

</details>

<details><summary><b>63.</b> What does `resample` do?</summary>

Groups time-series rows into regular time buckets (e.g. daily, monthly) and aggregates each bucket — like a `groupby` over time, requiring a datetime index or `on=`.

</details>

<details><summary><b>64.</b> How do you compute month-end average NAV from a daily series?</summary>

Set the date as the index (or use `on="nav_date"`) and call `df.resample("ME")["nav"].mean()` (`"ME"` = month-end frequency).

</details>

<details><summary><b>65.</b> What does the resample rule `"D"` vs `"W"` vs `"ME"` mean?</summary>

`"D"` = daily buckets, `"W"` = weekly, `"ME"` = month-end; the rule string sets the bucket frequency.

</details>

<details><summary><b>66.</b> What is required for `resample` to work directly on a DataFrame?</summary>

A `DatetimeIndex` (set via `set_index` or `parse_dates`), or pass the datetime column with `on="nav_date"`.

</details>

<details><summary><b>67.</b> How do you set a column as the index?</summary>

`df = df.set_index("nav_date")`.

</details>

<details><summary><b>68.</b> What is `NaN` in pandas?</summary>

"Not a Number" — the standard missing-value marker for floats; pandas also uses `NaT` for missing datetimes and `None`/`pd.NA` for missing objects.

</details>

<details><summary><b>69.</b> How do you count missing values per column?</summary>

`df.isna().sum()`, which sums the boolean `True`s (missing) for each column.

</details>

<details><summary><b>70.</b> What does `df.dropna()` do by default?</summary>

Drops every row that contains at least one `NaN` in any column; use `subset=` to limit which columns count, or `how="all"` to drop only fully-empty rows.

</details>

<details><summary><b>71.</b> What does `df.fillna(0)` do?</summary>

Replaces all `NaN` values with `0` (or another specified value), keeping the rows in place.

</details>

<details><summary><b>72.</b> When should you choose `fillna` over `dropna`?</summary>

Use `fillna` when missing values have a meaningful default and you must keep the rows; use `dropna` when rows with missing data are invalid or unusable for the analysis.

</details>

<details><summary><b>73.</b> What is forward-fill and how do you do it?</summary>

`df.ffill()` propagates the last valid value forward to fill gaps — useful for carrying a NAV over non-trading days; `bfill()` does the reverse.

</details>

<details><summary><b>74.</b> Why can summing a column with `NaN`s still work but a row-count be misleading?</summary>

pandas aggregations like `sum`/`mean` skip `NaN` by default, so they return a value, but the count of contributing rows is smaller than the total row count — check `count()` to see how many values were actually used.

</details>

<details><summary><b>75.</b> What is the difference between `==` and `.isna()` when checking for missing values?</summary>

`NaN == NaN` is `False`, so `df["col"] == np.nan` never matches; you must use `df["col"].isna()` (or `.isnull()`) to detect missing values.

</details>

<details><summary><b>76.</b> How do you replace specific values (not just NaN), e.g. `"N/A"` strings with missing?</summary>

`df["col"].replace("N/A", pd.NA)`, or pass `na_values=["N/A"]` to `read_csv` so they import as missing.

</details>

<details><summary><b>77.</b> How do you make a quick line chart of NAV over time from a DataFrame?</summary>

With a datetime index, `df["nav"].plot()` (uses matplotlib) draws a line chart; in JupyterLab it renders inline automatically.

</details>

<details><summary><b>78.</b> What does `df.plot(kind="bar")` produce versus `kind="line"`?</summary>

`kind="bar"` draws a bar chart (good for categorical comparisons like NAV per fund), while `kind="line"` draws a line chart (good for trends over time).

</details>

<details><summary><b>79.</b> Why might your chart not appear inline in a notebook, and what fixes it?</summary>

It usually appears automatically in JupyterLab; if not, ensure matplotlib is installed and import it (`import matplotlib.pyplot as plt`), and call `plt.show()` if needed.

</details>

<details><summary><b>80.</b> How do you write a DataFrame to a Parquet file?</summary>

`df.to_parquet("output.parquet")` (requires `pyarrow` or `fastparquet`).

</details>

<details><summary><b>81.</b> How do you write a DataFrame to a database table?</summary>

`df.to_sql("table_name", con=engine, if_exists="append", index=False)`, where `engine` is a SQLAlchemy connection.

</details>

<details><summary><b>82.</b> What does the `if_exists` argument of `to_sql` control?</summary>

What to do if the target table already exists: `"fail"` (default, error), `"replace"` (drop and recreate), or `"append"` (add rows).

</details>

<details><summary><b>83.</b> Why pass `index=False` to `to_sql` (and often `to_csv`)?</summary>

To avoid writing the DataFrame's index as an extra unnamed column in the table/file when the index is just a default `RangeIndex`.

</details>

<details><summary><b>84.</b> Why prefer `to_parquet` over `to_csv` for intermediate pipeline outputs?</summary>

Parquet keeps dtypes, is compressed and columnar (smaller, faster), and round-trips numbers and dates exactly, whereas CSV loses types and bloats on disk.

</details>

<details><summary><b>85.</b> What is a `category` dtype and when is it useful?</summary>

A memory-efficient dtype for columns with few distinct repeated values (e.g. `currency`, `fund_id`); it stores integer codes plus a small lookup, saving memory and speeding up groupby.

</details>

<details><summary><b>86.</b> How do you convert a column to `category` dtype?</summary>

`df["currency"] = df["currency"].astype("category")`.

</details>

<details><summary><b>87.</b> How do you change a column's dtype, e.g. string to float?</summary>

`df["nav"] = df["nav"].astype("float64")`, after cleaning any non-numeric characters; or use `pd.to_numeric(df["nav"], errors="coerce")` to turn bad values into `NaN`.

</details>

<details><summary><b>88.</b> What does `pd.to_numeric(s, errors="coerce")` do?</summary>

Converts a Series to numeric, turning any unparseable values into `NaN` instead of raising — handy for messy text columns like prices with stray symbols.

</details>

<details><summary><b>89.</b> How do you remove duplicate rows?</summary>

`df.drop_duplicates()`, optionally with `subset=["isin", "nav_date"]` to define duplicates by specific columns and `keep="first"/"last"`.

</details>

<details><summary><b>90.</b> How do you check for duplicate keys before a merge?</summary>

`df["isin"].duplicated().any()` returns `True` if any ISIN repeats; `df["isin"].value_counts()` shows which keys repeat and how often.

</details>

<details><summary><b>91.</b> How do you rename columns?</summary>

`df.rename(columns={"NAV_Date": "nav_date", "NAV": "nav"})`, which returns a new DataFrame with the renamed columns.

</details>

<details><summary><b>92.</b> How do you sort a DataFrame by a column?</summary>

`df.sort_values("nav_date")`, with `ascending=False` for descending and a list of columns for multi-key sorting.

</details>

<details><summary><b>93.</b> How do you create a new column from a calculation on existing columns?</summary>

Assign it directly, e.g. `df["market_value"] = df["nav"] * df["shares"]`, which is vectorised across all rows.

</details>

<details><summary><b>94.</b> Why prefer vectorised column operations over looping row by row?</summary>

Vectorised operations run in fast compiled C code over the whole array, while Python row loops (or `.iterrows()`) are far slower and harder to read.

</details>

<details><summary><b>95.</b> How do you get the unique values and their frequencies in a column?</summary>

`df["currency"].unique()` lists distinct values; `df["currency"].value_counts()` gives each value with its count, sorted descending.

</details>

<details><summary><b>96.</b> How do you pivot long data to wide, e.g. one column per currency?</summary>

`df.pivot_table(index="nav_date", columns="currency", values="nav", aggfunc="mean")`.

</details>

<details><summary><b>97.</b> Your `read_csv` fails with a parsing/tokenizing error about the wrong number of fields — what do you check first?</summary>

The delimiter (use `sep=";"` for European CSVs), quoting, or embedded delimiters in fields; also check for a ragged header or extra rows needing `skiprows`.

</details>

<details><summary><b>98.</b> A European EMT CSV uses `;` as separator and `,` as the decimal mark — how do you read it correctly?</summary>

`pd.read_csv("emt.csv", sep=";", decimal=",")` so fields split on `;` and numbers parse with a comma decimal.

</details>

<details><summary><b>99.</b> Your notebook gives different results than a colleague's despite identical code — what is the most likely cause?</summary>

Hidden state from running cells out of order or stale variables; both should restart the kernel and run all cells to compare on a clean, reproducible run.

</details>

<details><summary><b>100.</b> A column of ISINs lost its leading zeros after `read_csv` — why, and how do you prevent it?</summary>

pandas inferred it as a numeric dtype and dropped leading zeros; force it to text with `dtype={"isin": "string"}` (or `dtype=str`) at read time.

</details>


## Phase 0 · 0.10 Editor & IDE setup (VS Code) — 100 self-test questions

<details><summary><b>1.</b> What is a "workspace" in VS Code?</summary>

The project context VS Code opens — usually a single root folder (or a multi-root `.code-workspace` file) — that scopes the file explorer, search, settings, and recommended extensions to that project.

</details>

<details><summary><b>2.</b> What is the difference between User settings and Workspace settings in VS Code?</summary>

User settings apply globally to every project for your account, while Workspace settings live in `.vscode/settings.json` in the project folder and override User settings only for that project.

</details>

<details><summary><b>3.</b> Where are project-scoped VS Code settings stored on disk?</summary>

In a `.vscode/settings.json` file at the root of the workspace folder.

</details>

<details><summary><b>4.</b> Why commit a `.vscode/settings.json` to a team repo like `fundcli`?</summary>

So everyone gets the same interpreter, formatter, and lint behaviour — a NAV loader formatted and linted identically on every machine avoids "works on my editor" diffs.

</details>

<details><summary><b>5.</b> How do you open the integrated terminal in VS Code?</summary>

Use the Terminal menu, the keybinding Ctrl+backtick, or the command palette command `Terminal: Create New Terminal`.

</details>

<details><summary><b>6.</b> What working directory does a new integrated terminal open in by default?</summary>

The root folder of the current workspace, so relative paths in your commands resolve against the project you have open.

</details>

<details><summary><b>7.</b> Why is the integrated terminal preferable to a separate terminal window for this course?</summary>

It shares the workspace's folder, environment, and (over WSL) the same filesystem as the editor, so edit-run-debug stays in one window with no context switching.

</details>

<details><summary><b>8.</b> How do you run several shells side by side in the integrated terminal?</summary>

Split the terminal (the split icon or "Terminal: Split Terminal"), or open additional terminals from the dropdown — useful for running a loader in one pane and `tail`-ing its log in another.

</details>

<details><summary><b>9.</b> What is the VS Code command palette and how do you open it?</summary>

A fuzzy-searchable launcher for every command, opened with `Ctrl+Shift+P` (or `F1`); type part of a command name to find and run it without menus.

</details>

<details><summary><b>10.</b> How does the command palette differ from "Quick Open" (`Ctrl+P`)?</summary>

`Ctrl+P` jumps to files by name, while `Ctrl+Shift+P` runs commands; typing `>` in Quick Open switches it into command mode.

</details>

<details><summary><b>11.</b> What does "Remote - WSL" (now part of the WSL extension) let you do?</summary>

Run VS Code's UI on Windows while the language server, terminal, extensions, and file access all execute inside your WSL2 Linux distro.

</details>

<details><summary><b>12.</b> In a WSL-attached window, where does the integrated terminal's shell actually run?</summary>

Inside the Linux distro (e.g. Ubuntu) — it is a `bash`/`zsh` session in WSL, not Windows PowerShell or CMD.

</details>

<details><summary><b>13.</b> How can you tell a VS Code window is connected to WSL?</summary>

The green remote indicator in the bottom-left status bar shows something like `WSL: Ubuntu`.

</details>

<details><summary><b>14.</b> Why open your `fundcli` repo via the WSL remote rather than from the Windows path?</summary>

So the editor, terminal, and Python interpreter all sit on the Linux filesystem your lab uses — avoiding line-ending, permission, and `\\wsl$` performance problems.

</details>

<details><summary><b>15.</b> What command opens the current WSL directory in VS Code from a WSL terminal?</summary>

`code .` — the WSL extension wires up the `code` command inside the distro.

</details>

<details><summary><b>16.</b> Why is keeping project files under `~/` in WSL faster than under `/mnt/c/...`?</summary>

Files on the native Linux ext4 filesystem (`~`) avoid the cross-OS filesystem translation layer that makes `/mnt/c` Windows-drive access slow.

</details>

<details><summary><b>17.</b> When VS Code is attached to WSL, where do extensions install?</summary>

Extensions split into "UI" extensions that stay on the Windows side and "Workspace" extensions (like Python) that install into the WSL distro and must be enabled there per-distro.

</details>

<details><summary><b>18.</b> You open a folder under `/mnt/c/Users/...` in a WSL window and Python is slow to index — what is the likely cause?</summary>

The files live on the Windows drive accessed through `/mnt/c`, so every read crosses the WSL filesystem boundary; move the repo into the Linux home directory.

</details>

<details><summary><b>19.</b> What does the Python extension (Microsoft) add to VS Code?</summary>

IntelliSense/completions, interpreter and environment selection, the run/debug experience, test discovery, and integration with linters and formatters via Pylance.

</details>

<details><summary><b>20.</b> What is Pylance?</summary>

The Python language server that powers VS Code's completions, type-checking hints, hovers, and go-to-definition; it ships with the Python extension.

</details>

<details><summary><b>21.</b> How do you choose which Python interpreter VS Code uses for a project?</summary>

Run "Python: Select Interpreter" from the command palette and pick the environment (e.g. the project's `.venv`).

</details>

<details><summary><b>22.</b> Why must VS Code point at the project's `.venv` for a `uv`-managed repo?</summary>

So completions, debugging, and the integrated terminal use the same locked dependencies as `uv run`, instead of a system Python missing your packages.

</details>

<details><summary><b>23.</b> How does VS Code usually find a `uv`-created virtual environment automatically?</summary>

It detects the `.venv` folder in the workspace root and offers it as the recommended interpreter.

</details>

<details><summary><b>24.</b> What does the Ruff extension do in VS Code?</summary>

It runs the Ruff linter (and formatter) to surface lint diagnostics inline and can auto-fix and format Python on save.

</details>

<details><summary><b>25.</b> How do you make Ruff format and fix a file every time you save?</summary>

Set `editor.formatOnSave` true with Ruff as the default formatter, and enable `source.fixAll`/`source.organizeImports` code actions on save in settings.

</details>

<details><summary><b>26.</b> Why wire Ruff into the editor in Phase 0 rather than only running it in CI later?</summary>

So style and obvious errors are caught and fixed as you type a transfer-agency parser, not flagged hours later in a CI run.

</details>

<details><summary><b>27.</b> What does the Jupyter extension add to VS Code?</summary>

The ability to open, edit, and run `.ipynb` notebooks and interactive windows directly inside the editor, with a built-in kernel picker and variable explorer.

</details>

<details><summary><b>28.</b> What does the Docker extension (Container Tools) add?</summary>

A side panel to view images, containers, volumes, and registries, plus commands to build, run, and attach to containers and edit Dockerfiles with completions.

</details>

<details><summary><b>29.</b> Which four extensions does this lesson have you install for the `fundcli` setup?</summary>

WSL, Python, Ruff, Jupyter, and Docker (the WSL extension plus the four toolchain extensions).

</details>

<details><summary><b>30.</b> What is the `.vscode/extensions.json` file for?</summary>

It lists recommended extensions for the workspace so collaborators get prompted to install the same toolset when they open the repo.

</details>

<details><summary><b>31.</b> What is a breakpoint in a debugger?</summary>

A marker on a line that pauses program execution when reached, so you can inspect state at that exact point instead of guessing.

</details>

<details><summary><b>32.</b> How do you set a breakpoint in VS Code?</summary>

Click in the gutter to the left of a line number (a red dot appears) or press `F9` with the cursor on the line.

</details>

<details><summary><b>33.</b> Why is breakpoint debugging preferred over print-debugging a reconciliation script?</summary>

A breakpoint lets you inspect every variable live and step through logic in minutes, whereas adding/removing prints is slow, noisy, and easy to leave behind.

</details>

<details><summary><b>34.</b> What does the "Step Over" action do, and what is its default key?</summary>

It executes the current line and stops on the next line in the same function without descending into called functions; default `F10`.

</details>

<details><summary><b>35.</b> What does "Step Into" do, and its default key?</summary>

It descends into the function called on the current line so you can debug inside it; default `F11`.

</details>

<details><summary><b>36.</b> What does "Step Out" do, and its default key?</summary>

It finishes the current function and returns to the caller, stopping at the line after the call; default `Shift+F11`.

</details>

<details><summary><b>37.</b> What does "Continue" do, and its default key?</summary>

It resumes execution until the next breakpoint (or the program ends); default `F5`.

</details>

<details><summary><b>38.</b> How do you inspect a variable's current value while paused at a breakpoint?</summary>

Read it in the VARIABLES panel, hover over the identifier in the editor, or evaluate it in the DEBUG CONSOLE.

</details>

<details><summary><b>39.</b> What is the DEBUG CONSOLE used for during a paused session?</summary>

To evaluate arbitrary expressions in the current frame — e.g. type `len(funds)` or `nav.quantize('0.0001')` to test a fix before editing code.

</details>

<details><summary><b>40.</b> What is a "watch" expression in the debugger?</summary>

An expression you pin in the WATCH panel that VS Code re-evaluates and displays each time execution pauses, so you can monitor a value as you step.

</details>

<details><summary><b>41.</b> When debugging a currency filter that drops the wrong rows, what would you put in a watch?</summary>

Something like `row['currency']` or `len(filtered)` so you can see exactly which value the comparison is testing on each iteration.

</details>

<details><summary><b>42.</b> What is the CALL STACK panel?</summary>

It shows the chain of active function calls that led to the paused line, so you can click up the stack to inspect each caller's local variables.

</details>

<details><summary><b>43.</b> What is a conditional breakpoint and when is it useful?</summary>

A breakpoint that only triggers when an expression is true (e.g. `isin == 'LU0000000000'`), so you pause only on the problem fund instead of every row.

</details>

<details><summary><b>44.</b> How do you set a conditional breakpoint?</summary>

Right-click the breakpoint (or the gutter) and choose "Edit Breakpoint", then enter the condition expression.

</details>

<details><summary><b>45.</b> What is a logpoint?</summary>

A breakpoint variant that logs a message (with embedded expressions) to the debug console instead of pausing — a structured replacement for `print` that you don't have to delete.

</details>

<details><summary><b>46.</b> What file configures how VS Code launches the debugger?</summary>

`.vscode/launch.json`, which defines debug configurations (program, arguments, environment, interpreter).

</details>

<details><summary><b>47.</b> How can you start debugging the current Python file without writing a `launch.json`?</summary>

Use the Run and Debug panel's "Python File" configuration, or the "Python Debugger: Debug Python File" command.

</details>

<details><summary><b>48.</b> How do you pass command-line arguments to your script when debugging?</summary>

Add an `"args"` array to the configuration in `launch.json`, e.g. `"args": ["--currency", "EUR", "navs.csv"]`.

</details>

<details><summary><b>49.</b> Your breakpoint shows as a hollow grey circle and never hits — what does that mean?</summary>

VS Code couldn't bind it: the code path didn't run, the file isn't the one actually executing, or the debugger is attached to a different interpreter/environment.

</details>

<details><summary><b>50.</b> The debugger runs but uses the wrong packages — first thing to check?</summary>

Confirm "Python: Select Interpreter" points at the project `.venv`; a mismatched interpreter is the usual cause of import or version surprises.

</details>

<details><summary><b>51.</b> How do you stop a debugging session?</summary>

Press the stop button in the debug toolbar or `Shift+F5` ("Stop").

</details>

<details><summary><b>52.</b> What does "Restart" do in the debug toolbar?</summary>

It stops and relaunches the program with the same configuration; default `Ctrl+Shift+F5`.

</details>

<details><summary><b>53.</b> What is the value of "keyboard-first" habits in an editor?</summary>

Keeping hands on the keyboard removes the constant mouse round-trips that tax every edit; a dozen well-drilled bindings save far more time than memorising a hundred.

</details>

<details><summary><b>54.</b> What does "Go to Definition" do and what is its default key?</summary>

It jumps to where a symbol is defined; press `F12` with the cursor on the identifier (or `Ctrl+Click` it).

</details>

<details><summary><b>55.</b> What does "Peek Definition" do?</summary>

It shows the definition inline in a small embedded window without leaving your current file; default `Alt+F12`.

</details>

<details><summary><b>56.</b> What is "Go to References" and its key?</summary>

It lists every place a symbol is used across the project; default `Shift+F12`.

</details>

<details><summary><b>57.</b> How do you jump back to where you were after a Go to Definition jump?</summary>

Use "Go Back", `Alt+Left` (and `Alt+Right` to go forward again).

</details>

<details><summary><b>58.</b> What is multi-cursor editing?</summary>

Placing several cursors at once so the same edit applies in multiple locations simultaneously.

</details>

<details><summary><b>59.</b> How do you add a cursor on the next occurrence of the current selection?</summary>

`Ctrl+D` selects the next matching occurrence and adds a cursor there; repeat to grow the selection set.

</details>

<details><summary><b>60.</b> How do you select every occurrence of the current word at once?</summary>

`Ctrl+Shift+L` ("Select All Occurrences").

</details>

<details><summary><b>61.</b> How do you add a cursor above or below the current line by column?</summary>

`Ctrl+Alt+Up` / `Ctrl+Alt+Down` (Alt+Click also drops a cursor anywhere).

</details>

<details><summary><b>62.</b> Why is multi-cursor handy when fixing a hard-coded currency literal repeated across a parser?</summary>

You can select all `'USD'` occurrences with `Ctrl+Shift+L` and retype them as `'EUR'` in one keystroke, instead of editing each line.

</details>

<details><summary><b>63.</b> How do you rename a symbol everywhere it is referenced, safely?</summary>

Use "Rename Symbol" (`F2`) on the identifier — it updates all references via the language server, unlike a blind find-and-replace.

</details>

<details><summary><b>64.</b> What does `Ctrl+Shift+O` do?</summary>

"Go to Symbol in File" — a quick fuzzy jump to any function, class, or variable defined in the current file.

</details>

<details><summary><b>65.</b> What does `Ctrl+T` do?</summary>

"Go to Symbol in Workspace" — search and jump to symbols across the whole project, e.g. find `parse_emt` no matter which module it lives in.

</details>

<details><summary><b>66.</b> How do you comment or uncomment the selected lines quickly?</summary>

`Ctrl+/` toggles line comments on the selection.

</details>

<details><summary><b>67.</b> How do you open the project-wide search panel?</summary>

`Ctrl+Shift+F` opens Search, letting you grep across all files with regex, includes, and excludes.

</details>

<details><summary><b>68.</b> What is a `.ipynb` file?</summary>

A Jupyter notebook — a JSON document of ordered cells (code, Markdown, and outputs) that a kernel executes interactively.

</details>

<details><summary><b>69.</b> What is a kernel in the notebook context?</summary>

The language process (e.g. an IPython process bound to your `.venv`) that runs notebook code cells and holds the in-memory state between them.

</details>

<details><summary><b>70.</b> How do you run the current cell and move to the next in a VS Code notebook?</summary>

`Shift+Enter`; `Ctrl+Enter` runs the cell and keeps focus on it.

</details>

<details><summary><b>71.</b> How do VS Code notebooks and JupyterLab relate to each other?</summary>

They are two front-ends over the same Jupyter kernels and the same `.ipynb` format — the difference is ergonomics, not the underlying engine.

</details>

<details><summary><b>72.</b> Name one ergonomic advantage of VS Code notebooks over JupyterLab.</summary>

You get the full editor's IntelliSense, Git integration, debugging, and your extensions in the same window as the notebook.

</details>

<details><summary><b>73.</b> Name one thing JupyterLab does that VS Code notebooks are weaker at.</summary>

JupyterLab's browser UI excels at a dashboard-style multi-panel layout, rich interactive widgets, and a long-running server you can reconnect to remotely.

</details>

<details><summary><b>74.</b> When would you reach for a notebook over a `.py` script in fund-data work?</summary>

For exploratory analysis — eyeballing a NAV time series or profiling an EMT file's columns — where you want inline tables and plots; production loaders stay as scripts.

</details>

<details><summary><b>75.</b> How do you pick which kernel a VS Code notebook runs against?</summary>

Click the kernel picker at the top-right of the notebook and select the interpreter/environment (typically the project `.venv`).

</details>

<details><summary><b>76.</b> Why prefer the project `.venv` kernel over a global one for an exploration notebook?</summary>

So the notebook sees the same locked dependencies as the rest of the repo and your analysis is reproducible by anyone who runs `uv sync`.

</details>

<details><summary><b>77.</b> How do you launch JupyterLab from a `uv` project?</summary>

Add it as a dev dependency and run `uv run jupyter lab`, which starts the server using the project environment.

</details>

<details><summary><b>78.</b> What is the variable explorer / Data Viewer in VS Code notebooks?</summary>

A panel that lists current variables and lets you open tabular data (like a DataFrame of fund rows) in a scrollable, sortable grid.

</details>

<details><summary><b>79.</b> Can you set breakpoints inside notebook cells in VS Code?</summary>

Yes — the Jupyter extension supports cell debugging, so you can step through a parsing cell just like a script.

</details>

<details><summary><b>80.</b> Why are notebooks awkward under version control compared to scripts?</summary>

The `.ipynb` JSON embeds execution counts and output blobs, producing noisy diffs and merge conflicts; scripts diff cleanly line by line.

</details>

<details><summary><b>81.</b> What is one discipline that keeps notebooks reproducible despite out-of-order execution?</summary>

Periodically "Restart Kernel and Run All" so the notebook actually works top-to-bottom, since cells can otherwise depend on hidden out-of-order state.

</details>

<details><summary><b>82.</b> After opening `fundcli` in WSL, `code .` works but `python` isn't found in the terminal — first check?</summary>

Whether you've activated/selected the project `.venv`; the bare `python` may not be on PATH in the fresh WSL shell, and this course runs Python via `uv run`.

</details>

<details><summary><b>83.</b> Why does this course standardise on `uv run` rather than bare `python` inside the editor terminal?</summary>

`uv run` guarantees the locked project environment is used every time, avoiding the "wrong interpreter" class of bugs across machines.

</details>

<details><summary><b>84.</b> The Ruff extension shows no diagnostics on a file you know is messy — first thing to check?</summary>

That the Ruff extension is enabled in the WSL workspace (not only on the UI side) and that the file is recognised as Python with a Ruff config present.

</details>

<details><summary><b>85.</b> Format-on-save isn't running Ruff — what setting is most likely wrong?</summary>

`editor.defaultFormatter` isn't set to Ruff for Python (or `editor.formatOnSave` is off) in the active settings scope.

</details>

<details><summary><b>86.</b> What is the quickest way to see all keyboard shortcuts and rebind them?</summary>

Open "Preferences: Open Keyboard Shortcuts" (`Ctrl+K Ctrl+S`) to search, view, and reassign every binding.

</details>

<details><summary><b>87.</b> How do you open settings as raw JSON to edit precisely?</summary>

Run "Preferences: Open User Settings (JSON)" or "Open Workspace Settings (JSON)" from the command palette.

</details>

<details><summary><b>88.</b> What does the Problems panel show?</summary>

An aggregated list of diagnostics — lint errors, type warnings, and syntax errors — across open files, opened with `Ctrl+Shift+M`.

</details>

<details><summary><b>89.</b> How do you jump between problems/errors in a file from the keyboard?</summary>

`F8` goes to the next problem and `Shift+F8` to the previous one.

</details>

<details><summary><b>90.</b> What does the Source Control panel (`Ctrl+Shift+G`) give you?</summary>

A Git view of staged/unstaged changes, inline diffs, staging, commits, and branch operations without leaving the editor.

</details>

<details><summary><b>91.</b> What is the gutter "blame"/inline diff useful for when reviewing a loader change?</summary>

Seeing exactly which lines changed and their prior content, so a one-character currency-code edit is obvious before you commit.

</details>

<details><summary><b>92.</b> What is a Quick Fix and how do you invoke it?</summary>

A context action (auto-import, fix-all, etc.) offered by the language server/Ruff at the cursor, invoked with `Ctrl+.`.

</details>

<details><summary><b>93.</b> What does the "Testing" panel do for a pytest project?</summary>

After configuring the test framework, it discovers tests into a tree you can run or debug individually, with pass/fail markers in the gutter.

</details>

<details><summary><b>94.</b> How do you debug a single failing pytest test from the editor?</summary>

Use the "Debug Test" gutter/CodeLens action above the test, which launches it under the debugger so you can break inside the code under test.

</details>

<details><summary><b>95.</b> Why attach VS Code to WSL instead of editing WSL files over the `\\wsl$` share from a Windows-side window?</summary>

The remote attach runs the toolchain natively in Linux with correct permissions and speed, while the network-share approach suffers slow IO and missing Linux tooling.

</details>

<details><summary><b>96.</b> You set a breakpoint in a worker thread/async coroutine and it doesn't pause — what is a common cause?</summary>

The breakpoint is on a code path that runs in a context the debugger didn't attach to, or the line never executes; verify the call actually reaches it and the right config is launched.

</details>

<details><summary><b>97.</b> What is "justMyCode" in a Python debug configuration?</summary>

A setting that, when true, steps only through your code and skips library internals; set it false to step into third-party packages like a CSV/parquet reader.

</details>

<details><summary><b>98.</b> An EMT file parser throws on row 5000 only in production data — how do you pinpoint it fast in the debugger?</summary>

Set a conditional breakpoint on the parse line with a condition matching that row (e.g. the offending ISIN or `row_num == 5000`) so you pause exactly where it fails.

</details>

<details><summary><b>99.</b> Why is the integrated terminal's environment important when running a `uv` command interactively?</summary>

It inherits the workspace/WSL environment and selected interpreter, so `uv run pytest` there uses the same Python and dependencies the editor analyses.

</details>

<details><summary><b>100.</b> What is the single biggest payoff of completing this lesson before later phases?</summary>

A frictionless edit-run-debug loop — lint, terminal, debugger, and notebooks in one keyboard-driven window — so tooling never taxes the four years of work that follow.

</details>


## Phase 0 · 0.11 Unit testing from zero (pytest) — 100 self-test questions

<details><summary><b>1.</b> What is a unit test?</summary>

A small automated check that runs one piece of code (usually a single function or behaviour) in isolation and asserts that its output or effect matches what you expect.

</details>

<details><summary><b>2.</b> What is `pytest`?</summary>

A popular third-party Python testing framework that discovers and runs your tests, lets you use plain `assert`, and gives rich failure output, fixtures, and parametrization.

</details>

<details><summary><b>3.</b> Why write unit tests at all for a NAV-loading script?</summary>

They catch regressions automatically — if a refactor breaks the NAV parsing, a test fails immediately instead of you discovering wrong fund prices in production.

</details>

<details><summary><b>4.</b> How do you run pytest in this course's environment?</summary>

With `uv run pytest`, which runs pytest inside the project's managed virtual environment without you having to activate it manually.

</details>

<details><summary><b>5.</b> Why `uv run pytest` instead of just `pytest`?</summary>

`uv run` guarantees pytest and your dependencies come from the project's locked environment, so the run is reproducible and bare `python`/`pip` is avoided.

</details>

<details><summary><b>6.</b> How do you add pytest as a development dependency with uv?</summary>

Run `uv add --dev pytest`, which installs it and records it under the dev dependency group in `pyproject.toml`.

</details>

<details><summary><b>7.</b> What does `uv run pytest` do when you give it no arguments?</summary>

It starts test discovery from the current directory (or configured `testpaths`) and runs every test it finds.

</details>

<details><summary><b>8.</b> What filename pattern does pytest discover by default?</summary>

Files named `test_*.py` or `*_test.py`.

</details>

<details><summary><b>9.</b> Would pytest collect a file called `nav_tests.py` by default?</summary>

No — it does not match `test_*.py` or `*_test.py`, so rename it to `test_nav.py` (or configure `python_files`) for it to be discovered.

</details>

<details><summary><b>10.</b> What function-name pattern does pytest discover by default?</summary>

Functions whose name starts with `test`, for example `test_parse_isin`.

</details>

<details><summary><b>11.</b> Would pytest run a function named `check_isin`?</summary>

No — it does not start with `test`, so pytest ignores it as a test even if it contains assertions.

</details>

<details><summary><b>12.</b> What class-name pattern does pytest collect tests from by default?</summary>

Classes named `Test*` (with no `__init__` method), and inside them it collects methods named `test*`.

</details>

<details><summary><b>13.</b> Why must a test class not define an `__init__` method?</summary>

pytest will skip collecting it and warn, because it instantiates test classes itself and an `__init__` interferes with that.

</details>

<details><summary><b>14.</b> Where does pytest start searching for tests?</summary>

From the `rootdir` / the arguments you pass, recursing into directories — commonly a `tests/` folder or alongside your modules.

</details>

<details><summary><b>15.</b> What is the simplest possible passing test?</summary>

A function named `test_*` containing an `assert` that is true, e.g. `def test_one(): assert 1 + 1 == 2`.

</details>

<details><summary><b>16.</b> What does the plain `assert` statement do in a pytest test?</summary>

It raises `AssertionError` if the expression is falsy; pytest catches that, marks the test failed, and prints a detailed comparison.

</details>

<details><summary><b>17.</b> Why can you use plain `assert` in pytest instead of methods like `assertEqual`?</summary>

pytest rewrites assert statements so it can show the actual and expected values, so you get rich output without the `unittest`-style assertion methods.

</details>

<details><summary><b>18.</b> What does `assert parse_isin(raw) == "LU0123456789"` check?</summary>

That calling `parse_isin(raw)` returns exactly the string `"LU0123456789"`; any other value fails the test.

</details>

<details><summary><b>19.</b> In the dot output, what does a single `.` mean?</summary>

One test passed.

</details>

<details><summary><b>20.</b> In the dot output, what does `F` mean?</summary>

One test failed (an assertion failed or an unexpected exception was raised in the test body).

</details>

<details><summary><b>21.</b> What does `E` mean in pytest's per-test status output?</summary>

An error occurred during setup or in a fixture (not a plain assertion failure in the test body).

</details>

<details><summary><b>22.</b> What does `s` mean in pytest output?</summary>

The test was skipped.

</details>

<details><summary><b>23.</b> What does the final line `3 passed in 0.04s` tell you?</summary>

Three tests passed and the whole run took 0.04 seconds — the summary of the session.

</details>

<details><summary><b>24.</b> What does `1 failed, 2 passed` mean for your exit status?</summary>

pytest exits non-zero because at least one test failed, which is what makes CI pipelines fail the build.

</details>

<details><summary><b>25.</b> What exit code does pytest return when all tests pass?</summary>

`0`, the conventional success code that lets CI treat the step as passed.

</details>

<details><summary><b>26.</b> How do you run only the tests in one file?</summary>

Pass the path, e.g. `uv run pytest tests/test_nav.py`.

</details>

<details><summary><b>27.</b> How do you run a single test function by name?</summary>

Use `::`, e.g. `uv run pytest tests/test_nav.py::test_parse_nav`.

</details>

<details><summary><b>28.</b> How do you run a single method inside a test class?</summary>

Use the full path with two `::`, e.g. `uv run pytest tests/test_nav.py::TestNav::test_parse`.

</details>

<details><summary><b>29.</b> What does the `-k` option do?</summary>

It runs only tests whose names match a keyword expression, e.g. `uv run pytest -k isin` runs every test with `isin` in its name.

</details>

<details><summary><b>30.</b> How would you run all tests except those mentioning `slow`?</summary>

Use a `-k` expression with `not`, e.g. `uv run pytest -k "not slow"`.

</details>

<details><summary><b>31.</b> What does the `-v` flag do?</summary>

It runs in verbose mode, printing one line per test with its full node id and PASSED/FAILED instead of single dots.

</details>

<details><summary><b>32.</b> What does `-x` do?</summary>

It stops the whole run at the first failure, useful when you want to fix one thing at a time.

</details>

<details><summary><b>33.</b> What does `--maxfail=2` do?</summary>

It stops the run after two failures instead of running everything.

</details>

<details><summary><b>34.</b> What does the `-s` flag do?</summary>

It disables pytest's output capture so `print` statements show up in the console during the run.

</details>

<details><summary><b>35.</b> Why does pytest normally hide your `print` output?</summary>

It captures stdout/stderr per test and only shows it for failing tests, keeping passing runs quiet.

</details>

<details><summary><b>36.</b> What does `--lf` (`--last-failed`) do?</summary>

It re-runs only the tests that failed in the previous run, speeding up the fix loop.

</details>

<details><summary><b>37.</b> What is `@pytest.mark.parametrize`?</summary>

A decorator that runs the same test function once per set of input/expected values, turning one function into many test cases.

</details>

<details><summary><b>38.</b> Write a parametrize that checks `is_valid_isin` for two cases.</summary>

`@pytest.mark.parametrize("isin,expected", [("LU0123456789", True), ("XX1", False)])` then `def test_isin(isin, expected): assert is_valid_isin(isin) == expected`.

</details>

<details><summary><b>39.</b> What are the two main arguments to `parametrize`?</summary>

A string naming the parameters (comma-separated) and a list of value tuples, one tuple per generated test case.

</details>

<details><summary><b>40.</b> How many tests does a parametrize with five value tuples produce?</summary>

Five — pytest generates one independent test per tuple.

</details>

<details><summary><b>41.</b> Why is parametrize better than a `for` loop inside one test?</summary>

Each case becomes its own test, so a failure in one input does not stop the others and the report names exactly which input failed.

</details>

<details><summary><b>42.</b> How does a single parametrized case appear in `-v` output?</summary>

With the parameter values in square brackets in the node id, e.g. `test_isin[LU0123456789-True]`.

</details>

<details><summary><b>43.</b> How do you parametrize over a single parameter (not a tuple)?</summary>

Use one name and a flat list, e.g. `@pytest.mark.parametrize("isin", ["LU0123456789", "FR0000120271"])`.

</details>

<details><summary><b>44.</b> Can you stack two `parametrize` decorators on one test?</summary>

Yes — pytest produces the Cartesian product, so two decorators with 3 and 2 values give 6 tests.

</details>

<details><summary><b>45.</b> How do you give parametrized cases readable names?</summary>

Pass `ids=[...]` to `parametrize`, supplying a label per case so the report reads clearly instead of using auto-generated ids.

</details>

<details><summary><b>46.</b> How would you parametrize a NAV rounding test across several currencies?</summary>

`@pytest.mark.parametrize("amount,ccy,expected", [(1.005, "EUR", 1.01), (1.005, "JPY", 1.0)])` then assert your `round_nav(amount, ccy)` matches `expected`.

</details>

<details><summary><b>47.</b> What is a "pure function"?</summary>

A function whose output depends only on its inputs and which has no side effects (no file/network/global state changes) — same inputs always give the same output.

</details>

<details><summary><b>48.</b> Why are pure functions the easiest things to unit test?</summary>

You just call them with inputs and assert on the return value — no setup, no files, no mocking, fully deterministic.

</details>

<details><summary><b>49.</b> Give a fund-data example of a pure function worth testing.</summary>

A `parse_isin(raw) -> str` or `compute_nav(assets, liabilities, shares) -> Decimal` that only transforms its arguments and returns a value.

</details>

<details><summary><b>50.</b> What does "separating IO from logic" mean?</summary>

Keeping file/network reading in thin wrapper functions and putting the actual parsing/calculation in pure functions, so the logic can be tested without touching disk.

</details>

<details><summary><b>51.</b> Why refactor `load_and_parse_emt(path)` into two functions before testing?</summary>

Split it into `read_text(path)` (IO) and `parse_emt(text)` (pure) so you can test `parse_emt` directly on a string without needing a real EMT file.

</details>

<details><summary><b>52.</b> A function both reads a CSV and computes NAV — how do you make it testable?</summary>

Extract the calculation into a pure function that takes already-parsed rows, then test that function with in-memory data and keep the thin file-reading part minimal.

</details>

<details><summary><b>53.</b> Why is code that mixes calculation and `print`/`open` hard to test?</summary>

You cannot assert on a return value because the result is buried in side effects, so you would need captured output or temp files just to check the logic.

</details>

<details><summary><b>54.</b> What is "one behavior per test"?</summary>

The principle that each test should verify a single, specific behaviour, so a failure points to exactly one cause.

</details>

<details><summary><b>55.</b> Why is one-behavior-per-test better than one giant test with twenty asserts?</summary>

If the first assert fails the rest never run, and the test name no longer tells you what broke; small focused tests localise failures.

</details>

<details><summary><b>56.</b> How should you name a test that checks invalid ISINs are rejected?</summary>

Something descriptive like `test_rejects_isin_with_wrong_length` so the name alone tells you the behaviour under test.

</details>

<details><summary><b>57.</b> What is the Arrange-Act-Assert structure of a test?</summary>

Arrange the inputs/setup, Act by calling the code under test, then Assert on the result — a clear three-part shape per test.

</details>

<details><summary><b>58.</b> In Arrange-Act-Assert, what belongs in "Act"?</summary>

The single call to the function or behaviour you are testing, kept to one action so the assert clearly maps to it.

</details>

<details><summary><b>59.</b> What is a pytest fixture?</summary>

A function decorated with `@pytest.fixture` that provides reusable setup (and optional teardown) to tests by being requested as a parameter.

</details>

<details><summary><b>60.</b> How does a test use a fixture?</summary>

It declares the fixture's name as a parameter; pytest calls the fixture and passes its return value in automatically.

</details>

<details><summary><b>61.</b> Write a basic fixture that returns sample NAV rows.</summary>

`@pytest.fixture` then `def nav_rows(): return [{"isin": "LU0123456789", "nav": 10.5}]`, used by `def test_x(nav_rows): ...`.

</details>

<details><summary><b>62.</b> Why use a fixture instead of repeating setup in every test?</summary>

It removes duplication and gives one place to change the shared setup, keeping tests focused on their assertions.

</details>

<details><summary><b>63.</b> How does a fixture do teardown (cleanup after the test)?</summary>

Use `yield` instead of `return`: code before `yield` is setup, the yielded value is given to the test, and code after `yield` runs as teardown.

</details>

<details><summary><b>64.</b> What is the `tmp_path` fixture?</summary>

A built-in pytest fixture that gives each test a unique, empty temporary directory as a `pathlib.Path`, automatically created and cleaned up.

</details>

<details><summary><b>65.</b> What type does `tmp_path` provide?</summary>

A `pathlib.Path` object pointing to a fresh temporary directory unique to that test.

</details>

<details><summary><b>66.</b> Why use `tmp_path` instead of writing to a fixed file like `/tmp/test.csv`?</summary>

It isolates each test in its own directory, avoids clashes between tests or parallel runs, and pytest cleans it up automatically.

</details>

<details><summary><b>67.</b> How do you write a test EMT file into `tmp_path`?</summary>

Build a path like `f = tmp_path / "emt.csv"` then `f.write_text("header\nrow")`, and pass `f` to your reader under test.

</details>

<details><summary><b>68.</b> How would you test a function that reads a file using `tmp_path`?</summary>

Create the file in `tmp_path` with known contents, call your function on that path, and assert it returns the parsed result.

</details>

<details><summary><b>69.</b> What is the difference between `tmp_path` and `tmp_path_factory`?</summary>

`tmp_path` is per-test (function scope); `tmp_path_factory` is session-scoped and lets you create temp dirs shared across many tests.

</details>

<details><summary><b>70.</b> Where do you put fixtures so many test files can share them?</summary>

In a `conftest.py` file; pytest discovers fixtures there automatically for all tests in that directory and below, with no import needed.

</details>

<details><summary><b>71.</b> Do you have to import a fixture defined in `conftest.py`?</summary>

No — pytest makes `conftest.py` fixtures available to tests in the same directory tree automatically.

</details>

<details><summary><b>72.</b> What does fixture "scope" control?</summary>

How often the fixture is created — `function` (default, per test), `class`, `module`, `package`, or `session` (once per run).

</details>

<details><summary><b>73.</b> When would you use `scope="session"` for a fixture?</summary>

For expensive setup that is safe to share and never mutated across tests, like a read-only sample dataset loaded once per run.

</details>

<details><summary><b>74.</b> Can one fixture depend on another fixture?</summary>

Yes — a fixture can request other fixtures as parameters, and pytest resolves the dependency chain for you.

</details>

<details><summary><b>75.</b> What is the recommended first step of TDD-style fixing: watch a test fail?</summary>

Write or run a test that exercises the bug so you see it fail, proving the test actually detects the problem before you fix the code.

</details>

<details><summary><b>76.</b> Why deliberately watch a test fail before fixing the code?</summary>

A test that passes for the wrong reason (e.g. never runs, or asserts nothing meaningful) gives false confidence; seeing red first confirms it truly checks the behaviour.

</details>

<details><summary><b>77.</b> You fixed a bug but the test still passes the same before and after — what went wrong?</summary>

The test probably never actually exercised the bug (wrong input, wrong assert, or not collected), so confirm it failed against the broken code first.

</details>

<details><summary><b>78.</b> After fixing code so a test passes, what is the discipline?</summary>

Re-run the full suite to confirm the fix works and that you did not break any other test (no regressions).

</details>

<details><summary><b>79.</b> A test passes locally but you suspect it tests nothing — how do you check?</summary>

Break the production code on purpose and confirm the test goes red; if it stays green, the test is not asserting what you think.

</details>

<details><summary><b>80.</b> `uv run pytest` says "no tests ran" — what's the first thing to check?</summary>

That your files match `test_*.py` and functions start with `test`; misnaming is the most common cause of zero collection.

</details>

<details><summary><b>81.</b> pytest reports `ModuleNotFoundError` importing your own package in a test — likely cause?</summary>

The package isn't importable from the rootdir; install it editable (`uv pip install -e .` via uv / declare it in `pyproject.toml`) or fix the package layout so imports resolve.

</details>

<details><summary><b>82.</b> What is a `conftest.py` used for besides fixtures?</summary>

Shared hooks, plugins, command-line options, and path setup for the tests in its directory tree.

</details>

<details><summary><b>83.</b> What does `assert a == b` print when it fails on two dicts?</summary>

A detailed diff showing which keys/values differ, thanks to pytest's assertion rewriting.

</details>

<details><summary><b>84.</b> How do you assert that a function raises a specific exception?</summary>

Use `with pytest.raises(ValueError): parse_isin("bad")` — the test passes only if that exception type is raised inside the block.

</details>

<details><summary><b>85.</b> How do you also check the exception message?</summary>

Pass `match=` a regex: `with pytest.raises(ValueError, match="length"): ...`, which asserts the message matches.

</details>

<details><summary><b>86.</b> Why test the error path (e.g. a malformed ISIN), not just the happy path?</summary>

Because bad input is common in fund feeds; you want to confirm the code rejects it clearly rather than silently producing a wrong NAV.

</details>

<details><summary><b>87.</b> How do you compare floating-point results safely in a test?</summary>

Use `pytest.approx`, e.g. `assert compute(...) == pytest.approx(10.5)`, to allow tiny floating-point rounding differences.

</details>

<details><summary><b>88.</b> Why might `assert 0.1 + 0.2 == 0.3` fail?</summary>

Binary floating point can't represent those decimals exactly, so the sum is slightly off; use `pytest.approx` or `Decimal` for money/NAV.

</details>

<details><summary><b>89.</b> Why prefer `Decimal` over `float` for NAV and money in code under test?</summary>

`Decimal` gives exact decimal arithmetic and predictable rounding, avoiding the float surprises that make monetary tests flaky.

</details>

<details><summary><b>90.</b> How do you mark a test to be skipped?</summary>

Use `@pytest.mark.skip(reason="...")` to always skip, or `@pytest.mark.skipif(condition, reason="...")` to skip conditionally.

</details>

<details><summary><b>91.</b> What is `@pytest.mark.xfail` for?</summary>

To mark a test you expect to fail (e.g. a known bug not yet fixed); pytest reports it as `xfail` instead of a failure.

</details>

<details><summary><b>92.</b> How do you register a custom marker like `@pytest.mark.slow`?</summary>

Declare it under `[tool.pytest.ini_options] markers = [...]` in `pyproject.toml` (or `pytest.ini`) to avoid the unknown-marker warning.

</details>

<details><summary><b>93.</b> How do you run only tests marked `slow`?</summary>

Use `uv run pytest -m slow`, where `-m` selects by marker expression.

</details>

<details><summary><b>94.</b> Where can you configure pytest options for the project?</summary>

In `pyproject.toml` under `[tool.pytest.ini_options]`, or in `pytest.ini`/`tox.ini`/`setup.cfg`.

</details>

<details><summary><b>95.</b> What does setting `testpaths = ["tests"]` in config do?</summary>

Tells pytest to look only in the `tests` directory by default, speeding up discovery and avoiding stray collection.

</details>

<details><summary><b>96.</b> How do you measure code coverage with pytest?</summary>

Add the `pytest-cov` plugin and run `uv run pytest --cov=yourpackage`, which reports which lines were exercised by tests.

</details>

<details><summary><b>97.</b> Is 100% coverage the same as correct code?</summary>

No — coverage shows lines were executed, not that the assertions meaningfully check behaviour; you can run a line without testing its correctness.

</details>

<details><summary><b>98.</b> For a transfer-agency subscription processor, what's a good first unit test?</summary>

Extract the pure calc (shares = amount / nav) and test it with known inputs, including edge cases like a zero or missing NAV that should error.

</details>

<details><summary><b>99.</b> Why keep tests fast and not hitting real fund databases or SFTP servers?</summary>

Fast, IO-free tests run on every save and in CI without network flakiness; you test parsing/logic on sample strings and reserve real connections for separate integration tests.

</details>

<details><summary><b>100.</b> What is the overall fix loop this lesson teaches in one sentence?</summary>

Write a test for the behaviour, watch it fail with `uv run pytest`, fix the (pure, IO-separated) code, watch it pass, then re-run the whole suite to confirm no regressions.

</details>


## Phase 0 · 0.12 Code review basics — 100 self-test questions

<details><summary><b>1.</b> What is a code review?</summary>

A code review is a process where one or more people other than the author read a proposed code change and give feedback before it is merged, to catch defects and improve quality.

</details>

<details><summary><b>2.</b> What are the three main things reviewers typically look for?</summary>

Correctness (does it do the right thing without bugs), clarity (is it readable and maintainable), and scope (does the change stay focused on one concern without creep).

</details>

<details><summary><b>3.</b> What does "correctness" mean in the context of a review?</summary>

It means the code produces the right results, handles edge cases and errors, and behaves as the description and tests claim — not just that it compiles or runs.

</details>

<details><summary><b>4.</b> What does "clarity" mean when reviewing code?</summary>

Clarity means the code is easy to read and understand — good names, sensible structure, helpful comments where needed — so a future maintainer can follow it without the author present.

</details>

<details><summary><b>5.</b> What does "scope" mean as a review concern?</summary>

Scope is whether the change does only what it set out to do; unrelated refactors, drive-by changes, or feature creep make a change harder to review and riskier to merge.

</details>

<details><summary><b>6.</b> What does `PR` stand for?</summary>

`PR` stands for pull request — a proposed set of changes on a branch that you ask maintainers to review and merge into a target branch.

</details>

<details><summary><b>7.</b> Why are small PRs easier to review than large ones?</summary>

Reviewers can hold a small change fully in their head, spot bugs more reliably, and respond faster; review quality drops sharply as diff size grows.

</details>

<details><summary><b>8.</b> What is a rough rule of thumb for a reviewable PR size?</summary>

Keep it small enough to review in one sitting — often cited as a few hundred changed lines or fewer; beyond that, defect-finding effectiveness falls off.

</details>

<details><summary><b>9.</b> What does "one concern per PR" mean?</summary>

Each PR should address a single logical change — one bug fix, one feature, or one refactor — so reviewers and the git history each map to a clear, separable unit of work.

</details>

<details><summary><b>10.</b> Why should you self-review a PR before requesting review from others?</summary>

Self-review catches obvious mistakes, leftover debug code, and unclear bits, saving reviewers' time and signalling that you respect their attention.

</details>

<details><summary><b>11.</b> How do you self-review a PR effectively?</summary>

Read your own diff line by line as if you were the reviewer, in the PR's diff view rather than your editor, checking each change is intentional and explained.

</details>

<details><summary><b>12.</b> What belongs in a good PR description?</summary>

What the change does, why it is needed, how to test or verify it, and any context, trade-offs, or links to the issue or ticket it resolves.

</details>

<details><summary><b>13.</b> Why does the "why" matter more than the "what" in a PR description?</summary>

Reviewers can read the diff to see "what" changed, but only the author knows the motivation; the "why" lets reviewers judge whether the approach fits the goal.

</details>

<details><summary><b>14.</b> What is a "stacked" or "chained" PR?</summary>

A series of small dependent PRs where each builds on the previous one, letting you break a large feature into reviewable pieces that merge in order.

</details>

<details><summary><b>15.</b> Why is reviewing code, not the person, a core feedback principle?</summary>

Critiquing the code keeps feedback objective and non-defensive; attacking the author triggers ego responses and damages trust without improving the change.

</details>

<details><summary><b>16.</b> Rewrite "you always forget error handling" as code-focused feedback.</summary>

"This block doesn't handle the case where the file is missing — should we catch and log that?" — it points at the code and proposes a path forward.

</details>

<details><summary><b>17.</b> What are Conventional Comments?</summary>

A lightweight convention where each review comment starts with a labelled prefix (like `praise:`, `nitpick:`, `suggestion:`, `issue:`, `question:`) to signal its intent and severity.

</details>

<details><summary><b>18.</b> What does the `nitpick:` label communicate?</summary>

That the comment is minor and optional — a small preference the author can take or leave without it blocking the merge.

</details>

<details><summary><b>19.</b> What does the `suggestion:` label communicate?</summary>

That you are proposing a specific change the author should consider; it carries more weight than a nitpick but is usually still discussable.

</details>

<details><summary><b>20.</b> What does the `issue:` label communicate?</summary>

That you have found a real problem that should be addressed before merge — a bug, risk, or correctness concern, not just a preference.

</details>

<details><summary><b>21.</b> What does the `question:` label communicate?</summary>

That you genuinely do not understand something and want clarification, rather than asserting it is wrong — useful when you may be missing context.

</details>

<details><summary><b>22.</b> Why include `praise:` comments in a review?</summary>

Genuine praise reinforces good patterns, balances critical feedback, and keeps review a collaborative rather than purely fault-finding exercise.

</details>

<details><summary><b>23.</b> What is the value of marking comment severity explicitly?</summary>

It tells the author which comments are blocking versus optional, preventing them from over- or under-reacting and speeding up resolution.

</details>

<details><summary><b>24.</b> How should you respond to review feedback "without ego"?</summary>

Treat comments as being about the code, assume good intent, fix or discuss each point on its merits, and avoid taking critique as a personal attack.

</details>

<details><summary><b>25.</b> What should you do if you disagree with a reviewer's comment?</summary>

Respond respectfully with your reasoning, ask a clarifying question, or propose an alternative — discuss rather than silently ignore or comply resentfully.

</details>

<details><summary><b>26.</b> What should you do before resolving a review comment thread?</summary>

Make sure the comment is actually addressed — either by changing the code, or by replying with a rationale the reviewer accepts — not just clicking resolve to make it disappear.

</details>

<details><summary><b>27.</b> Who should resolve a review comment thread, the author or the reviewer?</summary>

Conventions vary, but a common rule is the author marks it resolved after addressing it, while the reviewer can re-open if not satisfied; agree on this as a team.

</details>

<details><summary><b>28.</b> Why is "review as design enforcement" important?</summary>

Review is the gate where the team checks that changes follow agreed architecture, patterns, and standards, preventing erosion of the design over time.

</details>

<details><summary><b>29.</b> How does code review serve as audit evidence?</summary>

A recorded review (who approved, when, what was discussed) provides a documented control showing changes were independently checked — valuable for regulated environments.

</details>

<details><summary><b>30.</b> Why does a regulated EU fund administrator care about code-review audit trails?</summary>

Regulators and auditors expect evidence of change control; a mandatory, recorded peer review of code touching NAV or investor data demonstrates segregation of duties and oversight.

</details>

<details><summary><b>31.</b> What is "segregation of duties" and how does review support it?</summary>

It means the person who makes a change is not the only one who approves it; requiring a reviewer's approval before merge enforces that separation.

</details>

<details><summary><b>32.</b> In Git terms, what does an approved PR usually gate?</summary>

It usually gates the merge into a protected branch like `main`, so unreviewed code cannot reach the branch that deploys to production.

</details>

<details><summary><b>33.</b> What is a "protected branch"?</summary>

A branch with rules preventing direct pushes and requiring conditions — like passing checks and at least one approval — before any change can merge in.

</details>

<details><summary><b>34.</b> What is a "required reviewer" or `CODEOWNERS` rule?</summary>

A rule that automatically requests review from designated owners of certain files or directories, ensuring the right experts approve changes to sensitive areas.

</details>

<details><summary><b>35.</b> What does a `CODEOWNERS` file do?</summary>

It maps file paths or patterns to owning users or teams so that PRs touching those paths automatically require review from the listed owners.

</details>

<details><summary><b>36.</b> Why is it bad to mix a refactor and a bug fix in one PR?</summary>

Reviewers cannot tell which diff lines fixed the bug versus merely moved code, making it harder to verify the fix and risky to revert later.

</details>

<details><summary><b>37.</b> What should you do if a PR is getting too big mid-development?</summary>

Split it — extract independent pieces into separate smaller PRs, or land prerequisite refactors first, so each review stays focused and manageable.

</details>

<details><summary><b>38.</b> What is a "draft" or "WIP" PR for?</summary>

To share work in progress for early feedback or visibility while signalling it is not ready to merge, so reviewers know not to do a final approval yet.

</details>

<details><summary><b>39.</b> What does it mean to "approve" a PR?</summary>

It records that you reviewed the change and believe it is ready to merge, accepting shared responsibility for the code going in.

</details>

<details><summary><b>40.</b> What does "request changes" mean on a PR?</summary>

It blocks the merge until the author addresses your concerns and you re-review, signalling that the change is not yet acceptable.

</details>

<details><summary><b>41.</b> What is the difference between "comment" and "approve" on a PR?</summary>

A plain comment leaves feedback without blocking or endorsing the merge, while approve actively signs off that it is ready to go in.

</details>

<details><summary><b>42.</b> Why should a reviewer pull and run the code in some cases rather than only reading the diff?</summary>

Reading catches logic and style issues, but running it reveals runtime behaviour, integration problems, and whether the change actually works as described.

</details>

<details><summary><b>43.</b> What is a "rubber stamp" review and why is it harmful?</summary>

Approving without really reading the change; it defeats the purpose of review, lets defects through, and creates false audit evidence of oversight.

</details>

<details><summary><b>44.</b> How does a reviewer avoid bikeshedding?</summary>

By focusing on substantive correctness and design issues and deferring trivial style debates to automated tools like linters and formatters.

</details>

<details><summary><b>45.</b> What is the role of automated linters and formatters in reducing review friction?</summary>

They handle objective style and formatting mechanically, so humans spend review time on logic and design instead of arguing over whitespace.

</details>

<details><summary><b>46.</b> What does CI mean in a PR context and why does it matter to reviewers?</summary>

CI (continuous integration) runs automated builds, tests, and checks on the PR; green CI lets the reviewer focus on judgement rather than re-verifying basics by hand.

</details>

<details><summary><b>47.</b> Why should you not review a PR whose CI is failing?</summary>

The failing checks may already reveal problems; reviewing prematurely wastes effort on code that will change once the author fixes the failures.

</details>

<details><summary><b>48.</b> What is a "blocking" comment versus a "non-blocking" one?</summary>

A blocking comment must be resolved before merge because it concerns correctness or risk; a non-blocking one is optional and can be deferred or ignored.

</details>

<details><summary><b>49.</b> How should you phrase a blocking comment so the author understands its weight?</summary>

State clearly that it must be addressed before merge and why, e.g. "issue (blocking): this will divide by zero when the fund has no holdings."

</details>

<details><summary><b>50.</b> Why keep review comments specific rather than vague?</summary>

Specific comments tell the author exactly what to change and where; vague ones like "this feels off" create back-and-forth and frustration.

</details>

<details><summary><b>51.</b> What is the benefit of suggesting code directly in a review comment?</summary>

A concrete suggestion (e.g. GitHub's suggestion blocks) removes ambiguity and lets the author apply the fix with one click, speeding resolution.

</details>

<details><summary><b>52.</b> When is it better to discuss a PR synchronously (call/pairing) instead of in comments?</summary>

When the thread is going in circles, the disagreement is deep, or the design needs rethinking — a quick conversation resolves it faster than many comment rounds.

</details>

<details><summary><b>53.</b> What is "scope creep" in a PR and why resist it?</summary>

Adding unrelated improvements beyond the stated goal; it bloats the diff, delays review, and entangles changes that should be independently reviewable and revertible.

</details>

<details><summary><b>54.</b> If you spot an unrelated bug while reviewing, what should you do?</summary>

Note it but keep it out of this PR — file an issue or a follow-up so the current change stays focused and the bug still gets tracked.

</details>

<details><summary><b>55.</b> Why is a small, single-concern PR easier to revert?</summary>

Because reverting it undoes exactly one logical change without dragging along unrelated work, keeping `git revert` clean and low-risk.

</details>

<details><summary><b>56.</b> What does `git revert` do?</summary>

It creates a new commit that undoes the changes of a previous commit, preserving history rather than rewriting it.

</details>

<details><summary><b>57.</b> Why is a clear PR title useful beyond review?</summary>

It becomes part of the merge commit and git history, so a descriptive title helps anyone later doing `git log` understand what each change did.

</details>

<details><summary><b>58.</b> What is a "self-review checklist" and why use one?</summary>

A short list of items to verify before requesting review (tests added, no debug prints, description complete); it standardises quality and reduces avoidable comments.

</details>

<details><summary><b>59.</b> Why should debug `print` statements or `console.log` calls be removed before review?</summary>

They clutter the diff, leak noise into production logs, and signal an unfinished self-review; reviewers shouldn't have to flag obvious leftovers.

</details>

<details><summary><b>60.</b> What does it mean that review feedback should be "actionable"?</summary>

Each comment should make clear what the author can do about it — a specific change, a question to answer, or a decision to make — not just an observation.

</details>

<details><summary><b>61.</b> How quickly should reviewers aim to respond to a PR, and why?</summary>

Quickly, often within a day, because a blocked PR stalls the author's work and large queues encourage rushed reviews; agree on a team turnaround norm.

</details>

<details><summary><b>62.</b> What is the risk of a PR sitting unreviewed for a long time?</summary>

It drifts out of date with `main`, accumulates merge conflicts, the author loses context, and the change becomes harder and riskier to land.

</details>

<details><summary><b>63.</b> How does keeping PRs small reduce merge conflicts?</summary>

Small PRs merge faster, so they spend less time diverging from `main`, reducing the window in which conflicting changes can land.

</details>

<details><summary><b>64.</b> What should the author do when a reviewer asks a clarifying question?</summary>

Answer it directly, and if the confusion stemmed from unclear code, improve the code or add a comment so the next reader doesn't have the same question.

</details>

<details><summary><b>65.</b> Why is "the reviewer was confused" itself useful signal?</summary>

If a competent reviewer misread the code, future maintainers likely will too; confusion often points to a real clarity problem worth fixing.

</details>

<details><summary><b>66.</b> Why should the author, not the reviewer, usually do the rework?</summary>

The author owns the change and has the most context; the reviewer's job is to identify issues, not to take over authorship.

</details>

<details><summary><b>67.</b> When might a reviewer push a commit directly to the author's branch?</summary>

Only for tiny, agreed fixes (like a typo) with the author's consent; otherwise it muddies ownership and skips the author's understanding of the change.

</details>

<details><summary><b>68.</b> What does "approve with comments" or "approve, non-blocking nits" signal?</summary>

That you trust the author to address minor suggestions at their discretion and you don't need to re-review before merge.

</details>

<details><summary><b>69.</b> Why is tone important in written review comments?</summary>

Text lacks vocal cues, so blunt phrasing reads harsher than intended; courteous, curious wording keeps the exchange collaborative.

</details>

<details><summary><b>70.</b> Rewrite "this is wrong" as a constructive review comment.</summary>

"I think this returns the previous day's NAV instead of today's — should the date filter use `>=` here?" — it explains the problem and invites discussion.

</details>

<details><summary><b>71.</b> Why should you assume good intent when reading review comments as an author?</summary>

Reviewers are trying to improve the change, not attack you; assuming good intent keeps you open to feedback and the discussion productive.

</details>

<details><summary><b>72.</b> What is "review fatigue" and how do small PRs help?</summary>

Review fatigue is declining attention over a long or large review; small PRs keep each review short enough to stay thorough.

</details>

<details><summary><b>73.</b> How should a reviewer prioritise their comments?</summary>

Lead with correctness and design issues that block merge, then clarity suggestions, then optional nitpicks — so the author addresses what matters first.

</details>

<details><summary><b>74.</b> What is the purpose of a PR template?</summary>

It prompts the author to fill in standard sections (summary, testing, risk) so every PR arrives with the context reviewers need.

</details>

<details><summary><b>75.</b> For a PR that parses EMT files, what correctness checks should a reviewer prioritise?</summary>

That mandatory EMT fields and the ISIN are validated, numeric and date formats parse correctly, and malformed or missing rows are handled rather than silently dropped.

</details>

<details><summary><b>76.</b> For a PR computing NAV, what should a reviewer scrutinise most?</summary>

Rounding and precision of monetary values, correct currency handling, the valuation date logic, and that totals reconcile — correctness errors here have real financial impact.

</details>

<details><summary><b>77.</b> Why use exact decimal types rather than floats for NAV in code under review?</summary>

Floating point introduces rounding errors unacceptable for money; a reviewer should flag `float` for monetary values and recommend a decimal type.

</details>

<details><summary><b>78.</b> What should a reviewer check about ISIN handling in a PR?</summary>

That ISINs are validated (12 characters, correct check digit) and treated as opaque identifiers, not parsed for meaning or silently truncated.

</details>

<details><summary><b>79.</b> For a transfer-agency code change touching investor records, what extra review rigour applies?</summary>

Higher scrutiny on data correctness, access controls, audit logging, and personal-data handling, plus likely required sign-off from a data owner via `CODEOWNERS`.

</details>

<details><summary><b>80.</b> Why might a fund-industry PR require two approvals instead of one?</summary>

For high-risk or regulated changes (NAV, investor money, reporting), a second reviewer strengthens the control and the audit evidence of independent oversight.

</details>

<details><summary><b>81.</b> How does linking a PR to a ticket help audit and review?</summary>

It ties the code change to an authorised business reason, creating a traceable chain from requirement to change to approval that auditors can follow.

</details>

<details><summary><b>82.</b> What is a "squash merge" and how does it relate to clean history?</summary>

It combines all of a PR's commits into one commit on merge, so the main branch shows one tidy entry per change rather than messy work-in-progress commits.

</details>

<details><summary><b>83.</b> What is the downside of many tiny "fix review comment" commits, and how is it handled?</summary>

They clutter history; squash-merging or interactive cleanup collapses them into a single meaningful commit on the target branch.

</details>

<details><summary><b>84.</b> Why should a PR's automated tests be part of what the reviewer evaluates?</summary>

Tests are the durable proof of correctness; the reviewer checks they exist, cover the change, and would actually fail if the behaviour broke.

</details>

<details><summary><b>85.</b> What is a red flag if a bug-fix PR has no test?</summary>

Without a regression test the bug can silently return; a reviewer should ask for a test that fails before the fix and passes after.

</details>

<details><summary><b>86.</b> How should a reviewer handle a PR that is correct but poorly named/structured?</summary>

Flag the clarity issues as suggestions or issues depending on severity; correctness is necessary but maintainability also matters for the long term.

</details>

<details><summary><b>87.</b> Why is "it works on my machine" not enough to satisfy a reviewer?</summary>

Correctness must hold across environments and inputs; reviewers look for tests, edge-case handling, and reproducibility, not just one passing local run.

</details>

<details><summary><b>88.</b> What is the author's responsibility regarding the PR diff's readability?</summary>

To present a clean, logically ordered diff — separate formatting from logic changes, avoid unrelated noise — so the reviewer can follow the intent easily.

</details>

<details><summary><b>89.</b> Why separate a pure-formatting commit from a logic commit?</summary>

So reformatting noise doesn't bury the real change; reviewers can skim the formatting commit and focus attention on the logic one.

</details>

<details><summary><b>90.</b> What should you do as a reviewer if a PR is simply too large to review well?</summary>

Say so and ask the author to split it; approving a too-large change you can't actually understand undermines the whole purpose of review.

</details>

<details><summary><b>91.</b> What is the danger of approving to "unblock a colleague" without real review?</summary>

It creates false audit evidence, lets defects through, and erodes the team's trust in approvals as a meaningful quality gate.

</details>

<details><summary><b>92.</b> How does code review spread knowledge across a team?</summary>

Reviewers learn the codebase and the change's context, and authors learn from feedback, reducing bus-factor risk and aligning the team on patterns.

</details>

<details><summary><b>93.</b> Why might a reviewer prefix a comment with "non-blocking:"?</summary>

To make explicit that, although they are raising a point, it should not hold up the merge and is at the author's discretion.

</details>

<details><summary><b>94.</b> What is the value of the author leaving inline self-comments on their own PR?</summary>

Pointing out tricky decisions, asking targeted questions, or flagging a workaround guides reviewers' attention and pre-empts confusion.

</details>

<details><summary><b>95.</b> How should disagreements that can't be resolved between author and reviewer be escalated?</summary>

To a tech lead, owning team, or agreed tie-breaker, so the change isn't deadlocked and the decision is recorded.

</details>

<details><summary><b>96.</b> What is a sensible first thing to check when a reviewer says "this doesn't do what the description claims"?</summary>

Re-read your own diff against the description — either the code has a bug or the description is inaccurate, and you fix whichever is wrong.

</details>

<details><summary><b>97.</b> Your PR has 40 review comments — what does that usually indicate and how do you respond?</summary>

It usually means the PR was too large or under-self-reviewed; address the comments calmly, and next time split the work and self-review first.

</details>

<details><summary><b>98.</b> A reviewer keeps re-requesting changes on style the linter doesn't catch — how do you resolve it sustainably?</summary>

Agree the rule as a team and encode it in the linter or a style guide, so the standard is enforced automatically rather than re-litigated per PR.

</details>

<details><summary><b>99.</b> Why is a merged, reviewed PR stronger audit evidence than an emailed approval?</summary>

It links the exact code diff, the reviewer's identity, timestamps, comments, and the passing checks in one immutable record tied to the change itself.

</details>

<details><summary><b>100.</b> What is the single best habit for getting fast, high-quality reviews?</summary>

Submit small, single-concern, well-described, self-reviewed PRs — they are quick to review, easy to approve, and least likely to hide defects.

</details>
