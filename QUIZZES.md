# Self-test Question Banks

100 questions per lesson. Click a question to reveal its answer. These also appear inside each lesson in the [tracker app](https://sergeiosipov.github.io/data-architect-roadmap/).


## Phase 0 · 0.1 Linux, the command line & shell — 100 self-test questions

<details><summary><b>1.</b> What is WSL2 and why would a Windows-based data engineer use it?</summary>

WSL2 (Windows Subsystem for Linux 2) runs a real Linux kernel in a lightweight VM on Windows, letting you run Ubuntu and Linux tooling natively; it lets you develop in the same Linux environment your production fund-data pipelines will run on.

</details>

<details><summary><b>2.</b> What command installs Ubuntu under WSL2 from a fresh Windows machine?</summary>

`wsl --install` (optionally `wsl --install -d Ubuntu`) installs WSL2 with Ubuntu as the default distribution.

</details>

<details><summary><b>3.</b> How do you check your Ubuntu version and release codename?</summary>

`lsb_release -a` shows the distributor, release number and codename; `cat /etc/os-release` is the file-based equivalent that scripts read.

</details>

<details><summary><b>4.</b> How do you list mounted filesystems and how much free space each has?</summary>

`df -h` lists every mounted filesystem with human-readable sizes; your home directory normally lives on the root (`/`) ext4 filesystem.

</details>

<details><summary><b>5.</b> On Windows/WSL2 (awareness), why keep project files under `~` (ext4) rather than `/mnt/c`?</summary>

Cross-filesystem access between the WSL Linux VM and the Windows drive (`/mnt/c`) has high I/O overhead, so reading/writing many files (e.g. a folder of EMT files) is much slower than working on the native ext4 filesystem — on a native Ubuntu laptop this penalty does not exist.

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

<details><summary><b>1.</b> What is VS Code?</summary>

A free, cross-platform code editor from Microsoft that runs natively on Ubuntu and gains language support, debugging, and tooling through installable extensions.

</details>

<details><summary><b>2.</b> How do you install VS Code on Ubuntu using the `.deb` package?</summary>

Download the `.deb` from the official site and install it with `sudo apt install ./code_*.deb`, which also registers Microsoft's apt repository so future updates arrive through `apt upgrade`.

</details>

<details><summary><b>3.</b> How do you install VS Code on Ubuntu via Snap?</summary>

Run `sudo snap install code --classic`; the `--classic` flag is required because the editor needs broad filesystem and tool access that strict snap confinement would block.

</details>

<details><summary><b>4.</b> What is the difference between the `.deb` and Snap installs of VS Code on Ubuntu?</summary>

The `.deb` integrates with apt and tends to start faster, while the Snap is sandboxed and self-updating; both give the same editor, so pick whichever fits how you manage software on your machine.

</details>

<details><summary><b>5.</b> What does the `code` command do from an Ubuntu terminal?</summary>

It launches VS Code; `code .` opens the current directory as a workspace, and `code myfile.py` opens a single file in the running window.

</details>

<details><summary><b>6.</b> What is a "workspace" in VS Code?</summary>

The project context VS Code opens — usually a single root folder (or a multi-root `.code-workspace` file) — that scopes the file explorer, search, settings, and recommended extensions to that project.

</details>

<details><summary><b>7.</b> How do you open a project folder as a workspace from the terminal?</summary>

From inside the project directory run `code .`, or run `code /path/to/project` from anywhere to open that folder.

</details>

<details><summary><b>8.</b> What is a multi-root workspace?</summary>

A workspace defined by a `.code-workspace` file that holds several top-level folders at once, useful when one task spans separate repositories like a loader repo and a shared library.

</details>

<details><summary><b>9.</b> Where does VS Code store per-project settings on disk?</summary>

In a `.vscode/settings.json` file at the root of the workspace folder.

</details>

<details><summary><b>10.</b> What is the difference between User settings and Workspace settings?</summary>

User settings apply globally to every project for your account, while Workspace settings live in `.vscode/settings.json` in the project folder and override User settings only for that project.

</details>

<details><summary><b>11.</b> Why commit a `.vscode/settings.json` to a team repo like `fundcli`?</summary>

So everyone gets the same interpreter, formatter, and lint behaviour — a NAV loader formatted and linted identically on every machine avoids "works on my editor" diffs.

</details>

<details><summary><b>12.</b> What shell does the integrated terminal run on Ubuntu by default?</summary>

It launches your default login shell, which on a standard Ubuntu install is `bash`, opened in the workspace folder.

</details>

<details><summary><b>13.</b> How do you open the integrated terminal in VS Code on Ubuntu?</summary>

Use the Terminal menu, the `Ctrl+backtick` keybinding, or the command palette command `Terminal: Create New Terminal`; on Ubuntu it opens a `bash` session in the workspace folder.

</details>

<details><summary><b>14.</b> How do you run a second terminal alongside the first inside VS Code?</summary>

Click the `+` in the terminal panel or run `Terminal: Create New Terminal`; you can split the active terminal side by side with `Ctrl+Shift+5`.

</details>

<details><summary><b>15.</b> Why does running `uv run pytest` in the integrated terminal behave the same as in a standalone terminal?</summary>

The integrated terminal is a real `bash` session inheriting your environment, so any command that works in a normal Ubuntu terminal works identically here.

</details>

<details><summary><b>16.</b> What is the VS Code command palette and how do you open it?</summary>

A keyboard-driven menu for running any command by name, opened with `Ctrl+Shift+P`; almost every action in the editor is reachable through it.

</details>

<details><summary><b>17.</b> What does Quick Open (`Ctrl+P`) do?</summary>

It lets you jump to any file in the workspace by typing part of its name, making file navigation fast without using the explorer.

</details>

<details><summary><b>18.</b> What does Go to Definition (`F12`) do?</summary>

It jumps from a symbol under the cursor to where that function, class, or variable is defined, even across files in the project.

</details>

<details><summary><b>19.</b> What does Rename Symbol (`F2`) do?</summary>

It renames the symbol under the cursor and updates every reference to it across the project in one operation, instead of you doing a risky find-and-replace.

</details>

<details><summary><b>20.</b> How is `F2` rename safer than a plain text find-and-replace?</summary>

It uses the language server's understanding of scope, so it renames only the actual symbol references and skips unrelated text that happens to share the name.

</details>

<details><summary><b>21.</b> What is multi-cursor editing?</summary>

Placing several insertion points at once so the same edit happens in multiple places simultaneously, for example adding a prefix to many lines.

</details>

<details><summary><b>22.</b> How do you add a cursor on the next occurrence of the current selection?</summary>

Press `Ctrl+D` to select and add a cursor at the next matching occurrence; repeat to keep adding.

</details>

<details><summary><b>23.</b> How do you add cursors above or below the current line?</summary>

Press `Ctrl+Alt+Up` or `Ctrl+Alt+Down` to stack a cursor on the adjacent line.

</details>

<details><summary><b>24.</b> What is the Extensions view and how do you open it?</summary>

The panel for searching, installing, and managing extensions, opened with `Ctrl+Shift+X` or from the activity bar.

</details>

<details><summary><b>25.</b> What does the Python extension add to VS Code?</summary>

It provides Python language support — interpreter selection, IntelliSense via Pylance, debugging, test discovery, and the environment picker in the status bar.

</details>

<details><summary><b>26.</b> What is Pylance?</summary>

The fast language server bundled with the Python extension that supplies code completion, type checking, hover information, and go-to-definition for Python.

</details>

<details><summary><b>27.</b> What does the Ruff extension add?</summary>

It integrates the Ruff linter and formatter into the editor, showing lint diagnostics inline and formatting files on save when configured.

</details>

<details><summary><b>28.</b> What does the Jupyter extension add?</summary>

It lets you create and run `.ipynb` notebooks inside VS Code, connecting to Jupyter kernels and rendering cell output in the editor.

</details>

<details><summary><b>29.</b> What does the Docker extension add?</summary>

It gives a sidebar view of images, containers, and registries plus commands to build, run, and inspect containers, with syntax help for `Dockerfile` and `compose.yaml`.

</details>

<details><summary><b>30.</b> How do you install an extension from the command line?</summary>

Run `code --install-extension <publisher.name>`, for example `code --install-extension charliermarsh.ruff`.

</details>

<details><summary><b>31.</b> What is the difference between installing and enabling an extension?</summary>

Installing downloads the extension to your machine, while enabling activates it; you can keep an extension installed but disabled globally or just for one workspace.

</details>

<details><summary><b>32.</b> Why might you disable an extension for a single workspace?</summary>

To keep a heavy or noisy extension out of projects that do not need it while leaving it active elsewhere, using the per-workspace Disable option in the Extensions view.

</details>

<details><summary><b>33.</b> What is an interpreter in the context of the Python extension?</summary>

The specific `python` executable VS Code uses for IntelliSense, running, and debugging — typically the one inside your project's virtual environment.

</details>

<details><summary><b>34.</b> How do you select the Python interpreter for a workspace?</summary>

Run `Python: Select Interpreter` from the command palette and pick the desired environment, or click the interpreter shown in the status bar.

</details>

<details><summary><b>35.</b> Where does this course's virtual environment live, and what creates it?</summary>

In a `.venv` folder at the project root, created by `uv`; commands are run through `uv run` so the right environment is always used.

</details>

<details><summary><b>36.</b> How do you point VS Code at the `.venv` that `uv` created?</summary>

Run `Python: Select Interpreter` and choose `./.venv/bin/python`; VS Code usually lists it automatically once the folder exists.

</details>

<details><summary><b>37.</b> Why does this course run Python via `uv run` rather than activating the venv?</summary>

`uv run` resolves and uses the project environment automatically for each command, so you avoid forgetting to activate and you always run against the locked dependencies.

</details>

<details><summary><b>38.</b> What is the Run and Debug panel?</summary>

The sidebar view, opened with `Ctrl+Shift+D`, where you start debug sessions, see call stacks, variables, watches, and breakpoints, and pick a debug configuration.

</details>

<details><summary><b>39.</b> What is a breakpoint?</summary>

A marker on a line that pauses execution there when the debugger reaches it, so you can inspect the program's state at that moment.

</details>

<details><summary><b>40.</b> How do you set or toggle a breakpoint on a line?</summary>

Click in the gutter to the left of the line number, or put the cursor on the line and press `F9`.

</details>

<details><summary><b>41.</b> What does Step Over (`F10`) do during debugging?</summary>

It executes the current line fully — including any function it calls — and stops on the next line in the same function.

</details>

<details><summary><b>42.</b> What does Step Into (`F11`) do?</summary>

It descends into the function called on the current line so you can debug that function's body line by line.

</details>

<details><summary><b>43.</b> What does Step Out (`Shift+F11`) do?</summary>

It runs the rest of the current function and pauses again at the line that called it.

</details>

<details><summary><b>44.</b> What does Continue (`F5`) do while paused?</summary>

It resumes running until the next breakpoint is hit or the program ends.

</details>

<details><summary><b>45.</b> How do you inspect a variable's value while paused at a breakpoint?</summary>

Read it in the Variables pane of the Run and Debug panel, or hover the variable in the editor to see its current value.

</details>

<details><summary><b>46.</b> What is a watch expression?</summary>

An expression you add to the Watch pane that the debugger re-evaluates each time execution pauses, so you can track a computed value like `nav / shares` across steps.

</details>

<details><summary><b>47.</b> What is a conditional breakpoint?</summary>

A breakpoint that only pauses when a condition you supply evaluates to true, for example `isin == "LU0123456789"`, so you skip irrelevant iterations.

</details>

<details><summary><b>48.</b> How do you create a conditional breakpoint?</summary>

Right-click the gutter and choose Add Conditional Breakpoint, or right-click an existing breakpoint and choose Edit Breakpoint, then type the condition.

</details>

<details><summary><b>49.</b> What is a logpoint?</summary>

A breakpoint variant that logs a message to the Debug Console instead of pausing, letting you trace values without stopping or editing the code with print statements.

</details>

<details><summary><b>50.</b> How do you add a logpoint?</summary>

Right-click the gutter, choose Add Logpoint, and enter a message; wrap expressions in curly braces, for example `row={row} nav={nav}`.

</details>

<details><summary><b>51.</b> Why is a logpoint often better than adding a temporary `print`?</summary>

It produces no code change, so there is nothing to forget and remove later and no risk of committing stray debug output.

</details>

<details><summary><b>52.</b> What is `launch.json` and where does it live?</summary>

A file in `.vscode/launch.json` that defines named debug configurations — what to run, with which arguments, environment, and interpreter — for the Run and Debug panel.

</details>

<details><summary><b>53.</b> How do you create an initial `launch.json`?</summary>

In the Run and Debug panel click "create a launch.json file" and pick a Python configuration; VS Code scaffolds the file for you to edit.

</details>

<details><summary><b>54.</b> How do you pass command-line arguments to a program in `launch.json`?</summary>

Set the `"args"` array in the configuration, for example `"args": ["--date", "2026-06-12"]` to feed a NAV loader its run date.

</details>

<details><summary><b>55.</b> How can a `launch.json` configuration set environment variables for the debugged process?</summary>

Use the `"env"` object to define variables, or point `"envFile"` at a `.env` file whose contents are loaded before the program starts.

</details>

<details><summary><b>56.</b> You set a breakpoint in a NAV filter that should drop rows with a null ISIN, but it never pauses — what is the first thing to check?</summary>

Confirm that branch actually runs with your input; if no row has a null ISIN, the line is never reached, so add a logpoint earlier or feed test data that triggers the condition.

</details>

<details><summary><b>57.</b> A conditional breakpoint `nav < 0` in your pricing loop never fires — what should you verify first?</summary>

Check the expression evaluates as you expect against the real data types, since a string `"-1.5"` is not less than the integer `0`; cast or compare correctly.

</details>

<details><summary><b>58.</b> In a transfer-agency loader you want to stop only on the row for one investor account — how do you avoid stepping through thousands of rows?</summary>

Set a conditional breakpoint such as `account_id == "TA000457"` so execution pauses only on the iteration you care about.

</details>

<details><summary><b>59.</b> What is the Source Control panel?</summary>

The sidebar view, opened with `Ctrl+Shift+G`, that shows changed files, lets you stage and unstage changes, write commit messages, and run common Git actions.

</details>

<details><summary><b>60.</b> How do you stage a changed file in the Source Control panel?</summary>

Hover the file under Changes and click the `+` (Stage Changes) icon to move it into Staged Changes.

</details>

<details><summary><b>61.</b> How do you commit staged changes in VS Code?</summary>

Type a message in the Source Control input box and press `Ctrl+Enter`, or click the commit checkmark.

</details>

<details><summary><b>62.</b> What is a "task" in VS Code?</summary>

A defined command — like a build, test, or lint run — configured in `.vscode/tasks.json` and launchable from the command palette so you do not retype it.

</details>

<details><summary><b>63.</b> How do you run a configured task?</summary>

Run `Tasks: Run Task` from the command palette and pick the task, or bind the default build task to `Ctrl+Shift+B`.

</details>

<details><summary><b>64.</b> Write a tasks.json command that runs this course's tests through `uv`.</summary>

Define a task with `"command": "uv"` and `"args": ["run", "pytest"]`, which executes `uv run pytest` in the integrated terminal when launched.

</details>

<details><summary><b>65.</b> Why put repeated commands in `tasks.json` instead of retyping them?</summary>

It standardises the exact command for everyone on the project, reduces typos, and makes the action one keystroke away.

</details>

<details><summary><b>66.</b> How does running a notebook in VS Code differ from running it in JupyterLab?</summary>

Both use the same Jupyter kernels and run the same `.ipynb` files, but VS Code embeds notebooks in the editor with its debugging and Git tooling, while JupyterLab is a browser environment with its own multi-document layout.

</details>

<details><summary><b>67.</b> Can a notebook authored in JupyterLab be opened and run in VS Code?</summary>

Yes; `.ipynb` is a shared format and both tools connect to the same kernels, so the notebook runs in either with no conversion.

</details>

<details><summary><b>68.</b> What hidden-state caveat applies to notebooks regardless of which tool you use?</summary>

Cells run out of order leave variables in the kernel that no longer match the visible code, so always Restart Kernel and Run All to confirm the notebook is reproducible.

</details>

<details><summary><b>69.</b> How do you select which kernel a VS Code notebook uses?</summary>

Click the kernel picker at the top right of the notebook and choose the Python environment, such as the project `.venv`.

</details>

<details><summary><b>70.</b> Why might you prefer VS Code notebooks over JupyterLab for a repo you commit to Git?</summary>

VS Code shows notebook diffs and lets you commit from the same window, keeping editing, debugging, and source control in one place.

</details>

<details><summary><b>71.</b> Why might you prefer JupyterLab over VS Code notebooks?</summary>

JupyterLab's browser layout, multiple synchronized views, and rich extension ecosystem suit exploratory, multi-notebook data work some people find more ergonomic.

</details>

<details><summary><b>72.</b> How do you format the current file on demand in VS Code?</summary>

Run `Format Document` from the command palette, which applies the configured formatter — Ruff in this course — to the whole file.

</details>

<details><summary><b>73.</b> How do you enable format-on-save with Ruff for a workspace?</summary>

In `.vscode/settings.json` set `"editor.formatOnSave": true` and set Ruff as the default formatter for Python files via `"editor.defaultFormatter": "charliermarsh.ruff"`.

</details>

<details><summary><b>74.</b> How do you make Ruff fix lint issues and organise imports automatically on save?</summary>

Add `"editor.codeActionsOnSave"` entries such as `"source.fixAll.ruff": "explicit"` and `"source.organizeImports.ruff": "explicit"` to settings.

</details>

<details><summary><b>75.</b> How do you set the default formatter specifically for Python without affecting other languages?</summary>

Use a language-scoped block in settings, `"[python]": { "editor.defaultFormatter": "charliermarsh.ruff" }`, so the choice applies only to Python files.

</details>

<details><summary><b>76.</b> VS Code does not list your project's `.venv` in `Python: Select Interpreter` — what is the first thing to check?</summary>

Make sure the `.venv` folder actually exists at the workspace root by running `uv sync` first; then use "Enter interpreter path" to point at `./.venv/bin/python` if it still does not appear.

</details>

<details><summary><b>77.</b> Ruff is installed but the file is not reformatting on save — what is the first thing to check?</summary>

Verify `"editor.formatOnSave"` is true and that Ruff is set as the Python default formatter, since without a default formatter VS Code does not know what to run on save.

</details>

<details><summary><b>78.</b> Ruff shows lint warnings but never reformats — what distinction explains this?</summary>

Linting and formatting are separate actions; you need format-on-save or `Format Document` configured to apply Ruff's formatter, as diagnostics alone do not rewrite the file.

</details>

<details><summary><b>79.</b> Breakpoints show as hollow grey circles and say "not bound" — what does that usually mean?</summary>

The debugger has not associated the breakpoint with running code, often because the file being executed is not the file with the breakpoint or the wrong interpreter is selected.

</details>

<details><summary><b>80.</b> A hollow "unverified" breakpoint persists when debugging — what should you check first?</summary>

Confirm you launched the debugger (not just ran the file), that the source path matches the executed module, and that the interpreter is the project `.venv`.

</details>

<details><summary><b>81.</b> `code .` returns "command not found" in the terminal — for a Snap install, how do you fix the `PATH`?</summary>

Ensure `/snap/bin` is on your `PATH`; the Snap places the launcher there, and re-logging in or adding it to your shell profile makes `code` resolve.

</details>

<details><summary><b>82.</b> On a `.deb` install, `code` is missing from `PATH` after a manual extract — how do you add it from inside VS Code?</summary>

Run the command palette command `Shell Command: Install 'code' command in PATH`, which creates the launcher so `code .` works from `bash`.

</details>

<details><summary><b>83.</b> What does `Ctrl+Shift+P` give you that menus do not?</summary>

Searchable access to every command, including ones with no menu entry, so you can find an action by typing part of its name instead of hunting through menus.

</details>

<details><summary><b>84.</b> How do you split the editor to view two files side by side?</summary>

Press `Ctrl+backslash` to split the active editor, or drag a tab to the side of the editor area.

</details>

<details><summary><b>85.</b> How do you search across all files in the workspace?</summary>

Open the Search view with `Ctrl+Shift+F` and type your query; results group by file and you can replace across the project.

</details>

<details><summary><b>86.</b> How do you jump to a specific line number?</summary>

Press `Ctrl+G` and type the line number, or type a colon and number in Quick Open.

</details>

<details><summary><b>87.</b> What does the Problems panel show?</summary>

A consolidated list of diagnostics — lint errors, type warnings, syntax issues — across open files, opened with `Ctrl+Shift+M`.

</details>

<details><summary><b>88.</b> What is the status bar interpreter indicator for?</summary>

It shows the currently selected Python interpreter and is a one-click shortcut to `Python: Select Interpreter`.

</details>

<details><summary><b>89.</b> How do you reload the VS Code window without fully restarting it?</summary>

Run `Developer: Reload Window` from the command palette, which restarts the editor process and reloads extensions, often clearing transient glitches.

</details>

<details><summary><b>90.</b> How do you see which extensions are recommended for a project?</summary>

Add an `.vscode/extensions.json` with a `"recommendations"` list; teammates opening the workspace are prompted to install them.

</details>

<details><summary><b>91.</b> Why list the Python, Ruff, Jupyter, and Docker extensions in `extensions.json` for a fund-data repo?</summary>

So a new contributor is prompted to install exactly the tools the project relies on, getting consistent linting, notebooks, and container support from day one.

</details>

<details><summary><b>92.</b> For cross-platform awareness, how does running VS Code natively on Ubuntu differ from a colleague using WSL2 on Windows or macOS?</summary>

On native Ubuntu the editor and terminal run directly on Linux with no bridge, whereas a Windows colleague's Remote-WSL setup runs the editor UI on Windows and the workspace inside a Linux subsystem; the editing experience is similar but the filesystem and paths differ.

</details>

<details><summary><b>93.</b> What does `"files.exclude"` in settings do?</summary>

It hides matching files and folders — like `__pycache__` or `.venv` — from the file explorer to reduce clutter without deleting them.

</details>

<details><summary><b>94.</b> How do you comment or uncomment the current line or selection?</summary>

Press `Ctrl+slash`, which toggles line comments using the current language's comment syntax.

</details>

<details><summary><b>95.</b> How do you move the current line up or down without cutting and pasting?</summary>

Press `Alt+Up` or `Alt+Down` to shift the line, taking the whole selection with it if several lines are selected.

</details>

<details><summary><b>96.</b> How do you trigger code completion (IntelliSense) manually?</summary>

Press `Ctrl+Space` to invoke the suggestion list at the cursor when it does not appear automatically.

</details>

<details><summary><b>97.</b> How do you find all references to a symbol?</summary>

Right-click it and choose Find All References, or press `Shift+F12`, to list every place it is used across the project.

</details>

<details><summary><b>98.</b> How do you run a single test from a Python test file in VS Code?</summary>

With the Python extension's test discovery enabled, use the green run icon beside the test in the editor gutter or the Test Explorer to run just that test.

</details>

<details><summary><b>99.</b> How do you debug a single failing test rather than the whole suite?</summary>

Use the debug icon next to that test in the gutter or Test Explorer, which launches it under the debugger so your breakpoints in the code under test bind.

</details>

<details><summary><b>100.</b> Why prefer keyboard-first workflows like the command palette and Quick Open?</summary>

They keep your hands on the keyboard and let you reach files and commands by name in a couple of keystrokes, which is faster and more accurate than mouse-hunting through menus once the shortcuts are habitual.

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


## Phase 1 · 1.6.1 ACID & isolation levels — 100 self-test questions

<details><summary><b>1.</b> What does the acronym `ACID` stand for?</summary>

`ACID` stands for Atomicity, Consistency, Isolation, and Durability — the four properties a transaction is expected to provide. They are a guarantee bundle: a transaction either applies fully or not at all, never leaves the database in an invalid state, runs as if alone, and survives a crash once committed. In practice "Consistency" is the odd one out because it depends on application-defined invariants, while the other three are database mechanisms.

</details>

<details><summary><b>2.</b> What is atomicity in the context of a database transaction?</summary>

Atomicity means a transaction is all-or-nothing: either every write inside it takes effect, or none of them do. If the transaction aborts halfway — by error, deadlock, or crash — the database rolls back any partial changes so no half-finished work is visible. The mechanism is the ability to discard or undo writes, which is why DDIA notes "atomicity" here really means "abortability".

</details>

<details><summary><b>3.</b> What is durability in the context of a transaction?</summary>

Durability means that once a transaction commits, its writes survive even if the machine crashes or loses power immediately afterward. The database must persist the committed data to non-volatile storage (or replicate it) before reporting success. In Postgres this is achieved by flushing the write-ahead log to disk at commit, so the change can be replayed during crash recovery.

</details>

<details><summary><b>4.</b> What is a write-ahead log (`WAL`) and why does it exist?</summary>

A `WAL` is an append-only log to which the database writes a record of every change *before* it modifies the actual data pages. It exists so that a commit can be made durable cheaply — appending sequentially is fast — and so the database can recover a consistent state after a crash by replaying the log. Postgres stores it under `pg_wal/`; the principle is "log first, apply later".

</details>

<details><summary><b>5.</b> How does the `WAL` make a commit survive a crash?</summary>

At commit time the database forces the WAL records up to that commit point to durable storage, typically via an `fsync`, before acknowledging the client. If the server crashes before the dirty data pages are written, recovery replays the committed WAL records to reconstruct the changes; uncommitted records are ignored or undone. The data pages themselves can be flushed lazily because the log is the authoritative record.

</details>

<details><summary><b>6.</b> Why is sequential `WAL` writing faster than updating data pages directly at commit?</summary>

Appending to the WAL is a sequential write to one growing file, which spinning disks and SSDs both handle far faster than the scattered random writes that updating many data pages in place would require. By making only the small, ordered log durable at commit, the database gets durability without paying for random I/O on the hot path. The heavyweight page writes are deferred and batched by the checkpointer.

</details>

<details><summary><b>7.</b> What is a checkpoint in relation to the `WAL`?</summary>

A checkpoint is a point at which the database flushes all dirty data pages to disk and records that the WAL up to that position is now reflected in the data files. After a crash, recovery only needs to replay WAL written *after* the last checkpoint, bounding recovery time. Checkpoints trade steady background I/O for shorter recovery and for letting old WAL segments be recycled.

</details>

<details><summary><b>8.</b> What does "isolation" promise when several transactions run at once?</summary>

Isolation promises that concurrently executing transactions do not interfere with each other's intermediate state — ideally each runs as if it were the only transaction on the system (serializability). In practice databases offer weaker, cheaper isolation levels that permit certain anomalies, so the real guarantee depends on the level you select. The architect's job is to know exactly what each level still allows.

</details>

<details><summary><b>9.</b> What is a "dirty read"?</summary>

A dirty read happens when one transaction reads a row that another transaction has written but not yet committed. If that other transaction later aborts, the reader has acted on data that never officially existed. For example, an order-processing job that reads an uncommitted NAV value and proceeds would be using a number that may be rolled back seconds later.

</details>

<details><summary><b>10.</b> At which isolation level are dirty reads possible, and where are they prevented?</summary>

Dirty reads are only possible at `READ UNCOMMITTED`; every level at `READ COMMITTED` and above forbids them. This is the most basic isolation guarantee and almost universally provided. Notably Postgres never actually performs dirty reads — its `READ UNCOMMITTED` behaves exactly like `READ COMMITTED`.

</details>

<details><summary><b>11.</b> What is a "dirty write"?</summary>

A dirty write occurs when one transaction overwrites a value that another transaction has written but not yet committed. It corrupts the all-or-nothing logic because two transactions' uncommitted changes get interleaved, often violating an invariant that spans multiple rows. Essentially every isolation level prevents dirty writes, typically by holding a row-level write lock until commit.

</details>

<details><summary><b>12.</b> What is a non-repeatable read (read skew)?</summary>

A non-repeatable read is when a transaction reads the same row twice and sees different committed values because another transaction modified and committed it in between. The first read and second read disagree, even though the reader changed nothing. This breaks any logic that assumes a row stays fixed across the life of a transaction.

</details>

<details><summary><b>13.</b> Give a fund-data failure story for a non-repeatable read.</summary>

A reconciliation job reads a fund's cash balance to start a calculation, does some work, then re-reads the same balance for a cross-check; between the two reads a settlement transaction commits a new balance, so the two reads disagree and the job flags a false break. The data is internally consistent at each moment, but the transaction saw a moving target. Raising the level to `REPEATABLE READ` pins both reads to one snapshot.

</details>

<details><summary><b>14.</b> What is a phantom read?</summary>

A phantom read is when a transaction runs the same query twice and the second run returns rows that did not exist (or no longer exist) the first time, because another transaction inserted or deleted rows matching the predicate. Unlike a non-repeatable read, it concerns the *set* of rows a predicate matches, not a single known row. The classic case is `SELECT COUNT(*) WHERE ...` returning a different count.

</details>

<details><summary><b>15.</b> Give a fund-data failure story for a phantom read.</summary>

A compliance check counts all pending subscription orders for a fund above a threshold to enforce a cap, then re-counts before committing; between the counts another session inserts a new qualifying order, so a phantom appears and the cap is breached even though the check "passed". The query predicate matched a new row that wasn't there at first read. Serializable isolation, or a range lock, closes this gap.

</details>

<details><summary><b>16.</b> What is write skew?</summary>

Write skew is an anomaly where two transactions each read an overlapping set of rows, make decisions based on what they read, and then each write to *different* rows — so neither overwrites the other, but their combined effect violates an invariant that held when each read. It is subtle precisely because there is no direct write-write conflict. The canonical example is two doctors each going off-call because each saw the other still on-call.

</details>

<details><summary><b>17.</b> Give a fund-accounting scenario where write skew corrupts data.</summary>

Two redemption transactions each read a fund cash balance of 100 and a rule "total withdrawals must not exceed the balance"; each independently sees enough cash for its 70 withdrawal and each writes its own withdrawal row, leaving the fund overdrawn by 40. Neither transaction overwrote the other's row, so snapshot isolation sees no conflict, yet the invariant is broken. Only `SERIALIZABLE` (or an explicit lock on the balance) prevents it.

</details>

<details><summary><b>18.</b> Why does snapshot isolation permit write skew but not lost updates on the same row?</summary>

Snapshot isolation gives each transaction a consistent point-in-time view and detects conflicts only when two transactions write the *same* object, which catches lost updates. Write skew involves reads of one set of rows and writes to a *different* set, so there is no first-committer-wins conflict to detect — the dangerous dependency is read-write across rows, which plain snapshot isolation ignores. Serializable Snapshot Isolation adds exactly the missing read-write dependency tracking.

</details>

<details><summary><b>19.</b> What is a lost update?</summary>

A lost update happens when two transactions read the same value, each computes a new value from it, and each writes back — so the second write silently clobbers the first, and one update is lost. A read-modify-write counter increment is the textbook case. Fixes include atomic update statements, explicit `SELECT ... FOR UPDATE` locking, or an isolation level that detects the conflict.

</details>

<details><summary><b>20.</b> How do non-repeatable reads, phantoms, and write skew differ from one another?</summary>

A non-repeatable read concerns a single known row changing value between two reads; a phantom concerns the *membership* of a result set changing because rows are inserted or deleted; write skew concerns two transactions reading overlapping data and writing disjoint data so that a multi-row invariant is broken. They escalate in subtlety: single row, set of rows, then cross-row invariant. Higher isolation levels are needed as you move down that list.

</details>

<details><summary><b>21.</b> What are the four ANSI/ISO SQL isolation levels, from weakest to strongest?</summary>

From weakest to strongest they are `READ UNCOMMITTED`, `READ COMMITTED`, `REPEATABLE READ`, and `SERIALIZABLE`. The ANSI standard defines them by which of three phenomena (dirty read, non-repeatable read, phantom read) each must prevent. The standard sets a floor — an implementation may prevent *more* anomalies than required at a given level.

</details>

<details><summary><b>22.</b> How does the ANSI standard formally define each isolation level?</summary>

ANSI defines the levels by the phenomena they forbid: `READ UNCOMMITTED` allows all three, `READ COMMITTED` forbids dirty reads, `REPEATABLE READ` additionally forbids non-repeatable reads, and `SERIALIZABLE` forbids phantoms too. It specifies what must *not* happen, not how to implement it, which is why vendors differ in mechanism and even in which extra anomalies they happen to prevent. A famous critique (Berenson et al.) showed these phenomenon definitions are ambiguous and miss anomalies like write skew.

</details>

<details><summary><b>23.</b> Why is the ANSI standard's phenomenon-based definition considered flawed?</summary>

Because it defines levels by a short list of named phenomena rather than by serializability, and that list is incomplete and ambiguously worded — it never mentions write skew or lost updates, and it does not cleanly distinguish lock-based from snapshot-based implementations. A 1995 critique by Berenson, Bernstein, Gray, and others demonstrated this and proposed snapshot isolation as a distinct level. The upshot is that two databases can both claim `REPEATABLE READ` yet permit different anomalies.

</details>

<details><summary><b>24.</b> What is snapshot isolation?</summary>

Snapshot isolation gives each transaction a consistent view of the database as of the moment it began (or its first read), so it sees a frozen snapshot and never observes other transactions' concurrent changes. Reads never block writes and writes never block reads, which is why it performs well. It prevents dirty reads, non-repeatable reads, and phantoms but still permits write skew, so it is not the same as serializability.

</details>

<details><summary><b>25.</b> Why is snapshot isolation not the same as `SERIALIZABLE`?</summary>

Snapshot isolation prevents read-anomalies by freezing a consistent view, but it only checks for write-write conflicts on the same object, so it allows write skew and read-only anomalies that a truly serial execution could not produce. Two transactions can each act on a stale view of rows the other modified and still commit. True serializability requires detecting read-write dependencies, which plain snapshot isolation does not do.

</details>

<details><summary><b>26.</b> What is multi-version concurrency control (`MVCC`)?</summary>

`MVCC` is a technique where each update creates a new version of a row rather than overwriting it in place, so different transactions can read different versions according to their snapshot. This lets readers see a consistent old version while writers create newer ones, so reads and writes rarely block each other. Postgres implements snapshot isolation on top of MVCC, keeping old row versions until no snapshot needs them.

</details>

<details><summary><b>27.</b> In an `MVCC` system like Postgres, why do readers not block writers?</summary>

Because a writer creates a new version of a row instead of overwriting the old one, a concurrent reader can continue reading the older version that belongs to its snapshot. The reader never needs a lock on data the writer is changing, so they proceed in parallel. This is the core performance benefit of MVCC and why Postgres avoids the read locks that a pure locking scheme would take.

</details>

<details><summary><b>28.</b> What is the cost of `MVCC` keeping old row versions around?</summary>

Old, no-longer-visible row versions ("dead tuples") accumulate and consume disk space and slow scans until they are cleaned up. Postgres reclaims them with `VACUUM` (and autovacuum); a long-running transaction can hold back the cleanup horizon and cause bloat. So MVCC trades simple concurrency for a maintenance obligation and sensitivity to long transactions.

</details>

<details><summary><b>29.</b> What is the default isolation level in PostgreSQL?</summary>

`READ COMMITTED` is the default isolation level in PostgreSQL. Each statement in a `READ COMMITTED` transaction sees a fresh snapshot taken at the start of that statement, so it sees data committed before the statement began. You can change it per transaction with `SET TRANSACTION ISOLATION LEVEL ...` or via `default_transaction_isolation`.

</details>

<details><summary><b>30.</b> How many *distinct* isolation levels does PostgreSQL actually implement, and why?</summary>

Postgres accepts all four standard level names but internally implements only three distinct behaviors, because its `READ UNCOMMITTED` mode behaves identically to `READ COMMITTED`. Postgres never returns uncommitted data, so there is no separate weaker behavior to provide. The three real levels are `READ COMMITTED`, `REPEATABLE READ`, and `SERIALIZABLE`.

</details>

<details><summary><b>31.</b> Why does Postgres treat `READ UNCOMMITTED` the same as `READ COMMITTED`?</summary>

Because Postgres's MVCC design never exposes uncommitted row versions to other transactions, so it physically cannot perform a dirty read. Offering a genuinely weaker `READ UNCOMMITTED` would mean building a dirty-read path that the architecture deliberately avoids. The standard permits providing a *stronger* guarantee than requested, so mapping `READ UNCOMMITTED` up to `READ COMMITTED` is conformant.

</details>

<details><summary><b>32.</b> In Postgres `READ COMMITTED`, when is the snapshot for a query taken?</summary>

At `READ COMMITTED`, a new snapshot is taken at the start of *each statement*, so every statement sees all data committed before it began. This is why two `SELECT`s in the same transaction can return different results — each got its own snapshot. It is the source of non-repeatable reads and phantoms at this level.

</details>

<details><summary><b>33.</b> In Postgres `REPEATABLE READ`, when is the snapshot taken?</summary>

At `REPEATABLE READ`, a single snapshot is taken at the time of the first non-transaction-control statement in the transaction, and all subsequent statements use that same snapshot. So the whole transaction sees one frozen point-in-time view of the database. This eliminates non-repeatable reads and phantoms within the transaction.

</details>

<details><summary><b>34.</b> Does PostgreSQL's `REPEATABLE READ` prevent phantom reads?</summary>

Yes — unlike the bare ANSI minimum, Postgres's `REPEATABLE READ` (which is really snapshot isolation) does not allow phantom reads, because the whole transaction reads from one consistent snapshot. The official isolation table marks phantom reads as "allowed by the standard, but not in PostgreSQL". This is a case of Postgres providing a stronger guarantee than the standard requires at that level.

</details>

<details><summary><b>35.</b> What anomaly does Postgres `REPEATABLE READ` still permit?</summary>

It still permits the serialization anomaly known as write skew (and certain read-only anomalies), because it is snapshot isolation and only detects write-write conflicts on the same row. Two transactions reading overlapping data and writing disjoint rows can both commit and break a multi-row invariant. To close that gap you must use `SERIALIZABLE`.

</details>

<details><summary><b>36.</b> What technique does PostgreSQL use to implement `SERIALIZABLE`?</summary>

Postgres implements `SERIALIZABLE` using Serializable Snapshot Isolation (`SSI`), which builds on snapshot isolation by adding runtime checks for the read-write dependency patterns that could produce a non-serializable outcome. It does not fall back to coarse locking; instead it monitors dependencies and aborts a transaction if a dangerous cycle is detected. This gives true serializability while preserving most of snapshot isolation's concurrency.

</details>

<details><summary><b>37.</b> What are predicate locks (`SIReadLock`) in Postgres `SERIALIZABLE`?</summary>

Predicate locks are bookkeeping locks Postgres takes to record which data a serializable transaction *read*, so it can later tell whether another transaction's write would have changed that read had it run first. They appear in `pg_locks` with mode `SIReadLock`. Crucially they do not block other transactions and cannot cause deadlocks — they only flag dependencies used to detect serialization anomalies.

</details>

<details><summary><b>38.</b> Do Postgres `SIReadLock` predicate locks block other transactions?</summary>

No — `SIReadLock` predicate locks never block writes or reads and cannot cause deadlocks; they are purely informational, used by SSI to track read-write dependencies. When a dangerous dependency pattern forms among concurrent serializable transactions, Postgres aborts one of them rather than having blocked it earlier. This non-blocking design is what keeps `SERIALIZABLE` performant compared to two-phase locking.

</details>

<details><summary><b>39.</b> What does `SERIALIZABLE` "buy" you compared to `REPEATABLE READ` in Postgres?</summary>

`SERIALIZABLE` buys you a guarantee that the concurrent transactions produce a result equivalent to *some* serial order, which eliminates write skew and the remaining serialization anomalies that snapshot isolation permits. You no longer have to reason about specific cross-row anomalies — if your transaction is correct run alone, it is correct under concurrency. The price is that some transactions are aborted with a serialization failure and must be retried.

</details>

<details><summary><b>40.</b> What does `SERIALIZABLE` "cost" you in Postgres?</summary>

It costs extra tracking of read-write dependencies (more memory and CPU for predicate locks) and, more importantly, a higher rate of transactions aborted with SQLSTATE `40001` that the application must catch and retry. Under contention these retries can dominate, and the predicate-lock tracking can be coarsened, raising false-positive aborts. So you adopt it where correctness demands it and engineer retry logic accordingly.

</details>

<details><summary><b>41.</b> What is the exact `SQLSTATE` code raised on a serialization failure in Postgres?</summary>

It is `40001`, the standard SQLSTATE for "serialization_failure". Postgres returns it under `REPEATABLE READ` or `SERIALIZABLE` when it cannot guarantee the transaction's result is consistent with a serial order. The application's contract is to roll back and retry the whole transaction when it sees this code.

</details>

<details><summary><b>42.</b> What error message accompanies a `40001` failure caused by a concurrent update?</summary>

Postgres reports `ERROR: could not serialize access due to concurrent update`. This typically arises at `REPEATABLE READ` when a row the transaction tries to update was changed and committed by another transaction after the snapshot was taken. The fix is to retry the transaction, which gets a fresh snapshot.

</details>

<details><summary><b>43.</b> What error message accompanies a `40001` failure caused by read/write dependencies?</summary>

Postgres reports `ERROR: could not serialize access due to read/write dependencies among transactions`. This is the SSI-specific message at `SERIALIZABLE` when the dependency tracker detects a pattern that could not occur in any serial execution. As with the other 40001 case, the correct response is to abort and retry the transaction.

</details>

<details><summary><b>44.</b> What must an application do when it receives SQLSTATE `40001`?</summary>

It must roll back the failed transaction and retry the *entire* transaction from the beginning, because the failure means no consistent serial result was possible this time. A fresh attempt gets a new snapshot and usually succeeds. Retries should be bounded with a cap and backoff so a hot conflict does not loop forever.

</details>

<details><summary><b>45.</b> Why must you retry the whole transaction, not just the failed statement, after `40001`?</summary>

Because the transaction's earlier reads were taken under a snapshot the database has now declared unsafe; re-running a single statement would mix old reads with new data and could still violate serializability. Only by restarting from `BEGIN` does the transaction get a coherent fresh snapshot for all its reads and writes. This is the defining difference between a transactional retry and a naive statement retry.

</details>

<details><summary><b>46.</b> What is the difference between an idempotent retry and a transactional retry?</summary>

A transactional retry re-runs an entire aborted transaction (e.g., after `40001`) because the database guarantees the failed attempt left no committed effect. An idempotent retry is needed when you are unsure whether a prior attempt's effect landed — for example after a network timeout — so the operation is designed to be safe to apply more than once. Serialization-failure retries are transactional; client-side resend-on-timeout retries usually need idempotency.

</details>

<details><summary><b>47.</b> Why does retrying after a network timeout require idempotency rather than just re-execution?</summary>

Because a timeout is ambiguous: the transaction may have actually committed before the acknowledgement was lost, so blindly re-running it could double-apply the effect. Idempotency — via a unique request key, an upsert, or a deduplicated insert — makes a second application a no-op. Without it, a "retry" of a placed fund order could book the order twice.

</details>

<details><summary><b>48.</b> How might you make a fund-order insert idempotent under retries?</summary>

Attach a unique client-supplied idempotency key (or a natural unique constraint like order reference plus account) and enforce it with a `UNIQUE` index, so a retried insert hits a duplicate-key conflict instead of creating a second order. Use `INSERT ... ON CONFLICT DO NOTHING` to turn the duplicate into a safe no-op and return the existing row. This way an ambiguous network retry cannot double-book the order.

</details>

<details><summary><b>49.</b> What is the default isolation level of Microsoft SQL Server (on-premises)?</summary>

On a default on-premises SQL Server install the default is `READ COMMITTED` implemented with locking — readers take short-lived shared locks row by row, so a reader can block a writer and vice versa. This is the pessimistic, lock-based flavor of `READ COMMITTED`. It differs from Postgres, whose `READ COMMITTED` is snapshot-based and non-blocking.

</details>

<details><summary><b>50.</b> What is the default isolation behaviour of Azure SQL Database, and how does it differ from on-premises SQL Server?</summary>

Azure SQL Database has Read Committed Snapshot Isolation (`RCSI`) enabled by default, so its `READ COMMITTED` uses row versioning to give each statement a transactionally consistent snapshot without taking read locks. On-premises SQL Server defaults to lock-based `READ COMMITTED` with `READ_COMMITTED_SNAPSHOT` off. So the same isolation-level name behaves optimistically in Azure SQL but pessimistically on a stock on-prem server.

</details>

<details><summary><b>51.</b> What is the default isolation level of Oracle Database?</summary>

Oracle's default is `READ COMMITTED`, providing automatic statement-level read consistency: each query sees a consistent view as of the time the statement began, reconstructed from undo data. Oracle does not offer a true `READ UNCOMMITTED`, and its `SERIALIZABLE` is implemented as snapshot isolation. Readers never block writers and writers never block readers, similar in spirit to Postgres MVCC.

</details>

<details><summary><b>52.</b> What does Oracle's "statement-level read consistency" mean?</summary>

It means that within a single SQL statement, Oracle guarantees the query sees data as it existed at the moment the statement started, even if other transactions commit changes while the statement runs. Oracle reconstructs older block versions from undo (rollback) data to honor that point-in-time view. At the default `READ COMMITTED`, each statement gets its own consistent point, which is why two statements in one transaction can still differ.

</details>

<details><summary><b>53.</b> Why can the same isolation-level name behave differently across vendors?</summary>

Because the SQL standard defines levels by which anomalies they must forbid, not by implementation, so each vendor chooses locking, MVCC, or snapshot mechanics and may prevent extra anomalies. Postgres `REPEATABLE READ` is snapshot isolation (no phantoms), while a lock-based engine's `REPEATABLE READ` might still allow phantoms; Oracle's `SERIALIZABLE` is snapshot isolation, not true serializability. The level name alone does not tell you the real guarantee.

</details>

<details><summary><b>54.</b> Why does the vendor default difference matter during a database migration?</summary>

Because application code is often written against the *behaviour* of the source database's default, not the level name, so moving to a database with different mechanics can introduce anomalies that "worked" before. For instance, code relying on Postgres's non-blocking snapshot `READ COMMITTED` may deadlock or block under lock-based on-prem SQL Server `READ COMMITTED`, and code that silently depended on Oracle's snapshot `SERIALIZABLE` may see real serialization failures elsewhere. You must re-test concurrency assumptions, not just port DDL.

</details>

<details><summary><b>55.</b> Name one concrete migration consequence of Postgres vs SQL Server `READ COMMITTED` differences.</summary>

Under Postgres, a long-running report at `READ COMMITTED` reads a consistent statement snapshot and never blocks writers; migrating that workload to lock-based on-prem SQL Server `READ COMMITTED` can have the same report acquire shared locks that block or deadlock with concurrent writes. The application that never saw lock contention before suddenly does. Enabling `READ_COMMITTED_SNAPSHOT` on SQL Server restores the snapshot semantics and avoids surprise blocking.

</details>

<details><summary><b>56.</b> What is `SET TRANSACTION ISOLATION LEVEL` used for in Postgres?</summary>

It sets the isolation level for the current transaction, e.g. `SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;` issued right after `BEGIN` and before any query. It only affects that transaction; once a query has run you can no longer change the level for it. To change the session or database default you use `SET default_transaction_isolation` or the server parameter.

</details>

<details><summary><b>57.</b> How do you start a serializable transaction in psql in a single statement?</summary>

You can write `BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;` (or `BEGIN ISOLATION LEVEL SERIALIZABLE;`) which begins the transaction and sets the level in one step. Alternatively `BEGIN;` followed by `SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;` before the first query has the same effect. The level must be set before any data-accessing statement runs.

</details>

<details><summary><b>58.</b> How do you inspect the current transaction's isolation level in Postgres?</summary>

Run `SHOW transaction_isolation;` which returns the level in effect for the current transaction (or session default if none is active). You can also query `SHOW default_transaction_isolation;` to see the configured default for new transactions. These are the quick first checks when an anomaly investigation begins.

</details>

<details><summary><b>59.</b> To run the two-session ACID lab, how do you start the Phase-1 Postgres container and connect?</summary>

Start the container (e.g. `docker compose up -d` or `docker run -d --name pg postgres`) so a Postgres server is listening, then open two terminals and connect each with `psql` to the same database. Two independent `psql` sessions let you interleave `BEGIN`/`SELECT`/`UPDATE`/`COMMIT` statements by hand and watch one transaction observe (or fail to observe) the other. Keeping them side by side is the entire concurrency lab.

</details>

<details><summary><b>60.</b> Why do you need *two* separate psql sessions to demonstrate isolation anomalies?</summary>

Because isolation anomalies are about how one transaction observes another transaction's concurrent activity, which you cannot show within a single serial session. Two sessions let you deliberately interleave statements — begin A, write in A, read in B, commit A, re-read in B — to expose dirty/non-repeatable/phantom reads and write skew. The manual interleaving is what makes the otherwise abstract definitions concrete.

</details>

<details><summary><b>61.</b> How would you reproduce a non-repeatable read at `READ COMMITTED` with two sessions?</summary>

In session A, `BEGIN; SELECT balance FROM fund_cash WHERE id=1;` and leave it open; in session B, `UPDATE fund_cash SET balance=balance-10 WHERE id=1; COMMIT;`; back in session A, re-run the same `SELECT` — it now returns the new value. The two reads in the same transaction disagree because `READ COMMITTED` takes a fresh snapshot per statement. Re-running the experiment at `REPEATABLE READ` makes both reads identical.

</details>

<details><summary><b>62.</b> How would you reproduce a phantom at `READ COMMITTED` with two sessions?</summary>

In session A, `BEGIN; SELECT count(*) FROM orders WHERE fund='X';`; in session B, `INSERT INTO orders(fund) VALUES ('X'); COMMIT;`; in session A re-run the count — it increases, a phantom row appeared. The predicate `fund='X'` now matches a row that did not exist at the first read. At `REPEATABLE READ` in Postgres the second count would stay unchanged.

</details>

<details><summary><b>63.</b> How would you reproduce write skew at `READ COMMITTED` or `REPEATABLE READ`?</summary>

Use a two-row `fund_cash` table and a rule that the sum stays non-negative; in session A and session B each `BEGIN`, each `SELECT` both balances and sees enough total, then A updates row 1 and B updates row 2, and both `COMMIT`. Neither overwrote the other's row, so both commit and the invariant breaks — that is write skew. Repeating at `SERIALIZABLE` causes one of them to abort with `40001`.

</details>

<details><summary><b>64.</b> When you re-run the write-skew interleaving at `SERIALIZABLE`, what happens?</summary>

One of the two transactions commits and the other is aborted with SQLSTATE `40001` and the message about read/write dependencies, because SSI detects the dangerous dependency cycle. The application is expected to retry the aborted transaction, which on its second attempt sees the first transaction's committed effect and correctly refuses to break the invariant. This is the concrete demonstration that `SERIALIZABLE` prevents write skew.

</details>

<details><summary><b>65.</b> What is the right isolation level for a fund-order workload that must never double-book or overdraw, and why?</summary>

For invariants that span multiple rows — total redemptions not exceeding cash, no over-allocation of a capped tranche — `SERIALIZABLE` is the safe default because it is the only level that prevents write skew and phantoms in one stroke. You pay with occasional `40001` retries, which is acceptable for correctness-critical fund accounting. Where a constraint can be expressed as a single-row check or database constraint, a lower level plus explicit locking can suffice.

</details>

<details><summary><b>66.</b> How should a fund-order application respond to a serialization failure?</summary>

It should catch SQLSTATE `40001`, roll back, and transparently retry the whole transaction a bounded number of times with a small backoff, surfacing an error only if retries are exhausted. The retry must restart from `BEGIN` so it reads a fresh snapshot, and any externally visible side effects (emails, downstream messages) must be deferred until commit or made idempotent. Done right, the end user never sees the transient conflict.

</details>

<details><summary><b>67.</b> Why is "is this exactly-once and serializable?" a question an architect cannot delegate?</summary>

Because the answer determines whether the platform can double-book orders, lose updates, or produce NAV figures that auditors will later be unable to reconcile — these are correctness and regulatory risks, not implementation details. Vendors, defaults, and retry behaviour interact subtly, and only someone reasoning at the architecture level can state the guarantee actually delivered end to end. Getting it wrong surfaces as unexplainable corrections that regulators find first.

</details>

<details><summary><b>68.</b> How does choosing the wrong isolation level lead to "unexplainable NAV corrections"?</summary>

If concurrent transactions are allowed an anomaly like write skew or a lost update, the persisted figures can violate an invariant nobody coded for, so a later NAV strikes off corrupted balances and must be corrected without a clear cause in the logs. The defect is non-deterministic and timing-dependent, so it resists reproduction and looks like a mystery. The root cause is an isolation gap, and the only durable fix is architectural, not a one-off data patch.

</details>

<details><summary><b>69.</b> What is a serialization anomaly?</summary>

A serialization anomaly is any outcome of concurrent transactions that could not have arisen from running those transactions one at a time in some order. Write skew and certain read-only anomalies are examples. `SERIALIZABLE` is precisely the level that forbids all serialization anomalies, which is why it is the gold standard for correctness.

</details>

<details><summary><b>70.</b> What is two-phase locking (`2PL`) at a high level?</summary>

`2PL` is a pessimistic concurrency-control protocol where each transaction acquires locks (shared for reads, exclusive for writes) in a growing phase and releases them only in a shrinking phase, typically holding all locks until commit (strict 2PL). Holding locks until commit guarantees serializability but causes readers and writers to block each other and can deadlock. It is the classic alternative to MVCC/SSI.

</details>

<details><summary><b>71.</b> How does `SSI` differ from two-phase locking as a route to serializability?</summary>

`2PL` is pessimistic — it blocks transactions by holding locks until commit, trading concurrency and risking deadlocks to guarantee a serial order. `SSI` is optimistic — it lets transactions run on snapshots without read locks, tracks read-write dependencies, and aborts a transaction only if a non-serializable pattern actually forms. SSI keeps read concurrency high but converts some conflicts into retryable aborts instead of waits.

</details>

<details><summary><b>72.</b> What is the difference between an optimistic and a pessimistic concurrency-control strategy?</summary>

Pessimistic control (e.g. `2PL`) assumes conflicts are likely and prevents them up front by locking and blocking, accepting reduced concurrency. Optimistic control (e.g. snapshot isolation with SSI) assumes conflicts are rare, lets transactions proceed, and detects conflicts at commit, aborting and retrying when one occurs. Optimistic wins under low contention; pessimistic can win when contention is high and retries would thrash.

</details>

<details><summary><b>73.</b> When does an optimistic strategy like `SERIALIZABLE`/`SSI` perform poorly?</summary>

Under high contention on the same data, optimistic control aborts many transactions with `40001`, and the resulting retry storm can waste more work than pessimistic locking would. Each abort discards completed work and the retry may conflict again, so throughput collapses. In such hotspots, explicit locking or queueing the contended operation can outperform repeated optimistic retries.

</details>

<details><summary><b>74.</b> What does `SELECT ... FOR UPDATE` do, and when would you use it?</summary>

`SELECT ... FOR UPDATE` takes an exclusive row-level lock on the selected rows, so any other transaction trying to update or lock them must wait until you commit. You use it to serialize a read-modify-write on specific rows — for example, locking a fund's cash-balance row before debiting it — to prevent lost updates without escalating to `SERIALIZABLE`. It is an explicit, targeted alternative to changing the isolation level.

</details>

<details><summary><b>75.</b> How can explicit locking prevent write skew at a level below `SERIALIZABLE`?</summary>

By taking a lock that materializes the conflict the anomaly relies on — for instance `SELECT ... FOR UPDATE` on the shared rows both transactions read, or a lock on a summary/guard row — you force the two transactions to serialize on that object. The second transaction blocks until the first commits and then re-reads the updated state, so the invariant holds. This is a deliberate trade: more code and lock contention, but no `SERIALIZABLE` retries.

</details>

<details><summary><b>76.</b> What is a "materializing conflict" pattern for avoiding write skew?</summary>

It is deliberately introducing a row whose update both transactions must perform, so a write skew that otherwise touches disjoint rows becomes a detectable write-write conflict on that shared row. For example, both redemption transactions update a single "fund balance guard" row, forcing one to wait or conflict. It converts an invisible read-write dependency into a visible write-write conflict that lower levels catch.

</details>

<details><summary><b>77.</b> Why is `READ COMMITTED` the common default rather than `SERIALIZABLE`?</summary>

Because `READ COMMITTED` offers good concurrency with minimal blocking and no serialization-failure retries, while preventing the most jarring anomaly (dirty reads), which suits the majority of workloads. `SERIALIZABLE` adds correctness for multi-row invariants but at the cost of tracking overhead and application retry logic that many simple workloads do not need. Defaults favor broad usability; the architect overrides them where invariants demand.

</details>

<details><summary><b>78.</b> What does `READ COMMITTED` "silently permit" that can bite you?</summary>

It permits non-repeatable reads, phantoms, lost updates, and write skew — none of which raise an error, so they corrupt data quietly under concurrency. Code that reads a value, decides, and writes can lose updates or break invariants without any signal. The danger is precisely that nothing fails loudly, so the gap is found later in reconciliation or audit.

</details>

<details><summary><b>79.</b> What is a read-only serialization anomaly?</summary>

It is a case where a read-only transaction, by observing a particular snapshot, witnesses a state inconsistent with any serial order even though it writes nothing. Snapshot isolation can produce these, which is one reason it is weaker than serializability. Postgres `SERIALIZABLE` can still abort a read-only transaction (or a concurrent writer) to prevent such anomalies, which surprises people who assume read-only transactions never fail.

</details>

<details><summary><b>80.</b> Can a read-only transaction be aborted with `40001` under Postgres `SERIALIZABLE`?</summary>

Yes — under SSI a read-only `SERIALIZABLE` transaction can be rolled back with `40001` if it participates in a dangerous read-write dependency cycle with concurrent writers. To reduce this, you can declare it `READ ONLY DEFERRABLE`, which makes it wait for a safe snapshot and then never be aborted. This is a Postgres-specific tool for long analytical reads that must be serializable.

</details>

<details><summary><b>81.</b> What does the `READ ONLY DEFERRABLE` transaction mode do in Postgres?</summary>

Declaring a transaction `SERIALIZABLE READ ONLY DEFERRABLE` makes it wait until it can obtain a snapshot guaranteed free of serialization anomalies, after which it runs without ever being aborted and without taking predicate locks. It trades a possible start-up delay for immunity from `40001` and lower overhead. It suits long-running, serializable, read-only reports such as a consistent NAV or holdings snapshot.

</details>

<details><summary><b>82.</b> What is the relationship between MVCC, snapshot isolation, and Postgres `REPEATABLE READ`?</summary>

MVCC is the storage mechanism (multiple row versions); snapshot isolation is the isolation model built on it (each transaction reads one consistent snapshot); and Postgres's `REPEATABLE READ` is its concrete implementation of snapshot isolation. So "Postgres REPEATABLE READ" and "snapshot isolation" are effectively the same guarantee here. `SERIALIZABLE` then layers SSI dependency checks on top of that snapshot model.

</details>

<details><summary><b>83.</b> Why might a transaction that worked under `READ COMMITTED` suddenly fail under `REPEATABLE READ`?</summary>

At `REPEATABLE READ` the transaction uses one snapshot for its whole life, so an `UPDATE` targeting a row another transaction has since modified and committed cannot proceed and raises `could not serialize access due to concurrent update` (`40001`). Under `READ COMMITTED` that same `UPDATE` would re-read the latest row version and succeed. The stricter level surfaces the conflict as an error the application must now retry.

</details>

<details><summary><b>84.</b> What is "first-updater-wins" / "first-committer-wins" in snapshot isolation?</summary>

When two snapshot-isolation transactions update the same row, the database lets only the first to commit keep its change; the second detects that the row changed under it and is aborted (in Postgres, with `40001` at `REPEATABLE READ`). This rule prevents lost updates on the same object. It does not prevent write skew, which involves writes to *different* objects.

</details>

<details><summary><b>85.</b> Why does `REPEATABLE READ` prevent lost updates but `READ COMMITTED` may not?</summary>

At `REPEATABLE READ`, an `UPDATE` to a row changed by a committed concurrent transaction fails with a serialization error instead of silently overwriting, so a read-modify-write cannot lose the other's change unnoticed. At `READ COMMITTED`, the `UPDATE` re-reads the latest version and proceeds, so a naive read-then-write in application code can clobber a concurrent update. To be safe at `READ COMMITTED` you need `SELECT ... FOR UPDATE` or an atomic update expression.

</details>

<details><summary><b>86.</b> How can you avoid a lost update without raising the isolation level at all?</summary>

Use an atomic update that computes the new value in the database, e.g. `UPDATE fund_cash SET balance = balance - 10 WHERE id = 1;`, so the read and write happen as one statement under a row lock. Alternatively lock the row first with `SELECT ... FOR UPDATE` or use a compare-and-set `WHERE balance = :expected`. These avoid the read-modify-write race entirely.

</details>

<details><summary><b>87.</b> What does an optimistic compare-and-set (version column) look like for a fund row?</summary>

You add a `version` column and update with `UPDATE fund SET nav = :new, version = version + 1 WHERE id = :id AND version = :expected;`, then check the affected-row count. If zero rows changed, someone else updated the row first and you re-read and retry. This is application-level optimistic concurrency that works even at `READ COMMITTED`.

</details>

<details><summary><b>88.</b> Why does CMU 15-445 frame isolation levels as a contract between database and application?</summary>

Because the isolation level defines exactly which interleavings the database promises to prevent and which it allows, so the application is responsible for handling everything the chosen level still permits. If you pick `READ COMMITTED`, the database will not stop write skew — that is now your problem to design around. Treating the level as a contract makes explicit who guarantees what, which is the architect's framing.

</details>

<details><summary><b>89.</b> What is timestamp-ordering concurrency control (briefly)?</summary>

Timestamp ordering assigns each transaction a timestamp and ensures conflicting operations are processed in timestamp order, aborting transactions that would violate that order. It is an alternative serializability mechanism to `2PL`, avoiding locks but potentially causing more aborts. MVCC borrows the idea of versions tagged with transaction identifiers to decide visibility.

</details>

<details><summary><b>90.</b> How does MVCC decide which row version a transaction can see?</summary>

Each row version carries the transaction IDs that created and (if applicable) deleted it, and each transaction has a snapshot describing which transactions had committed when the snapshot was taken. A version is visible if its creating transaction is committed-and-visible to the snapshot and its deleting transaction is not. This visibility check is what implements snapshot isolation on top of MVCC.

</details>

<details><summary><b>91.</b> What is transaction ID wraparound and why does it matter for durability/correctness?</summary>

Postgres uses 32-bit transaction IDs for MVCC visibility, and if the oldest unfrozen transaction ID gets too close to the wraparound horizon, old rows could appear to be from the future and become invisible — risking data "loss". Autovacuum freezes old rows to prevent this; if it falls behind, Postgres eventually forces a shutdown to protect data. It is a real operational concern in long-lived, high-write fund databases.

</details>

<details><summary><b>92.</b> A nightly fund-valuation job sees a different cash balance on its second read of the same row — first thing to check?</summary>

First check the isolation level the job runs at: at the default `READ COMMITTED`, each statement gets a fresh snapshot, so a committed concurrent update between the two reads explains the discrepancy. Confirm with `SHOW transaction_isolation;` and look for a concurrent settlement transaction. The fix is to run the job at `REPEATABLE READ` (or `SERIALIZABLE`) so all its reads share one snapshot.

</details>

<details><summary><b>93.</b> A subscription-cap check passes but the cap is breached in production — first thing to check?</summary>

Suspect a phantom or write skew: at `READ COMMITTED` or even snapshot `REPEATABLE READ`, a concurrent transaction can insert a qualifying order or two checks can each pass on stale views and both write. Confirm the isolation level and look for concurrent inserts matching the cap predicate. The remedy is `SERIALIZABLE`, or a guard lock that serializes the cap evaluation.

</details>

<details><summary><b>94.</b> Your application logs frequent `ERROR: could not serialize access ... (SQLSTATE 40001)` — is this a bug?</summary>

Not necessarily — `40001` is the expected, correct signal at `REPEATABLE READ`/`SERIALIZABLE` that the database prevented an anomaly, and the application is supposed to catch it and retry. It becomes a problem only if there is no retry logic (so it surfaces as user errors) or if the rate is so high it indicates a hotspot needing redesign. First check whether a bounded retry-with-backoff is in place around the transaction.

</details>

<details><summary><b>95.</b> Throughput collapses after switching a hot table to `SERIALIZABLE` — what is happening and what do you do?</summary>

High contention on the table is producing many `40001` aborts and retries that thrash, so effective throughput drops. Options: revert most operations to a lower level and protect only the truly invariant-critical path, serialize the hot operation with explicit `SELECT ... FOR UPDATE` or a queue, or reduce the conflict footprint (narrower predicates, shorter transactions). The goal is to apply `SERIALIZABLE` surgically rather than globally.

</details>

<details><summary><b>96.</b> Two psql sessions both `BEGIN` and `UPDATE` the same row and one hangs — what is going on?</summary>

The second `UPDATE` is blocked waiting for the first transaction's row-level write lock, which is held until that transaction commits or rolls back. This is normal lock waiting, not an isolation anomaly; finishing or aborting the first session releases the lock and the second proceeds (or, at `REPEATABLE READ`, fails with `40001`). You can inspect the wait in `pg_locks` and `pg_stat_activity`.

</details>

<details><summary><b>97.</b> A long-running report holds a transaction open and table bloat grows — what is the link to isolation/MVCC?</summary>

An open transaction keeps an old snapshot alive, so MVCC cannot remove dead row versions newer than that snapshot's horizon; `VACUUM` is held back and the table bloats. The report's isolation does not change the data it sees, but its mere longevity pins the cleanup horizon. The fix is to shorten the transaction, use `READ ONLY DEFERRABLE` where appropriate, or run heavy reads against a replica.

</details>

<details><summary><b>98.</b> Why might you route a NAV-history report to a read replica or a deferrable read-only transaction?</summary>

To keep a long, consistent read off the primary's MVCC cleanup horizon and out of the way of write contention, while still getting a consistent snapshot. A `SERIALIZABLE READ ONLY DEFERRABLE` transaction gives a serializable, abort-free snapshot for the report; a replica offloads the I/O entirely (at the cost of replication lag). Either keeps the write-heavy order path healthy.

</details>

<details><summary><b>99.</b> How do isolation levels relate to the regulated requirement that fund records be auditable and reproducible?</summary>

Auditability depends on the database never persisting states that no serial execution could have produced, because an anomaly leaves a record that cannot be explained by any ordering of legitimate operations. Choosing the right level (often `SERIALIZABLE` for invariant-critical paths) ensures every committed state is reconstructible from a serial history. That reproducibility is exactly what auditors and reconciliation rely on.

</details>

<details><summary><b>100.</b> Summarize the one-line difference between snapshot isolation and serializability for a design review.</summary>

Snapshot isolation gives every transaction a consistent point-in-time view and prevents read anomalies and same-row lost updates, but still allows write skew because it ignores cross-row read-write dependencies; serializability additionally guarantees the outcome equals some serial order, eliminating write skew at the cost of retryable serialization failures. In Postgres terms: `REPEATABLE READ` is snapshot isolation, `SERIALIZABLE` adds SSI dependency checks. Use the stronger one wherever a multi-row invariant must hold.

</details>


## Phase 1 · 1.6.3 + 1.6.4 + 1.6.5 The consistency spectrum — 100 self-test questions

<details><summary><b>1.</b> What does "eventual consistency" actually promise?</summary>

It promises only that if writes stop, all replicas will *eventually* converge to the same value — given enough time and no new updates. It says nothing about *when* convergence happens, nor about what any single read returns in the meantime, so a read may legitimately see arbitrarily stale data. The guarantee is a liveness property (it happens someday), not a safety property bounding how stale or out-of-order any given read is.

</details>

<details><summary><b>2.</b> What does eventual consistency explicitly *not* promise?</summary>

It never bounds staleness, never guarantees you read your own writes, and never guarantees monotonic (non-going-backwards) reads. A client can read a fresh value, then read an older value a moment later from a lagging replica, and that is still legal under pure eventual consistency. Because of this, "eventual" is the weakest useful model and almost always needs strengthening with session guarantees for user-facing reads.

</details>

<details><summary><b>3.</b> Why is eventual consistency described as a liveness property rather than a safety property?</summary>

A safety property says "nothing bad ever happens" and must hold at every instant; a liveness property says "something good eventually happens" with no deadline. Eventual consistency only promises convergence *eventually*, which is liveness — you can never point to a moment and prove it has been violated, only observe that it has not yet converged. This is exactly why it is so weak: an unbounded "eventually" is impossible to test against in finite time.

</details>

<details><summary><b>4.</b> What is the practical difference between strong and eventual consistency for a reader?</summary>

Under strong consistency every read returns the most recent committed write, so the reader behaves as if there were a single up-to-date copy. Under eventual consistency a read may return any past value that has not yet been overwritten by convergence, so the reader can see stale or out-of-order data. The cost of strong is higher latency and lower availability during partitions, because the system must coordinate before answering.

</details>

<details><summary><b>5.</b> Define replication lag and name the anomalies it causes.</summary>

Replication lag is the delay between a write committing on the leader and that write becoming visible on a follower/replica. It causes three classic read-after-write anomalies: reading-your-own-writes violations (your write seems lost), monotonic-read violations (time appears to go backwards), and causal violations (effects appear before causes). All three are consequences of asynchronous replication, and all three are fixable with the corresponding session guarantee.

</details>

<details><summary><b>6.</b> What is the "read-your-writes" guarantee?</summary>

Read-your-writes (also called read-after-write) guarantees that once a user has made a write, any subsequent read *by that same user* will see that write or a later state — never an older one. It is a per-user, per-session guarantee, not a global one: other users may still see stale data. It does not require the whole system to be up to date, only that a writer is never shown a version older than their own write.

</details>

<details><summary><b>7.</b> Give a concrete user-visible bug when read-your-writes is violated in a fund platform.</summary>

An investor submits a subscription order, sees the confirmation, then refreshes the order-status page and the order has vanished because the refresh hit a lagging read replica that has not yet received the write. The investor reasonably concludes the order failed and may resubmit, causing a duplicate. This is an architectural read-your-writes violation, not a UI bug, and the fix is to route that user's reads to the leader or to a replica known to have their write.

</details>

<details><summary><b>8.</b> How do you typically implement read-your-writes against read replicas?</summary>

Common techniques: route reads for recently-written keys to the leader for a short window; track the write's log position (LSN/version) on the client and only read from replicas that have caught up to that position; or pin the user's session to a single sufficiently-fresh replica. Azure Cosmos DB does this automatically via *session consistency* using a session token that acts as a minimum-version barrier. The unifying idea is that the read must carry enough information to reject too-old replicas.

</details>

<details><summary><b>9.</b> What is the "monotonic reads" guarantee?</summary>

Monotonic reads guarantees that if a client reads a value, any later read by that client returns that same value or a newer one — never an older one, so the client never sees time go backwards. It is weaker than read-your-writes: it does not require seeing your own writes, only that successive reads do not regress. Without it, a client bouncing between a fresh replica and a lagging replica can watch a comment appear and then disappear.

</details>

<details><summary><b>10.</b> Give a user-visible bug when monotonic reads is violated.</summary>

A user views the NAV-history dashboard and sees yesterday's published NAV, then refreshes and the latest data point disappears because the second read landed on a more-lagged replica. The published value appears to "un-publish," which in a regulated reporting context looks like data corruption or a recalculation. The fix is to pin the session to one replica or require each read to be at least as fresh as the previous one.

</details>

<details><summary><b>11.</b> Why is monotonic reads strictly weaker than read-your-writes?</summary>

Monotonic reads only constrains the *order among a client's reads* (never go backwards), whereas read-your-writes additionally constrains reads relative to that client's *writes* (you must see at least your own write). A system can satisfy monotonic reads while still failing to show you your latest write, if all your reads happen to land on a replica that has your earlier state but lacks the most recent write. So read-your-writes implies a stronger freshness floor.

</details>

<details><summary><b>12.</b> What are "session guarantees" and which ones break first under replication lag?</summary>

Session guarantees are per-client-session consistency promises — read-your-writes, monotonic reads, monotonic writes, and writes-follow-reads — that hold for one client's view without requiring global consistency. They are the first guarantees to break when you add read replicas, because a client whose reads scatter across replicas of differing freshness immediately violates read-your-writes and monotonic reads. They are also the cheapest to restore, which is why session consistency is the most widely used productized level.

</details>

<details><summary><b>13.</b> Define causal consistency.</summary>

Causal consistency guarantees that operations related by a cause-and-effect (happens-before) relationship are seen by every replica in the same causal order; concurrent operations may be seen in any order. Concretely, if write B was made after observing write A, no reader ever sees B without also seeing A. It preserves "question before answer" ordering without requiring a single global total order, making it the strongest model still compatible with high availability.

</details>

<details><summary><b>14.</b> Give a user-visible bug when causal consistency is violated.</summary>

In a messaging or comment thread, a reply ("the NAV looks wrong") appears before the message it answers ("today's NAV is 12.34"), so the conversation reads nonsensically. Causally, the reply *happened-after* the original, but a replica delivered them out of order. Preserving causal order ensures the answer never shows up without the question that prompted it.

</details>

<details><summary><b>15.</b> What does causal consistency allow that linearizability forbids?</summary>

Causal consistency allows concurrent (causally unrelated) operations to be observed in different orders on different replicas, and it does not require any global notion of "most recent." Linearizability forbids both: it imposes a single real-time total order on all operations, so every observer agrees on recency. The payoff of the weaker causal model is that it remains available during network partitions, which linearizability cannot.

</details>

<details><summary><b>16.</b> Why is causal consistency considered the strongest model that survives a partition?</summary>

Because tracking and respecting happens-before relationships only requires propagating causal metadata (e.g., version vectors), not real-time global coordination, replicas can keep accepting reads and writes while a partition heals. Any guarantee stronger than causal — such as linearizability — requires cross-replica agreement on recency, which is exactly what a partition makes impossible. This makes causal the practical ceiling for highly-available systems.

</details>

<details><summary><b>17.</b> Define linearizability.</summary>

Linearizability is a single-object recency guarantee: it makes a replicated register behave as if there were exactly one copy, and every operation appears to take effect atomically at some instant between its invocation and its response, consistent with real-time order. Once a write completes, every subsequent read (anywhere) must return that write or a later one. It is about *recency of one object*, not about transactions spanning multiple objects.

</details>

<details><summary><b>18.</b> Define serializability.</summary>

Serializability is a multi-object transaction-isolation guarantee: the outcome of concurrently executing transactions is equivalent to *some* serial (one-at-a-time) execution of those transactions. It constrains how transactions over many objects interleave, ensuring no anomaly that a serial schedule could not produce. Crucially, the equivalent serial order need not match real-time order, so serializability alone says nothing about recency.

</details>

<details><summary><b>19.</b> What different questions do linearizability and serializability answer?</summary>

Linearizability answers "is this *single* object's value as recent as real time demands?" — a recency question about one register. Serializability answers "did these *multi-object transactions* interleave as if run one at a time?" — an isolation question about transaction ordering. They are orthogonal: a system can be serializable but not linearizable (stale snapshots) or linearizable but not serializable (single-object, no transactions).

</details>

<details><summary><b>20.</b> What is strict serializability and how does it combine the two?</summary>

Strict serializability is serializability plus linearizability's real-time constraint: transactions are equivalent to a serial order, *and* that order respects the real-time order of non-overlapping transactions. It is the gold-standard guarantee delivered by systems like Google Spanner. It answers both questions at once — correct multi-object isolation and single-object recency — at the cost of the most coordination.

</details>

<details><summary><b>21.</b> Can a system be serializable without being linearizable? Give an example.</summary>

Yes. Serializable snapshot isolation can serve a transaction from a slightly stale consistent snapshot: the result is equivalent to *some* serial order, but a read may not reflect the very latest committed write, violating linearizability's real-time recency. PostgreSQL's `SERIALIZABLE` isolation level on a read replica is a practical example — serializable per transaction, yet a replica read can be stale. So "serializable" does not imply "always reads the freshest value."

</details>

<details><summary><b>22.</b> Can a system be linearizable without being serializable? Give an example.</summary>

Yes. A single-object atomic register (e.g., an atomic compare-and-set on one key) can be linearizable — every read sees the latest write in real-time order — yet offer no multi-object transactions at all, so it cannot be serializable across keys. Many key-value stores provide per-key linearizability without cross-key transaction isolation. Linearizability is about one object; serializability is about whole transactions.

</details>

<details><summary><b>23.</b> Why is "strong consistency" an ambiguous term that an architect should pin down?</summary>

"Strong" is marketing/colloquial and can mean linearizability, strict serializability, or merely "stronger than eventual," depending on the vendor. An architect must name the *specific* guarantee actually delivered — linearizable? serializable? read-your-writes? — because each has different latency, availability, and failure semantics. Saying a system is "strongly consistent" without the precise model is exactly the vague claim this lesson trains you to reject.

</details>

<details><summary><b>24.</b> Where does replication lag bite first in a typical web architecture?</summary>

It bites on read-after-write: a user performs a write to the leader, then an immediately-following read is served by an asynchronous replica that has not yet applied the write, so the user's own change appears missing. This is the single most common production complaint when read replicas are added for scaling. The second-most-common is monotonic-read violations as a user's reads scatter across replicas of different freshness.

</details>

<details><summary><b>25.</b> What is the "lost-write window" during a cross-region failover?</summary>

When an asynchronous replica is promoted after the primary region fails, any writes that committed on the old primary but had not yet replicated are lost — that gap is the lost-write window, quantified as the Recovery Point Objective (RPO). With asynchronous replication the RPO is non-zero; with synchronous replication it can be zero but at the cost of write latency and availability. In a fund platform this window is precisely the set of orders or NAV updates that could silently disappear in a DR event.

</details>

<details><summary><b>26.</b> How does the choice between synchronous and asynchronous replication affect the lost-write window?</summary>

Synchronous replication waits for the replica to acknowledge before the write is considered committed, so a failover loses nothing (RPO ≈ 0) but every write pays cross-replica latency and stalls if the replica is unreachable. Asynchronous replication acknowledges the write immediately and ships it later, giving low latency and high availability but a non-zero lost-write window on failover. This is the core durability-versus-latency trade the architect must state explicitly.

</details>

<details><summary><b>27.</b> In a geo-DR setup, why can a lower consistency level mean a larger RPO?</summary>

Weaker consistency levels (session, consistent prefix, eventual) replicate asynchronously across regions, so on a region outage the un-replicated tail of writes is lost — Cosmos DB documents this as an RPO of under 15 minutes for those levels with a single write region. Strong consistency replicates to a global majority before acknowledging, giving RPO = 0 but the highest write latency. Thus the same knob that buys you low-latency writes also widens the data you can lose in a disaster.

</details>

<details><summary><b>28.</b> List Azure Cosmos DB's five consistency levels from strongest to weakest.</summary>

Strong, then Bounded staleness, then Session, then Consistent prefix, then Eventual. This ordered spectrum is the vocabulary Azure design reviews use, sitting between the two extremes most NoSQL stores offer. Each step down trades a weaker guarantee for lower latency, higher availability, and (for reads) higher throughput.

</details>

<details><summary><b>29.</b> Which textbook guarantee does Cosmos DB's Strong level implement?</summary>

Strong implements linearizability — reads are guaranteed to return the most recent committed write, and a client never sees an uncommitted or partial write. It is the single-object recency guarantee, achieved by committing writes to a global majority of regions before acknowledging. This is why multi-region Strong incurs write latency equal to roughly two round-trips between the two farthest regions plus about 10 ms at the 99th percentile.

</details>

<details><summary><b>30.</b> What does Cosmos DB's Bounded staleness level guarantee, and how is the bound configured?</summary>

Bounded staleness guarantees that reads lag the latest write by no more than a configured bound, expressed as *K* versions (updates) of an item or *T* time interval, whichever is hit first. Within the bound, reads are consistent-prefix-ordered; outside regions never exceed *K* or *T* of staleness. If a partition's lag would exceed the bound, Cosmos DB throttles writes for that partition until it catches up.

</details>

<details><summary><b>31.</b> For a multi-region single-write account, what are the minimum K and T values for Bounded staleness?</summary>

Per Microsoft's documentation, for multi-region accounts the minimum bounded-staleness values are 100,000 write operations (*K*) or 300 seconds (*T*). For a single-region account the minimums are much smaller — 10 write operations or 5 seconds. These minimums also define the floor of the achievable RPO when using bounded staleness, because the lag bound is exactly the data you can lose on failover.

</details>

<details><summary><b>32.</b> Which textbook guarantees does Cosmos DB's Session level provide?</summary>

Session consistency provides the session guarantees within a single client session: read-your-writes, monotonic reads, monotonic writes, and writes-follow-reads. It does this with a session token returned after each write, which the client passes on reads as a minimum-version barrier so it never reads data older than its own session. It is the default and most widely used level because it gives user-correct behavior at eventual-consistency-like latency and throughput.

</details>

<details><summary><b>33.</b> How does the Cosmos DB session token actually enforce read-your-writes?</summary>

After each write the server returns an updated session token (a per-partition logical version); the client caches it and attaches it to subsequent reads. If the replica handling the read lacks data for that token, the client retries against another replica — and if needed other regions — until a replica at or beyond that version answers. Because the token is a *minimum* barrier, you always get your own write or newer, never older.

</details>

<details><summary><b>34.</b> What happens to Cosmos DB reads if the client has no session token for a partition?</summary>

If the client never wrote to that physical partition, or its token cache was lost (for example the client was re-created), it holds no token, so reads to that partition behave as Eventual consistency until subsequent writes rebuild the cache. This is a subtle gotcha: a freshly restarted service can momentarily lose read-your-writes guarantees it previously enjoyed. Session tokens are also partition-bound, so a token for one partition does nothing for another.

</details>

<details><summary><b>35.</b> What does Cosmos DB's Consistent prefix level guarantee?</summary>

Consistent prefix guarantees that reads never see writes out of order: if writes happened in order A, B, C, a reader sees some prefix — A, or A,B, or A,B,C — but never A,C without B. Single-document writes get eventual ordering, but multi-document transactional batches are always visible together (all or nothing) and in committed order. So you might see stale data, but never a causally-scrambled sequence.

</details>

<details><summary><b>36.</b> Map Cosmos DB Consistent prefix to a textbook guarantee.</summary>

Consistent prefix corresponds to the consistent-prefix property within causal/sequential consistency: replicas apply writes in an order consistent with their commit order, so no reader observes a later write without the earlier ones it followed. It is weaker than full causal consistency because it does not track cross-session causal dependencies, but it rules out the out-of-order "answer before question" anomaly within a write sequence. It sits above pure eventual, below session.

</details>

<details><summary><b>37.</b> Which textbook guarantee does Cosmos DB's Eventual level implement, and what is its risk?</summary>

Eventual is plain eventual consistency: reads hit any one replica in the region, which may be lagging and may even return values *older* than a previous read — there are no ordering or monotonicity guarantees. The documented risk is that a client can read values older than ones it read before, so it is suitable only where ordering is irrelevant, such as a like count or non-threaded comment count. For fund order status or anything a user expects to persist, it is unsafe.

</details>

<details><summary><b>38.</b> Why does Cosmos DB cost the same request units for writes across all consistency levels but differ for reads?</summary>

Writes always go to a local majority (or, for Strong, a global majority) regardless of level, and the RU cost of a write of a given type is identical across levels. Reads differ because Strong and Bounded staleness must read from two replicas (a local minority quorum) to verify recency, doubling read RU cost and halving read throughput, while Session, Consistent prefix, and Eventual use single-replica reads. So you pay for stronger reads in throughput, not just latency.

</details>

<details><summary><b>39.</b> Why is multi-region-write plus Strong consistency disallowed in Cosmos DB?</summary>

A multi-write-region account cannot guarantee both RPO = 0 and RTO = 0 with strong consistency, so Cosmos DB blocks the combination. Moreover, Strong would require every write to commit to all regions anyway, giving the same write latency as a single-write-region account with no benefit. The intended pattern for multi-write accounts is to read and write in the same region, where cross-region lag is irrelevant.

</details>

<details><summary><b>40.</b> Why is Bounded staleness considered an anti-pattern for multi-region-write Cosmos DB accounts?</summary>

Bounded staleness depends on bounding *cross-region replication lag*, but in a multi-write-region design each application server should read and write in its own local region, where that lag is irrelevant. Coupling correctness to inter-region lag in such a topology adds throttling risk and cost for a guarantee you do not need. Microsoft therefore recommends Session (or local Strong-equivalents) for multi-write accounts and reserves Bounded staleness for single-write-region accounts wanting near-strong cross-region reads.

</details>

<details><summary><b>41.</b> In Cosmos DB, can overriding the consistency level make a strongly-configured account weaker for one request?</summary>

Yes — an SDK client or per-request override can read at Session or weaker even when the account default is Strong, and that read then uses a single replica. The override affects only *reads within the SDK client*; the account still writes and replicates synchronously to every region. So you can opportunistically read cheaper/faster on a strong account, but you cannot make a session-configured account read stronger than its writes were committed.

</details>

<details><summary><b>42.</b> A fund order-status API and a NAV-history dashboard sit on the same platform — which needs the stronger guarantee and why?</summary>

The order-status API needs at least read-your-writes (ideally session or stronger), because an investor must always see an order they just placed; a vanished order triggers duplicate submissions and a compliance incident. The NAV-history dashboard tolerates staleness, because a few seconds' lag on a historical, already-published series has no user-correctness or regulatory impact. Defended in one line: order status is read immediately after a write by the same actor, NAV history is not.

</details>

<details><summary><b>43.</b> Defend in one sentence why NAV history tolerates staleness but order status does not.</summary>

NAV history is a slowly-changing, already-published series read long after it was written, so seconds of lag are invisible; order status is read seconds after the same user wrote it, so any lag manifests as a missing order and an apparent failure. The difference is the temporal gap between write and read by the same actor. That gap, not the data's importance, determines the minimum guarantee.

</details>

<details><summary><b>44.</b> For a transfer-agency register lookup, what consistency consideration matters most?</summary>

A transfer-agency (TA) register lookup is read after registrations/transfers are posted, and it underpins ownership and entitlement decisions, so it needs read-your-writes and monotonic reads at minimum so a just-recorded holding is never shown as absent. For settlement and regulatory ownership questions, you may push toward linearizable/strong reads on the authoritative register, accepting higher latency. The gotcha is serving TA lookups from a lagging analytics replica, which can show stale ownership.

</details>

<details><summary><b>45.</b> Why can a NAV publication that "un-publishes" on refresh be a monotonic-read violation rather than a recalculation?</summary>

If the first read landed on an up-to-date replica showing the published NAV and a later read landed on a more-lagged replica missing it, the value appears to disappear — that is monotonic reads going backwards, not the business recalculating anything. The data was correct; the reads regressed because they scattered across replicas of different freshness. The fix is to pin the dashboard session to one replica or require each read to be at least as fresh as the last.

</details>

<details><summary><b>46.</b> What is the relationship between the session guarantees and causal consistency?</summary>

The session guarantees (read-your-writes, monotonic reads, monotonic writes, writes-follow-reads) are the per-client building blocks; together, writes-follow-reads in particular captures causality within a session. Full causal consistency generalizes this to a system-wide happens-before order across all clients, not just within one session. So session consistency is a pragmatic, per-session approximation of causal ordering that is cheap to implement with tokens or sticky routing.

</details>

<details><summary><b>47.</b> Why does adding read replicas for scale silently downgrade your consistency guarantee?</summary>

A single-leader database read from the leader gives strong reads, but the moment you offload reads to asynchronous replicas, those reads may be stale and unordered relative to the leader — you have silently moved from strong to eventual (or session at best) for replica reads. Nothing in the API announces this change; it manifests only as user-visible anomalies. The architect's job is to name the new, weaker guarantee explicitly rather than assume "strong" still holds.

</details>

<details><summary><b>48.</b> How can a cache in front of a database downgrade consistency, and what is the user-visible symptom?</summary>

A cache returns a previously-stored value that may be older than the current database state, so reads served from cache can violate read-your-writes (your write went to the DB but the cache still serves the old value) and monotonic reads. The user-visible symptom is the classic "I changed it but it still shows the old value," or a value that flips between fresh (cache miss) and stale (cache hit). Mitigations include write-through caching, cache invalidation on write, or short TTLs.

</details>

<details><summary><b>49.</b> A user reports "my submitted order disappeared after I refreshed" — what is the first thing to check?</summary>

First confirm whether the read after submission was served by a different (lagging) replica or cache than the leader the write hit — i.e., suspect a read-your-writes violation from replica lag, not a failed write. Check the order actually committed on the leader (it almost certainly did), then check the read routing and replication lag for that path. The fix is architectural: route post-write reads to the leader or enforce session consistency, not "retry the order."

</details>

<details><summary><b>50.</b> Two users see the same fund's holdings in different orders of recent transactions — which guarantee is missing?</summary>

If unrelated transactions appear in different orders to different users, that is acceptable under causal/eventual models; but if *causally related* events (e.g., a buy then its matching settlement) appear out of order, causal consistency is being violated. Determine whether the swapped events have a happens-before relationship. If they do, you need at least causal consistency (or consistent-prefix ordering for a single write sequence) to forbid the anomaly.

</details>

<details><summary><b>51.</b> Why does linearizability reduce availability during a network partition?</summary>

To guarantee every read returns the latest write in real-time order, a linearizable system must coordinate with a majority/quorum before answering; if a partition isolates a node from that quorum, it must refuse to serve rather than risk returning stale data. Refusing is unavailability. This is the CAP trade in concrete terms: under partition, linearizability forces you to sacrifice availability for some nodes.

</details>

<details><summary><b>52.</b> What is "monotonic writes" and why is it sometimes the missing guarantee?</summary>

Monotonic writes guarantees that writes from a single client are applied to replicas in the order the client issued them, so an earlier write is never overwritten by a later replica applying them out of order. It is part of the session guarantees. It is the missing piece when, for example, two rapid updates to the same record by one client land out of order on a replica, leaving the stale value.

</details>

<details><summary><b>53.</b> What is "writes-follow-reads" and how does it preserve causality?</summary>

Writes-follow-reads (also called session causality) guarantees that if a client reads value X and then makes a write W, W is ordered after the write that produced X on all replicas. This preserves the natural "I saw this, therefore I wrote that" causal chain — for instance, replying to a message only after having read it. It is the session guarantee most directly responsible for keeping "question before answer" ordering intact.

</details>

<details><summary><b>54.</b> Why is "eventually consistent" insufficient language for a design review, and what should you say instead?</summary>

"Eventually consistent" hides whether the system offers read-your-writes, monotonic reads, or any bounded staleness — the very properties that determine whether users see correct behavior. In a review you should state the precise model (e.g., "session consistency with per-user session tokens, RPO under 15 minutes on regional failover"). Naming the exact guarantee turns a hand-wave into a verifiable, costable design decision.

</details>

<details><summary><b>55.</b> How does bounded staleness differ from eventual consistency in what it promises a reader?</summary>

Eventual promises only eventual convergence with no bound, so a read can be arbitrarily stale and even non-monotonic. Bounded staleness promises that reads lag the latest write by at most *K* versions or *T* time, and within that window observe a consistent prefix (no out-of-order writes). So bounded staleness gives you a *quantified worst-case staleness*, which is exactly what makes it usable for "near-strong but available" requirements.

</details>

<details><summary><b>56.</b> Why is bounded staleness attractive for a single-write-region, globally-read fund platform?</summary>

It lets remote regions serve fast local reads while guaranteeing they are never more than *K* versions or *T* seconds behind the write region — near-strong freshness without paying Strong's global-commit write latency. For a fund platform with one authoritative write region and worldwide read access, this caps how stale a remote NAV or position read can be, which you can map directly to a regulatory tolerance. The cost is write throttling if a region falls behind the bound.

</details>

<details><summary><b>57.</b> What does "consistent prefix" forbid that "eventual" permits?</summary>

Consistent prefix forbids out-of-order observation of a write sequence: you can never see a later write without the earlier writes it followed, so no "answer before question." Eventual permits exactly that — a replica could surface a newer value while still missing an older one, scrambling the sequence. Consistent prefix thus rules out the most jarring ordering anomalies while still allowing overall staleness.

</details>

<details><summary><b>58.</b> Map each Cosmos DB level to its textbook guarantee in one pass.</summary>

Strong = linearizability (single-object recency); Bounded staleness = consistent-prefix reads bounded by *K*/*T* staleness; Session = the per-session guarantees (read-your-writes, monotonic reads/writes, writes-follow-reads) via session tokens; Consistent prefix = ordered-prefix (no out-of-order writes) but otherwise eventual; Eventual = eventual consistency with no ordering or monotonicity. This mapping is the core deliverable of the lesson and the vocabulary Azure reviews assume.

</details>

<details><summary><b>59.</b> Why is "the system is consistent" a meaningless claim without qualification?</summary>

"Consistent" spans a whole spectrum — from eventual to causal to linearizable to strict serializable — each with radically different recency, ordering, latency, and availability properties. Saying a system is "consistent" tells you nothing about which anomalies it permits. The architect's discipline is to always attach the specific model name (and, for transactions, the isolation level) so the claim is testable.

</details>

<details><summary><b>60.</b> What is the difference between consistency models (replication recency) and isolation levels (transaction interleaving)?</summary>

Consistency models (linearizability, causal, eventual) describe how *recent and ordered* reads of replicated single objects are. Isolation levels (read committed, snapshot/repeatable read, serializable) describe how concurrent *multi-statement transactions* may interleave and which anomalies (dirty read, write skew, etc.) are prevented. They are different axes — DDIA stresses that conflating them is a common error — and a complete design names both.

</details>

<details><summary><b>61.</b> Why does snapshot isolation not provide linearizability?</summary>

Snapshot isolation serves each transaction from a consistent snapshot taken at start time, so a long-running transaction can read values that are already stale by commit time, and two snapshots can disagree on recency. Linearizability requires every read to reflect the latest committed write in real time, which a fixed snapshot cannot. Hence a system can give strong isolation (snapshot/serializable) yet still return non-linearizable, slightly-stale reads.

</details>

<details><summary><b>62.</b> In DDIA's framing, why is linearizability "the strongest single-object guarantee" yet still not enough for everything?</summary>

Linearizability makes one register behave like a single up-to-date copy, which is the strongest you can say about *one object's recency*. But it says nothing about *atomicity across multiple objects* — you still need serializability/transactions to coordinate multi-object invariants. So a correct multi-object design often needs both linearizability (for recency, e.g., on a lock or counter) and serializability (for transaction isolation).

</details>

<details><summary><b>63.</b> What is a quorum, and how do read/write quorums relate to consistency?</summary>

A quorum is a minimum number of replicas that must respond for an operation to be considered successful. If the read quorum R and write quorum W satisfy R + W > N (total replicas), every read overlaps at least one replica that saw the latest write, enabling strong/linearizable-ish reads. Cosmos DB applies this idea: Strong and Bounded staleness read a local minority (two of four) to verify recency, while weaker levels read a single replica.

</details>

<details><summary><b>64.</b> Why does reading from two replicas (a minority quorum) let Cosmos DB guarantee recency for Strong reads?</summary>

Within a region, writes commit to a local majority — three of four replicas — so any two replicas read together are guaranteed to include at least one carrying the newest data. Consulting two replicas (a local minority quorum) therefore always surfaces the most up-to-date value available in the region. That overlap is precisely why Strong and Bounded staleness reads cost double the RUs of single-replica reads.

</details>

<details><summary><b>65.</b> What does it mean that Cosmos DB "guarantees 100% of reads meet the chosen level," yet you often get stronger?</summary>

The guarantee is a floor: every read satisfies at least the configured level's promise. In practice, when there is little or no concurrent write activity, a Session or Eventual read may happen to return fully up-to-date data — stronger than promised. Cosmos DB exposes a Probabilistically Bounded Staleness (PBS) metric to quantify how often you actually get stronger-than-configured reads, but you must design against the floor, not the lucky case.

</details>

<details><summary><b>66.</b> What is Probabilistically Bounded Staleness (PBS) and why is it useful?</summary>

PBS estimates the probability (in milliseconds) that a read under a weaker level actually returns up-to-date data — "how eventual your eventual really is." Cosmos DB surfaces it as a portal metric so you can see, for a given write/read region pair, how often you are getting effectively strong reads. It helps you judge whether a cheaper level is empirically safe enough for a workload without paying for Strong.

</details>

<details><summary><b>67.</b> Why can two clients legitimately disagree about "the current value" under eventual consistency, and is that a bug?</summary>

Under eventual consistency each client may read a different replica at a different point in convergence, so disagreement is expected, not a bug — the model never promised a single agreed-upon current value at any instant. It only promises they will converge if writes stop. Whether that disagreement is *acceptable* depends on the use case; for a like count it is fine, for an account balance it is not.

</details>

<details><summary><b>68.</b> How would you choose a consistency level for a fund-order status API on Cosmos DB, and what does it cost?</summary>

Choose Session at minimum, so the investor always reads their own just-placed order via the session token; consider Bounded staleness or Strong if regulators require cross-region freshness on order state. The cost of Session is essentially eventual-level latency and throughput, which is cheap; stepping up to Strong roughly halves read throughput and adds multi-region write latency. The memo should state this trade explicitly: Session buys correctness for the writer at negligible cost.

</details>

<details><summary><b>69.</b> How would you choose a consistency level for a NAV-history dashboard, and why?</summary>

Eventual or Consistent prefix is appropriate, because the data is historical, already published, and read long after it was written, so staleness of seconds is invisible to users and regulators. This gives the lowest latency, highest read throughput, and best availability. Choosing Strong here would needlessly halve read throughput and add latency for a guarantee no one needs — the classic over-provisioning of consistency the lesson warns against.

</details>

<details><summary><b>70.</b> What is the latency cost of choosing Strong consistency in multi-region Cosmos DB, concretely?</summary>

For a multi-region Strong account, write latency is approximately two round-trip times between the two farthest regions plus about 10 ms at the 99th percentile, because the write must commit to a global majority before acknowledging. So two regions ~5,000 miles apart pay tens of milliseconds per write just in speed-of-light/RTT terms. Cosmos DB even blocks Strong for accounts spanning more than 5,000 miles by default due to this cost.

</details>

<details><summary><b>71.</b> What is "dynamic quorum" in Cosmos DB Strong consistency and why does it exist?</summary>

With three or more regions on a Strong account, if some regions become slow or unresponsive, Cosmos DB can temporarily remove them from the quorum set to keep committing writes against the remaining majority — preserving Strong without waiting on stragglers. This improves write availability and replication latency during partial regional trouble. Removed regions cannot serve reads until they catch up and rejoin the quorum.

</details>

<details><summary><b>72.</b> Why does the number of regions affect how many can be dropped under dynamic quorum?</summary>

A quorum needs a majority, so the count droppable is total minus majority. In a three- or four-region account the majority is two or three, leaving room to drop only one; in a five-region account the majority is three, so up to two unresponsive regions can be removed. More regions therefore give more slack to tolerate slow/failed regions while still maintaining Strong.

</details>

<details><summary><b>73.</b> What RPO does each Cosmos DB consistency level give on a region-wide outage (single write region)?</summary>

Strong gives RPO = 0 (committed everywhere before ack). Bounded staleness gives RPO equal to its configured *K* and *T*. Session, Consistent prefix, and Eventual give RPO under 15 minutes. Single-region accounts give under 240 minutes for any level. This table is the bridge from "consistency level" to "how much data a disaster can lose," which is what business-continuity planning actually needs.

</details>

<details><summary><b>74.</b> Why is RPO = 0 impossible for a multi-write-region Cosmos DB account?</summary>

With multiple write regions accepting writes independently, a region can commit writes locally that have not yet replicated when it fails, so some recently-committed data is unavoidably lost on failover — RPO cannot be zero, and neither can RTO. That is exactly why Strong (which demands RPO = 0) is disallowed for multi-write accounts. The architecture trades zero data loss for multi-region write availability.

</details>

<details><summary><b>75.</b> Distinguish RPO from RTO in the consistency context.</summary>

RPO (Recovery Point Objective) is how much *data* you can lose — the lost-write window measured in time or versions before the failure point. RTO (Recovery Time Objective) is how long *recovery takes* — how long the service is down before it is restored. Consistency level directly drives RPO (stronger = less data loss); it does not by itself set RTO, which depends on failover automation.

</details>

<details><summary><b>76.</b> An EMT (European MiFID Template) file is generated nightly from positions read off a replica — what consistency risk applies?</summary>

If positions are read from an asynchronous replica that has not caught up to the cut-off time, the EMT file may be built from stale holdings, producing a regulatory file that disagrees with the authoritative book — a monotonic/read-your-writes hazard at the batch level. The fix is to read the EMT inputs from the leader or a replica proven caught up to the snapshot timestamp (a bounded-staleness or LSN check). Stale regulatory output is a compliance issue, not a cosmetic one.

</details>

<details><summary><b>77.</b> Why might a SWIFT message confirming a trade and the internal position update need causal ordering?</summary>

The position update is *caused by* the confirmed trade, so any system observing both must never show the position change without the corresponding confirmation — that is a happens-before relationship requiring at least causal consistency. If a reconciliation view shows an updated position before (or without) the confirming message, it looks like an unexplained, possibly fraudulent change. Causal (or consistent-prefix) ordering forbids that out-of-order appearance.

</details>

<details><summary><b>78.</b> How does an LEI (Legal Entity Identifier) reference-data store's consistency requirement differ from a transactional order store?</summary>

LEI reference data changes rarely and is read widely, so eventual or consistent-prefix consistency is usually fine — a few seconds of staleness on an entity's LEI record rarely affects correctness. A transactional order store is written and immediately read by the same actor and underpins money movement, demanding at least read-your-writes/session. Matching the consistency level to the read/write pattern — not to the data's perceived importance — is the architect's discipline.

</details>

<details><summary><b>79.</b> Why is "ISIN + valuation date" a useful natural key when reasoning about consistency of NAV reads?</summary>

Because each (ISIN, date) NAV is written once and effectively immutable thereafter, reads of historical NAVs are safe under weak consistency — there is no later write to be stale relative to, so eventual reads are correct. Consistency anomalies only bite on *mutable, recently-written* keys. Recognizing which keys are append-only/immutable lets you safely down-tier consistency (and cost) for the bulk of read traffic.

</details>

<details><summary><b>80.</b> A Luxembourg fund's order cut-off relies on a timestamp written then read across regions — what guarantee prevents accepting a late order as on-time?</summary>

You need at least monotonic reads plus read-your-writes (session), and ideally linearizable reads of the authoritative clock/cut-off state, so a region never reads a stale "still open" status after the cut-off has been recorded closed. A weak read could let a late order slip through against a lagging replica that still shows the window open. For a regulated cut-off, the recency of that single status object is exactly a linearizability requirement.

</details>

<details><summary><b>81.</b> Why might a regulated NAV-publication workflow justify Strong consistency despite its latency cost?</summary>

Once an official NAV is published it is authoritative for subscriptions/redemptions, so every consumer must see the same single value with no staleness window — a linearizability requirement on the published value to avoid two investors transacting on different NAVs. The latency/throughput cost of Strong is acceptable because publication is infrequent and correctness is regulatory. This is a case where over-provisioning consistency is the *right* call, justified explicitly.

</details>

<details><summary><b>82.</b> What is the danger of serving transfer-agency register reads from an analytics/reporting replica?</summary>

Analytics replicas are typically the most lagged (optimized for throughput, not freshness), so a TA register lookup there can show stale ownership — a holding that was just transferred may still appear under the old holder. For entitlement, settlement, or regulatory ownership decisions this is a read-your-writes/monotonic-read violation with legal consequences. Authoritative TA lookups should hit the leader or a freshness-bounded replica, reserving the analytics replica for non-authoritative dashboards.

</details>

<details><summary><b>83.</b> When designing read paths, why list the replication topology each path sits on before choosing a guarantee?</summary>

The topology (single-leader, leader-follower replicas, multi-region, cache-fronted) determines which anomalies are even possible and how stale a read can be, so it scopes the minimum guarantee a path must enforce. Choosing a consistency level without knowing whether reads hit the leader, a lagging replica, or a cache leads to either silent staleness bugs or needless over-provisioning. The Do-step's path-by-path table exists precisely to force this mapping.

</details>

<details><summary><b>84.</b> For each violated guarantee, what is the canonical user-visible bug — summarize the three.</summary>

Read-your-writes violated: a user's own just-made change appears missing (e.g., a submitted order vanishes on refresh). Monotonic reads violated: data goes backwards in time (a value seen then unseen on the next read). Causal violated: effect appears before cause (a reply shows up before the message it answers). Being able to attach a concrete bug to each name is a Done-when criterion of this lesson.

</details>

<details><summary><b>85.</b> Why does the lesson insist the fix for a read-your-writes violation is "architectural, not a UI bug"?</summary>

Because the data did commit correctly — the defect is in *where reads are routed* and *what freshness they require*, which is a property of the replication and routing design, not the front-end. Patching the UI to hide the symptom (e.g., re-fetch loops) leaves the underlying anomaly and can mask real failures. The genuine fix is to route post-write reads to a sufficiently-fresh replica or enforce session consistency at the data layer.

</details>

<details><summary><b>86.</b> How does Jepsen's consistency map help an architect communicate guarantees?</summary>

Jepsen provides a precise, agreed-upon vocabulary and hierarchy of consistency models (linearizable, sequential, causal, read-your-writes, monotonic, etc.) and how they relate, so two engineers can refer to "monotonic reads" or "linearizability" and mean exactly the same thing. Using its names avoids the ambiguity of "strong" or "consistent." It is the reference map that disciplines design-review language.

</details>

<details><summary><b>87.</b> Why does causal consistency require tracking metadata, and what metadata is typically used?</summary>

To respect happens-before, a replica must know which writes a given write depends on, which means carrying causal metadata — commonly version vectors (vector clocks) or dependency lists — so it can withhold a write until its dependencies are applied. Without that metadata it cannot tell which orderings are causal versus concurrent. The overhead of this metadata is the price of causal ordering, and it is why causal is more expensive than eventual but cheaper than linearizable.

</details>

<details><summary><b>88.</b> Why is sequential consistency stronger than causal but weaker than linearizable?</summary>

Sequential consistency requires all clients to agree on a *single total order* of operations consistent with each client's program order, but it does *not* require that order to match real time. Causal only orders causally-related operations (concurrent ones may differ across replicas), so it is weaker. Linearizable adds the real-time constraint on top of a total order, so it is stronger. The ladder is: eventual < causal < sequential < linearizable.

</details>

<details><summary><b>89.</b> A read replica is consistently 30 seconds behind. Which consistency models can it still satisfy and which not?</summary>

A 30-second-lagged replica can still satisfy eventual and consistent-prefix (ordered but stale), and bounded staleness *if* the bound is ≥ 30 seconds; with sticky routing it can give monotonic reads and even read-your-writes for that client. It cannot satisfy linearizability/Strong, because its reads are not real-time recent. The lag is fine or fatal entirely depending on which guarantee the read path requires.

</details>

<details><summary><b>90.</b> What does "consistent prefix preserved but data stale" mean for a fund transaction feed?</summary>

It means a consumer reading the feed sees transactions in their true committed order but possibly trailing the latest — e.g., it has processed transactions up to 10:00:00 correctly ordered, while the leader is at 10:00:05. No transaction appears out of order or skipped within the prefix, so ordering-dependent logic (running balances) stays correct; only the *frontier* is stale. This is exactly why consistent prefix is acceptable for ordered event processing where some lag is tolerable.

</details>

<details><summary><b>91.</b> Why is "exactly the latest write everywhere instantly" physically impossible across regions?</summary>

Information cannot propagate faster than the speed of light, so a write in one region cannot be reflected in a distant region until at least the one-way latency has elapsed; "instant global recency" would violate physics. Strong consistency copes by *waiting* (paying that latency) before acknowledging, not by avoiding it. This physical floor is why every cross-region consistency choice is fundamentally a latency trade.

</details>

<details><summary><b>92.</b> How do you verify a read-your-writes fix actually works?</summary>

Write a value, then immediately issue the read through the *same* path a user would, repeatedly and across replica routing, asserting the read always returns the value just written or newer. Inject replica lag (or test during real lag) and confirm the read still never regresses below your write. For Cosmos DB Session, confirm the session token is being propagated on the read so stale replicas are rejected.

</details>

<details><summary><b>93.</b> Why can restarting a service reintroduce a consistency anomaly that was previously absent?</summary>

Session-style guarantees often depend on client-side state — a cached session token or LSN watermark — that is lost on restart; without it, the client cannot reject too-stale replicas and reads degrade to eventual until the cache rebuilds. Cosmos DB documents exactly this: a re-created client with an empty token cache reads as Eventual for those partitions until new writes repopulate tokens. The gotcha is intermittent post-deploy "missing write" reports.

</details>

<details><summary><b>94.</b> Summarize the one-line memo conclusion contrasting order-status and NAV-history consistency choices.</summary>

Order status needs Session (read-your-writes) so an investor always sees their just-placed order, at near-zero latency/throughput cost; NAV history needs only Eventual/Consistent prefix because it is historical, already-published, and tolerant of seconds of staleness, buying the best latency, throughput, and availability. Each choice is justified by the temporal gap between write and read by the same actor — not by the data's importance. Stronger than needed wastes throughput; weaker than needed breaks correctness.

</details>

<details><summary><b>95.</b> Why is matching consistency level to read/write *pattern* more reliable than matching it to data *importance*?</summary>

Importance is subjective and tempts you to slap Strong on everything "critical," over-provisioning latency and throughput needlessly; the pattern (is the data read soon after a write by the same actor? is it mutable? is order observable?) objectively determines which anomalies can actually harm correctness. NAV publication is critical yet read long after write, so weak reads of history are safe; order status is mundane yet read immediately after write, so it needs session. Pattern, not gravitas, predicts the anomaly.

</details>

<details><summary><b>96.</b> Why does DDIA argue that "eventual consistency" is a poorly chosen name?</summary>

The word "eventual" describes only the happy ending — convergence once writes stop — while saying nothing about the user-facing anomalies along the way, which is where all the engineering difficulty lives. DDIA suggests "convergence" would be a more honest label, since the hard part is not that replicas converge but the unbounded, unordered staleness they exhibit before they do. The name lulls designers into ignoring read-your-writes and monotonic-read failures that bite real users.

</details>

<details><summary><b>97.</b> After a leader failover, a client that read fresh data now reads stale data from the new leader — which guarantee broke and why?</summary>

Monotonic reads broke: the new leader was an asynchronous follower that had not yet applied the most recent writes, so reads regressed to an older state after the client had already seen newer data. This is a classic failover anomaly — the promotion exposed the lost-write window as a backwards jump in the client's view. Mitigations include waiting for the follower to fully catch up before promotion, or tracking the client's last-seen version and rejecting a leader behind it.

</details>

<details><summary><b>98.</b> Why can a serializable batch report still disagree with the live book in a fund platform, and is that a defect?</summary>

Serializability only guarantees the report is equivalent to *some* serial order, not that its snapshot is real-time current, so a long-running report reading a consistent snapshot can lag writes committed after the snapshot opened. That is not a defect if the report is explicitly an as-of-snapshot view — it is internally consistent, just not linearizable. The defect would be presenting it as "live" when it is a fixed-point-in-time snapshot, which is a labeling problem, not an isolation failure.

</details>

<details><summary><b>99.</b> A reconciliation finds a position update with no matching trade confirmation after a cross-region failover — what consistency explanation should you check first?</summary>

First suspect a consistent-prefix or causal-ordering violation combined with the lost-write window: the failover promoted a region that received the position update's dependency partially, or the confirming write fell inside the un-replicated tail and was lost (non-zero RPO). Check whether the confirmation actually committed before the outage and whether replication ordering was preserved across the failover. The fix is either stronger cross-region ordering (causal/consistent-prefix) or a lower RPO via more synchronous replication for that critical pair.

</details>

<details><summary><b>100.</b> What is the single most common mistake architects make about consistency, per this lesson?</summary>

Assuming "strong" by default — believing replicated platforms still deliver linearizable reads after read replicas, caches, or geo-DR have silently downgraded the actual guarantee to eventual or session. The discipline is to name the guarantee *actually delivered* on each read path and to attach the concrete user-visible bug that the gap permits. Everything else in the lesson — the Cosmos spectrum, the session guarantees, RPO mapping — is tooling for making that named claim precise and defensible.

</details>


## Phase 1 · 1.7.1 + 1.7.2 CAP & PACELC — 100 self-test questions

<details><summary><b>1.</b> What does the acronym CAP stand for, and in what year was the conjecture first stated by Eric Brewer?</summary>

CAP stands for Consistency, Availability, and Partition tolerance, and Brewer presented it as a conjecture in his 2000 PODC keynote. It was later proved as a theorem by Gilbert and Lynch in 2002 under a formal model. The shorthand "pick two of three" comes from this framing, but as the rest of this lesson shows, that shorthand is the single most misunderstood part of distributed-systems folklore.

</details>

<details><summary><b>2.</b> In CAP's formal definitions, what specific property does the "C" stand for?</summary>

The "C" in CAP is linearizability, the strongest single-object consistency model, where every read returns the most recent completed write as if there were a single up-to-date copy of the data. It is not the "C" of ACID (which means satisfying integrity constraints) and not a vague notion of "the data being correct". Confusing CAP-consistency with ACID-consistency is one of the most common errors in design reviews.

</details>

<details><summary><b>3.</b> What does linearizability actually guarantee to a client?</summary>

Linearizability guarantees that once a write completes, every subsequent read (by any client) returns that value or a newer one, so the system behaves as if there is one single copy of the data updated atomically. It gives a real-time ordering: operations appear to take effect at some instant between their invocation and their response. This is why it is also called "atomic consistency" or "strong consistency".

</details>

<details><summary><b>4.</b> In CAP's definitions, what does "A" (availability) precisely require?</summary>

CAP-availability requires that every request received by a non-failing node must result in a non-error response, even when the node cannot reach other nodes. The catch is "non-failing": a node that has crashed is not required to answer, so this is a strict, all-or-nothing definition. This is much stronger than the colloquial "the service is up most of the time" SLA notion of availability.

</details>

<details><summary><b>5.</b> What does "P" (partition tolerance) mean in CAP?</summary>

Partition tolerance means the system continues to operate despite an arbitrary number of messages being dropped or delayed between nodes, i.e. the network splitting into groups that cannot communicate. Because networks genuinely do partition, P is not really optional for any distributed system spanning machines. That is why the real CAP choice is between C and A *during* a partition, not a free pick among all three.

</details>

<details><summary><b>6.</b> Why does DDIA call its section "The Unhelpfulness of CAP"?</summary>

DDIA argues that CAP's definitions are so narrow — a specific consistency model (linearizability), a specific availability definition, and only one fault type (partitions) — that it captures almost nothing of a real system's design space. It excludes latency, node crashes, durability, and weaker consistency models entirely. So while CAP is historically important, using it as a practical classification tool is misleading, which is exactly the chapter's point.

</details>

<details><summary><b>7.</b> Why does DDIA claim most real systems are neither "CP" nor "AP"?</summary>

Because the CP/AP labels assume a system makes a single, fixed choice at partition time, but real systems behave differently per operation, per configuration, and per fault, and most do not even provide linearizability or strict availability to begin with. A database may offer linearizable reads on some paths and stale reads on others. Forcing a whole product into one bucket discards the nuance that actually matters for design.

</details>

<details><summary><b>8.</b> Is "consistency tolerance vs availability" a real CAP choice when the network is healthy?</summary>

No. CAP only forces a choice during a partition; when the network is healthy there is no theorem-mandated tradeoff between C and A. As Brewer noted, because partitions are rare "there is little reason to forfeit C or A when the system is not partitioned". This gap — the everyday, non-partitioned tradeoff — is precisely what PACELC was invented to capture.

</details>

<details><summary><b>9.</b> According to Brewer's "CAP Twelve Years Later", why was the "2 of 3" formulation always misleading?</summary>

Brewer wrote that the "2 of 3" formulation "tended to oversimplify the tensions among properties", because it implies you statically forfeit one property forever. In reality CAP "prohibits only a tiny part of the design space: perfect availability and consistency in the presence of partitions, which are rare". So the choice is situational and only binds during a partition, not as a permanent system label.

</details>

<details><summary><b>10.</b> In Brewer's reframing, what three-step approach does he propose for handling partitions?</summary>

Brewer proposes: (1) detect that a partition has started, (2) enter an explicit partition mode that may limit some operations, and (3) initiate a recovery process when communication is restored, reconciling state and compensating for mistakes made during the partition. This turns CAP from a static label into an operational strategy. It reframes the question as "how do you behave during and after a partition", not "are you CP or AP".

</details>

<details><summary><b>11.</b> Brewer says "latency and partitions are deeply related." What does he mean?</summary>

He means a partition is effectively a time bound on communication: when a node waits for a response and a timeout elapses, it must decide to either keep waiting (sacrificing availability) or proceed without the other side (sacrificing consistency). The timeout threshold is what turns an unbounded delay into a "partition" decision. So latency tuning and partition handling are the same dial viewed at different timescales.

</details>

<details><summary><b>12.</b> What does PACELC stand for, and who formulated it?</summary>

PACELC was formulated by Daniel Abadi (2010 blog post, 2012 IEEE Computer paper) and reads: if there is a Partition (P), choose between Availability (A) and Consistency (C); Else (E), choose between Latency (L) and Consistency (C). It extends CAP by adding the "Else" clause covering normal, non-partitioned operation. The mnemonic captures both the rare failure-time tradeoff and the everyday latency tradeoff.

</details>

<details><summary><b>13.</b> Which half of PACELC did Abadi argue is more important in practice, and why?</summary>

Abadi argued the "Else" half (EL vs EC) matters more in practice because partitions are rare while normal operation is constant, so the latency-versus-consistency tradeoff is the price you pay every single day. The CAP "PA vs PC" half only bites during the unusual event of a network split. This reframes database selection around steady-state latency cost rather than failure-mode folklore.

</details>

<details><summary><b>14.</b> What are the four PACELC category labels a system can carry?</summary>

The four labels are PA/EL, PA/EC, PC/EL, and PC/EC, pairing a partition-time choice (PA or PC) with a normal-operation choice (EL or EC). For example PA/EL means "favour availability under partition, favour latency otherwise", while PC/EC means "favour consistency in both regimes". The pair is what makes PACELC more expressive than CAP's single label.

</details>

<details><summary><b>15.</b> What is the standard PACELC classification of PostgreSQL, and why?</summary>

A single-primary PostgreSQL is classified PC/EC: it favours consistency over availability and over latency in both regimes. Under a partition, a synchronous-replication or single-node setup will refuse or block writes rather than serve divergent data, and in normal operation it provides strong, linearizable-style reads from the primary rather than trading consistency for speed. The everyday cost is the latency of going to the authoritative copy.

</details>

<details><summary><b>16.</b> How is Apache Cassandra classified in PACELC, and what behaviour earns that label?</summary>

Cassandra is the textbook PA/EL system: under a partition it stays available on both sides, and in normal operation it lets you lower latency by reading/writing at low consistency levels (e.g. `ONE`) instead of waiting for a quorum. Its tunable consistency means you choose per-query how much of the L-vs-C tradeoff to pay. This is why Cassandra is Abadi's canonical example of the "Else, Latency" branch.

</details>

<details><summary><b>17.</b> How is Google Spanner classified in PACELC?</summary>

Spanner is PC/EC: it prioritizes strong, externally-consistent (linearizable) reads and writes both under partition and in normal operation. It achieves this with TrueTime — GPS and atomic-clock-bounded timestamps — and Paxos-replicated splits, accepting added commit latency (commit-wait) as the everyday cost. So its "Else" choice is consistency, paid for in latency, not the other way around.

</details>

<details><summary><b>18.</b> How is DynamoDB typically classified in PACELC, and what nuance applies?</summary>

DynamoDB is commonly placed in the PA/EL family because its default reads are eventually consistent and low-latency, and it stays available across partitions. The nuance is that DynamoDB also offers strongly-consistent reads as an option, which cost more and have different availability characteristics, so the label describes the default rather than a fixed behaviour. Some sources put it as PA/EC; the honest statement is "tunable, defaulting toward availability and latency".

</details>

<details><summary><b>19.</b> How is MongoDB usually classified in PACELC, and why is there disagreement?</summary>

MongoDB with default `majority`/primary read and write concerns behaves like PC/EC, because writes go to a primary and acknowledged reads reflect a consistent view; under a partition the minority side steps down and stops accepting writes. Disagreement (some sources say PA/EC) arises because MongoDB is tunable: relaxed read/write concerns trade consistency for latency or availability. The defaults are what justify the PC/EC reading.

</details>

<details><summary><b>20.</b> Why is Cosmos DB awkward to give a single PACELC label?</summary>

Cosmos DB exposes five tunable consistency levels (Strong, Bounded staleness, Session, Consistent prefix, Eventual), so a single PA/EL or PC/EC label hides per-level tradeoffs in both the partition and the latency dimensions. At Strong it leans PC/EC; at Eventual it leans PA/EL; the others sit in between. The single-label classification is therefore only meaningful once you fix the configured consistency level.

</details>

<details><summary><b>21.</b> List Azure Cosmos DB's five consistency levels from strongest to weakest.</summary>

From strongest to weakest they are Strong, Bounded staleness, Session, Consistent prefix, and Eventual. Each step trades a consistency guarantee for lower latency, lower cost (fewer request units consumed on reads), and higher availability. This explicit five-level menu is exactly why a single PACELC label cannot describe Cosmos DB without specifying the level.

</details>

<details><summary><b>22.</b> What does Cosmos DB's "Strong" consistency level guarantee, and at what cost?</summary>

Strong guarantees linearizability: a read always returns the most recent committed write, so clients never see stale or out-of-order data. The cost is that reads are served from a quorum of replicas, which roughly halves read throughput per request unit compared with weaker levels and raises latency, and it constrains multi-region write topologies. It is the level you reach for when correctness must never be sacrificed for speed.

</details>

<details><summary><b>23.</b> What is Cosmos DB's default consistency level, and what does it provide?</summary>

The default is Session consistency, which scopes guarantees to a single client session: within that session you get read-your-own-writes, monotonic reads, and consistent-prefix ordering. It is the most widely used level because it provides intuitive per-client correctness at single-replica read cost. Different sessions, however, may observe each other's writes with some lag.

</details>

<details><summary><b>24.</b> What does Cosmos DB "Bounded staleness" let you configure, and using which parameters?</summary>

Bounded staleness guarantees reads lag the latest write by at most a configured bound, set either as a number of versions/operations (`MaxStalenessPrefix`) or a time interval (`MaxStalenessIntervalInSeconds`). Within that bound reads can be stale, but never more, and writes are always consistently ordered. It is the practical middle ground when Strong is too costly but unbounded staleness is unacceptable for reporting.

</details>

<details><summary><b>25.</b> What is the difference between Cosmos DB "Consistent prefix" and "Eventual"?</summary>

Consistent prefix guarantees reads see writes in order with no gaps — you may see an older prefix of the write sequence but never writes out of order — whereas Eventual makes no ordering guarantee at all and only promises convergence eventually. Both are weaker than Session. Consistent prefix is useful when ordering matters (e.g. a sequence of NAV revisions) but freshness can lag.

</details>

<details><summary><b>26.</b> Why do Cosmos DB Strong and Bounded staleness reads cost roughly twice the request units of weaker levels?</summary>

Because Strong and Bounded staleness must read from a quorum (a minority set of replicas in the four-replica set) to verify the value is current, whereas Session, Consistent prefix, and Eventual can be satisfied from a single replica. Reading multiple replicas consumes more RU per operation, so for the same provisioned throughput you get about half the read throughput. This is the concrete everyday latency/cost manifestation of the "EC" choice.

</details>

<details><summary><b>27.</b> Why does a single-region Azure SQL deployment sit "outside CAP's frame entirely"?</summary>

CAP is a statement about distributed systems that can be partitioned; a single-region, single-node (or tightly-coupled HA) Azure SQL deployment has no network partition between independent replicas to reason about, so the C-vs-A tradeoff simply never arises. There is one authoritative copy, so it is trivially consistent and available except during ordinary downtime, which CAP does not model. Asking "is it CP or AP" is a category error there.

</details>

<details><summary><b>28.</b> Why is "CP vs AP" the wrong frame even for a multi-replica relational database in normal operation?</summary>

Because CP/AP only describes behaviour during a partition, and partitions are rare; in normal operation the relevant tradeoff is latency vs consistency (PACELC's Else clause), which CAP says nothing about. Most of the time you are paying steady-state latency to reach the authoritative copy, not making a partition-time availability choice. So PACELC's EL/EC dimension is the one that actually drives the everyday user experience.

</details>

<details><summary><b>29.</b> A colleague says "we chose an AP database so it's always available." Why is that statement imprecise?</summary>

AP only promises availability *during a partition*; it says nothing about ordinary uptime, node crashes, or operational availability, and "available" in CAP means every non-failing node answers, not that the service meets an SLA. The system can still be down for deployment, overload, or bugs. The precise statement is "during a network partition it favours answering over consistency", which is a much narrower claim.

</details>

<details><summary><b>30.</b> What does Postgres do to writes when a synchronously-replicated standby becomes unreachable?</summary>

With `synchronous_commit = on` and a `synchronous_standby_names` quorum that cannot be met, the primary will block (hang) committing transactions until a required standby acknowledges, rather than commit data that might not survive failover. This is the PC behaviour: it sacrifices availability to preserve consistency/durability guarantees. Operators often mitigate with `ANY n` quorum settings or by relaxing `synchronous_commit`, which shifts the tradeoff.

</details>

<details><summary><b>31.</b> How does Postgres behave on the minority side of a partition in a typical primary/standby setup?</summary>

A standby on the minority side cannot be promoted safely without risking split-brain, so a well-configured cluster keeps it read-only or fences it; the old primary, if isolated, should stop accepting writes (e.g. via a quorum-aware failover controller like Patroni). The system favours not diverging over staying writable — the PC choice. Misconfiguration here is exactly how two primaries (split-brain) and data loss occur.

</details>

<details><summary><b>32.</b> In a Dynamo-style quorum system, what do the parameters N, W, and R control?</summary>

N is the number of replicas a value is stored on, W is the number of replicas that must acknowledge a write, and R is the number that must respond to a read. Choosing W + R > N gives a read overlap that can return the latest value (strong-ish consistency); W + R ≤ N favours availability and latency at the risk of stale reads. Tuning these is how quorum systems slide along the PACELC L/C spectrum.

</details>

<details><summary><b>33.</b> Why does W + R > N not actually guarantee linearizability in a Dynamo-style system?</summary>

Because quorum overlap only guarantees a read touches at least one node with the latest write, not that concurrent operations are totally ordered; without a coordination protocol you can still get read-after-write anomalies, lost updates from concurrent writes, and reads seeing a write that is later rolled back during failure. DDIA covers these "limitations of quorum consistency" explicitly. So sloppy quorums and node failures break the simple overlap argument.

</details>

<details><summary><b>34.</b> What is a "sloppy quorum" and how does it affect consistency?</summary>

A sloppy quorum lets writes go to any W reachable nodes (including ones not in the value's "home" set) during a partition, with hinted handoff to forward them later, which increases availability but means a subsequent read may not overlap the nodes that took the write. So even with W + R > N nominally, you can read stale data. It is a deliberate PA/EL lever: more availability and lower latency, weaker consistency.

</details>

<details><summary><b>35.</b> For fund NAV reporting, why might a PC/EC store be the safer default than a PA/EL one?</summary>

Regulated NAV reporting must not publish a price computed from a stale or divergent view of holdings; a PC/EC store guarantees reads reflect the latest committed state, eliminating "unexplained stale reads" in the official record. A PA/EL store could silently serve a NAV based on out-of-date positions during normal operation, which is hard to defend to an auditor. The price you pay is latency, which is usually acceptable for end-of-day batch NAV.

</details>

<details><summary><b>36.</b> When might an asset-management platform legitimately choose a PA/EL store despite the consistency cost?</summary>

For high-volume, latency-sensitive, non-authoritative workloads — for example a real-time market-data cache, click/telemetry ingestion, or a denormalized read model feeding dashboards — where a few seconds of staleness is harmless and availability/throughput matter more. The authoritative books and records stay in a PC/EC store; the PA/EL store serves derived, tolerant views. Matching the store to the data's regulatory weight is the architect's job.

</details>

<details><summary><b>37.</b> A design review proposes Cassandra as the system of record for transfer-agency shareholder positions. What is your PACELC-grounded objection?</summary>

As a PA/EL store, Cassandra by default trades consistency for latency and availability, so without careful per-query quorum settings a position read could be stale or a concurrent update lost — unacceptable for the authoritative register of who owns what units. You would either steer to a PC/EC store for the system of record, or insist on `QUORUM`/`LOCAL_QUORUM` writes and reads plus lightweight transactions, and document the residual risk. The point is to make the tradeoff explicit, not accept it by default.

</details>

<details><summary><b>38.</b> Why is it wrong to say "Kafka is CP" or "Kafka is AP" without qualification?</summary>

Kafka is a replicated log, not a single-object store, and its consistency depends on configuration: with `acks=all` and a healthy in-sync-replica (ISR) set it favours durability/consistency and will reject writes if too few replicas are in sync, whereas `acks=1` or `unclean.leader.election.enable=true` trades durability for availability and latency. So Kafka spans the PACELC space by configuration. The right answer names the settings, not a single label.

</details>

<details><summary><b>39.</b> What does Kafka's `acks=all` plus `min.insync.replicas` give you in PACELC terms?</summary>

It pushes Kafka toward PC/EC: a produce is only acknowledged once `min.insync.replicas` in-sync replicas have it, so if a partition shrinks the ISR below that threshold the broker rejects writes (`NotEnoughReplicas`) rather than risk data loss. That is the consistency-over-availability choice under partition, and the everyday acknowledgement latency is the EC cost. Loosening either setting moves it back toward EL/PA.

</details>

<details><summary><b>40.</b> How does Redis (single primary with async replicas) classify in PACELC, and what is the risk?</summary>

Default Redis async replication leans PA/EL: it is fast and stays available, but because replication is asynchronous, a failover can lose recently-acknowledged writes that never reached the promoted replica. So it trades consistency for latency and availability. `WAIT` and Redis Enterprise/Raft-based modes can tighten this, but stock Redis is not a safe authoritative store for must-not-lose financial writes.

</details>

<details><summary><b>41.</b> Why does Abadi say the "Else" tradeoff is paid "every day" while the partition tradeoff is paid only occasionally?</summary>

Because partitions are infrequent events, but every single read and write in normal operation either waits for stronger consistency (more latency) or returns faster with weaker guarantees — the L/C dial is engaged continuously. So the EL/EC choice dominates the steady-state user-visible behaviour and cost. This is the core reason PACELC is a better database-selection lens than CAP.

</details>

<details><summary><b>42.</b> Give a concrete example of the latency cost of choosing consistency in PACELC's "Else" case.</summary>

In Cosmos DB, switching reads from Session to Strong forces a quorum read across replicas, roughly halving read throughput per RU and adding cross-replica round-trip latency on every read — a measurable everyday tax for linearizable freshness. Similarly, Spanner's commit-wait adds latency on every write to honour TrueTime bounds. In both cases you pay milliseconds per operation, all day, to guarantee no stale or out-of-order reads.

</details>

<details><summary><b>43.</b> Why is latency considered "the same dial" as partition tolerance rather than a separate concern?</summary>

Because a partition is operationally just a communication delay that exceeds your timeout: choosing a short timeout makes more delays look like partitions (favouring availability/latency), while a long timeout waits for consistency (favouring C, sacrificing availability). So the latency budget you set is what defines when a partition "happens" for your system. Brewer's "latency and partitions are deeply related" is exactly this insight.

</details>

<details><summary><b>44.</b> What is the difference between CAP-consistency and ACID-consistency?</summary>

CAP-consistency is linearizability — a property of how reads and writes are ordered across replicas — whereas ACID-consistency means a transaction moves the database from one valid state to another, satisfying declared integrity constraints (e.g. foreign keys, checks). They are unrelated properties that share a letter. Conflating them is a frequent source of muddled design-review arguments.

</details>

<details><summary><b>45.</b> Does a system providing serializable transactions automatically provide linearizability?</summary>

No. Serializability is about transactions appearing to run in *some* serial order; linearizability is about single-object operations respecting *real-time* order. A system can be serializable without being linearizable (it may serialize to an order in the past), and the strong combination — "strict serializability" — requires both. Spanner's "external consistency" is precisely strict serializability.

</details>

<details><summary><b>46.</b> In CAP terms, what is the difference between a node crash and a network partition?</summary>

CAP models only partitions — dropped/delayed messages between still-running nodes — and treats a partition as the fault to choose around; a node crash is a different fault that CAP's availability definition explicitly excuses (only non-failing nodes must answer). Real systems must handle both, plus slow nodes, disk failures, and clock skew. This narrowness is part of why DDIA finds CAP unhelpful as a complete model.

</details>

<details><summary><b>47.</b> Why is "highly available" in the SLA sense not the same as CAP's "A"?</summary>

SLA availability is a statistical uptime target (e.g. 99.99%) measured over time across all fault types, whereas CAP's A is a binary guarantee that during a partition every non-failing node returns a non-error response. A system can have excellent SLA availability while being "CP" in CAP terms, because partitions are rare. Mixing the two definitions leads people to wrongly equate "CP" with "frequently down".

</details>

<details><summary><b>48.</b> What is "eventual consistency" and where does it sit relative to CAP and PACELC?</summary>

Eventual consistency only promises that, absent new writes, all replicas eventually converge to the same value, with no guarantee about when or what intermediate reads return. It is the weakest common model and is the kind of consistency an AP/EL system offers when favouring availability and latency. It is acceptable for tolerant, derived data but dangerous for authoritative records that must read fresh.

</details>

<details><summary><b>49.</b> What is "read-your-writes" consistency and which Cosmos DB level provides it?</summary>

Read-your-writes guarantees that after a client writes a value, that same client's later reads will see at least that write (never an older value). In Cosmos DB this is provided by Session consistency, scoped to the client's session. It is often the minimum acceptable guarantee for interactive apps, even when global strong consistency is too costly.

</details>

<details><summary><b>50.</b> What is "monotonic reads" consistency, and why does it matter?</summary>

Monotonic reads guarantees a client never sees time go backwards: once it has read a value, subsequent reads won't return an older version. Without it, a client load-balanced across lagging replicas could see a NAV update, then on refresh see the prior NAV — confusing and, in regulated reporting, potentially misleading. Session consistency in Cosmos DB includes this guarantee within a session.

</details>

<details><summary><b>51.</b> Why does DDIA say linearizability has a real performance and availability cost?</summary>

Because providing linearizability requires coordination — replicas must agree on the latest value before responding, typically via a quorum or consensus round-trip — which adds latency in normal operation and forces unavailability on the minority side during a partition. This is the concrete mechanism behind the PACELC EC and PC choices. There is no free linearizability across a network.

</details>

<details><summary><b>52.</b> A team claims their globally-distributed database gives "strong consistency with zero latency penalty." Why be skeptical?</summary>

Because cross-region strong consistency fundamentally requires coordination across the wide-area network — quorum reads or consensus — which adds round-trip latency proportional to inter-region distance; you cannot have linearizable multi-region reads and writes for free. Spanner pays commit-wait; Cosmos Strong pays quorum reads with topology limits. The honest claim is "strong consistency with a bounded, quantifiable latency cost", and you should ask to see the numbers.

</details>

<details><summary><b>53.</b> How would you build the one-table PACELC classification the lesson's "Do" task asks for?</summary>

List the eight stores (Postgres, Cassandra, Kafka, Cosmos DB, DynamoDB, Spanner, Redis, MongoDB) as rows, with columns for the partition choice (PA/PC) and the Else choice (EL/EC) plus a one-line justification each. For tunable systems (Cosmos DB, Cassandra, DynamoDB, MongoDB) record the default behaviour and note the levers. The goal is to defend each row in one sentence without notes, per the "Done when" criteria.

</details>

<details><summary><b>54.</b> For the lesson's classification table, what is a defensible one-line justification for Postgres?</summary>

"Single-primary Postgres is PC/EC: under partition it blocks or fences rather than diverge, and in normal operation it serves authoritative reads from the primary, paying latency for consistency." That one sentence ties both PACELC dimensions to concrete behaviour (synchronous-commit blocking; primary reads). It is exactly the kind of no-notes defence the "Done when" criteria require.

</details>

<details><summary><b>55.</b> What is a defensible one-line PACELC justification for Spanner?</summary>

"Spanner is PC/EC: TrueTime plus Paxos give externally-consistent reads and writes under partition and in normal operation, with commit-wait latency as the everyday cost." This names the mechanism (TrueTime/Paxos), the partition choice (consistency), and the Else cost (commit-wait latency). It defends both halves of the label in one breath.

</details>

<details><summary><b>56.</b> What is a defensible one-line PACELC justification for Cassandra?</summary>

"Cassandra is PA/EL: it stays available on both sides of a partition and lets you lower latency with low consistency levels like `ONE`, trading freshness for speed by default." It captures the partition behaviour and the tunable Else dial. Mentioning the `ONE`/`QUORUM` lever shows you understand the tradeoff is per-query.

</details>

<details><summary><b>57.</b> Why might the Cosmos DB row in your table need a footnote rather than a single label?</summary>

Because Cosmos DB's behaviour depends entirely on the chosen consistency level — Strong is effectively PC/EC, Eventual is PA/EL, and the three middle levels sit in between — so a single cell would misrepresent it. The lesson explicitly asks you to sanity-check this row against Microsoft's documentation and note the per-level nuance. The honest entry says "tunable across five levels; default Session" with the spectrum spelled out.

</details>

<details><summary><b>58.</b> What nuance does Microsoft's own Cosmos DB documentation reveal that a single PACELC label hides?</summary>

It reveals five distinct, formally-defined levels each with different consistency, latency, throughput (RU), and availability characteristics, plus regional-topology constraints (e.g. Strong limits multi-region writes). So the C/A and L/C tradeoffs are configurable per account or per request, not fixed. A one-letter label collapses a genuine five-point spectrum into a single, lossy point.

</details>

<details><summary><b>59.</b> Why is Kafka's PACELC classification best stated as "configuration-dependent"?</summary>

Because Kafka's durability/consistency depends on producer `acks`, `min.insync.replicas`, and `unclean.leader.election.enable`: tighten them and it behaves PC/EC (reject writes when ISR is too small), loosen them and it behaves PA/EL (stay writable, risk loss). There is no single correct label without the config. Stating the settings is the architecturally honest answer.

</details>

<details><summary><b>60.</b> In the "Else" tradeoff, what does choosing EL (latency) typically buy and cost a fund-data read API?</summary>

Choosing EL buys lower response times and higher throughput by reading from a nearby or single replica without coordination, which is great for tolerant dashboards and caches. The cost is potential staleness — a read may miss the most recent write — which is unacceptable for authoritative figures like a published NAV or a confirmed transfer-agency position. The architect places EL workloads only on derived, non-authoritative data.

</details>

<details><summary><b>61.</b> What is the relationship between consensus algorithms (like Raft/Paxos) and linearizability?</summary>

Consensus algorithms let a set of nodes agree on a single ordered log of operations even under failures, and serving reads/writes through that agreed order is how systems implement linearizable, fault-tolerant state. So linearizability is typically built on top of consensus. The cost is the coordination round-trips, which is the latency you pay in the PACELC Else case.

</details>

<details><summary><b>62.</b> Why does choosing strong consistency reduce availability specifically during partitions (the PC choice)?</summary>

Because to guarantee linearizability a node must confirm it has the latest value, which requires reaching a quorum; if a partition isolates a node from the quorum it cannot safely answer and must return an error or block, reducing availability. The minority side is forced offline to avoid serving stale or divergent data. This is the precise CP behaviour CAP describes.

</details>

<details><summary><b>63.</b> A NAV-calculation service reads positions from a replicated store and occasionally produces a NAV that disagrees with the books. What PACELC question do you ask first?</summary>

First ask which consistency the read path uses in normal operation (the Else choice): if it reads from a lagging replica with eventual/EL consistency, it can compute on stale positions even with no partition present. The fix is to route authoritative NAV reads to strong/EC consistency or the primary, accepting the latency. Only after ruling out everyday staleness do you investigate partition-time behaviour.

</details>

<details><summary><b>64.</b> How does an asynchronous read replica produce stale reads with no partition involved at all?</summary>

An async replica applies the primary's changes after a replication lag, so a read served from it can reflect an older state even though the network is perfectly healthy — this is pure EL behaviour, not a CAP partition. The lag grows under write load or replica I/O pressure. This is why "CP vs AP" misses the real-world bug: it is a latency/consistency (Else) issue.

</details>

<details><summary><b>65.</b> What does it mean that "PACELC subsumes CAP"?</summary>

It means PACELC contains CAP's partition-time choice (the PA/PC part) and adds the orthogonal normal-operation choice (the EL/EC part), so every CAP statement is expressible in PACELC but not vice versa. CAP is the special case of PACELC restricted to partition behaviour. That is why PACELC is the more complete framework for comparing real databases.

</details>

<details><summary><b>66.</b> Who turned Brewer's CAP conjecture into a proved theorem, and what model did they use?</summary>

Seth Gilbert and Nancy Lynch proved CAP in 2002, formalizing it in the asynchronous network model where messages can be arbitrarily delayed or dropped (a partition) and showing no protocol can guarantee both linearizable consistency and total availability under such conditions. They also discussed a weaker "delayed-t" or partially-synchronous variant. The proof is what elevated Brewer's PODC conjecture to "theorem" status.

</details>

<details><summary><b>67.</b> A fund's SLA promises "99.99% availability" yet the architecture team labels the store "CP". Is that a contradiction?</summary>

No contradiction: the SLA figure is statistical uptime across all fault types over time, while "CP" describes only the choice made during the rare event of a network partition. A CP store can easily hit 99.99% because partitions are infrequent and brief. The two statements live on different axes — operational uptime versus partition-time C/A behaviour — and conflating them is a classic CAP misreading.

</details>

<details><summary><b>68.</b> A Postgres HA cluster managed by Patroni shows two nodes both claiming to be primary after a network blip. What does CAP/PACELC tell you to check first?</summary>

This is split-brain — the cluster failed to make the CP choice cleanly — so first check the consensus/leader-election layer (Patroni's DCS, e.g. etcd/Consul) for quorum loss and whether fencing/`failsafe_mode` kept the isolated old primary writable. A correct CP setup fences the minority side so only one primary accepts writes. The root cause is almost always a DCS quorum or watchdog/fencing misconfiguration that let availability win when consistency should have.

</details>

<details><summary><b>69.</b> Why can two databases both be "CP" yet behave very differently day to day?</summary>

Because CP only fixes their partition-time choice (favour consistency), saying nothing about normal operation, where one could be EC (strong, higher latency) and another EL (fast, eventually consistent) — radically different everyday behaviour. PACELC distinguishes them via the Else letter. This is the concrete payoff of adding the L/C dimension.

</details>

<details><summary><b>70.</b> What is "strict serializability" and which system in your table provides it?</summary>

Strict serializability combines serializability (transactions appear in some serial order) with linearizability (that order respects real time), so it is the strongest practical transactional guarantee. Spanner provides it under the name "external consistency", using TrueTime to bound timestamp uncertainty. It is the gold standard when both transactional correctness and real-time freshness are required.

</details>

<details><summary><b>71.</b> Why does DDIA argue you should reason about specific consistency models rather than CAP labels?</summary>

Because the design space has many useful intermediate models — read-your-writes, monotonic reads, consistent prefix, causal, bounded staleness, eventual — that CAP's binary frame cannot express, and these are what actually determine whether an application behaves correctly. Picking the weakest model that still satisfies the requirements is the real engineering task. CAP's CP/AP buckets hide all of this nuance.

</details>

<details><summary><b>72.</b> What is causal consistency, and why is it attractive?</summary>

Causal consistency guarantees that operations causally related (e.g. a reply after a post) are seen in that order by all clients, while concurrent operations may be seen in any order. It is attractive because it is the strongest model that can still be provided with high availability under partitions — it does not require global coordination. It is a sweet spot for collaborative and messaging-style workloads.

</details>

<details><summary><b>73.</b> A vendor says their database is "100% available, always consistent, and partition-tolerant." Why is the strong version of this claim impossible?</summary>

Because the CAP theorem proves you cannot have perfect linearizable consistency AND full availability during a network partition; one must yield. A vendor claiming all three in the strong sense is either redefining the terms (e.g. weaker consistency, or "available" meaning SLA uptime) or overselling. The right follow-up is "what exactly happens to reads and writes during a partition?".

</details>

<details><summary><b>74.</b> How do tunable-consistency databases (Cassandra, Cosmos DB, DynamoDB) complicate PACELC classification?</summary>

They let you choose the C/L and C/A tradeoff per request or per account, so the system occupies a *range* of PACELC behaviours rather than a single point — a `QUORUM` Cassandra read is far more consistent than a `ONE` read. Classifying them requires stating the default and the levers, not one fixed label. The lesson's table should record defaults and footnote the tunability.

</details>

<details><summary><b>75.</b> For transfer-agency settlement records, why would you avoid an eventually-consistent read on the dedup/uniqueness check?</summary>

Because an eventually-consistent read might not see a recently-inserted record, so a uniqueness or "already processed" check could pass twice during the replication window, allowing a duplicate subscription or redemption to settle. That is a correctness and regulatory failure, not just a latency annoyance. Such checks belong on strongly-consistent (EC) reads or the primary, accepting the latency cost.

</details>

<details><summary><b>76.</b> What is the practical meaning of Brewer's advice to "enter an explicit partition mode"?</summary>

It means designing the system to detect a partition and deliberately restrict or queue risky operations (e.g. block certain writes, mark data provisional) instead of silently diverging, then reconcile on recovery. This makes partition behaviour a designed, testable feature rather than an emergent accident. For regulated data, that explicit mode plus a documented recovery/reconciliation procedure is auditable.

</details>

<details><summary><b>77.</b> Why is "recovery and compensation" the third pillar of Brewer's partition-handling model?</summary>

Because during a partition both sides may have made progress that conflicts, so on reconnection the system must merge state, resolve conflicts, and possibly compensate for actions taken under partial information (e.g. reverse a tentative allocation). Without an explicit recovery step, a partition leaves permanent inconsistency. Designing the compensation logic up front is what separates a robust AP design from a hopeful one.

</details>

<details><summary><b>78.</b> How does the timeout setting in a client/driver embody the CAP choice in practice?</summary>

A short timeout makes the client give up and either fail (favouring consistency by not proceeding blindly) or fall back to a replica/stale value (favouring availability), while a long timeout waits for the authoritative response (favouring consistency at the cost of responsiveness). So the timeout is where the abstract C-vs-A decision becomes a concrete config value. This is Brewer's "a partition is a time bound on communication" made operational.

</details>

<details><summary><b>79.</b> Why does DDIA caution that linearizability is not always needed even when it feels safer?</summary>

Because linearizability imposes coordination latency and reduces availability under partitions, and many use cases are satisfied by weaker models (causal, read-your-writes), so insisting on it everywhere wastes performance and resilience. The skill is identifying exactly which operations truly require it — typically uniqueness constraints, locks, and leader election. Over-applying strong consistency is a real and common design smell.

</details>

<details><summary><b>80.</b> Which kinds of operations genuinely require linearizability?</summary>

Operations where correctness depends on a single global view of "the latest state": acquiring a lock or lease, electing a single leader, enforcing a uniqueness constraint (e.g. one unique account or ISIN registration), and ordering that must respect real time. These cannot tolerate stale reads without risking split-brain or duplicates. Most other reads can use a weaker, faster model.

</details>

<details><summary><b>81.</b> A reviewer labels your message queue "AP" to justify possible duplicate deliveries. Is the label doing the work?</summary>

Not really — duplicate delivery is a consequence of at-least-once semantics, which is a delivery-guarantee choice, not directly the CAP A/C tradeoff; the AP label is being used as a vague excuse. The right framing is "we accept at-least-once delivery and require idempotent consumers". Hiding a delivery-semantics decision behind a CAP letter obscures the actual design contract.

</details>

<details><summary><b>82.</b> Why does Abadi consider PACELC a better *database-selection* tool than CAP?</summary>

Because database selection is dominated by steady-state latency and consistency behaviour — the Else clause — which CAP ignores entirely, while partition-time behaviour, though important, is a rarer event. PACELC forces you to confront the everyday L/C cost you will actually pay in production. So it aligns the classification with the metric that drives most real procurement decisions.

</details>

<details><summary><b>83.</b> How would you concretely measure the EL-vs-EC latency cost for a candidate store?</summary>

Run identical read benchmarks at two consistency settings — e.g. Cosmos DB Session vs Strong, or Cassandra `ONE` vs `QUORUM` — under the same load, and compare p50/p99 latency and achieved throughput (or RU consumed). The delta is the quantified everyday price of consistency. Capturing these numbers is exactly the "one concrete example" the lesson's "Done when" asks you to defend.

</details>

<details><summary><b>84.</b> Why is it misleading to say "NoSQL is AP and SQL is CP"?</summary>

Because the SQL/NoSQL split is about data model and query language, not consistency: there are strongly-consistent NoSQL systems (Spanner, HBase, Cosmos Strong) and eventually-consistent or async-replica SQL setups. Consistency behaviour follows replication and coordination design, not the query language. The blanket pairing is a folklore shortcut that fails on real systems.

</details>

<details><summary><b>85.</b> What does "linearizability is a recency guarantee" mean?</summary>

It means linearizability is fundamentally about freshness in real time — any read after a write completes must see that write or a later one — rather than about transaction grouping or isolation. It pins each operation to a single point on a global timeline. This recency framing is why it directly conflicts with serving fast, local, possibly-stale reads (the EL choice).

</details>

<details><summary><b>86.</b> Why might bounded staleness be a good fit for an EMT/EPT data distribution feed?</summary>

An EMT/EPT (European MiFID/PRIIPs Template) cost-and-charges feed is consumed downstream where data must be recent and correctly ordered but need not be linearizably fresh to the millisecond; bounded staleness guarantees consumers lag the source by no more than a configured window with ordered writes. That caps how out-of-date a distributed file/record can be while keeping read cost lower than Strong. It is the explicit, auditable freshness bound regulators and counterparties appreciate.

</details>

<details><summary><b>87.</b> Why is "consistent prefix" a relevant guarantee when distributing a sequence of NAV revisions?</summary>

Consistent prefix ensures consumers see NAV revisions in order with no gaps — they may lag, but will never see revision 5 before revision 4 — which prevents a downstream system from acting on an out-of-order or partially-applied sequence. Pure eventual consistency could reorder them. For an ordered event stream like daily NAV corrections, prefix ordering is often the minimum acceptable guarantee.

</details>

<details><summary><b>88.</b> How does LEI/ISIN reference-data replication illustrate the EL-vs-EC tradeoff?</summary>

Reference data such as LEI and ISIN mappings changes slowly and is read constantly, so serving it from low-latency eventually-consistent caches (EL) is usually fine, while the authoritative master that mints or corrects mappings should be strongly consistent (EC) to avoid two conflicting definitions. The architecture splits the hot read path (tolerant, fast) from the system of record (consistent, slower). Matching consistency to the data's role is the recurring lesson.

</details>

<details><summary><b>89.</b> Why is it dangerous to apply a single CP/AP label across an entire microservices fund platform?</summary>

Because different services have different consistency needs — the ledger/positions service needs strong consistency (PC/EC), while a market-data or notifications service can be PA/EL — so one platform-wide label is meaningless and pushes the wrong default onto some services. PACELC, applied per data store, lets each service make the right local tradeoff. The architect classifies stores individually, not the platform as a whole.

</details>

<details><summary><b>90.</b> In CAP, why is partition tolerance described as "not really a choice" for distributed systems?</summary>

Because real networks inevitably drop and delay packets, so any system spanning multiple machines must tolerate partitions or risk total failure when one occurs; you cannot opt out of the network being unreliable. Therefore the genuine decision is between C and A *during* a partition, which is why "pick P plus one of C/A" is the only meaningful reading. Single-node systems sidestep this only by not being distributed.

</details>

<details><summary><b>91.</b> What is the danger of building a system that simply "ignores" partitions (chooses both C and A)?</summary>

A system that pretends partitions don't happen will, when one occurs, either silently diverge (violating consistency while believing it is consistent) or hang unexpectedly (violating availability), with no designed recovery — the worst of both worlds. CAP says you cannot have both during a partition, so ignoring the choice means it gets made for you, badly. Brewer's explicit detect/partition-mode/recover model is the antidote.

</details>

<details><summary><b>92.</b> Why does DDIA stress that CAP only considers one consistency model and one fault type?</summary>

To highlight how narrow CAP is: it uses linearizability as *the* consistency and network partitions as *the* fault, ignoring weaker consistency models, latency, crashes, and other failures that dominate real operations. Decisions made purely on CAP therefore optimize for a corner case while missing everyday behaviour. PACELC and the full menu of consistency models fill that gap.

</details>

<details><summary><b>93.</b> How does the choice of W=1, R=1 in a Dynamo-style store map onto PACELC?</summary>

W=1, R=1 (with W+R ≤ N) is a strong EL/PA stance: writes and reads complete after touching just one replica, minimizing latency and maximizing availability, but reads can easily be stale and concurrent writes can conflict. It is the fastest, least consistent corner of the quorum dial. You would choose it only for tolerant, high-throughput data.

</details>

<details><summary><b>94.</b> How does W=N (or quorum) shift a Dynamo-style store along PACELC?</summary>

Raising W toward N (or using `QUORUM` with W+R>N) moves the store toward EC/PC: more replicas must acknowledge, increasing consistency and durability at the cost of higher write latency and reduced availability if replicas are unreachable. It buys fresher, safer reads for slower writes. This per-operation tunability is why such stores span a PACELC range, not a point.

</details>

<details><summary><b>95.</b> What does it mean operationally that "exactly-once delivery is a myth" in the context of partitions and CAP?</summary>

Network partitions and message loss mean a sender can never know if a message arrived before an acknowledgement was lost, so it must retry, producing at-least-once delivery; true exactly-once *delivery* is impossible over an unreliable network. The practical equivalent is at-least-once delivery plus an idempotent consumer (covered in the next lesson). CAP's partition reality is the root cause of this limitation.

</details>

<details><summary><b>96.</b> When defending a PA/EL classification for DynamoDB in one sentence, what should you say?</summary>

"DynamoDB defaults to eventually-consistent, low-latency reads and stays available across partitions, so it is PA/EL by default, with optional strongly-consistent reads as a per-request lever." That sentence names the default behaviour, both PACELC dimensions, and the tunability caveat. It is defensible without notes, as the "Done when" requires.

</details>

<details><summary><b>97.</b> Why might you classify MongoDB as PC/EC yet still warn it can be tuned weaker?</summary>

With default `majority` write concern and primary reads, MongoDB gives consistent, ordered reads and steps down the minority side on partition (PC/EC), but read/write concerns like `local` or secondary reads trade that for latency or availability, sliding it toward EL/PA. So the label reflects defaults, and the warning reflects the levers. Stating both is the honest, no-notes defence.

</details>

<details><summary><b>98.</b> A stakeholder asks "should we pick a CP or AP database for our golden-source fund ledger?" How do you reframe the question?</summary>

Reframe it with PACELC: "Our ledger needs PC/EC — strong consistency under partition and in normal operation — because regulated positions must never be stale or divergent; the question is which PC/EC store gives acceptable latency, not CP vs AP." That moves the conversation from folklore to the actual everyday tradeoff and the regulatory requirement. You then compare candidate PC/EC stores on measured latency.

</details>

<details><summary><b>99.</b> What is the single most important thing PACELC adds over CAP for an architect's daily work?</summary>

It surfaces the latency-versus-consistency tradeoff that applies during normal, partition-free operation — the cost you actually pay on every read and write — which CAP entirely omits. Since that steady-state behaviour dominates user experience and database selection, the "Else" clause is where most real decisions live. CAP's partition-time choice, while real, is the rarer event.

</details>

<details><summary><b>100.</b> Summarize, in one statement, why "CP vs AP folklore" is dangerous for regulated fund-data store selection.</summary>

Because it frames selection around a rare partition-time choice and ignores PACELC's everyday latency-vs-consistency tradeoff, leading teams to either pay needless latency or, worse, accept unexplained stale reads that corrupt regulated outputs like NAV and positions. The disciplined approach classifies each store with PACELC, matches consistency to the data's regulatory weight, and quantifies the latency cost. That turns a slogan into a defensible architectural decision.

</details>


## Phase 1 · 1.8.1 Idempotency — 100 self-test questions

<details><summary><b>1.</b> What does it mean for an operation to be idempotent?</summary>

An operation is idempotent if applying it more than once produces the same end state as applying it exactly once. The mechanism that matters in pipelines is that retries, replays, and reruns converge on one correct result instead of accumulating duplicates. For example, `SET balance = 100` is idempotent whereas `balance = balance + 10` is not, because the second form's effect depends on how many times it ran.

</details>

<details><summary><b>2.</b> Why is idempotency described as "the single biggest reliability lever" in pipelines?</summary>

Because networks, brokers, and orchestrators all retry on failure, so any non-idempotent step turns an ordinary transient failure into corrupted data. If every step is retry-safe, you can re-run freely without fear, which underpins disaster recovery, replay, and regulated reruns. Without it, a single timeout on a NAV load can double-book trades and force a manual reconciliation.

</details>

<details><summary><b>3.</b> What are the three places in a pipeline where idempotency must hold?</summary>

The source read, the transform, and the sink write — each must be retry-safe on its own. You get an idempotent read by reading a deterministic slice (a fixed date partition rather than "everything new since last time"), an idempotent transform by making it a pure deterministic function of its input, and an idempotent sink write by using upsert/MERGE or overwrite-partition instead of blind append. If any one of the three appends or mutates incrementally, the whole rerun stops being safe.

</details>

<details><summary><b>4.</b> What is an idempotency key?</summary>

An idempotency key is a client-supplied identifier attached to a request or record that lets the server answer "have I already applied this?" deterministically. The mechanism is that the sink stores seen keys (or enforces uniqueness on them) so a retried request with the same key is recognised and not applied twice. Payment APIs like Stripe use exactly this: you send an `Idempotency-Key` header so a retried charge does not bill the customer twice.

</details>

<details><summary><b>5.</b> Why must the idempotency key be supplied by the client rather than generated by the server?</summary>

Because the whole point is to survive a retry where the server may never have seen the first attempt succeed — only the client knows "this is the same logical request I sent before." If the server minted the key, every retry would look like a brand-new request and get a fresh key, defeating dedup. The client therefore generates the key once and reuses it across all retries of that one logical operation.

</details>

<details><summary><b>6.</b> What is the difference between a natural dedup key and a synthetic one?</summary>

A natural key is a business identifier that already uniquely identifies the record, such as an order reference or `ISIN` plus valuation date. A synthetic key is one you mint yourself (a UUID or a hash of the payload) when no business field, or no stable combination of fields, is unique enough to rely on. You prefer natural keys when they exist and are trustworthy, and fall back to synthetic only when the data forces it.

</details>

<details><summary><b>7.</b> When does a natural business key suffice for deduplication?</summary>

When some column or combination of columns is guaranteed unique per logical record and is stable across retries — for trades, often `order_ref`, or `ISIN` plus trade date plus a sequence. It suffices precisely when re-sending the same logical row always carries the same value in that key, so a uniqueness constraint can catch the duplicate. If the "unique" field can repeat legitimately (two genuine fills at the same price), the natural key alone is not enough.

</details>

<details><summary><b>8.</b> When are you forced to mint a synthetic dedup key?</summary>

When no natural field, or combination, reliably distinguishes one logical record from another — for example a feed of unkeyed events where two genuinely distinct rows can be byte-identical except for arrival order. You then mint a deterministic synthetic key, such as a hash of the meaningful payload plus a source-provided sequence number, so retries of the same row reproduce the same key. The danger is choosing inputs that differ between a retry and the original, which would let duplicates slip through.

</details>

<details><summary><b>9.</b> Why can hashing the entire row be a poor choice of synthetic key?</summary>

Because if any volatile field changes between the original send and the retry — an ingestion timestamp, a load-batch id, a reformatted decimal — the hash changes and the retry is treated as a new record, reintroducing the duplicate you were trying to prevent. The fix is to hash only the stable, business-meaningful fields. It is a classic gotcha: the key must be a function of identity, not of incidental metadata.

</details>

<details><summary><b>10.</b> What is an idempotent write at the sink?</summary>

An idempotent write is one where re-issuing the same logical insert leaves the table in the same state rather than adding a second row. In Postgres the two main mechanisms are `INSERT ... ON CONFLICT` (upsert) and `MERGE`, both keyed on a unique constraint so a repeat collapses into a no-op or an in-place update. This is the sink-side half of "at-least-once delivery plus idempotent consumer."

</details>

<details><summary><b>11.</b> What is an upsert?</summary>

An upsert is a single statement that inserts a row if it does not exist and updates it if it does, decided by a uniqueness check. It is the canonical idempotent write because a repeated load of the same key updates in place instead of appending. In Postgres it is spelled `INSERT ... ON CONFLICT (key) DO UPDATE` (or `DO NOTHING`).

</details>

<details><summary><b>12.</b> What is the basic syntax of `INSERT ... ON CONFLICT` in Postgres?</summary>

It is `INSERT INTO t (...) VALUES (...) ON CONFLICT (conflict_target) DO NOTHING` or `... DO UPDATE SET col = EXCLUDED.col`. The `conflict_target` names the column(s) or constraint whose violation triggers the alternative action, and `DO UPDATE` updates the existing conflicting row. For example `INSERT INTO trades (order_ref, qty) VALUES ('A1', 100) ON CONFLICT (order_ref) DO UPDATE SET qty = EXCLUDED.qty`.

</details>

<details><summary><b>13.</b> What does the special `EXCLUDED` table refer to in `ON CONFLICT DO UPDATE`?</summary>

`EXCLUDED` references the row that was proposed for insertion but excluded because of the conflict, so `EXCLUDED.col` is the new incoming value. You use it in the `SET` list to copy incoming values onto the existing row, e.g. `SET price = EXCLUDED.price`. It reflects the effect of any `BEFORE INSERT` triggers and requires `SELECT` privilege on the columns referenced.

</details>

<details><summary><b>14.</b> What is the difference between `ON CONFLICT DO NOTHING` and `ON CONFLICT DO UPDATE`?</summary>

`DO NOTHING` silently skips the row on conflict, leaving the existing row untouched, which is ideal for an append-only fact where a duplicate carries no new information. `DO UPDATE` overwrites the existing row with the incoming values, which you want when a re-sent record may carry corrections. Choose `DO NOTHING` for pure dedup and `DO UPDATE` when later versions of the same key should win.

</details>

<details><summary><b>15.</b> Why must `ON CONFLICT` have a unique index or constraint to infer against?</summary>

Because the database decides "is this a conflict?" by looking for a violation of a specific unique index or constraint (the arbiter), and with no such constraint there is nothing to violate — so there is nothing to do on conflict. The conflict target columns must match a unique or primary-key index. Without one, duplicates can land and the statement cannot tell them apart.

</details>

<details><summary><b>16.</b> What is a conflict target's "arbiter index"?</summary>

The arbiter index is the unique index Postgres uses to detect the conflict, inferred from the columns or expression you list in `ON CONFLICT (...)`, or named explicitly via `ON CONFLICT ON CONSTRAINT name`. Inference matches the columns without regard to their order and supports partial unique indexes through a `WHERE` predicate. Naming the constraint directly is less flexible because it breaks if the index is later replaced.

</details>

<details><summary><b>17.</b> Can `ON CONFLICT DO UPDATE` use a `WHERE` clause, and what does it do?</summary>

Yes — a `WHERE` after the `SET` list makes the update conditional, so only existing rows matching the predicate are actually updated. A common use is "only update if the incoming version is newer," e.g. `... DO UPDATE SET ... WHERE EXCLUDED.updated_at > t.updated_at`. Note all conflicting rows are still locked even when the `WHERE` is false; rows the predicate excludes are simply not changed.

</details>

<details><summary><b>18.</b> Why does a repeated run of a `DO NOTHING` upsert leave row counts unchanged?</summary>

Because the second run's rows all collide with the unique key already present from the first run, so every one of them is skipped and no new rows are inserted. The end state — and therefore the row count and any whole-table checksum — is identical to after the first run. This is precisely the property you assert when you claim a loader is rerunnable.

</details>

<details><summary><b>19.</b> What is the overwrite-partition pattern?</summary>

It is the batch-pipeline idiom where a rerun rewrites a deterministic slice of output — typically one date or business partition — by deleting-and-reinserting (or atomically swapping) that slice rather than appending to the table. Because the slice is fully recomputed from its input, re-running produces the same bytes regardless of how many times it runs. It is the partition-level analogue of an idempotent write.

</details>

<details><summary><b>20.</b> Why does the overwrite-partition pattern make a batch job rerunnable?</summary>

Because the job's output for a given partition is a pure function of that partition's input: re-executing replaces the entire slice with a freshly computed identical copy, so partial prior runs are erased rather than added to. A failed run that produced half a partition is harmless because the rerun overwrites the whole thing. The key constraint is that the partition boundary must be deterministic, e.g. "all trades dated 2026-06-12," not "rows since last run."

</details>

<details><summary><b>21.</b> Why is appending fundamentally unsafe for reruns, while overwriting a partition is safe?</summary>

Appending adds rows unconditionally, so a rerun (or a retried half-run) stacks a second copy on top of the first, doubling the data. Overwriting a deterministic partition discards whatever was there and writes the recomputed result, so the count of runs cannot affect the outcome. The lesson: prefer "replace this slice" semantics over "add these rows" in any step that might be retried.

</details>

<details><summary><b>22.</b> A loader appends rows and a network blip causes the orchestrator to retry the activity. What is the likely data outcome?</summary>

You get duplicate rows — the first attempt likely committed some or all of its inserts before the connection dropped, and the retry inserts them again because nothing tells it they already exist. The first thing to check is whether the sink has a unique constraint on the dedup key; if not, the append simply doubles. The fix is to switch the append to an upsert keyed on the natural or synthetic dedup key.

</details>

<details><summary><b>23.</b> What does "effective exactly-once" mean?</summary>

It means the observable result is as if each message were processed exactly once, achieved by combining at-least-once delivery with an idempotent consumer — not by guaranteeing the message is physically delivered exactly once. The delivery layer may hand the same message over several times; the consumer deduplicates so duplicates have no effect. This is the practical, achievable form of exactly-once that real systems ship.

</details>

<details><summary><b>24.</b> Why is true exactly-once delivery often called a myth?</summary>

Because between any two machines an acknowledgement can be lost, so a sender can never be certain a message arrived; it must choose between resending (risking a duplicate) or not (risking a loss). You cannot get both at-most-once and at-least-once over an unreliable channel, so "exactly-once delivery" is unattainable. What you can build is exactly-once effect: at-least-once delivery plus idempotent processing.

</details>

<details><summary><b>25.</b> How do at-least-once delivery and an idempotent consumer combine to give exactly-once semantics?</summary>

At-least-once guarantees no message is lost, at the cost of occasional duplicates; the idempotent consumer guarantees duplicates have no additional effect. Together, every message is reflected in the final state exactly once even though some were delivered twice. The idempotent consumer is what "absorbs" the redundancy the delivery guarantee creates.

</details>

<details><summary><b>26.</b> Why can you not simply choose at-most-once delivery to avoid duplicates?</summary>

Because at-most-once drops a message whenever the acknowledgement is uncertain, so you trade duplicates for silent data loss — unacceptable for a trade or NAV feed where a missing record is a reconciliation break. At-least-once keeps everything and pushes the dedup responsibility to the consumer, which is the controllable side. In regulated pipelines, losing data is worse than seeing a duplicate you can dedup.

</details>

<details><summary><b>27.</b> In a managed orchestrator like Azure Data Factory, what actually re-executes when an activity is retried after failure?</summary>

The activity is re-run from its start with the same inputs — the orchestrator does not resume mid-statement, it re-invokes the whole activity. So if a copy or stored-procedure activity partially committed before failing, the retry repeats the entire operation, and any non-idempotent side effect happens again. This is exactly why the activity's logic, not the orchestrator, must be idempotent.

</details>

<details><summary><b>28.</b> Why does retry/rerun behaviour in orchestrators put the idempotency burden on your activity rather than the platform?</summary>

Because the orchestrator can only re-invoke your activity; it has no way to know which rows your code already wrote, so it cannot "undo" a partial run for you. If your activity appends, the retry double-appends; if it upserts or overwrites a partition, the retry is harmless. The platform gives you retries for free, but only idempotent activity logic makes those retries safe.

</details>

<details><summary><b>29.</b> What is the relationship between a retry and a rerun?</summary>

A retry is the orchestrator automatically re-attempting a failed activity in the same pipeline run, usually after a transient error; a rerun is a human or schedule deliberately re-executing the pipeline (often for a past date) to recompute or backfill. Both re-invoke your logic with the same logical inputs, so both demand idempotency. The difference is who triggers it and why, not what safety property is required.

</details>

<details><summary><b>30.</b> For a trades CSV with order refs and ISINs, how would you decide the natural dedup key?</summary>

You pick the smallest column set that uniquely identifies one logical trade and is stable across resends — often `order_ref` alone if the source guarantees it is unique. If `order_ref` can repeat across days or systems, you widen it, e.g. `(source_system, order_ref)` or `(ISIN, trade_date, sequence_no)`. You then put a unique constraint on that set so the upsert has an arbiter to detect duplicates.

</details>

<details><summary><b>31.</b> Why is `ISIN` alone never a valid dedup key for a trades load?</summary>

Because an `ISIN` identifies a security, not a trade — thousands of trades can share one `ISIN`, so deduping on it would collapse all trades in that instrument into a single row. You need it combined with something that distinguishes the individual trade, such as trade date plus an order reference or sequence. `ISIN` contributes to the key but can never be the whole key for trade-level idempotency.

</details>

<details><summary><b>32.</b> How would you prove a loader is idempotent after writing it?</summary>

Run it twice against the same input and compare the table row count and a whole-table checksum after each run; identical numbers prove the second run changed nothing. The checksum matters because counts alone miss in-place mutations — two runs could keep the count but alter values. Committing both results to the repo turns the claim "it is idempotent" into reproducible evidence.

</details>

<details><summary><b>33.</b> Why is a row-count comparison alone insufficient to prove idempotency?</summary>

Because a non-idempotent `DO UPDATE` could leave the count unchanged while silently rewriting column values on the second run — for instance overwriting a corrected price back to the original. A row count cannot detect content drift, only cardinality drift. You therefore pair the count with a content checksum so both quantity and contents are verified.

</details>

<details><summary><b>34.</b> How can you compute a whole-table checksum in Postgres to verify idempotency?</summary>

Concatenate the rows in a deterministic order and hash the result, for example `SELECT md5(string_agg(t::text, '|' ORDER BY order_ref)) FROM trades t`. The deterministic `ORDER BY` is essential because `string_agg` without ordering can return rows in any sequence, producing a different hash for identical data. Comparing this single value before and after a rerun gives a one-glance idempotency check.

</details>

<details><summary><b>35.</b> Why must the `ORDER BY` inside a checksum aggregation be deterministic?</summary>

Because Postgres does not guarantee row order without an explicit `ORDER BY`, so two runs over identical data could concatenate the rows differently and yield different hashes — a false negative on idempotency. Ordering by a unique key (or a unique key set) makes the concatenation, and thus the hash, reproducible. A common gotcha is ordering by a non-unique column, which still leaves ties unordered.

</details>

<details><summary><b>36.</b> You kill the loader mid-run and then rerun it. What property guarantees the final state is still identical?</summary>

Idempotency of the sink write plus determinism of the input slice: the rerun reapplies the same upsert (or rewrites the same partition), so whatever the killed run partially committed is overwritten or no-opped into the same end state. The partial run leaves no lasting damage because nothing the loader does depends on run count. You verify this exactly as before — the row count and checksum match the clean single-run baseline.

</details>

<details><summary><b>37.</b> After a kill-and-rerun, why might the row count be correct but you still need the checksum?</summary>

Because a kill mid-run can leave rows that were inserted but not yet updated to their final values, or vice versa; an upsert rerun fixes the contents but a count check alone would already have passed even before the fix. The checksum confirms every column landed at its final correct value, not just that the right number of rows exist. It is the content-level proof that the partial run left no subtle corruption.

</details>

<details><summary><b>38.</b> Is wrapping a load in a single transaction enough to make it idempotent? Why or why not?</summary>

No — a transaction gives atomicity (all-or-nothing for one attempt) but not idempotency across attempts. A committed transaction that is then retried will run its appends again, so you get atomic duplication. Transactions and idempotency are orthogonal: you need the write itself to be a no-op on repeat (upsert/overwrite), and the transaction just makes each attempt clean.

</details>

<details><summary><b>39.</b> How do `INSERT ... ON CONFLICT` and `MERGE` differ for concurrent upserts in Postgres?</summary>

`INSERT ... ON CONFLICT` is specifically designed for concurrent insert conflicts and handles them gracefully under high concurrency, collapsing a race into an update. `MERGE` follows ordinary transaction-isolation rules and can raise a `unique_violation` or cardinality violation when concurrent sessions race on the same key. For a simple concurrent upsert, the Postgres docs recommend `ON CONFLICT`; reserve `MERGE` for multi-action conditional logic.

</details>

<details><summary><b>40.</b> In which version was `MERGE` introduced in PostgreSQL?</summary>

`MERGE` was introduced in PostgreSQL 15. Before that, the idiomatic upsert was `INSERT ... ON CONFLICT`, available since PostgreSQL 9.5, which remains the recommended choice for plain concurrent upserts. If you target an older server, `MERGE` is simply unavailable and you must use `ON CONFLICT` or a manual staged approach.

</details>

<details><summary><b>41.</b> What can `MERGE` do that `INSERT ... ON CONFLICT` cannot?</summary>

`MERGE` can perform `INSERT`, `UPDATE`, and `DELETE` in a single statement across multiple `WHEN` branches — including `WHEN NOT MATCHED BY SOURCE` to delete target rows with no source match. `ON CONFLICT` only inserts with an optional update of the conflicting row and has no delete branch. So `MERGE` suits a full reconcile-and-sync; `ON CONFLICT` suits a focused idempotent insert.

</details>

<details><summary><b>42.</b> Why does `MERGE` not provide an `EXCLUDED` pseudo-table?</summary>

Because `MERGE` joins an explicit source to the target, so inside a `WHEN` clause you reference the source columns directly by their alias rather than through a synthetic `EXCLUDED` row. `ON CONFLICT` has no join — it inserts proposed values — so it needs `EXCLUDED` to expose the row that was about to be inserted. The two statements have different shapes, hence different ways to name incoming values.

</details>

<details><summary><b>43.</b> What is a staged MERGE (load-to-staging-then-merge) and why use it?</summary>

You bulk-load the incoming batch into a staging table, then run a single `MERGE` (or `INSERT ... SELECT ... ON CONFLICT`) from staging into the target keyed on the dedup key. It is fast because the bulk load avoids per-row conflict handling, and it is idempotent because the merge step collapses duplicates against the target. It also lets you validate or transform in staging before touching the production table.

</details>

<details><summary><b>44.</b> Why can a non-deterministic transform break pipeline idempotency even with an idempotent sink?</summary>

Because if the transform produces different output for the same input on each run — say it stamps `now()` into a column or sorts non-deterministically — then the "same" row carries different content, so an upsert keeps rewriting it and a checksum never stabilises. Idempotency of the whole pipeline requires the transform to be a pure function of its input. Pushing volatile values like wall-clock time outside the dedup-relevant columns is the usual fix.

</details>

<details><summary><b>45.</b> What makes a source read non-idempotent, and how do you fix it?</summary>

A read is non-idempotent when "what it returns" depends on hidden state, such as "give me everything new since the last offset" where the offset advances destructively — a retry then sees a different (smaller) set. You fix it by reading a deterministic, named slice: a fixed date partition, an explicit offset range, or a snapshot, so re-reading returns the identical rows. The principle is that the read's result must be a function of stated parameters, not of mutable cursor state.

</details>

<details><summary><b>46.</b> Why is `SELECT ... FROM feed WHERE loaded = false` a fragile basis for an idempotent load?</summary>

Because the predicate depends on a mutable flag that the load itself flips, so a crash between reading and flipping leaves the same rows visible to a retry, and a crash after flipping but before committing can hide rows entirely. The read is coupled to side effects, which is exactly what idempotency forbids. A deterministic partition or an atomic claim-and-commit is more robust.

</details>

<details><summary><b>47.</b> How does a uniqueness constraint act as a last line of defence for idempotency?</summary>

Even if upstream logic accidentally tries to insert a duplicate, a `UNIQUE` constraint on the dedup key makes the database reject it, surfacing the problem instead of silently doubling data. Combined with `ON CONFLICT DO NOTHING`, the constraint turns a would-be duplicate into a harmless no-op. It converts "we hope nothing duplicates" into "the schema guarantees nothing duplicates."

</details>

<details><summary><b>48.</b> What is the risk of relying only on application-side dedup without a database constraint?</summary>

If two concurrent loaders both check "does this key exist?" and both see "no," they will both insert, creating a duplicate that the application logic believed it had prevented. Only a unique constraint enforced by the database closes this race, because the second insert hits the constraint. Application checks are advisory; the constraint is authoritative.

</details>

<details><summary><b>49.</b> Why is choosing the primary key well central to idempotency?</summary>

Because the primary (or unique) key is the identity the sink uses to recognise "I have seen this before," so a wrong or too-narrow key either lets duplicates through or wrongly collapses distinct rows. The key must exactly match the business notion of "the same logical record." Getting it right is the design decision that makes every upsert and overwrite correct.

</details>

<details><summary><b>50.</b> A double run of your loader yields different checksums but identical row counts. What is the most likely cause?</summary>

Some column is being written non-deterministically — a load timestamp, a generated UUID, a `random()` default, or a `now()` value — so contents differ run to run even though cardinality does not. The first thing to check is which columns differ between the two runs, typically by diffing or hashing per column. The fix is to make those columns deterministic or exclude them from the meaningful payload.

</details>

<details><summary><b>51.</b> A double run yields different row counts. Where do you look first?</summary>

At the sink write: it is almost certainly appending rather than upserting, or the unique constraint that the upsert relies on is missing or does not match the conflict target. Confirm the dedup key has a unique index and that the `ON CONFLICT` target names it correctly. If the constraint is absent, the database has no way to recognise the duplicates and every row inserts twice.

</details>

<details><summary><b>52.</b> Why is the order reference often the ideal idempotency key for a trade load?</summary>

Because an order reference is a stable, source-issued identifier for one logical order that the upstream system reuses if it resends — exactly the property an idempotency key needs. Re-sending the same order carries the same reference, so a unique constraint on it catches the duplicate. You should still confirm uniqueness scope (per source, per day) before trusting it as the sole key.

</details>

<details><summary><b>53.</b> In a transfer-agency subscription/redemption feed, why does idempotency matter for investor positions?</summary>

Because a retried or replayed subscription that is not deduplicated would credit the investor's holding twice, corrupting their position and any downstream NAV-based fees or statements. Keying the load on a stable deal reference and upserting ensures a redelivered instruction updates rather than re-applies. In a regulated TA context this is the difference between a clean book and a reportable error.

</details>

<details><summary><b>54.</b> How does idempotency relate to EMT/EPT file ingestion?</summary>

EMT and EPT files (the European MiFID/PRIIPs templates) are periodic regulatory data drops that may be re-sent as corrected versions, so the loader must key on the instrument identifier plus reporting period and upsert, letting a corrected file overwrite rather than duplicate. Without that, a resent EMT file doubles the instrument rows and breaks downstream cost/charge reporting. The natural key is typically the `ISIN` plus the reporting reference date.

</details>

<details><summary><b>55.</b> Why is overwrite-by-partition a natural fit for a daily NAV load?</summary>

Because a NAV is computed per fund per valuation date, so the deterministic slice "fund X, date D" is exactly one partition that a rerun can fully replace — recomputing it yields the same value. If a valuation is corrected, overwriting the partition cleanly supersedes the prior figure with no duplicate NAV rows. The valuation date gives you a stable, reproducible partition boundary.

</details>

<details><summary><b>56.</b> How would you make a SWIFT message ingestion idempotent?</summary>

Key on the message's unique reference fields — for an MT message the transaction reference (field 20) and related references — and upsert so a redelivered message updates rather than reinserts. SWIFT networks can redeliver, so without dedup you would book the same settlement instruction twice. The message reference is the natural idempotency key the standard already provides.

</details>

<details><summary><b>57.</b> Why is an LEI not a suitable idempotency key for transaction records?</summary>

Because an LEI identifies a legal entity (a counterparty or fund), not an individual transaction, so many records share the same LEI — deduping on it would wrongly collapse distinct trades or instructions for that entity. Like `ISIN`, an LEI is a useful attribute but identifies a party, not an event. The idempotency key must be the record's own identity, e.g. a transaction reference.

</details>

<details><summary><b>58.</b> Under DORA's resilience expectations, how does idempotency support disaster recovery?</summary>

Because recovery often means replaying or re-running ingestion from a checkpoint, idempotent loads let you re-execute without fear of double-counting, so the recovered state matches the pre-incident state exactly. DORA pushes regulated financial entities to demonstrate they can recover cleanly; a non-idempotent pipeline cannot make that demonstration. Idempotency is what makes "just re-run it" a safe recovery action rather than a second incident.

</details>

<details><summary><b>59.</b> Why does a replay-based architecture (reprocessing an event log) demand idempotent consumers?</summary>

Because replay re-delivers events that were already processed once, so any consumer that is not idempotent will double-apply them and corrupt derived state. The whole appeal of an event log — rebuild state by replaying from the start — only works if applying an event twice equals applying it once. Idempotent consumers are the precondition that makes replay a feature rather than a hazard.

</details>

<details><summary><b>60.</b> What is the difference between idempotency and commutativity?</summary>

Idempotency means repeating the same operation has no extra effect; commutativity means the order of two different operations does not change the result. They are independent properties: an upsert is idempotent, while two upserts to different keys are also commutative, but a "last write wins" upsert to the same key is order-sensitive. Distinguishing them matters when reasoning about out-of-order delivery, not just duplicates.

</details>

<details><summary><b>61.</b> If messages can arrive out of order, why is a plain "last write wins" upsert sometimes wrong?</summary>

Because an older message arriving after a newer one will, under naive last-write-wins, overwrite the newer correct value with stale data — idempotent against duplicates but not safe against reordering. The fix is a version or timestamp guard, e.g. `DO UPDATE ... WHERE EXCLUDED.version > t.version`, so only strictly newer data wins. This combines idempotency (duplicates no-op) with monotonicity (stale updates rejected).

</details>

<details><summary><b>62.</b> How does a monotonic version column make an upsert safe against both duplicates and reordering?</summary>

A duplicate carries the same version, so the `WHERE EXCLUDED.version > t.version` guard makes it a no-op; a stale (older) message carries a lower version and is also rejected; only a genuinely newer version updates. This single guard gives you idempotency and ordering safety at once. The version must be sourced from the producer's logical clock, not the loader's arrival time.

</details>

<details><summary><b>63.</b> Why is `created_at = now()` a dangerous default on an idempotently loaded table?</summary>

Because `now()` is evaluated on each insert attempt, so a re-inserted (or upserted-then-reinserted) row can carry a different timestamp than the original, breaking content checksums and confusing audit trails. If you need an immutable creation time, set it only on first insert (e.g. leave it untouched in the `DO UPDATE`) or source it from the data. A wall-clock default is a frequent silent cause of "the data keeps changing on rerun."

</details>

<details><summary><b>64.</b> In `INSERT ... ON CONFLICT DO UPDATE`, how do you preserve the original `created_at` while still updating other columns?</summary>

Simply omit `created_at` from the `SET` list — `DO UPDATE` only changes the columns you name, so the existing `created_at` is left intact while you update, say, `price = EXCLUDED.price`. Only set `created_at = EXCLUDED.created_at` if you actually want the latest send's value. This is how you get an immutable insertion time alongside mutable business fields.

</details>

<details><summary><b>65.</b> What restriction does Postgres place on `ON CONFLICT` and partitioned tables?</summary>

You cannot use `ON CONFLICT DO UPDATE` to change a partition key in a way that would move the row to a different partition; ordinary column updates are fine. The conflict handling otherwise works across the partitioned table via its unique indexes. The restriction exists because moving a row between partitions is a delete-plus-insert, which the upsert path does not perform.

</details>

<details><summary><b>66.</b> Why can't an exclusion constraint serve as the arbiter for `ON CONFLICT DO UPDATE`?</summary>

Because `ON CONFLICT DO UPDATE` only supports unique indexes and unique/primary-key constraints as arbiters; exclusion constraints are not supported for the `DO UPDATE` action. You can still get a conflict error from an exclusion constraint, but you cannot route it into an upsert. For idempotent writes you therefore rely on a plain unique constraint over the dedup key.

</details>

<details><summary><b>67.</b> What cardinality rule does `ON CONFLICT` enforce within a single statement?</summary>

A single `INSERT ... ON CONFLICT` cannot affect the same existing row more than once, and the proposed rows must not duplicate each other in the arbiter index terms; violating this raises a cardinality error. So if your one statement contains two rows with the same dedup key, Postgres rejects it rather than applying them twice. You must dedup the incoming batch before the upsert, or load via staging.

</details>

<details><summary><b>68.</b> Why might `INSERT ... ON CONFLICT` unexpectedly raise a unique violation, and when?</summary>

While `CREATE INDEX CONCURRENTLY` or `REINDEX CONCURRENTLY` is running on the relevant unique index, `INSERT ... ON CONFLICT` statements on that table may unexpectedly fail with a unique violation. This is a documented transient condition tied to concurrent index builds, not a flaw in your loader. The mitigation is to avoid concurrent index maintenance during heavy upsert load, or to retry the failed statement.

</details>

<details><summary><b>69.</b> What SQLSTATE does Postgres raise on a unique-constraint violation, and why does it matter for idempotency?</summary>

It raises SQLSTATE `23505` (`unique_violation`). It matters because a loader can catch `23505` to treat the duplicate as "already loaded" and continue, turning an error into an idempotent no-op — though using `ON CONFLICT DO NOTHING` is cleaner than catching the exception. Knowing the exact code lets you write precise error handling rather than swallowing all errors.

</details>

<details><summary><b>70.</b> Why is catching `unique_violation` in application code an inferior idempotency mechanism compared to `ON CONFLICT`?</summary>

Because catching the exception means the failed `INSERT` has already aborted the surrounding transaction (or savepoint), so you must roll back and retry, which is slower and more error-prone than letting the database resolve the conflict in one statement. `ON CONFLICT` resolves the duplicate inline without aborting anything. Exception-catching also risks masking unrelated `23505`s from a different constraint.

</details>

<details><summary><b>71.</b> How can a savepoint help if you must rely on catching duplicate-key errors?</summary>

Wrapping each risky insert in a savepoint lets you roll back just that statement on `23505` without discarding the whole transaction, then continue with the next row. Without a savepoint, the first unique violation poisons the entire transaction and all subsequent statements fail with `25P02` (in-failed-sql-transaction). Still, `ON CONFLICT` is preferable because it avoids the abort entirely.

</details>

<details><summary><b>72.</b> What is "at-least-once" delivery in one sentence, and what does it cost you?</summary>

At-least-once guarantees every message is delivered one or more times — never lost — at the cost of occasional duplicate deliveries. The duplicates are the price of never losing data over an unreliable channel where acknowledgements can vanish. You pay that price by making the consumer idempotent so the duplicates are harmless.

</details>

<details><summary><b>73.</b> Why is idempotency a precondition for safe automatic retries in any orchestrator?</summary>

Because automatic retries re-execute work whose success was uncertain, and only idempotent work can be re-executed without changing the result; non-idempotent work duplicates or corrupts on each retry. So enabling retries on a non-idempotent activity actively manufactures bad data. The rule is: make the step idempotent first, then turn retries on.

</details>

<details><summary><b>74.</b> What does "deterministic slice" mean and why is it required for rerunnable batch output?</summary>

A deterministic slice is an output partition whose membership is fixed by stated parameters (e.g. all rows for valuation date D), independent of when or how often the job runs. It is required because a rerun must recompute and replace exactly the same set; a slice defined by mutable state ("since last run") would shift between runs and break the overwrite. Determinism of the slice is what lets overwrite equal idempotence.

</details>

<details><summary><b>75.</b> Why is "process everything since the last watermark, then advance the watermark" risky on failure?</summary>

Because if the job advances the watermark before its output is durably committed, a crash loses the in-flight slice (the watermark moved past data never written); if it advances after but crashes mid-write, a rerun reprocesses an overlapping slice. Either way the read is coupled to mutable cursor state, which is non-idempotent. Committing the output and the watermark atomically, or overwriting a deterministic partition, removes the hazard.

</details>

<details><summary><b>76.</b> How does idempotency interact with exactly-once stream processing frameworks?</summary>

Such frameworks typically achieve exactly-once effect by combining checkpointed at-least-once delivery with either idempotent sinks or transactional (two-phase) sink commits, so reprocessing after a checkpoint restore does not double-apply. The framework gives you the replay; the idempotent or transactional sink gives you the "once" semantics. It is the same at-least-once-plus-idempotent-consumer pattern, packaged.

</details>

<details><summary><b>77.</b> Why is a transactional sink an alternative to an idempotent sink for exactly-once effect?</summary>

Because a sink that commits its writes in the same transaction (or coordinated commit) as the consumer's offset advance ensures either both happen or neither, so a replay re-reads from an offset whose effects were never committed — no duplicate appears. Idempotency tolerates the duplicate write; transactionality prevents the duplicate write from ever committing. Both yield exactly-once effect; the choice depends on whether your sink supports transactional commit.

</details>

<details><summary><b>78.</b> When is `DO NOTHING` preferable to `DO UPDATE` for a fund-data load?</summary>

When the records are immutable facts that are never legitimately corrected via resend — for example a settled, finalised trade where a redelivery should be ignored rather than overwrite the booked row. `DO NOTHING` then makes redeliveries pure no-ops and protects the original. If the source can send corrections, you instead want `DO UPDATE` (often guarded by a version) so the correction wins.

</details>

<details><summary><b>79.</b> What problem arises if two columns can both serve as a unique key but you upsert on only one?</summary>

You can get a conflict on the column you did not name — the insert violates the second unique constraint and aborts instead of being caught by `ON CONFLICT`, raising `23505`. The conflict target must match the constraint that will actually be violated. The fix is to choose one true dedup key and ensure the conflict target names exactly that constraint.

</details>

<details><summary><b>80.</b> How do you make a Python loader idempotent end-to-end with `uv run`?</summary>

Read a deterministic input slice, transform it as a pure function (no wall-clock or random values in keyed columns), and write with a parameterised `INSERT ... ON CONFLICT (key) DO UPDATE`/`DO NOTHING`; invoke the whole thing via `uv run loader.py` so the environment is reproducible. Reproducible environment plus deterministic read plus idempotent write yields a rerunnable loader. You then prove it with the double-run count-and-checksum check.

</details>

<details><summary><b>81.</b> Why does using `uv run` rather than a bare `python` invocation matter for reproducible idempotency evidence?</summary>

Because `uv run` resolves and uses the project's locked dependency set, so the loader behaves identically across machines and reruns — a different pandas or driver version could change formatting and thus the checksum. Reproducibility of the runtime is part of reproducibility of the result. Running bare `python` risks picking up a different environment and producing non-comparable evidence.

</details>

<details><summary><b>82.</b> Why should the dedup key be enforced at the schema level even in a "trusted" internal pipeline?</summary>

Because trust is not a guarantee — a code change, a bad backfill, or a concurrent run can still attempt duplicates, and only a `UNIQUE` constraint stops them at the database boundary. The constraint converts an entire class of "we assumed it wouldn't happen" bugs into immediate, visible errors. It is cheap insurance that makes the idempotency property structural rather than aspirational.

</details>

<details><summary><b>83.</b> What does "the design is not finished until you can point to where idempotency holds" mean for an architect?</summary>

It means for every step — read, transform, write — you must be able to name the concrete mechanism that makes a rerun safe (a deterministic partition, a pure transform, an upsert on a stated key). If any step has no such answer, that step is a latent double-booking waiting for the next retry. Architecting includes locating and naming each idempotency boundary, not just drawing boxes and arrows.

</details>

<details><summary><b>84.</b> How would you demonstrate idempotency evidence in a way an auditor accepts?</summary>

Commit to the repo the exact commands run, the row counts and whole-table checksums after the first run and after the second run (and after a kill-and-rerun), showing they are identical. Reproducibility plus a content-level checksum gives objective, re-verifiable proof rather than assertion. In a regulated context this turns "the load is rerunnable" into evidence that survives challenge.

</details>

<details><summary><b>85.</b> Why is appending with a "load batch id" column not a substitute for idempotency?</summary>

Because tagging each append with a batch id still leaves multiple physical copies of the same logical record in the table, so downstream queries double-count unless they always filter to one batch — fragile and easy to forget. Idempotency means the table holds one correct row per key regardless of run count, not many rows you must remember to filter. Batch ids help lineage, not dedup.

</details>

<details><summary><b>86.</b> How does idempotency support backfilling a historical date range?</summary>

Because each date is a deterministic partition that the backfill overwrites (or upserts) independently, you can re-run any past date — or the whole range — repeatedly and converge on the same correct state. A non-idempotent backfill would stack duplicates on dates that already had data. Idempotency is precisely what makes "just backfill 2026-01 through 2026-05 again" a safe operation.

</details>

<details><summary><b>87.</b> What is the danger of making the synthetic key depend on input row order?</summary>

If the key incorporates a position or arrival sequence that the source does not reproduce on resend, a retried batch in a different order yields different keys, so the same logical rows look new and duplicate. The synthetic key must derive only from stable content, not from where a row happened to sit in the file. A reordered redelivery is a realistic event you must design against.

</details>

<details><summary><b>88.</b> How does idempotency change the way you handle "did my write succeed?" uncertainty?</summary>

Instead of trying to determine whether the prior attempt committed — often impossible after a lost ack — you simply re-issue the idempotent write, knowing a repeat is harmless. Idempotency converts an unanswerable question into a no-op, which is its core operational value. This is why retry-on-uncertainty is safe only when the operation is idempotent.

</details>

<details><summary><b>89.</b> Why is "exactly-once" a property of the system as a whole rather than of the network?</summary>

Because no network can deliver exactly once, but a system composed of an at-least-once channel plus an idempotent (or transactional) consumer can produce exactly-once effects on its state. The guarantee lives at the boundary where duplicates are absorbed, not on the wire. Saying a system is exactly-once is a statement about its end-to-end design, not its transport.

</details>

<details><summary><b>90.</b> In a staged-load design, where exactly does deduplication happen?</summary>

Either in the staging table before the merge (dedup the batch so the cardinality rule is not violated) or in the `MERGE`/`ON CONFLICT` step that resolves staging rows against the target by key. Often you do both: collapse intra-batch duplicates in staging, then let the upsert handle batch-vs-target duplicates. Splitting the two stages keeps each step simple and lets you validate before touching production.

</details>

<details><summary><b>91.</b> Why must you dedup the incoming batch before an `ON CONFLICT` upsert if it can contain repeated keys?</summary>

Because `ON CONFLICT` forbids affecting the same target row twice in one statement and rejects proposed rows that duplicate each other in the arbiter terms, raising a cardinality error. So two rows with the same key in one `INSERT` fail rather than upsert. You pre-dedup (e.g. keep the latest per key via `DISTINCT ON`) or load through staging to avoid this.

</details>

<details><summary><b>92.</b> How would you use `DISTINCT ON` to keep the latest version per key before upserting in Postgres?</summary>

Use `SELECT DISTINCT ON (order_ref) * FROM staging ORDER BY order_ref, version DESC` to collapse each key to its highest-version row, then upsert that result. `DISTINCT ON` keeps the first row per group as ordered, so ordering by the key then by version descending yields the latest per key. This satisfies `ON CONFLICT`'s one-row-per-key requirement deterministically.

</details>

<details><summary><b>93.</b> Why is determinism of the transform also a regulatory concern, not just a correctness one?</summary>

Because in a regulated fund context you may have to reproduce a past output for an auditor or regulator, and only a deterministic transform over a preserved input can regenerate the identical figure. Non-determinism means you cannot prove what you produced on a given day. Idempotent, deterministic pipelines make historical reproduction — and therefore defensible reporting — possible.

</details>

<details><summary><b>94.</b> What is the relationship between idempotency and "rerunnable" batch jobs in DDIA's framing?</summary>

DDIA frames a well-designed batch job as one whose output is a deterministic function of its input, so it can be safely re-run on failure with no externally visible difference — that re-runnability is idempotency at the job level. The job avoids in-place mutation of shared state and instead produces output that fully replaces the prior run's output. Idempotency is the property; rerunnability is its operational payoff.

</details>

<details><summary><b>95.</b> A scheduled daily job ran twice (a duplicate trigger fired) and downstream NAV is now wrong. What is the root-cause class?</summary>

The job's sink write is non-idempotent — most likely appending — so the duplicate trigger doubled that day's rows; an idempotent overwrite-partition or upsert would have made the second trigger a no-op. The first thing to check is whether the day's partition holds duplicate rows for the same keys. The durable fix is to make the load idempotent so a stray re-trigger cannot corrupt NAV.

</details>

<details><summary><b>96.</b> Why is "idempotent consumer" the more controllable half of exactly-once than "exactly-once delivery"?</summary>

Because you cannot change the physics of an unreliable network to deliver exactly once, but you fully control your consumer's logic and can make it dedup. Engineering effort spent making delivery perfectly once is wasted on an impossible target; effort spent on an idempotent consumer is achievable and sufficient. So the design pressure goes to the consumer, where you have leverage.

</details>

<details><summary><b>97.</b> How does an idempotency key store (a "seen keys" table) implement an idempotent consumer?</summary>

The consumer records each processed key (often within the same transaction as its effect) and checks that store before acting, skipping any key already present. The atomic write of effect-plus-key is what makes a redelivery a no-op even across crashes. This is the explicit, general form of what a unique constraint plus `ON CONFLICT DO NOTHING` does implicitly for an insert.

</details>

<details><summary><b>98.</b> Why must the "seen keys" record be written in the same transaction as the side effect it guards?</summary>

Because if the effect commits but the key record does not (or vice versa), a redelivery either re-applies the effect or wrongly skips an unapplied one — the two must succeed or fail together to stay consistent. Atomicity of effect-plus-key is the crux of a correct idempotent consumer. Splitting them across transactions reintroduces exactly the double-apply you were preventing.

</details>

<details><summary><b>99.</b> When is `ON CONFLICT DO UPDATE` effectively a no-op on rerun, and when does it still "change" the row?</summary>

It is a true no-op when the incoming values equal the stored values, so the update writes the same data; the visible state is unchanged even though an update technically executed. It would change the row if any source-derived column differs — which on a clean rerun of deterministic data it should not. The checksum staying constant is the proof the update was effectively idempotent.

</details>

<details><summary><b>100.</b> Summarise the idempotency checklist an architect should apply to every pipeline stage.</summary>

For the read, confirm it returns a deterministic slice independent of run count; for the transform, confirm it is a pure function with no wall-clock or random keyed values; for the write, confirm it upserts or overwrites a partition on a unique business or synthetic key. Then prove the whole thing with identical row counts and checksums across a double run and a kill-and-rerun. If you can point to the mechanism at all three stages and show the evidence, the design's retry-safety is finished.

</details>


## Phase 1 · 1.8.9 Distributed transactions & 2PC — 100 self-test questions

<details><summary><b>1.</b> What is a distributed transaction?</summary>

A distributed transaction is a single logical transaction whose atomic commit spans two or more separate participants — different databases, message brokers, or services — so that all of them commit or all of them abort together. The hard part is achieving atomicity across processes that can each crash or become unreachable independently. Unlike a local transaction, no single node can unilaterally decide the outcome, which is what forces protocols like two-phase commit into existence.

</details>

<details><summary><b>2.</b> What does `2PC` stand for and what problem does it solve?</summary>

`2PC` stands for two-phase commit, an atomic commit protocol that coordinates several participants so they reach the same commit-or-abort decision. It solves the distributed atomicity problem: making a transaction that touches multiple nodes appear all-or-nothing even though each node commits its own local data. It does this by splitting commit into a voting phase and a decision phase under a single coordinator.

</details>

<details><summary><b>3.</b> Name the two phases of `2PC`.</summary>

The two phases are the prepare phase (phase 1) and the commit phase (phase 2). In prepare, the coordinator asks every participant whether it can commit, and each votes yes or no; in commit, the coordinator broadcasts the final decision — commit if all voted yes, abort otherwise. The phase boundary is the crucial commit point: once the coordinator has collected all yes votes and durably records its decision, the transaction is irrevocably committed.

</details>

<details><summary><b>4.</b> What role does the coordinator (transaction manager) play in `2PC`?</summary>

The coordinator, also called the transaction manager, drives the protocol: it issues the prepare request, collects votes, makes the single global commit-or-abort decision, durably logs that decision, and then tells every participant what to do. It is the only entity allowed to decide the outcome, which centralizes authority but also makes it the single point whose failure can block everyone. In XA terminology the participants are resource managers and the coordinator is the transaction manager (TM).

</details>

<details><summary><b>5.</b> What exactly does a participant promise when it replies "yes" / "prepared" in phase 1?</summary>

By voting "prepared" a participant promises that it can definitely commit the transaction later if asked, and that it will not abort it on its own initiative — it has surrendered its right to unilaterally decide. To back that promise it must have durably written everything needed (typically the WAL records and locks) so the commit can survive a crash. From that moment the participant is bound to whatever the coordinator decides, even across a restart.

</details>

<details><summary><b>6.</b> Why is the vote in phase 1 described as "the point of no return" for a participant?</summary>

Once a participant answers "prepared", it has given up the option to abort unilaterally, so it must wait for the coordinator's decision no matter how long that takes. It cannot time out and roll back, because the coordinator may have already told other participants to commit, and rolling back would break atomicity. This is precisely why a prepared-but-undecided participant is stuck holding locks until it hears back.

</details>

<details><summary><b>7.</b> What are the two "points of no return" that together make `2PC` atomic?</summary>

First, when a participant votes "yes/prepared" it can no longer abort on its own. Second, when the coordinator durably logs its commit decision, it can no longer change its mind. These two irrevocable commitments, taken together, guarantee that once the coordinator decides commit, every participant will eventually commit, giving the protocol its all-or-nothing property.

</details>

<details><summary><b>8.</b> How does `2PC` differ from a single-node commit in a database like Postgres?</summary>

A single-node commit is atomic for free: one process flushes one WAL record and the transaction is durably committed in one step, with no voting. `2PC` adds a round trip — prepare, collect votes, log decision, broadcast — to coordinate independent nodes that each have their own crash and network failure modes. The extra phase exists only because no single node can speak for the others.

</details>

<details><summary><b>9.</b> In Postgres, which command places a transaction into the prepared state for external coordination?</summary>

`PREPARE TRANSACTION 'some_gid'` writes the transaction's state durably to disk and dissociates it from the current session, leaving it prepared but not yet committed. A coordinator can later issue `COMMIT PREPARED 'some_gid'` or `ROLLBACK PREPARED 'some_gid'`. This is exactly the participant side of `2PC`; the prepared transaction keeps holding its locks until one of those commands arrives.

</details>

<details><summary><b>10.</b> What is the `max_prepared_transactions` setting in Postgres and why does it default to 0?</summary>

`max_prepared_transactions` caps how many transactions can be in the prepared state at once, and it defaults to `0`, which disables `PREPARE TRANSACTION` entirely. It ships off by default because prepared transactions that are never resolved hold locks and pin resources indefinitely, so the feature is opt-in for systems that actually run an external transaction coordinator. Leaving it at 0 is a deliberate "don't let people accidentally create in-doubt transactions" guardrail.

</details>

<details><summary><b>11.</b> Describe the happy-path `2PC` message flow at a high level.</summary>

The coordinator sends `prepare` to all participants; each does its local work, durably records it, and replies `yes`. The coordinator collects every reply, sees all yeses, durably logs a commit decision, and sends `commit` to all participants; each commits locally and acknowledges. The transaction is logically committed the instant the coordinator's decision hits durable storage, even before the acks come back.

</details>

<details><summary><b>12.</b> What happens in `2PC` if any single participant votes "no" in the prepare phase?</summary>

A single "no" vote forces a global abort: the coordinator logs an abort decision and sends `rollback` to every participant, including those that voted yes. This preserves atomicity — one participant being unable to commit means none may commit. Participants that had voted yes simply release their locks and discard the prepared work.

</details>

<details><summary><b>13.</b> For an order-service plus position-service write, sketch where `2PC` inserts itself.</summary>

The coordinator first tells the order service and the position service to prepare their respective writes — inserting the order row and updating the position row — and each locks those rows and votes prepared. Once both vote yes, the coordinator logs commit and tells both to commit, making the order and the position change atomically visible together. The single transaction guarantees you never see an executed order without its matching position change.

</details>

<details><summary><b>14.</b> In that order/position example, what is "atomic visibility" and why is it the thing `2PC` buys you?</summary>

Atomic visibility means no observer can ever see a state where the order is recorded but the position is not, or vice versa — both writes become visible at the same instant. `2PC` delivers this by deferring all commits until the single global decision, so the two services flip from "not committed" to "committed" together. That is the entire value proposition you are weighing against availability when you reject it.

</details>

<details><summary><b>15.</b> What is an "in-doubt" transaction in `2PC`?</summary>

An in-doubt transaction is one on a participant that has voted "prepared" but has not yet received the coordinator's final commit-or-abort decision. The participant cannot resolve it on its own because either outcome is still possible and only the coordinator knows the answer. Until the decision arrives, the transaction sits prepared, holding all its locks.

</details>

<details><summary><b>16.</b> What is the central blocking failure mode of `2PC`?</summary>

If the coordinator crashes after participants have voted "prepared" but before delivering the decision, those participants are stuck in-doubt: they cannot commit, cannot abort, and must wait for the coordinator to recover. During that wait they hold their locks, blocking any other transaction that needs the same rows. This is why `2PC` is called a blocking protocol — a single coordinator failure can freeze every participant indefinitely.

</details>

<details><summary><b>17.</b> When a `2PC` coordinator dies mid-commit, what happens to the participants' locks?</summary>

The locks held by every prepared, in-doubt participant stay held — they are not released, because releasing them could violate atomicity if the coordinator had actually decided commit. So rows touched by the transaction remain locked, and other transactions that need those rows block behind them. The locks persist until the coordinator recovers and replays its decision, or an operator manually resolves the transaction.

</details>

<details><summary><b>18.</b> Who is able to release the locks of an in-doubt participant, and who is not?</summary>

Only the coordinator's recovered decision (or a human operator stepping in) can legitimately release them; the in-doubt participant itself cannot, because it lacks the information to know whether commit or abort is correct. A participant that unilaterally guessed and was wrong would break atomicity across the system. This is the heart of why `2PC` blocks: the one actor who could safely decide is exactly the one that is down.

</details>

<details><summary><b>19.</b> Why can't an in-doubt participant simply time out and abort like a normal transaction would?</summary>

Because the coordinator may have already collected all yes votes, logged a commit decision, and told other participants to commit before crashing. If this participant aborted while others committed, atomicity is shattered. Having voted "prepared", it forfeited the right to abort on its own, so timing out is not a safe option — it must wait.

</details>

<details><summary><b>20.</b> How does the coordinator recover its decision after a crash in `2PC`?</summary>

The coordinator writes its commit-or-abort decision to a durable transaction log before sending it out, so on restart it reads that log to learn the outcome of every in-flight transaction. For any transaction whose decision was logged, it re-sends commit or abort to the participants until they acknowledge. Transactions that crashed before the decision was logged are aborted, since no participant could have been told to commit yet.

</details>

<details><summary><b>21.</b> Why must the coordinator's log write happen before it contacts any participant in phase 2?</summary>

If the coordinator told even one participant to commit and then crashed without having logged the decision, it would forget the outcome on restart while a participant had already committed — an unrecoverable inconsistency. Logging first guarantees that any decision visible to a participant is also recoverable by the coordinator. This ordering, decision-to-log then decision-to-participants, is what makes recovery deterministic.

</details>

<details><summary><b>22.</b> Can participants ask each other to resolve an in-doubt transaction if the coordinator is down?</summary>

In basic `2PC`, no — participants do not generally know each other and have no protocol to learn the global decision from a peer, so they remain blocked. There is a variant called three-phase commit (3PC) that adds a pre-commit phase to reduce blocking under certain failure assumptions, but it relies on bounded network delays and is rarely used in practice. Plain `2PC` simply blocks until the coordinator returns.

</details>

<details><summary><b>23.</b> What is a "heuristic decision" in the context of XA / in-doubt transactions?</summary>

A heuristic decision is when a resource manager, tired of waiting for an absent transaction manager, unilaterally commits or rolls back an in-doubt branch on its own — a heuristic commit or heuristic rollback. It breaks the protocol's guarantee deliberately to free locks, gambling on the likely outcome. If different resource managers guess differently you get a "heuristic mixed" outcome, where the distributed transaction is no longer atomic and a human must reconcile it.

</details>

<details><summary><b>24.</b> What is a "heuristic mixed" outcome and why is it dangerous?</summary>

A heuristic mixed (or heuristic hazard) outcome occurs when some participants heuristically committed while others heuristically rolled back the same distributed transaction, so atomicity is permanently violated. It is dangerous because the data is now inconsistent across systems in a way the protocol cannot self-correct — for example one ledger recorded a trade leg while the other did not. Resolving it requires manual investigation and compensating action, exactly the operational nightmare `2PC` was supposed to prevent.

</details>

<details><summary><b>25.</b> Why does holding locks during the in-doubt window make `2PC` especially bad for a busy fund platform?</summary>

In a high-throughput book, the same instrument rows (positions, cash balances per ISIN) are contended by many concurrent operations, so an in-doubt transaction holding those locks stalls every other order touching them. A coordinator outage during the trading day therefore cascades from one stuck transaction into a platform-wide freeze on the affected books. This is the "holds locks across the books at the worst possible moment" failure the lesson warns about.

</details>

<details><summary><b>26.</b> What does `XA` stand for and who defined it?</summary>

`XA` is the standard interface for distributed transactions defined by the X/Open consortium (now The Open Group) as part of its Distributed Transaction Processing (DTP) model. It specifies how a transaction manager coordinates multiple resource managers using `2PC`. It is the spec behind Java's JTA and the `XA` drivers offered by many databases and message brokers.

</details>

<details><summary><b>27.</b> In the `XA` / DTP model, what are the roles of the transaction manager and resource managers?</summary>

The transaction manager (TM) is the coordinator: it begins the global transaction and drives the `2PC` prepare/commit cycle. Each resource manager (RM) — a database, queue, or other transactional store — manages its own local data and participates by voting and committing. The `XA` interface (with calls like `xa_prepare`, `xa_commit`, `xa_rollback`) is the contract between TM and RMs.

</details>

<details><summary><b>28.</b> Name two or three `XA` interface calls a resource manager must implement.</summary>

A compliant resource manager implements calls such as `xa_start` and `xa_end` (to associate work with a transaction branch), `xa_prepare` (vote), `xa_commit` and `xa_rollback` (apply the decision), and `xa_recover` (list in-doubt branches after a crash). These C-style entry points are how the transaction manager drives `2PC` across heterogeneous resources. `xa_recover` is what lets a restarted TM find branches still awaiting a decision.

</details>

<details><summary><b>29.</b> According to DDIA, why do heterogeneous distributed transactions tend to "rot" in real systems?</summary>

Because `XA` is only as strong as its weakest link: every participating system must implement the protocol correctly, and the transaction manager itself becomes a critical, stateful component whose log must be durable and highly available. In practice the coordinator is often an afterthought, its log lives on one application server, and a crash there blocks the databases it coordinates — so the whole arrangement is fragile and operationally painful. Mixing vendors multiplies the chance that some participant mishandles in-doubt recovery.

</details>

<details><summary><b>30.</b> Why is the transaction manager's own durability a frequent weak point in `XA` deployments?</summary>

The TM must durably remember every global decision, yet it is often just a library running inside an application process rather than a replicated, fault-tolerant service. If that process and its log disk are lost, every database it coordinated is left with unresolvable in-doubt transactions. DDIA highlights this irony: you add `2PC` for reliability but introduce a new, often under-engineered single point of failure.

</details>

<details><summary><b>31.</b> How does `2PC` interact with connection pooling and stateless application servers?</summary>

Badly — a prepared transaction is bound to a specific database connection and must be completed from the coordinator's perspective, but stateless app servers and pooled connections assume any connection is interchangeable and can be recycled freely. An in-doubt transaction pins its connection and locks until resolved, which clashes with the pool's churn. This impedance mismatch is one of the practical reasons `XA` is awkward to run in modern microservice fleets.

</details>

<details><summary><b>32.</b> Does `2PC` work cleanly when one participant is a message broker rather than a database?</summary>

Only if the broker is a fully `XA`-capable resource manager that supports prepared, in-doubt message state — and even then it inherits all the blocking and recovery problems. Many popular brokers either do not support `XA` or support it with caveats, so you cannot reliably enlist them in a heterogeneous distributed transaction. This is a big reason the industry moved to the transactional outbox, which needs only a local database transaction.

</details>

<details><summary><b>33.</b> Why does adding more participants make `2PC` exponentially less attractive operationally?</summary>

Each additional participant is another node that can crash or partition during the in-doubt window, and a single one being unreachable blocks the whole transaction. The probability that at least one participant is unavailable grows with the number of participants, so availability degrades as you add resources. You are multiplying failure surfaces while the protocol can tolerate none of them without blocking.

</details>

<details><summary><b>34.</b> How does `2PC` performance compare with local transactions, and why?</summary>

`2PC` is substantially slower: it adds network round trips for prepare and commit, forces extra durable log flushes on the coordinator and participants, and holds locks for the full duration of the slowest participant plus any network delay. Throughput is gated by the slowest node and by lock contention during the extended commit window. DDIA notes order-of-magnitude penalties are common, which alone disqualifies it for hot paths.

</details>

<details><summary><b>35.</b> Is `2PC` an example of a consensus algorithm? Explain.</summary>

No — `2PC` is an atomic commit protocol, not a consensus algorithm, even though both get nodes to agree on something. The key difference is that `2PC` requires unanimous agreement and a single coordinator whose failure blocks progress, whereas consensus tolerates a minority of failures and never blocks on any single node. They solve related but distinct problems, and conflating them is a common mistake.

</details>

<details><summary><b>36.</b> What problem does Raft (consensus) solve that `2PC` does not?</summary>

Raft lets a cluster keep making progress and agreeing on a value even when a minority of nodes — including the leader — fail, because decisions are made by a majority quorum rather than by one indispensable coordinator. `2PC`, by contrast, blocks the moment its single coordinator is unreachable. So Raft removes the single blocking point that is `2PC`'s defining weakness.

</details>

<details><summary><b>37.</b> State in two sentences what Raft guarantees that `2PC` cannot.</summary>

Raft guarantees liveness despite the failure of any minority of nodes, including its leader, by electing a new leader from the surviving majority and continuing without manual intervention. `2PC` cannot guarantee this because its single coordinator is a blocking point: if it dies mid-commit, prepared participants are stuck until it returns.

</details>

<details><summary><b>38.</b> What is a quorum in Raft, and how many failures can a 5-node cluster tolerate?</summary>

A quorum is a majority of nodes — strictly more than half — required to elect a leader and to commit a log entry. With `2f+1` nodes you tolerate `f` failures, so a 5-node cluster (`f=2`) keeps working with up to 2 nodes down. The overlapping-majority property ensures any two quorums share at least one node, which prevents two conflicting decisions.

</details>

<details><summary><b>39.</b> How does Raft avoid the single-coordinator blocking that plagues `2PC`?</summary>

Raft has a leader, but the leader is not indispensable: if it fails, the remaining majority detects the missing heartbeats, runs an election, and elects a new leader, so the cluster never depends on one fixed node surviving. Because commit requires only a majority acknowledgment rather than unanimity, the failure of a minority — leader included — does not block progress. The role of coordinator is replaceable, which is exactly what `2PC` lacks.

</details>

<details><summary><b>40.</b> Why does `2PC` require unanimity while Raft requires only a majority?</summary>

`2PC` is solving atomic commit across distinct resources, where every participant owns data that must all change together, so a single "no" or a single absent participant must veto or block the transaction. Raft is solving replicated agreement on a single log among interchangeable replicas, so as long as a majority agrees, the minority can be brought up to date later. The different requirements stem from different problems: distributed atomicity versus fault-tolerant replication.

</details>

<details><summary><b>41.</b> Can you build an atomic commit that does not block, and how does consensus relate?</summary>

Yes — DDIA notes that an atomic commit protocol can be made non-blocking if it is built on a consensus algorithm, because consensus survives minority failures. Systems like Google's Spanner effectively layer `2PC` over Paxos/Raft groups so that each "participant" is itself a fault-tolerant replicated group, removing the single-coordinator block. So consensus is the foundation that lets atomic commit stop being a blocking protocol.

</details>

<details><summary><b>42.</b> Why isn't replacing `2PC` with Raft a drop-in solution for cross-service writes?</summary>

Raft replicates a single state machine among homogeneous replicas; it does not, by itself, atomically commit writes across two different services that own different data and schemas. You would still need an atomic-commit layer over the consensus groups, plus all the latency and coupling that implies. For ordinary microservice writes, that coupling is usually worse than just embracing eventual consistency via outbox or saga.

</details>

<details><summary><b>43.</b> What is the transactional outbox pattern?</summary>

The transactional outbox pattern writes the business change and an "outbox" message row in the same local database transaction, so they commit atomically without any distributed transaction. A separate relay process then reads new outbox rows and publishes them to the message broker, marking them sent. This converts a risky dual-write into one local commit plus reliable, retryable delivery.

</details>

<details><summary><b>44.</b> How does the outbox pattern give you atomicity without `2PC`?</summary>

The only atomic operation it needs is a single local transaction in one database, which every relational engine provides for free — the business row and the outbox row commit or roll back together. There is no coordinator, no prepared state, and no cross-system lock, so there is nothing to block. The trade is that the message is published slightly later (asynchronously), giving eventual rather than atomic visibility.

</details>

<details><summary><b>45.</b> What is a message relay / "polling publisher" in the outbox pattern?</summary>

It is the component that moves messages from the outbox table to the broker, either by periodically polling the table for unsent rows (polling publisher) or by tailing the database's change log (transaction-log tailing, e.g. with Debezium). It publishes each message and marks it as dispatched, retrying on failure. Because publishing is idempotent-friendly and at-least-once, downstream consumers must deduplicate.

</details>

<details><summary><b>46.</b> What delivery guarantee does the outbox typically provide, and what does that demand of consumers?</summary>

It typically provides at-least-once delivery: a message may be published more than once if the relay crashes after publishing but before marking the row sent. Consumers must therefore be idempotent — processing the same message twice must have the same effect as processing it once, often via a unique message id and a processed-ids table. This is the standard price of avoiding distributed transactions.

</details>

<details><summary><b>47.</b> What is a saga?</summary>

A saga is a sequence of local transactions across multiple services, where each step commits independently and publishes an event that triggers the next step. If a later step fails, the saga runs compensating transactions to semantically undo the prior steps, since you cannot roll back already-committed local transactions. It trades global atomicity for a managed, eventually-consistent multi-step workflow.

</details>

<details><summary><b>48.</b> What is a compensating transaction in a saga?</summary>

A compensating transaction is an explicit, business-level action that semantically undoes a previously committed step — for example, "cancel the reservation" to compensate "make the reservation", since the original local commit cannot be physically rolled back. Sagas rely on these compensations to recover from partial failure. Designing correct compensations (and handling that some actions are hard to undo, like a sent SWIFT message) is the main difficulty of the pattern.

</details>

<details><summary><b>49.</b> Contrast orchestration-based and choreography-based sagas.</summary>

In choreography, each service reacts to events and emits the next event with no central brain, which is decentralized but can become hard to follow as steps grow. In orchestration, a dedicated orchestrator tells each service what to do next and handles compensations, which centralizes the logic and is easier to reason about and monitor. The choice trades coupling and visibility against having a central component to maintain.

</details>

<details><summary><b>50.</b> What does a saga give up compared with `2PC`, and what does it gain?</summary>

A saga gives up atomic visibility and isolation: intermediate states are observable, so another transaction can see a half-finished saga, and you must compensate rather than roll back. In return it gains availability and loose coupling — every step is a fast local commit with no cross-service locks or coordinator, so one service being down does not freeze the others. This availability-for-isolation trade is exactly the point of an ADR rejecting `2PC`.

</details>

<details><summary><b>51.</b> Why is "lack of isolation" the headline weakness of sagas?</summary>

Because a saga's intermediate local commits are immediately visible, another operation can read or act on data that a not-yet-complete saga will later compensate away — analogous to a dirty read across services. You mitigate this with semantic locks, versioning, or status flags ("pending"), but you never get the clean serializable isolation a single transaction offers. Recognizing and designing around this exposure is the core saga skill.

</details>

<details><summary><b>52.</b> For the order-service/position-service write, how would outbox replace `2PC`?</summary>

The order service, in one local transaction, inserts the order row and an outbox row describing "order executed"; a relay publishes that event, and the position service consumes it and updates the position in its own local transaction. There is no coordinator and no cross-service lock — each side commits locally — so a position update may lag the order by milliseconds. You accept brief eventual consistency in exchange for not freezing the books when one service is down.

</details>

<details><summary><b>53.</b> When writing an ADR that rejects `2PC`, what is the minimum it should state?</summary>

It should name the consistency requirement, state that `2PC`/`XA` would meet it but at the cost of blocking and lock-holding when the coordinator fails, and name the chosen alternative — transactional outbox or saga. Crucially it must state the explicit trade: you give up atomic visibility (intermediate states become observable) and gain availability and decoupling. An ADR that just says "2PC is bad" without naming the trade-off is incomplete.

</details>

<details><summary><b>54.</b> In an ADR, what exactly do you write that you "give up" by choosing outbox/saga over `2PC`?</summary>

You give up atomic cross-service visibility: there will be a window where one service has committed and the other has not, so observers can see a partial state, and you must compensate rather than roll back on failure. You also give up clean isolation, accepting at-least-once delivery and the need for idempotent consumers. Naming these concessions honestly is what makes the ADR defensible.

</details>

<details><summary><b>55.</b> In an ADR, what exactly do you write that you "gain" by choosing outbox/saga over `2PC`?</summary>

You gain availability and fault isolation: each service commits locally with no coordinator and no cross-service locks, so one service being down or slow does not block the others or hold locks across the books. You also gain operational simplicity — no XA coordinator log to keep highly available, no in-doubt recovery runbooks. The system degrades gracefully instead of freezing.

</details>

<details><summary><b>56.</b> Why is "steer to outbox/saga with reasons, not taste" the architect's job here?</summary>

Because anyone can have an opinion that `2PC` is old-fashioned, but an architect must justify the choice with the concrete failure mode — coordinator death leaving in-doubt transactions that hold locks across contended rows — and the precise trade being made. Reasoned rejection survives pushback from a vendor or a senior engineer who proposes XA; taste does not. The lesson's whole point is to be able to defend the decision mechanically.

</details>

<details><summary><b>57.</b> A teammate proposes `XA` `2PC` between the order and position services. What is your first counter-argument?</summary>

That `2PC` makes the two services share fate: if the coordinator dies after prepare, both services sit in-doubt holding locks on the contended order/position rows, turning a coordinator blip into a trading-floor outage. That blocking failure mode is unacceptable on a hot path, and outbox gives you the same business outcome with eventual consistency and no shared lock. Lead with the lock-holding outage, because that is the visceral operational cost.

</details>

<details><summary><b>58.</b> What is the dual-write problem that outbox specifically solves?</summary>

The dual-write problem is needing to update a database and publish a message as one atomic action, but doing them as two separate operations means a crash between them leaves the system inconsistent — the row changed but the event was lost, or vice versa. Outbox solves it by making the database write and the event-row write a single local transaction, then publishing from that durable row. It removes the gap where the two writes could diverge.

</details>

<details><summary><b>59.</b> Why is "just publish to Kafka after committing to the database" not a safe alternative to outbox?</summary>

Because the process can crash in the gap between the database commit and the Kafka publish, losing the event while the data change persisted — the classic dual-write failure. There is no transaction spanning the database and Kafka to make them atomic. Outbox closes the gap by committing the event into the same database transaction and publishing it reliably afterward.

</details>

<details><summary><b>60.</b> How does log-tailing (CDC) relate to the outbox pattern?</summary>

Instead of polling an outbox table, you can tail the database's transaction log with change-data-capture (e.g. Debezium reading the Postgres WAL) and turn committed changes into messages. This avoids the polling overhead and the extra outbox table in some designs, while still publishing only durably committed changes. It is an implementation variant of the same "publish from the durable log, not a dual write" idea.

</details>

<details><summary><b>61.</b> What does it mean that `2PC` provides atomicity but not high availability?</summary>

It means `2PC` correctly guarantees all-or-nothing commit across participants, but it achieves this by blocking — sacrificing the ability to make progress — whenever the coordinator or a participant is unreachable. So it is safe (never inconsistent) but not live (can freeze). The alternatives flip this: they relax atomic visibility to stay available.

</details>

<details><summary><b>62.</b> Map `2PC`'s trade-off onto CAP-style thinking.</summary>

`2PC` favors consistency over availability: faced with a partition or coordinator loss it blocks rather than risk an inconsistent commit, so it gives up availability to preserve atomicity. Saga and outbox lean the other way — they stay available and accept eventual consistency, surfacing intermediate states. This is the same C-vs-A tension expressed at the commit-protocol level.

</details>

<details><summary><b>63.</b> Scenario: positions are locked and orders are timing out across multiple books at once. What `2PC`-related cause should you check first?</summary>

Check whether an `XA`/`2PC` coordinator has died or partitioned, leaving prepared transactions in-doubt and holding locks on the shared position rows. Look for prepared transactions on the database — in Postgres, query `pg_prepared_xacts` — and confirm whether the transaction manager is reachable. A dead coordinator is the textbook cause of simultaneous lock-up across contended books.

</details>

<details><summary><b>64.</b> How would you list in-doubt prepared transactions on a Postgres participant?</summary>

Query the `pg_prepared_xacts` system view, which shows every transaction that has been `PREPARE TRANSACTION`'d but not yet committed or rolled back, including its global id, owner, and prepare time. Long-lived rows there are your in-doubt transactions holding locks. You then resolve each with `COMMIT PREPARED` or `ROLLBACK PREPARED` once you know (from the coordinator) the correct outcome.

</details>

<details><summary><b>65.</b> An in-doubt Postgres prepared transaction is blocking trading. The coordinator is permanently gone. What are your options and risks?</summary>

Your only options are to manually `COMMIT PREPARED` or `ROLLBACK PREPARED` it to free the locks, but you are guessing the global outcome the dead coordinator never delivered. Guess wrong and you create a heuristic outcome — this participant disagrees with another, breaking atomicity across the books and requiring reconciliation. You must determine the intended outcome from other evidence (other participants' state, logs) before forcing it, and document the manual intervention.

</details>

<details><summary><b>66.</b> Why does the lesson call a blocked `2PC` coordinator "an outage at the worst possible moment"?</summary>

Because the in-doubt window holds locks precisely on the hottest, most contended rows — positions and cash per instrument — during active trading, so the freeze hits when volume and stakes are highest. A coordinator failure that would be a minor blip in a quiet system becomes a book-wide trading halt. The damage scales with how busy and contended the data is, which in a fund platform is maximal during the trading day.

</details>

<details><summary><b>67.</b> How does NAV calculation relate to the dangers of distributed transactions across services?</summary>

NAV depends on consistent, complete inputs — positions, prices, cash, corporate actions — often owned by different services, and a `2PC` arrangement to keep them in lockstep would block NAV-relevant writes whenever the coordinator failed, potentially during the valuation window. An outbox/saga design keeps each input service available and reconciles to a consistent snapshot, accepting brief eventual consistency. You would rather compute NAV from a known-consistent cut than have a coordinator freeze the inputs.

</details>

<details><summary><b>68.</b> If a saga step is "send a SWIFT settlement message", why is compensation hard?</summary>

Because a sent SWIFT message is an external, real-world side effect that cannot be un-sent — you cannot roll it back, only issue a follow-up cancellation or correction message (e.g. a reversal), which is itself a new business action that may not always be possible. This is the classic "irreversible step" problem in sagas: some actions have no clean compensator. You must order such steps carefully (often last, as a pivot/retriable step) and design explicit reversal flows.

</details>

<details><summary><b>69.</b> What is a "pivot transaction" in saga design and why does it matter for irreversible steps?</summary>

The pivot transaction is the step after which the saga is committed to completing — steps before it are compensatable, steps after it are retriable (must eventually succeed) and cannot be compensated. Placing an irreversible action like a SWIFT send at or after the pivot means the saga is structured to always drive it to completion rather than undo it. Identifying the pivot is how you handle steps that cannot be compensated.

</details>

<details><summary><b>70.</b> How do EMT/EPT file generation pipelines benefit from outbox over distributed transactions?</summary>

Producing EMT (European MiFID Template) or EPT (European PRIIPs Template) files draws on cost, risk, and product data from several systems; coordinating those reads/writes via `2PC` would couple their availability and risk blocking during the generation run. An outbox/event-driven approach lets each source publish its data changes reliably and the file-builder consume a consistent set, decoupling failures. You accept eventual consistency in exchange for a generation pipeline that does not freeze when one source is briefly down.

</details>

<details><summary><b>71.</b> Why might a transfer-agency platform prefer saga/outbox for a subscription workflow?</summary>

A subscription touches the order book, cash/settlement, the register of holders, and possibly AML checks — often different services — and a `2PC` across them would hold locks and block the whole flow on any coordinator hiccup. A saga lets each step commit locally and compensate on failure (e.g. reverse a provisional allocation), keeping the platform available under partial failure. The intermediate "pending" states are made explicit to the operations team rather than hidden behind a blocking commit.

</details>

<details><summary><b>72.</b> How does an LEI- or ISIN-keyed reference data update illustrate the dual-write problem?</summary>

Suppose updating an instrument's reference data must both persist the change and notify downstream systems keyed by ISIN/LEI; doing the database write and the notification as separate steps risks a crash that persists the data but loses the notification, leaving consumers stale. Outbox fixes this by committing the change and an outbox event in one transaction, then publishing reliably. Downstream caches keyed by ISIN then converge once the event is delivered.

</details>

<details><summary><b>73.</b> Why is idempotency by message id essential in a fund-data outbox pipeline?</summary>

Because at-least-once delivery means a position or cash event may arrive twice, and applying it twice — double-counting a trade or a fee — would corrupt the books or NAV. Consumers must record processed message ids and skip duplicates, so reprocessing is a no-op. In a regulated context, this deterministic, replayable processing is also what makes the pipeline auditable and recoverable.

</details>

<details><summary><b>74.</b> Could a regulator's expectation of consistency (e.g. under UCITS/AIFMD reporting) force you back toward `2PC`?</summary>

Not usually — regulators care about correct, reconcilable, auditable end states, not about microsecond-level atomic visibility across services, which is what `2PC` uniquely buys. An eventually-consistent design with reliable delivery, idempotent processing, and reconciliation produces correct reports while staying available, which is generally preferable. You document in the ADR that the consistency requirement is "eventually reconciled and auditable", not "atomically visible".

</details>

<details><summary><b>75.</b> How does DORA's emphasis on operational resilience inform the `2PC`-vs-saga choice?</summary>

DORA stresses that systems must withstand and recover from operational disruptions, and a blocking protocol that freezes the books when a single coordinator fails is the antithesis of resilience. Choosing outbox/saga, which degrades gracefully and recovers via retries and compensations, aligns with that resilience expectation. The ADR can cite operational resilience as an explicit reason to reject `2PC`'s single blocking point.

</details>

<details><summary><b>76.</b> What is the difference between atomicity and isolation, and which does a saga sacrifice?</summary>

Atomicity is all-or-nothing completion; isolation is that concurrent transactions do not see each other's partial work. A saga sacrifices isolation first and foremost — intermediate committed steps are visible to others — while it preserves a weaker, eventual form of "atomicity" through compensation rather than rollback. So the precise concession to name is loss of isolation (visible intermediate states), not loss of all atomicity.

</details>

<details><summary><b>77.</b> Why does `2PC` hold locks for longer than a normal transaction even on the happy path?</summary>

Because locks acquired during local work must be held all the way through the prepare phase, the network round trip to collect votes, the coordinator's durable log write, and the commit broadcast — a much longer window than a single-node commit. Lock duration is bounded by the slowest participant and the slowest network hop, not by local work. Longer lock hold times mean more contention and lower concurrency even when nothing fails.

</details>

<details><summary><b>78.</b> What is the relationship between `2PC` and the FLP impossibility / blocking?</summary>

`2PC`'s blocking is a concrete instance of the general truth that you cannot have a non-blocking atomic commit with a single coordinator under asynchronous failures — there is no safe action for an in-doubt participant when the decider is unreachable. Consensus algorithms sidestep this by using majorities and replaceable leaders, trading the requirement of unanimity for fault tolerance. This is why "just use 2PC" does not escape the fundamental difficulty; it only relocates it to the coordinator.

</details>

<details><summary><b>79.</b> How would you explain to a non-expert stakeholder why you are not using `2PC`?</summary>

You can say `2PC` is like requiring two clerks to stamp a document at the exact same instant with a manager watching — if the manager steps out mid-stamp, both clerks freeze with the document locked and nobody else can touch it until the manager returns. We instead let each clerk stamp their own copy and reconcile, so a missing manager never freezes the office. The cost is a brief moment where the copies disagree, which we detect and fix automatically.

</details>

<details><summary><b>80.</b> What durable state must a `2PC` participant write at prepare time, and why?</summary>

At prepare it must durably persist all the transaction's effects and its lock state — typically flushing the relevant WAL records — so that even after a crash and restart it can still honor a later commit. This is what backs its promise that it can definitely commit if asked. Without that durable record, the "prepared" vote would be a lie the moment the participant restarted.

</details>

<details><summary><b>81.</b> After a participant restarts, how does it know which transactions are in-doubt and how to handle them?</summary>

On restart it reads its own durable prepared-transaction records (in Postgres, these reappear in `pg_prepared_xacts`; via XA, `xa_recover` lists branches) and re-acquires the corresponding locks, then waits to learn each transaction's fate from the coordinator. It must not assume an outcome. The coordinator, recovering its decision log, re-delivers commit or abort so each in-doubt branch is finally resolved.

</details>

<details><summary><b>82.</b> Why must locks be re-acquired by a participant when it recovers an in-doubt transaction after a crash?</summary>

Because the transaction is still unresolved and might commit, so the rows it touched must stay protected from conflicting concurrent changes until the decision arrives. If the participant released the locks on restart and the transaction later committed, intervening writes could have produced an inconsistent result. Re-acquiring the locks preserves the same isolation guarantee that existed before the crash.

</details>

<details><summary><b>83.</b> What is the difference between `2PC` and two-phase locking (`2PL`)?</summary>

They are unrelated despite the similar names: `2PC` is an atomic commit protocol coordinating multiple nodes, while two-phase locking (`2PL`) is a single-database concurrency-control technique that acquires locks in a growing phase and releases them in a shrinking phase to ensure serializability. One is about distributed commit, the other about local isolation. Confusing them is a classic interview trap.

</details>

<details><summary><b>84.</b> In the `2PC` flow, at exactly what instant is the transaction considered committed?</summary>

The transaction becomes committed the moment the coordinator durably writes its commit decision to its log — even before any participant has been told or has acknowledged. From that instant the outcome is fixed and recoverable, so all participants will eventually commit no matter what crashes next. Pinpointing this commit point is essential to reasoning about recovery.

</details>

<details><summary><b>85.</b> If the coordinator crashes after logging "commit" but before telling participants, what happens?</summary>

Nothing is lost: on restart the coordinator reads its log, sees the commit decision, and re-sends commit to every participant until they acknowledge. The participants were in-doubt and holding locks during the outage but were never at risk of an inconsistent outcome. This is the "good" coordinator crash — recovery completes the protocol correctly, just with a blocking delay.

</details>

<details><summary><b>86.</b> If the coordinator crashes after prepare but before logging any decision, what happens?</summary>

It aborts: on restart it finds no recorded decision for that transaction, and since no participant could yet have been told to commit, the only safe choice is to abort and tell participants to roll back. The in-doubt participants release their locks and discard the prepared work. The protocol stays consistent, again at the cost of a blocking window during the outage.

</details>

<details><summary><b>87.</b> Why can't you avoid `2PC`'s blocking simply by adding a timeout that aborts in-doubt transactions?</summary>

Because a participant timing out and aborting might contradict a commit decision the coordinator already logged and possibly delivered to others, producing a split outcome. The safe answer to "what should an in-doubt participant do?" is "wait", and a timeout that acts violates that. This is exactly why automatic timeout-abort is unsafe and why true non-blocking commit needs consensus, not just a clock.

</details>

<details><summary><b>88.</b> What does "atomic commit requires the same value to be agreed by all" have to do with consensus?</summary>

Atomic commit is essentially a consensus problem with the extra constraint of unanimity — every participant must agree on the single commit-or-abort value, and a "no" from any one forces abort. Pure consensus relaxes this to majority agreement, which is why it can be non-blocking. Recognizing atomic commit as "consensus plus unanimity" clarifies both why `2PC` blocks and why building it over consensus removes the block.

</details>

<details><summary><b>89.</b> How does Spanner relate to `2PC` and consensus in your mental model?</summary>

Spanner runs `2PC` across shards, but each shard is itself a Paxos group, so every participant in the commit is a fault-tolerant replicated entity rather than a single fragile node. This removes `2PC`'s single-coordinator block by making each role survive minority failures via consensus. It is the canonical example that `2PC` is not irredeemable — its blocking comes from non-fault-tolerant participants, which consensus fixes.

</details>

<details><summary><b>90.</b> Why is "use a saga" not a license to ignore consistency entirely?</summary>

Because a saga still must reach a correct final state through compensations, and you must design and test those compensations, handle partial-failure ordering, and expose intermediate "pending" states safely. Eventual consistency is a discipline, not an absence of consistency — you owe reconciliation and idempotency. A sloppy saga can corrupt data just as badly as a misused `2PC`.

</details>

<details><summary><b>91.</b> What is a semantic lock in saga terminology?</summary>

A semantic lock is an application-level marker — like a `status = 'PENDING'` flag on a record — that tells other operations the data is mid-saga and should be treated cautiously, partially recovering the isolation that sagas otherwise lack. It is not a database lock; it is a business-level signal that the value may still be compensated away. It is one of the standard countermeasures for the lack-of-isolation problem.

</details>

<details><summary><b>92.</b> Summarize when, if ever, `2PC` is the right choice.</summary>

`2PC`/`XA` is occasionally justified within a single, controlled environment where all participants are XA-capable, the coordinator is highly available, transactions are short, contention is low, and you genuinely need atomic visibility you cannot reconcile after the fact. Even then, modern systems usually prefer consensus-backed commit or outbox/saga. For cross-service writes on a busy fund platform's hot path, the blocking risk almost always rules it out.

</details>

<details><summary><b>93.</b> What is the single most important sentence to put in the "Done when" check about coordinator death and locks?</summary>

"When a `2PC` coordinator dies mid-commit, prepared participants are left in-doubt and keep holding their locks — they can neither commit nor abort on their own — until the coordinator recovers its logged decision (or an operator manually resolves them), and only those parties can safely release the locks." That sentence captures the failure mode, the lock fate, and who can resolve it. It is the lesson's core takeaway in one breath.

</details>

<details><summary><b>94.</b> How would you phrase, in two sentences, the Raft-vs-`2PC` distinction for the "Done when" check?</summary>

Raft guarantees the cluster keeps agreeing and making progress despite the failure of any minority of nodes, including the leader, because decisions need only a majority quorum and the leader is replaceable. `2PC` cannot guarantee this: its single coordinator is a blocking point, so its failure leaves prepared participants stuck until it returns.

</details>

<details><summary><b>95.</b> Why is naming the alternative pattern (not just rejecting `2PC`) required for a complete ADR?</summary>

Because an architectural decision record exists to record what you will do, not merely what you will avoid — rejecting `2PC` without naming outbox or saga leaves the team without a path forward. Naming the pattern, and the trade it accepts (atomic visibility for availability), makes the decision actionable and reviewable. It also signals you understand the alternative deeply enough to defend it.

</details>

<details><summary><b>96.</b> A reviewer says "outbox is just eventual consistency, which is risky for money." How do you respond?</summary>

You acknowledge it is eventual consistency, then explain the risk is bounded and managed: at-least-once delivery plus idempotent consumers plus reconciliation means the books converge to a correct, auditable state, and the visibility lag is milliseconds, not minutes. The riskier alternative is `2PC` freezing the books when a coordinator dies during trading. For money, a brief, detected, self-correcting divergence beats an unbounded lock-up.

</details>

<details><summary><b>97.</b> What durable component does outbox require that the dual-write does not, and why is that acceptable?</summary>

Outbox requires an outbox table (or log-tailing of the existing WAL) and a relay process, which is modest extra machinery compared to running a highly available XA coordinator. It is acceptable because the only atomic operation needed is a single local transaction the database already provides, and the relay's failures are recoverable via at-least-once retry. You trade a small, well-understood relay for eliminating distributed-commit blocking.

</details>

<details><summary><b>98.</b> Why is message ordering a subtle concern in an outbox/saga design, and how do you address it?</summary>

Because at-least-once asynchronous delivery can reorder or duplicate events, a position-update consumer might apply a later trade before an earlier one and corrupt the running balance. You address it by carrying a monotonic sequence or version per aggregate and having consumers reject or buffer out-of-order events, often pinning a partition key (e.g. by ISIN or account) so a given key's events stay ordered. Designing for reordering up front is part of accepting eventual consistency responsibly.

</details>

<details><summary><b>99.</b> How does an outbox/saga design support auditability and replay, which `2PC` does not naturally provide?</summary>

Every state change flows through durable event rows (the outbox/log), giving you an immutable, ordered record you can replay to rebuild state or to investigate a discrepancy — invaluable in a regulated fund context for proving how a NAV or position figure arose. `2PC` leaves only the final committed state, with the coordinator's transient log discarded after recovery, so it offers no comparable replayable history. The event trail is a side benefit that often makes the eventual-consistency design the better audit story as well.

</details>

<details><summary><b>100.</b> Tie it together: what is the one-line reason an architect steers a fund platform away from `2PC` for cross-service writes?</summary>

Because `2PC`'s single coordinator is a blocking point whose death leaves prepared participants in-doubt, holding locks on the most contended position and cash rows during trading, so the safe-but-not-available trade it makes is the wrong one for a hot path — outbox or saga keeps the books available at the cost of brief, reconcilable eventual consistency. That sentence names the mechanism, the failure, the trade, and the chosen alternative, which is exactly what the lesson asks you to be able to say.

</details>


## Phase 1 · 1.5.1–1.5.4 Storage paradigms — 100 self-test questions

<details><summary><b>1.</b> What is the fundamental difference between a row-oriented (row-store) and a column-oriented (columnar) physical layout?</summary>

A row-store keeps all the fields of one record contiguous on disk, so reading a whole row is one sequential fetch; a columnar store keeps all the values of one column contiguous, so reading one attribute across many rows is sequential. The layout decides what is cheap: row-stores are cheap for whole-record reads and writes, columnar stores are cheap for scanning a few columns across millions of rows.

</details>

<details><summary><b>2.</b> Why do analytical scans (OLAP) "love columns"?</summary>

Analytical queries typically touch a handful of columns out of many but read most of the rows, e.g. `SUM(amount) GROUP BY isin` over a trades table. A columnar layout lets the engine read only the bytes of the columns referenced and skip the rest entirely, so a 50-column table where you touch 2 columns reads roughly 2/50 of the data instead of all of it.

</details>

<details><summary><b>3.</b> Why do OLTP point-writes "love rows"?</summary>

Transactional workloads insert, update, and read whole records by key — "give me order 12345 and all its fields." A row-store places those fields together, so the operation is one contiguous read or write; a columnar store would have to touch every column file to assemble or modify a single row, turning one logical write into many scattered I/Os.

</details>

<details><summary><b>4.</b> In the `Do` step you store a 10M-row trades table as both CSV and Parquet and run the same aggregate in DuckDB. Why is the Parquet run usually much faster?</summary>

Parquet is columnar and compressed, so `SUM(amount) GROUP BY isin` reads only the `amount` and `isin` columns in compressed form, skipping every other column; CSV is row-oriented text, so DuckDB must read and parse every byte of every row including columns you never use. The gap comes from less data read off disk plus no text parsing, not from any single "Parquet is faster" rule.

</details>

<details><summary><b>5.</b> The lesson insists you explain the CSV-vs-Parquet timing gap "not as Parquet is faster but why." What three factors must your explanation name?</summary>

Layout, compression, and I/O. Columnar layout means only the referenced columns are read; compression means those columns occupy far fewer bytes; together they cut the bytes scanned off disk, and CSV additionally pays a text-parsing cost per row. Your write-up should cite your measured timings and bytes-scanned numbers, not just assert the result.

</details>

<details><summary><b>6.</b> What is "bytes scanned" and why does the lesson ask you to record it alongside timings?</summary>

Bytes scanned is the volume of data the engine actually reads from storage to answer a query, distinct from the file's total size. Recording it proves the mechanism: if Parquet scans far fewer bytes than CSV for the same aggregate, you have evidence that columnar projection and compression — not chance or caching — caused the speedup.

</details>

<details><summary><b>7.</b> Why does columnar data compress so much better than row-oriented data?</summary>

A column holds values of a single type and domain — all ISINs, all amounts, all dates — so adjacent values are highly similar and predictable, which compression and encoding exploit. A row mixes types and domains field by field (a string, then a number, then a date), so there is far less local redundancy for a compressor to remove.

</details>

<details><summary><b>8.</b> Name three encodings Parquet uses to compress columnar data before general-purpose compression is even applied.</summary>

Dictionary encoding (replace repeated values with small integer codes into a per-column-chunk dictionary), run-length encoding / bit-packing hybrid (store a run of identical values as value-plus-count, and pack small integers tightly), and delta encoding (store the difference between consecutive values). These exploit the within-column similarity that a row layout cannot, and Parquet applies dictionary encoding aggressively by default.

</details>

<details><summary><b>9.</b> How does dictionary encoding work in Parquet, and which columns benefit most?</summary>

Dictionary encoding builds a dictionary of the distinct values in a column chunk, stored in a dictionary page, and the data pages store small bit-packed integer indices into that dictionary instead of the raw values. Low-to-medium cardinality columns benefit most — a `currency` column of `EUR`/`USD`/`GBP` or an `isin` column with a few thousand distinct values shrinks dramatically because each value is stored once and referenced by a tiny code.

</details>

<details><summary><b>10.</b> What is run-length encoding (RLE), and why is it effective on a sorted or clustered column?</summary>

RLE stores a run of identical consecutive values as the value plus a repeat count, so `EUR, EUR, EUR, EUR` becomes `EUR × 4`. It is highly effective when equal values cluster together — for example a trades file sorted by `currency` or `fund_id` — because long runs collapse to a single value-and-count pair. Parquet uses an RLE/bit-packing hybrid that switches between long runs and bit-packed sequences of varied values.

</details>

<details><summary><b>11.</b> What is delta encoding and when does it shine?</summary>

Delta encoding stores the first value, then only the difference from each previous value, so a monotonically increasing sequence like a timestamp or auto-increment id stores tiny deltas instead of full values. It shines on sorted integer or date columns where consecutive differences are small or constant — an arithmetic sequence can compress to near-constant space.

</details>

<details><summary><b>12.</b> What is "late materialization" in a columnar engine?</summary>

Late materialization means the engine defers reconstructing full rows for as long as possible, operating on individual compressed columns and positional row-ids through filters and aggregations, and only stitching the surviving columns back into rows at the very end. This keeps data compressed and column-local during the heavy work, avoiding the cost of building rows that a filter will immediately discard.

</details>

<details><summary><b>13.</b> Why is late materialization a performance win rather than just an implementation detail?</summary>

Reconstructing rows early forces the engine to read and decode every column for every candidate row, including rows a `WHERE` clause will reject and columns no aggregate needs. By staying columnar — evaluating predicates on a single compressed column, carrying only matching positions forward — the engine touches far less data and can run vectorized operations on tight, type-homogeneous arrays.

</details>

<details><summary><b>14.</b> Contrast "early materialization" with "late materialization."</summary>

Early materialization reconstructs whole rows up front, then runs operators over rows — simpler but it pays to assemble rows that may be filtered out. Late materialization keeps columns separate and applies filters and projections on columns first, materializing rows only for the final result set, so it does less wasted work; column-stores favour late materialization for exactly this reason.

</details>

<details><summary><b>15.</b> What is projection pushdown, and how does DuckDB use it on a Parquet file?</summary>

Projection pushdown means pushing the column selection down into the scan so only the columns a query references are read. DuckDB does this automatically on Parquet: for `SELECT SUM(amount) ... GROUP BY isin`, only the `amount` and `isin` column chunks are read and decoded, and every other column is skipped entirely with no decode and no CPU spent.

</details>

<details><summary><b>16.</b> What is predicate (filter) pushdown, and what Parquet feature makes it possible?</summary>

Predicate pushdown pushes `WHERE` conditions down into the file reader so it can skip data that cannot match. Parquet stores per-row-group (and per-page) min/max statistics — "zonemaps" — so DuckDB can skip an entire row group whose `trade_date` max is below your lower bound or min is above your upper bound, reading only the row groups that might contain matching rows.

</details>

<details><summary><b>17.</b> Describe the internal hierarchy of a Parquet file from the top down.</summary>

A Parquet file is divided into row groups (a horizontal slice of rows); within each row group, data is stored column-by-column as column chunks; each column chunk is split into pages, the minimum read unit. Each row group also carries per-column statistics (min, max, null count) that enable skipping, and dictionary pages support dictionary encoding.

</details>

<details><summary><b>18.</b> What is a Parquet "row group" and why does its size matter?</summary>

A row group is a horizontal partition of the table holding a subset of rows, stored columnar internally, and it is the unit at which min/max statistics enable skipping. Size is a trade-off: large row groups give better compression and fewer metadata reads but coarser skipping (a single non-matching value drags the whole group's min/max range); small row groups skip more precisely but add metadata overhead.

</details>

<details><summary><b>19.</b> What is a Parquet "page" and how does it relate to compression?</summary>

A page is the smallest unit Parquet reads and decodes, typically around 1 MB by default, sitting inside a column chunk. Encoding and compression are applied at the page level, and page-level statistics can let a reader skip pages within a row group, giving even finer-grained filter pushdown than row-group skipping alone.

</details>

<details><summary><b>20.</b> A colleague says "CSV is fine, it's just a few extra megabytes." For a 10M-row trades table scanned daily, what is your counterargument grounded in this lesson?</summary>

CSV forces a full read and text parse of every byte of every column on every query, while Parquet reads only the referenced compressed columns and skips non-matching row groups. The cost is not the file size at rest but the repeated scan cost: a daily `GROUP BY isin` aggregate over CSV re-parses tens of millions of rows you never needed, where Parquet reads a small fraction of the bytes.

</details>

<details><summary><b>21.</b> Why can text CSV never match Parquet on analytical scan speed even if you gzip the CSV?</summary>

Gzip shrinks the bytes on disk but the file is still row-oriented and untyped, so to answer a column aggregate the engine must decompress and parse the entire row stream, including every unused column, and convert text to typed values. Parquet keeps columns separate and pre-typed, so it reads only the needed columns and skips parsing the rest entirely.

</details>

<details><summary><b>22.</b> In DuckDB, how can you generate a large synthetic trades table without an external file, per the lesson's `Do` step?</summary>

Use DuckDB's range/series functions, e.g. `SELECT * FROM range(10000000)` or `generate_series`, combined with expressions to fabricate columns like `isin`, `amount`, and `trade_date`. You then write it out twice with `COPY ... TO 'trades.csv' (FORMAT CSV)` and `COPY ... TO 'trades.parquet' (FORMAT PARQUET)` to create the two files for the comparison.

</details>

<details><summary><b>23.</b> Which DuckDB command writes a query result to a Parquet file?</summary>

`COPY (SELECT ...) TO 'trades.parquet' (FORMAT PARQUET);` writes the result set as Parquet, and you can add options such as `COMPRESSION 'zstd'` or `ROW_GROUP_SIZE`. To write CSV instead you use `(FORMAT CSV, HEADER)`. DuckDB can then read either back with `read_parquet('trades.parquet')` or `read_csv_auto('trades.csv')`.

</details>

<details><summary><b>24.</b> How would you measure bytes-scanned and timing for the two files in DuckDB?</summary>

Enable timing with `.timer on` (CLI) or wrap the query and read the wall-clock time, and inspect the plan with `EXPLAIN ANALYZE` to see operators and rows processed. For bytes, compare the Parquet scan's read volume against the CSV file size read in full; the point is to show Parquet's aggregate touches far fewer bytes than CSV's full-file parse.

</details>

<details><summary><b>25.</b> What does MPP stand for, and what is the core idea?</summary>

MPP stands for massively parallel processing. The core idea is to split a table across many independent nodes, each with its own CPU, memory, and local storage, and run the same query fragment on every node in parallel over its local slice, then combine partial results. Throughput scales with node count as long as the work divides evenly.

</details>

<details><summary><b>26.</b> What is data partitioning (distribution) in an MPP system?</summary>

Partitioning decides which node stores which rows of a table, typically by hashing a chosen distribution key, by round-robin, or by replicating the table to every node. The choice determines whether a query's rows are already co-located for joins and aggregations or must be shuffled across the network, which dominates MPP performance.

</details>

<details><summary><b>27.</b> What is data skew in an MPP cluster?</summary>

Data skew is uneven distribution of rows (or work) across nodes, so some nodes hold or process far more than others. Because a parallel query finishes only when its slowest node finishes, a skewed partition turns the whole cluster's runtime into that one overloaded node's runtime, wasting the rest of the cluster's capacity.

</details>

<details><summary><b>28.</b> Explain the lesson's line that "one hot key turns a 16-node cluster into a 1-node job."</summary>

If you hash-distribute on a key with one dominant value — say `currency` where 90% of trades are `EUR` — most rows land on the single node owning the `EUR` hash bucket. That node does almost all the work while the other 15 sit idle, so a 16-way cluster effectively runs as one node, and you pay for 16 but get the speed of 1.

</details>

<details><summary><b>29.</b> You distribute a trades fact table by `currency` and queries crawl. What is the likely cause and the fix?</summary>

`currency` is low-cardinality and heavily skewed, so hash-distributing on it piles most rows on a few nodes and creates a hot partition. The fix is to choose a high-cardinality, evenly-distributed key that is also commonly joined on — for example a surrogate `trade_id` or a well-balanced `account_id` — so rows spread evenly and joins stay co-located.

</details>

<details><summary><b>30.</b> What makes a good MPP distribution key?</summary>

A good key has high cardinality and an even value frequency so rows spread uniformly, and it matches the column you most often join or group on so related rows land on the same node and avoid network shuffles. Low-cardinality or skewed columns (currency, country, boolean flags) make poor keys because they concentrate rows and work.

</details>

<details><summary><b>31.</b> In Azure Synapse dedicated SQL pools, what are the three table distribution options the lesson asks you to evaluate?</summary>

Hash, round-robin, and replicated. Hash distributes rows by hashing a chosen column and suits large fact tables joined on that column; round-robin spreads rows evenly with no key and suits staging or load tables; replicated copies the whole table to every node and suits small dimension tables so joins need no data movement.

</details>

<details><summary><b>32.</b> When is a replicated distribution the right choice in MPP, and when is it wrong?</summary>

Replicated is right for small, slowly-changing dimension tables (a few MB, like a fund or currency reference table) because every node has a local copy and joins to it need no shuffle. It is wrong for large tables: replicating a multi-gigabyte fact table wastes storage on every node and makes writes expensive, since every copy must be maintained.

</details>

<details><summary><b>33.</b> When is round-robin distribution appropriate despite causing shuffles on joins?</summary>

Round-robin is appropriate when you have no obviously good distribution key or for transient staging tables you load fast and then redistribute, because it guarantees even row spread with zero skew. The cost is that joins on it usually require a shuffle, so it is a poor permanent choice for a frequently-joined fact table.

</details>

<details><summary><b>34.</b> What is a "shuffle" (data movement) in MPP, and why is it expensive?</summary>

A shuffle redistributes rows across nodes over the network so that rows needing to be joined or grouped end up co-located. It is expensive because network bandwidth is far slower than local memory/disk and the operation is all-to-all, so a query that shuffles a large fact table can spend most of its time moving data rather than computing.

</details>

<details><summary><b>35.</b> How does choosing the join key as the distribution key avoid shuffles?</summary>

If both tables are hash-distributed on the same join column, matching rows are guaranteed to live on the same node, so each node joins its local slices with no network movement — a co-located join. Distribute the trades fact and the holdings table both on `account_id`, and an `account_id` join runs locally on every node in parallel.

</details>

<details><summary><b>36.</b> What is "shared-nothing" architecture?</summary>

Shared-nothing means each node owns its own CPU, memory, and storage, and nodes communicate only by passing messages over the network. No node depends on another's disk, so the design scales out by adding independent nodes, and a single node's failure is isolated to the data it owned rather than affecting the whole system's storage.

</details>

<details><summary><b>37.</b> What is "shared-disk" architecture?</summary>

Shared-disk means all compute nodes read and write a single common storage layer accessible to every node, while each node has its own CPU and memory. Any node can serve any data because storage is central, which simplifies data management, but the shared storage and its concurrency control can become a contention bottleneck and a global dependency.

</details>

<details><summary><b>38.</b> In shared-nothing, which failures stay isolated and which become global?</summary>

A single node's failure isolates to the partition that node owned — only those rows are unavailable until recovery or replication promotes a copy. Failures become global only when they hit shared coordination (the cluster controller/metadata) or when the lost partition has no replica, since the rest of the cluster keeps serving its own local data.

</details>

<details><summary><b>39.</b> In shared-disk, which component is the global dependency, and why does that matter for failure behaviour?</summary>

The shared storage layer is the global dependency: because every node reads and writes it, storage unavailability or contention degrades every node at once, not just one. That centralizes both the failure domain and the scaling bottleneck, which is why classic shared-disk systems lean on caching and careful concurrency control to keep the shared layer from becoming the limiter.

</details>

<details><summary><b>40.</b> Which scaling problem is shared-nothing good at, and which one is it bad at?</summary>

Shared-nothing is good at scaling read/compute throughput linearly by adding independent nodes, since each works on its own local slice with no contention. It is bad at workloads with heavy data movement or skew, and at rebalancing — adding or removing nodes forces repartitioning, and an unevenly distributed key undermines the parallelism the design depends on.

</details>

<details><summary><b>41.</b> How does Snowflake describe its own architecture relative to shared-disk and shared-nothing?</summary>

Snowflake describes itself as "a hybrid of traditional shared-disk and shared-nothing database architectures." Like shared-disk it uses a central data repository accessible from all compute nodes; like shared-nothing it processes queries with MPP clusters where each node caches a portion of the data locally, aiming for shared-disk's management simplicity with shared-nothing's scale-out performance.

</details>

<details><summary><b>42.</b> What are the three layers in Snowflake's architecture?</summary>

Database Storage, Compute (Query Processing), and Cloud Services. Database Storage holds the data as compressed, columnar micro-partitions in cloud object storage; Compute is the virtual warehouses that run queries; Cloud Services coordinates security, metadata, query optimization, and transaction management across the platform.

</details>

<details><summary><b>43.</b> What is a Snowflake "virtual warehouse"?</summary>

A virtual warehouse is a cluster of compute resources — CPU, memory, and local cache — that executes SQL statements. Each warehouse runs independently and does not share compute with others, so you can size and scale warehouses separately and spin them up or down on demand without affecting the stored data or other warehouses' workloads.

</details>

<details><summary><b>44.</b> What is a Snowflake "micro-partition"?</summary>

A micro-partition is a contiguous unit of storage, typically tens of megabytes uncompressed, into which Snowflake automatically divides all table data, stored columnar and compressed. Snowflake keeps min/max and other metadata per micro-partition so it can prune (skip) partitions that cannot match a query's filter, analogous to Parquet row-group skipping via zonemaps.

</details>

<details><summary><b>45.</b> What does "separation of storage and compute" mean?</summary>

It means the persistent data lives in one independently-scaled storage layer (cloud object storage) while query execution runs on separate, independently-scaled compute clusters. Either layer can grow or shrink without the other: you add compute for more concurrency or speed without copying data, and you grow storage without provisioning idle compute.

</details>

<details><summary><b>46.</b> Name two cost/elasticity consequences that follow from separating storage and compute.</summary>

First, you can scale compute up for a heavy month-end NAV run and back down afterwards, paying for compute only while it runs while storage cost stays flat. Second, multiple compute clusters can read the same data concurrently without copying it, so you can isolate workloads (loading, reporting, ad-hoc) on separate warehouses sized and billed independently.

</details>

<details><summary><b>47.</b> In a storage/compute-separated system, what happens to your data when you suspend all compute?</summary>

The data remains fully persisted and intact in the storage layer, and you stop paying for compute entirely while continuing to pay only the (much cheaper) storage cost. When you resume a warehouse, it reattaches to the same data with no reload, which is why suspend/resume is a core cost lever in Snowflake- and BigQuery-style systems.

</details>

<details><summary><b>48.</b> How does BigQuery exemplify storage/compute separation differently from Snowflake?</summary>

BigQuery stores data in a managed columnar format in Google's storage and executes queries on a serverless, on-demand pool of compute (slots) that you do not provision as named clusters. Snowflake exposes compute as explicit virtual warehouses you size and suspend; BigQuery abstracts compute further into automatically-allocated slots, but both decouple persistent storage from the engines that scan it.

</details>

<details><summary><b>49.</b> Sketch the Snowflake-style three-layer architecture in words and say which failure behaviour follows from each separation.</summary>

Cloud Services on top coordinates metadata and optimization; multiple independent Compute warehouses in the middle scan data; one central Storage layer at the bottom holds the data. A single warehouse failing affects only its own queries (compute is isolated), storage stays globally available to all warehouses, and only a Cloud Services / metadata outage is truly global because it coordinates everything.

</details>

<details><summary><b>50.</b> Which cost behaviour follows from compute being separate, multiple, and independently sized?</summary>

You pay per warehouse for the time it runs at the size you chose, so a small warehouse for light reporting and a large one for a heavy load can run concurrently and be billed independently. Idle warehouses can auto-suspend to stop accruing cost, turning compute spend into a per-workload, on-demand line item rather than a fixed cluster cost.

</details>

<details><summary><b>51.</b> Which cost behaviour follows from storage being central and shared?</summary>

Storage is billed once for the single copy regardless of how many warehouses read it, so adding compute for more concurrency does not multiply storage cost, and isolating workloads onto separate warehouses does not require duplicating data. You pay storage for the data you keep, and compute separately for the work you run against it.

</details>

<details><summary><b>52.</b> Describe one workload where shared-nothing MPP beats storage/compute separation.</summary>

A steady, predictable, scan-heavy workload that fully and continuously utilizes a fixed cluster — for example a large enterprise reporting mart hit hard all day with co-located joins on a well-chosen distribution key. Here local-disk MPP has no object-store latency and no per-query compute spin-up, so a tuned, always-on shared-nothing cluster maximizes throughput per dollar.

</details>

<details><summary><b>53.</b> Describe one workload where storage/compute separation beats shared-nothing MPP.</summary>

A spiky, multi-tenant workload — quiet most of the day, then a heavy month-end NAV and regulatory run — with several teams needing isolated, independently-sized compute over the same data. Separation lets you scale compute up only for the spike and isolate workloads on separate warehouses without copying data, where a fixed shared-nothing cluster would be over-provisioned off-peak and contended at peak.

</details>

<details><summary><b>54.</b> Why does a fixed shared-nothing cluster waste money on a spiky workload?</summary>

You must provision the cluster for the peak, so off-peak the nodes sit mostly idle but still cost money, and you cannot cheaply shrink because rebalancing data across fewer nodes is disruptive. Storage/compute separation avoids this by letting compute scale to zero between spikes while the data stays put, matching spend to actual usage.

</details>

<details><summary><b>55.</b> Why might storage/compute separation lose to shared-nothing on a saturating, always-on workload?</summary>

When a cluster is fully utilized around the clock, the elasticity of separation provides no savings (you never scale down) while you pay the architectural overheads of fetching from remote object storage and re-warming caches. A purpose-built shared-nothing cluster keeps data on local disk and avoids per-query compute startup, so it can deliver more sustained throughput per dollar.

</details>

<details><summary><b>56.</b> How does columnar storage interact with vectorized execution?</summary>

Columnar layout hands the engine tight, type-homogeneous arrays of one column's values, which a vectorized engine processes in batches with CPU SIMD instructions and good cache locality, applying one operation across many values at once. Row layout interleaves types, defeating SIMD and wasting cache lines on unneeded fields, so columnar and vectorization reinforce each other.

</details>

<details><summary><b>57.</b> Why does DuckDB choose a columnar, vectorized design for analytics?</summary>

Analytical queries scan many rows over few columns and benefit from reading only those columns, compressing them well, and processing them in vectorized batches — exactly what a columnar engine delivers. DuckDB is built for in-process OLAP, so a columnar vectorized model gives it cache-efficient, SIMD-friendly scans and native, fast Parquet reading with projection and filter pushdown.

</details>

<details><summary><b>58.</b> For a write-heavy OLTP system recording individual fund subscription orders as they arrive, would you choose a row-store or a columnar store, and why?</summary>

A row-store. Each order is inserted and later read or updated as a whole record by key, which a row-store does in one contiguous I/O, whereas a columnar store would scatter a single insert across every column and pay extra to assemble a row on read. Save the columnar format for the downstream analytical copy.

</details>

<details><summary><b>59.</b> For a reporting mart aggregating daily NAV and holdings across thousands of funds, would you choose row or columnar, and why?</summary>

Columnar. The reports scan huge numbers of rows but reference only a few columns (date, fund, NAV, AUM), so columnar projection reads just those columns, compression shrinks the bytes, and late materialization avoids reconstructing unneeded rows. This is textbook analytical territory where a row-store would needlessly read every column of every row.

</details>

<details><summary><b>60.</b> Why is storing tick-level or trade-level fund data as Parquet partitioned by date especially effective for time-range queries?</summary>

Partitioning by date lets the engine prune whole files (partitions) outside the query's date range before any scan, and within each file Parquet's row-group min/max statistics prune further. A "last quarter's EUR trades" query then reads only the relevant date partitions and, inside them, only the `currency` and `amount` columns — a tiny fraction of the data.

</details>

<details><summary><b>61.</b> A `WHERE trade_date BETWEEN ...` query on a Parquet file still reads the whole file. What would you check first?</summary>

Check whether the data is ordered/clustered by `trade_date` so that row-group min/max ranges are tight and non-overlapping; if rows are randomly ordered, every row group's date range spans the whole period and none can be skipped. Sorting by the filter column before writing Parquet makes zonemap pruning effective.

</details>

<details><summary><b>62.</b> Your DuckDB Parquet query is slow because it reads many columns you do not need. What is the fix, and why does it work?</summary>

Select only the columns you need instead of `SELECT *`, so projection pushdown reads just those column chunks and skips the rest. It works because Parquet stores columns separately; naming two columns means DuckDB decodes two column chunks instead of every column in every row group, cutting bytes read and CPU spent decoding.

</details>

<details><summary><b>63.</b> Why can a columnar engine apply a `WHERE` filter without reading the columns in the `SELECT` list first?</summary>

Because columns are independent, the engine can read just the predicate column, evaluate the filter to get the set of matching row positions, and only then read the selected columns at those positions. This is late materialization: it avoids touching projected columns for rows that fail the filter, reading far less data than a row-store that must assemble whole rows.

</details>

<details><summary><b>64.</b> What is the trade-off of very aggressive compression (e.g. high-level zstd) on a Parquet file?</summary>

Higher compression shrinks storage and reduces bytes read off disk, but it costs more CPU to compress on write and to decompress on read. If your bottleneck is I/O (cloud object storage, network), heavier compression usually wins; if your scans are CPU-bound and storage is cheap local disk, a lighter codec can be faster overall.

</details>

<details><summary><b>65.</b> Why is "compression ratio" not the only thing that matters when choosing a Parquet codec?</summary>

Decompression speed and CPU cost matter just as much for query latency: a codec that compresses 10% tighter but decompresses half as fast can make scans slower if you are CPU-bound. The right choice balances storage savings, I/O reduction, and decode speed for your hardware and access pattern, which is why `snappy` and `zstd` are common defaults over maximum-ratio options.

</details>

<details><summary><b>66.</b> How do Parquet's per-row-group statistics resemble Snowflake's micro-partition metadata?</summary>

Both store min/max (and other) statistics per storage chunk so the engine can prune chunks that cannot satisfy a filter without reading them. Parquet keeps min/max per row group (and page); Snowflake keeps metadata per micro-partition and prunes them at query time. The shared idea is metadata-driven skipping — read only the chunks whose value ranges overlap the predicate.

</details>

<details><summary><b>67.</b> What does it mean that Snowflake "prunes" micro-partitions, and what makes pruning effective?</summary>

Pruning means Snowflake uses each micro-partition's min/max metadata to skip partitions whose value ranges cannot match the query's filters, scanning only the rest. Pruning is effective when data is naturally clustered on the filtered column so partition ranges are tight and non-overlapping; if values are scattered, ranges overlap and few partitions can be skipped.

</details>

<details><summary><b>68.</b> Why does data clustering/ordering matter so much for skipping in both Parquet and Snowflake?</summary>

Skipping relies on min/max ranges per chunk; if a column's values are sorted, each chunk covers a narrow, distinct range and a filter eliminates most chunks. If values are randomly ordered, every chunk's range spans nearly the whole domain, the ranges all overlap the predicate, and the engine cannot skip anything — so clustering is what converts statistics into actual I/O savings.

</details>

<details><summary><b>69.</b> Why would loading data sorted by `isin` or `trade_date` before writing Parquet speed up later filtered queries?</summary>

Sorting clusters equal or near values into the same row groups, so each row group's min/max range for that column is tight, and filter pushdown can skip the row groups outside the predicate range. It also improves compression (longer RLE runs, better dictionary locality), so the file is both smaller and more skippable.

</details>

<details><summary><b>70.</b> What is the difference between OLTP and OLAP, framed in terms of storage layout?</summary>

OLTP (online transaction processing) handles many small reads/writes of whole records by key and favours row-stores that keep a record's fields together. OLAP (online analytical processing) scans many rows over few columns to aggregate and favours columnar stores that read only the needed columns and compress them well. The layout follows the access pattern.

</details>

<details><summary><b>71.</b> Why do many fund platforms keep an OLTP row-store and a separate OLAP columnar store rather than one system?</summary>

The two workloads want opposite layouts: order capture and account updates are point-writes that love rows, while NAV/holdings reporting is scan-heavy aggregation that loves columns. Running both on one row-store makes reports crawl; on one columnar store makes writes expensive. Splitting them — transactional Postgres plus a columnar warehouse fed by ETL — gives each workload its ideal physical model.

</details>

<details><summary><b>72.</b> How does separation of storage and compute enable "zero-copy" workload isolation?</summary>

Because data lives in one central storage layer, several independent compute warehouses can read the same data simultaneously without each needing its own copy. You can give the load process, the reporting team, and ad-hoc analysts separate warehouses sized for their needs, all over one dataset, so heavy reporting never starves the load and no data duplication is required.

</details>

<details><summary><b>73.</b> What is the risk of running every workload on a single shared virtual warehouse?</summary>

A single warehouse serializes or contends across all workloads, so a heavy month-end reporting job can slow down concurrent data loads and interactive queries, and you cannot size compute to each workload independently. Workload isolation — one warehouse per concern — is precisely the benefit storage/compute separation makes cheap, since all warehouses share the same data.

</details>

<details><summary><b>74.</b> Why is "auto-suspend" of an idle warehouse a direct consequence of separating storage from compute?</summary>

Because the data persists independently in storage, the compute cluster holds no permanent state and can be shut down without losing data, then resumed later attached to the same data. In a shared-nothing system where each node holds part of the data on local disk, you cannot simply shut compute off without losing access to that data, so auto-suspend is not freely available.

</details>

<details><summary><b>75.</b> What is the "cache re-warming" cost when a suspended warehouse resumes?</summary>

A virtual warehouse keeps a local cache of recently scanned data on its compute nodes; suspending it discards that cache, so after resume the first queries must re-fetch data from the remote storage layer and rebuild the cache, running slower until it warms. This is an explicit cost of the separation model traded against the savings of suspending idle compute.

</details>

<details><summary><b>76.</b> How does the shared-disk side of Snowflake's hybrid simplify data management compared with pure shared-nothing?</summary>

With one central data repository, you do not have to manually partition, distribute, and rebalance data across nodes, and any compute node can access any data. Pure shared-nothing requires choosing distribution keys and repartitioning when you scale, which is operationally heavy; the shared-disk central store removes that burden while MPP local caching restores the performance.

</details>

<details><summary><b>77.</b> How does the shared-nothing side of Snowflake's hybrid restore performance that pure shared-disk lacks?</summary>

Each MPP node in a warehouse caches a portion of the working set on local SSD and processes its slice in parallel, so most reads hit fast local cache instead of contending on the central store. This gives the scale-out, parallel performance of shared-nothing while the central repository underneath still provides the single-source simplicity of shared-disk.

</details>

<details><summary><b>78.</b> Why does an architect need to "derive cost and failure behavior from these decisions" rather than read vendor slides?</summary>

Because the storage paradigm dictates the consequences: whether a failure is local or global, whether scaling costs are fixed or elastic, whether a hot key cripples the cluster. An architect who can reason from row-vs-columnar, shared-nothing-vs-shared-disk, and storage/compute separation can audit a vendor's claims and predict behaviour under load, instead of trusting the marketing.

</details>

<details><summary><b>79.</b> A vendor claims "infinite elastic scaling." Which storage-paradigm questions let you audit that claim?</summary>

Ask whether storage and compute are truly separate (so compute scales without moving data), how data is distributed (so skew does not cap parallelism), and what the failure domains are (which outages are local vs global). The answers reveal whether scaling is genuinely elastic and isolated or whether a central bottleneck, a rebalancing cost, or a skewed key limits it.

</details>

<details><summary><b>80.</b> Why is "Parquet vs CSV" really a stand-in for the broader row-vs-columnar lesson?</summary>

CSV is the canonical row-oriented, untyped, uncompressed text format and Parquet is the canonical columnar, typed, compressed, statistics-bearing format, so comparing them on an aggregate isolates exactly the columnar advantages — projection, compression, skipping, late materialization. The measured gap teaches the general principle that physical layout, not the engine alone, drives analytical scan cost.

</details>

<details><summary><b>81.</b> What does "I/O-bound" mean for an analytical scan, and how does columnar storage help?</summary>

An I/O-bound scan spends most of its time reading bytes from storage rather than computing, so reducing bytes read directly reduces runtime. Columnar storage helps by reading only the referenced columns (projection), storing them compressed (fewer bytes), and skipping non-matching chunks (statistics) — three ways to cut the bytes the scan must fetch.

</details>

<details><summary><b>82.</b> How can columnar processing turn an I/O-bound scan into a CPU-bound one, and why is that progress?</summary>

By cutting bytes read so aggressively that decoding and computing on the compressed columns becomes the new bottleneck. That is progress because the scan is now limited by fast CPU/SIMD work on tight column arrays rather than by slow disk or network reads, which is exactly where vectorized columnar engines are designed to excel.

</details>

<details><summary><b>83.</b> Why is a wide table (hundreds of columns) far less painful in a columnar store than in a row-store for analytics?</summary>

In a columnar store, query cost scales with the columns you reference, not the table's total width, so a 300-column table queried for 3 columns reads roughly 3 columns' worth of data. In a row-store, every scan reads full rows including all 300 columns, so wide tables make every analytical query proportionally more expensive.

</details>

<details><summary><b>84.</b> Why does adding rarely-used columns to a columnar fact table cost little for existing queries?</summary>

Because those columns live in their own column chunks that projection pushdown simply skips when a query does not reference them, so existing aggregates read the same bytes as before. In a row-store the new columns would bloat every row and slow every full-row scan, but a columnar layout isolates the cost to queries that actually touch the new columns.

</details>

<details><summary><b>85.</b> In MPP, why does a `COUNT(*)` scale almost perfectly while a skewed `GROUP BY` may not?</summary>

`COUNT(*)` divides evenly — each node counts its local rows and the coordinator sums the partial counts — so work matches the even-ish row distribution. A `GROUP BY` on a skewed key sends all rows of a dominant group to one node (or one reducer), so that node does disproportionate work and the query waits on it, regardless of how many nodes exist.

</details>

<details><summary><b>86.</b> What is a co-located join versus a redistributed (shuffle) join in MPP?</summary>

A co-located join happens when both tables are distributed on the join key, so matching rows are already on the same node and each node joins locally with no network movement. A redistributed join happens when they are not aligned, so the engine must shuffle one or both tables across the network to bring matching rows together — far more expensive.

</details>

<details><summary><b>87.</b> Two large fact tables are joined frequently on `account_id` but distributed on different keys, causing constant shuffles. What is the architectural fix?</summary>

Distribute both tables on `account_id` (the common join key) so the join becomes co-located and runs locally on every node without shuffling. If they must also join on other keys, you accept a shuffle for the less frequent join and optimize for the dominant one, since you can only physically co-locate on one key per table.

</details>

<details><summary><b>88.</b> Why is repartitioning an MPP cluster (changing the distribution key) an expensive operation?</summary>

Changing the distribution key means recomputing which node every row belongs to and physically moving rows across the network to their new homes — effectively a full table shuffle and rewrite. On a large fact table this is a heavy, often offline operation, which is why getting the distribution key right up front matters so much in shared-nothing MPP.

</details>

<details><summary><b>89.</b> How does storage/compute separation make "resizing" cheaper than repartitioning a shared-nothing cluster?</summary>

With separation, resizing means attaching more or fewer compute nodes to the same untouched central storage — no data moves, so it is near-instant. In shared-nothing, adding nodes requires repartitioning data onto them (a full shuffle), so scaling is slow and disruptive; decoupling compute from data removes that data-movement cost from scaling.

</details>

<details><summary><b>90.</b> What is the relationship between a Parquet row group and an MPP partition conceptually?</summary>

Both are horizontal slices of a table used to parallelize and prune work: a Parquet row group is an intra-file slice with its own statistics for skipping, while an MPP partition is a slice assigned to a node for parallel processing. The shared theme is dividing rows into independently-processable, independently-skippable units, though one is a file-format unit and the other a distribution unit.

</details>

<details><summary><b>91.</b> For storing 10 years of daily NAV history per share class, why is a columnar, date-partitioned design natural?</summary>

NAV-history reporting scans long date ranges but few columns (date, share class, NAV), so columnar projection and compression cut the bytes, and date partitioning prunes irrelevant years before scanning. A point-lookup of one day's NAV is rare; the dominant access is range aggregation, which is exactly what a date-partitioned columnar layout serves.

</details>

<details><summary><b>92.</b> Why might `ISIN` be a poor choice as an MPP distribution key for a trades fact table even though it identifies the instrument?</summary>

Distribution skew: a few highly-traded instruments can account for a large share of rows, so hashing on `ISIN` concentrates those instruments' trades on a few nodes and creates hot partitions. A more uniformly distributed key — or a surrogate trade id — spreads rows evenly, while you keep `ISIN` indexed for filtering rather than for distribution.

</details>

<details><summary><b>93.</b> How does dictionary encoding interact with a low-cardinality `currency` column in a fund trades table?</summary>

A `currency` column has very few distinct values (`EUR`, `USD`, `GBP`, ...), so dictionary encoding stores each once and represents the column as tiny integer codes, often then run-length-encoded if values cluster. The column shrinks to a fraction of its raw size, and predicate evaluation on it can work on the compact codes rather than full strings.

</details>

<details><summary><b>94.</b> Why does a columnar store make `SELECT AVG(nav) FROM nav_history WHERE share_class = 'X'` cheap?</summary>

It reads only the `share_class` column to find matching rows (or prune row groups via statistics) and only the `nav` column to average, skipping every other column entirely. Compression further reduces those two columns' bytes, and late materialization means no full rows are reconstructed — so the query touches a small slice of the table's total data.

</details>

<details><summary><b>95.</b> What is the danger of treating "Parquet is faster" as a rule rather than understanding the mechanism?</summary>

For a whole-row point lookup or a single-row insert, Parquet/columnar is often slower than a row-store, so the rule fails outside analytical scans. Understanding the mechanism — projection, compression, skipping, late materialization help column scans but not row point-access — lets you predict when columnar wins and when it loses, which is the architect's job.

</details>

<details><summary><b>96.</b> Why can compression in a columnar store sometimes speed up queries, not just save disk?</summary>

Because if the scan is I/O-bound, fewer bytes to read from disk or network means a faster scan, and many engines operate directly on compressed/encoded columns (e.g. comparing dictionary codes) without fully decompressing. So compression cuts both storage cost and the I/O that often dominates analytical query time.

</details>

<details><summary><b>97.</b> What does "shared-nothing scales linearly until skew or coordination dominates" mean in practice?</summary>

Up to a point, adding nodes proportionally increases throughput because work divides evenly and stays local. Past that point either data skew loads one node disproportionately (so adding nodes does not help the bottleneck) or cross-node coordination and shuffles grow faster than the added capacity, so the speedup curve flattens — the cluster stops scaling linearly.

</details>

<details><summary><b>98.</b> A 16-node MPP query runs no faster than on 4 nodes. List the first two things to check.</summary>

First, data skew on the distribution key — if one value dominates, most work piles on one node regardless of cluster size, so check per-node row counts and runtime. Second, shuffles — if the query redistributes large tables because the join/group keys do not match the distribution, network movement caps throughput; check the plan for redistribute/broadcast operators.

</details>

<details><summary><b>99.</b> Why does the architect's lens favour understanding paradigms over memorizing a specific vendor's product?</summary>

Vendors package the same few primitives — row vs columnar, shared-nothing vs shared-disk, storage/compute coupling — differently and rename them in marketing. An architect who reasons from the primitives can map any new product onto known cost and failure behaviour, evaluate it under fund-platform load, and avoid being steered by slides, which is the durable skill the lesson builds.

</details>

<details><summary><b>100.</b> Summarize the through-line connecting all four storage-paradigm topics in this lesson.</summary>

Physical storage decisions — row vs columnar layout, how data is compressed and materialized, how it is partitioned across nodes, and whether storage and compute are coupled — together determine an analytical system's speed, cost, and failure behaviour. The CSV-vs-Parquet experiment proves the layout/compression/I/O mechanism hands-on, and the Snowflake three-layer sketch ties partitioning and separation to the cost and failure consequences an architect must be able to derive and defend.

</details>


## Phase 1 · 3.2.1 Relational internals (the database under everything) — 100 self-test questions

<details><summary><b>1.</b> What is a "page" (block) in PostgreSQL and what is its default size?</summary>

A page is the fixed-size unit of storage PostgreSQL reads and writes between disk and memory; the default is 8 KB (`BLCKSZ`, set at compile time). The whole engine — heap, indexes, the buffer pool, and the WAL — is organized in these units, so I/O accounting in tools like `EXPLAIN (ANALYZE, BUFFERS)` is reported in page counts. A single row is never split across pages in the normal case; oversized values go to TOAST instead.

</details>

<details><summary><b>2.</b> What is a heap file in a relational engine?</summary>

A heap file is the unordered collection of pages that physically stores a table's rows (tuples), with no inherent sort order — new rows go wherever there is free space. "Heap" here means "pile", not the data-structure heap; row location is tracked by a tuple identifier (`ctid`) of the form (page number, item offset). Because heaps are unordered, range and equality lookups need an index or a sequential scan that reads every page.

</details>

<details><summary><b>3.</b> What is the buffer pool (shared buffers) and what does it cache?</summary>

The buffer pool is PostgreSQL's own in-process cache of recently used 8 KB pages, sized by the `shared_buffers` setting (commonly ~25% of RAM as a starting point). It holds heap and index pages so repeated access avoids disk I/O, and it is where dirty pages live before a checkpoint flushes them. Every read goes through the pool: a backend asks for a page, and the pool either returns a cached copy (a hit) or fetches it from the OS/disk (a read).

</details>

<details><summary><b>4.</b> Why does PostgreSQL manage its own buffer pool instead of just relying on the OS page cache?</summary>

The database knows access patterns and correctness requirements the OS cannot see — which pages are dirty, the ordering required for crash recovery (WAL-before-data), and which pages a long scan should not let evict the working set. By managing its own cache it can pin pages during use, enforce write ordering for durability, and apply DB-aware eviction; it still benefits from the OS cache as a second layer (hence "double buffering"). This is why `shared_buffers` is tuned but not set to all of RAM — the OS cache backstops it.

</details>

<details><summary><b>5.</b> PostgreSQL uses a clock-sweep (not strict LRU) algorithm for buffer replacement — what problem does that design avoid?</summary>

Clock-sweep is an approximate-LRU that uses a per-buffer usage counter swept in a circle, avoiding the contention and bookkeeping cost of maintaining a true global LRU list under heavy concurrency. A strict LRU would need a hot, globally locked list updated on every access; clock-sweep just decrements counters and evicts the first zero it finds. It also resists a single large sequential scan flushing the whole cache, because such pages get a low usage count.

</details>

<details><summary><b>6.</b> What does "buffer hit ratio" tell you, and why is a high ratio not always good news?</summary>

It is the fraction of buffer requests served from `shared_buffers` without a disk/OS read (hits ÷ (hits + reads)); a high ratio usually means the working set fits in cache. But a 99% hit ratio can hide a query that reads millions of buffers unnecessarily — you are efficiently re-reading pages you should never have touched. Always read absolute buffer counts in `EXPLAIN (ANALYZE, BUFFERS)`, not just the ratio.

</details>

<details><summary><b>7.</b> What is a B+tree and why is it PostgreSQL's default index type?</summary>

A B+tree is a balanced, multi-way search tree where all keys live in leaf nodes linked in sorted order, giving logarithmic lookups and efficient ordered range scans. It is the default because it answers the most common predicate shapes — equality (`=`), ranges (`<`, `<=`, `>`, `>=`, `BETWEEN`), `IN`, sorting, and prefix `LIKE 'abc%'` — and supports multicolumn keys. Its self-balancing keeps height shallow even for billions of rows, so a point lookup is a handful of page reads.

</details>

<details><summary><b>8.</b> A query filters `WHERE settlement_date BETWEEN '2026-01-01' AND '2026-03-31'` on a 200M-row trades table — which index types are candidates and how do you choose?</summary>

A B+tree on `settlement_date` handles the range directly and works regardless of physical order, but on a huge table a BRIN index is far smaller and can win if rows are physically clustered by date (e.g. appended chronologically). The choice hinges on correlation: if `pg_stats.correlation` for the column is near 1.0, BRIN's block-range min/max pruning is effective; if rows are scattered, BRIN reads too many blocks and B+tree is better. Check `EXPLAIN (ANALYZE, BUFFERS)` for buffers read with each.

</details>

<details><summary><b>9.</b> When would you reach for a hash index in PostgreSQL, and what is its key limitation?</summary>

A hash index supports only equality (`=`) lookups and can be marginally faster and smaller than a B+tree for that single case, e.g. exact-match lookups on a long opaque token. Its limitation is that it cannot serve range queries, sorting, or multicolumn keys, so a B+tree (which also handles `=`) is usually preferred for flexibility. Hash indexes became crash-safe and WAL-logged only in PostgreSQL 10, which is why they were long avoided.

</details>

<details><summary><b>10.</b> What predicate shapes does a GIN index serve, and give a fund-data example?</summary>

GIN (Generalized Inverted Index) indexes composite/multi-value columns — arrays, `jsonb`, and full-text `tsvector` — answering containment and overlap operators like `@>`, `<@`, `&&`, and `@@`. For example, a `securities` table storing a `tags text[]` or a `jsonb` attributes blob could use GIN so `WHERE attributes @> '{"asset_class":"equity"}'` or `WHERE tags && ARRAY['UCITS','ESG']` is indexed. GIN builds an inverted map from each element to the rows containing it, so it shines when one column holds many searchable elements.

</details>

<details><summary><b>11.</b> What is a BRIN index and on what kind of column does it pay off?</summary>

BRIN (Block Range INdex) stores only the min/max (summary) of an indexed column per range of consecutive heap blocks, making it tiny — often kilobytes for a table that a B+tree would index in gigabytes. It pays off on very large tables whose physical row order correlates with the column, classically an append-only timestamp like NAV-history `as_of_date`. A range query scans the small BRIN, skips block ranges whose min/max cannot match, and only reads the surviving blocks.

</details>

<details><summary><b>12.</b> Why can a BRIN index on `nav_date` become nearly useless after heavy random updates and inserts?</summary>

BRIN relies on physical/value correlation: each block range's stored min/max is only selective if rows in those blocks really are clustered by `nav_date`. Random inserts and updates (which place new tuples wherever there is free space) scatter dates across blocks, widening every range's min/max until almost no range can be pruned. Re-establishing correlation needs a `CLUSTER` or a rewrite, plus `brin_summarize_new_values()`/autosummarize to summarize fresh ranges.

</details>

<details><summary><b>13.</b> What is the difference between a sequential scan and an index scan in a plan?</summary>

A sequential scan (`Seq Scan`) reads every page of the heap and filters rows in memory; an index scan walks an index to find matching tuple locations, then fetches those heap rows. Sequential scans win when a large fraction of the table matches (reading sequentially is cheap), while index scans win for selective predicates. The planner chooses based on estimated selectivity and cost, not on whether an index merely exists.

</details>

<details><summary><b>14.</b> What is a Bitmap Index Scan plus Bitmap Heap Scan, and when does the planner pick it?</summary>

A `Bitmap Index Scan` builds an in-memory bitmap of matching heap page locations from one or more indexes, then a `Bitmap Heap Scan` visits those pages in physical order. The planner picks it for medium-selectivity predicates where a plain index scan would jump around the heap inefficiently but a full seq scan is too much. Visiting pages in physical order turns scattered random reads into more sequential I/O, and it can also combine multiple indexes via `BitmapAnd`/`BitmapOr`.

</details>

<details><summary><b>15.</b> Name the three core join algorithms PostgreSQL can choose and the situation each fits.</summary>

Nested loop joins probe the inner side once per outer row and suit small outer inputs with an index on the inner join key. Hash joins build a hash table on the smaller input and probe it with the larger, fitting large unsorted equijoins. Merge joins exploit sorted inputs (from an index or an explicit sort) and suit large joins where both sides are already ordered, especially with range or inequality merge conditions.

</details>

<details><summary><b>16.</b> What is cardinality estimation and why is it the most consequential part of planning?</summary>

Cardinality estimation is the planner's prediction of how many rows each node will emit, derived from table statistics in `pg_statistic` (gathered by `ANALYZE`). Every cost — and therefore every join order and join algorithm choice — is downstream of these row estimates, so a wrong estimate cascades into a wrong plan. This is why a single misestimate can be catastrophic even when each individual cost formula is correct.

</details>

<details><summary><b>17.</b> How does a cardinality misestimate produce a "nested-loop disaster"?</summary>

If the planner estimates the outer side of a nested loop has, say, 5 rows but it actually has 5 million, it will run the inner lookup millions of times instead of switching to a hash join. The plan looks cheap on paper but executes the inner probe far more often than budgeted, turning seconds into hours. The tell is `EXPLAIN ANALYZE` showing a huge gap between `rows=` (estimate) and `actual rows=` on the nested loop's outer node.

</details>

<details><summary><b>18.</b> In `EXPLAIN ANALYZE`, what is the difference between the estimated `rows` and `actual rows`, and what does a large gap signal?</summary>

`rows` is the planner's pre-execution estimate; `actual rows` (with `loops`) is what the node really produced at runtime. A large multiplicative gap signals stale or insufficient statistics, correlated columns the planner treats as independent, or a predicate it cannot estimate well. Closing that gap — via `ANALYZE`, higher statistics targets, or extended statistics — is usually how you fix a bad plan rather than fighting the symptom.

</details>

<details><summary><b>19.</b> What does `ANALYZE` do and how does it differ from `VACUUM`?</summary>

`ANALYZE` samples a table and updates the planner statistics (row counts, most-common values, histograms, correlation) in `pg_statistic` so cost estimates are accurate. `VACUUM` reclaims space from dead tuples and updates the visibility/free-space maps; it does not by itself refresh planner stats unless you run `VACUUM ANALYZE`. Autovacuum runs both autovacuum and autoanalyze as separate triggers, so a table can have fresh space but stale stats or vice versa.

</details>

<details><summary><b>20.</b> What does raising a column's statistics target (`ALTER TABLE ... ALTER COLUMN ... SET STATISTICS n`) achieve?</summary>

It increases the number of most-common-value entries and histogram buckets `ANALYZE` collects for that column (default 100, up to 10000), giving finer-grained selectivity estimates. This helps skewed or high-cardinality columns where the default sample misjudges how many rows a predicate matches. The cost is slightly slower `ANALYZE` and a larger `pg_statistic`, so you raise it selectively on columns that drive bad plans.

</details>

<details><summary><b>21.</b> What problem do extended statistics (`CREATE STATISTICS`) solve?</summary>

By default the planner assumes columns are independent, so for correlated columns (e.g. `fund_id` and `share_class_currency`) it multiplies selectivities and badly underestimates combined predicates. `CREATE STATISTICS` with `dependencies`, `ndistinct`, or `mcv` records the actual correlation so the estimate for `WHERE fund_id = ? AND currency = ?` reflects reality. This is the standard fix when a multi-column filter produces a wildly low row estimate and a bad join order.

</details>

<details><summary><b>22.</b> What does MVCC stand for and what is its central idea in PostgreSQL?</summary>

MVCC is Multi-Version Concurrency Control: rather than overwriting rows in place, the engine keeps multiple versions of a row so readers and writers do not block each other. Each transaction sees a consistent snapshot determined by transaction IDs (`xmin`/`xmax`) on each tuple, so a reader never waits on a writer's lock and vice versa. The cost of this no-blocking design is that old versions accumulate and must be cleaned up later.

</details>

<details><summary><b>23.</b> How does PostgreSQL implement an `UPDATE` at the storage level under MVCC?</summary>

An `UPDATE` does not modify the existing tuple in place; it marks the old tuple's `xmax` with the updating transaction and inserts a brand-new tuple version with the new values. The old version remains visible to transactions whose snapshot predates the change, providing isolation without locking readers. The consequence is that every update creates a dead tuple once no snapshot needs the old version, which is the root cause of bloat.

</details>

<details><summary><b>24.</b> What are `xmin` and `xmax` on a tuple and how do they drive visibility?</summary>

`xmin` is the transaction ID that created the row version and `xmax` is the transaction ID that deleted/updated it (0 if still live). A tuple is visible to a transaction if its `xmin` committed and is in the snapshot, and its `xmax` is unset or belongs to an uncommitted/invisible transaction. This per-tuple bookkeeping is exactly how MVCC gives each transaction a consistent point-in-time view without read locks.

</details>

<details><summary><b>25.</b> What is table bloat and how does it hurt a NAV-history table specifically?</summary>

Bloat is the accumulation of dead tuples (and the resulting empty space) left by updates and deletes that vacuum has not yet reclaimed or that space remains allocated to the table. On a frequently corrected NAV-history table, repeated price corrections create dead versions that inflate the table and its indexes, so scans read more pages for the same live rows and queries slow down. Severe bloat can require `VACUUM FULL` or `pg_repack` to physically shrink the files.

</details>

<details><summary><b>26.</b> What does a plain `VACUUM` actually do, and what does it not do?</summary>

Plain `VACUUM` scans the table, removes dead tuples that are no longer visible to any snapshot, marks that space free for reuse within the table, and updates the visibility and free-space maps. It does not normally return space to the operating system — the file stays the same size, with internal free space available for new rows. To physically shrink the file you need `VACUUM FULL` (which rewrites and takes an exclusive lock) or `pg_repack` (online).

</details>

<details><summary><b>27.</b> Why is `VACUUM FULL` dangerous to run casually on a large production table?</summary>

`VACUUM FULL` rewrites the entire table into a new file to eliminate all free space, taking an `ACCESS EXCLUSIVE` lock that blocks every read and write for the whole operation. On a large NAV-history table that can mean a long outage and it temporarily needs disk space for both old and new copies. Routine bloat is better managed by tuned autovacuum, and online compaction by `pg_repack` rather than `VACUUM FULL`.

</details>

<details><summary><b>28.</b> What is a HOT (Heap-Only Tuple) update and why does it reduce bloat?</summary>

A HOT update is an update where no indexed column changes and the new tuple fits on the same page, so PostgreSQL chains the new version on that page without inserting new entries into any index. This avoids index bloat entirely and lets the page be cleaned up cheaply ("HOT pruning") without a full vacuum. The practical lesson: keeping volatile, frequently-updated columns out of indexes makes more updates eligible for HOT and dramatically cuts index churn.

</details>

<details><summary><b>29.</b> What is transaction ID (XID) wraparound and why must vacuum prevent it?</summary>

PostgreSQL uses 32-bit transaction IDs (~4 billion) compared circularly, so without intervention old committed rows could appear to be in the "future" and become invisible, corrupting visibility. Vacuum "freezes" old tuples — marking them as permanently visible to all future transactions — which retires their XID so it can be reused. If autovacuum cannot keep up, the database forces aggressive vacuums and, at the limit, refuses new transactions to protect data integrity.

</details>

<details><summary><b>30.</b> What does it mean to "freeze" a tuple, and which process normally does it?</summary>

Freezing marks a tuple as unconditionally visible to all current and future transactions, removing its dependence on its original `xmin` and freeing that XID for reuse. Autovacuum performs anti-wraparound (aggressive) vacuums to freeze tuples before the XID age crosses configured thresholds. Frozen, all-visible pages can then be skipped by later vacuums via the visibility map, which is how vacuum stays affordable on huge static tables.

</details>

<details><summary><b>31.</b> What is the visibility map and how does it make vacuum and index-only scans cheaper?</summary>

The visibility map is a per-table bitmap with bits indicating whether all tuples on a page are visible to all transactions (and separately, all frozen). Vacuum can skip all-visible pages entirely, so it does work proportional to changed data rather than table size. Index-only scans use the same map: if the page is all-visible they can return data straight from the index without visiting the heap to check visibility.

</details>

<details><summary><b>32.</b> What is the WAL (Write-Ahead Log) and what guarantee does it provide?</summary>

The WAL is an append-only log of every change, written to durable storage before the corresponding data pages are flushed — the write-ahead rule. This guarantees that after a crash, committed changes can be replayed (redo) and uncommitted ones undone, so a `COMMIT` survives a crash even though the data pages may still be dirty in memory. It is also the foundation of replication and point-in-time recovery, since replicas consume the same log stream.

</details>

<details><summary><b>33.</b> What does `fsync` actually buy you at commit time, and what breaks if it is off?</summary>

At commit, PostgreSQL `fsync`s the WAL so the operating system and storage actually persist it to disk rather than leaving it in a volatile write cache. That is what makes durability real: with `fsync = off` a power loss can lose committed transactions and even corrupt the cluster, because WAL and data may be inconsistent on disk. You never disable it in production; `synchronous_commit` is the safer, transaction-level knob for trading a little durability for speed.

</details>

<details><summary><b>34.</b> What is a checkpoint and why does it exist?</summary>

A checkpoint flushes all dirty buffer-pool pages to the data files and records a point in the WAL up to which all changes are guaranteed persisted. It bounds crash-recovery time, because recovery only needs to replay WAL written after the last checkpoint, and it lets the server recycle older WAL segments. Checkpoints are spread out (`checkpoint_completion_target`) to avoid an I/O spike that would stall queries.

</details>

<details><summary><b>35.</b> What is ARIES-style logging, and which two principles from it does PostgreSQL recovery embody?</summary>

ARIES is the classic recovery algorithm built on write-ahead logging with three recovery phases — analysis, redo, then undo. PostgreSQL embodies the WAL principle (log the change before the data page) and redo from a known checkpoint, replaying logged changes to bring data files forward after a crash. Postgres differs in undo: instead of an undo log it relies on MVCC and vacuum to discard aborted/old row versions, so it does not need ARIES-style undo passes.

</details>

<details><summary><b>36.</b> Walk through what crash recovery does when PostgreSQL restarts after a power loss.</summary>

On restart it finds the last checkpoint record in the WAL and replays (redo) every logged change after it, reconstructing the dirty pages that never reached disk. Transactions that had committed before the crash are made durable by this redo; transactions that were in flight are simply never made visible because their tuples' creating XIDs did not commit. Because Postgres uses MVCC rather than an undo log, those uncommitted row versions are just dead tuples that vacuum later removes.

</details>

<details><summary><b>37.</b> What is the purpose of `EXPLAIN` versus `EXPLAIN ANALYZE`?</summary>

`EXPLAIN` shows the planner's chosen plan with estimated costs and row counts without running the query. `EXPLAIN ANALYZE` actually executes the query and reports real timings, `actual rows`, and loop counts so you can compare estimates against reality. Because it runs the statement, you must wrap data-modifying `EXPLAIN ANALYZE` in a transaction you roll back, or it will really insert/update/delete.

</details>

<details><summary><b>38.</b> Why should you add `BUFFERS` to `EXPLAIN (ANALYZE, BUFFERS)` when tuning?</summary>

`BUFFERS` reports the I/O each node did in 8 KB pages — `shared hit`, `shared read`, `dirtied`, and `written` — revealing where actual disk/cache traffic happens, not just where time was spent. Timing alone can mislead because a warm cache hides a query that reads far too many pages on a cold run. Reading buffers tells you whether a fix reduced real I/O or merely benefited from caching during your test.

</details>

<details><summary><b>39.</b> In `BUFFERS` output, what is the difference between `shared hit` and `shared read`?</summary>

`shared hit` counts pages found already in the buffer pool (no I/O), while `shared read` counts pages that missed the cache and had to be fetched from the OS cache or disk. A node with high `shared read` is doing real I/O and is the place to optimize; high `shared hit` is cheap but large counts still signal you are touching too many pages. The sum of the two is the total pages the node accessed.

</details>

<details><summary><b>40.</b> What do `dirtied` and `written` mean in `BUFFERS` output, and why might a `SELECT` dirty pages?</summary>

`dirtied` is the number of previously clean buffer pages this statement modified, and `written` is dirty pages it had to flush to make room. A read-only `SELECT` can dirty pages because the first reader after writes sets hint bits and prunes HOT chains on the page, which counts as a modification. Seeing dirties on a `SELECT` is normal on a freshly written table and typically settles after the first scan.

</details>

<details><summary><b>41.</b> A plan shows `Rows Removed by Filter: 4827193` on a Seq Scan — what does that tell you and what is the first fix to consider?</summary>

It means the scan read those rows from the heap and threw them away because they failed the `WHERE` predicate — wasted I/O and CPU. The first thing to consider is an index on the filtered column so the engine fetches only matching rows instead of scanning and discarding most of the table. If an index exists but is unused, check selectivity, stale statistics, or a non-sargable predicate (e.g. a function wrapping the column).

</details>

<details><summary><b>42.</b> What is a "sargable" predicate and why does wrapping a column in a function break index use?</summary>

Sargable (Search ARGument ABLE) means the predicate can use an index to seek directly, e.g. `WHERE trade_date = '2026-06-13'`. Wrapping the column in a function — `WHERE date(trade_ts) = '2026-06-13'` — forces the engine to compute the function for every row, so the plain column index cannot be used. The fixes are to rewrite as a range on the raw column (`trade_ts >= ... AND trade_ts < ...`) or to build an expression index on `date(trade_ts)`.

</details>

<details><summary><b>43.</b> What is a covering index and how does an index-only scan use it?</summary>

A covering index contains all columns a query needs (key columns plus `INCLUDE` payload columns), so the query can be answered from the index alone. With the visibility map marking pages all-visible, the planner uses an `Index Only Scan` that never visits the heap, cutting I/O substantially. The gotcha: if the table is heavily updated and not vacuumed, many pages are not all-visible, so the "index-only" scan still does heap fetches (shown as `Heap Fetches:` in the plan).

</details>

<details><summary><b>44.</b> Why might the planner ignore a perfectly good index and choose a sequential scan instead?</summary>

Because it estimates the predicate is not selective enough — if a query returns a large fraction of the table, reading sequentially is cheaper than millions of random index lookups. Other causes include stale statistics that misjudge selectivity, a non-sargable predicate, a type mismatch forcing a cast, or the index simply not matching the column order. Run `EXPLAIN ANALYZE` and compare estimated vs actual rows before assuming the planner is wrong.

</details>

<details><summary><b>45.</b> What is connection pooling and why does a fund platform front PostgreSQL with a pooler like PgBouncer?</summary>

Connection pooling reuses a small set of established server connections across many client connections, instead of each client opening its own backend. PostgreSQL spawns one OS process per connection, which is memory-heavy and context-switch-costly, so thousands of app connections would exhaust the server; a pooler multiplexes them onto far fewer backends. A high-fanout fund platform with many app instances therefore puts PgBouncer in front to keep backend count and memory bounded.

</details>

<details><summary><b>46.</b> Contrast PgBouncer's session, transaction, and statement pooling modes.</summary>

In session mode a server connection is dedicated to a client for the whole client session and returned at disconnect — safest, least multiplexing. In transaction mode the server connection is handed back to the pool at every `COMMIT`/`ROLLBACK`, allowing far more clients per backend but forbidding session-scoped state across transactions. Statement mode returns the connection after each individual statement and breaks multi-statement transactions, so it is the most aggressive and rarely used.

</details>

<details><summary><b>47.</b> Why do prepared statements historically break under PgBouncer transaction pooling, and what changed?</summary>

Prepared statements are session-scoped server objects, but in transaction mode a client can land on a different backend for its next transaction, where the prepared statement does not exist. PgBouncer added protocol-level tracking of named prepared statements in transaction/statement mode starting in version 1.21 (via `max_prepared_statements`), so they can work without per-statement re-preparation. Before that, you used session mode or disabled server-side prepared statements in the driver.

</details>

<details><summary><b>48.</b> In a fund platform on transaction-mode pooling, which session-level features must you avoid relying on across transactions?</summary>

Anything that lives on the server connection beyond a single transaction: session-level `SET` (e.g. `search_path`, `timezone`) that you expect to persist, advisory locks held across transactions, `LISTEN`/`NOTIFY`, `WITH HOLD` cursors, temporary tables, and (pre-1.21) prepared statements. Because the backend is reassigned at each commit, the next transaction may run on a different connection without that state. The fix is to set such state inside each transaction or pin those workloads to session mode.

</details>

<details><summary><b>49.</b> What is table partitioning in PostgreSQL and how is it declared?</summary>

Partitioning splits one logical table into multiple physical child tables by a key, declared with `PARTITION BY RANGE`, `LIST`, or `HASH`, then attaching partitions (e.g. one per month for NAV history). The parent is an empty routing table; rows are stored in the matching child, and queries against the parent are transparently routed. It is the standard way to manage very large, time-series-shaped tables like NAV or trade history.

</details>

<details><summary><b>50.</b> What is partition pruning and when does it actually help?</summary>

Partition pruning is the planner/executor eliminating partitions that cannot satisfy the query based on the partition key in the `WHERE` clause, so it scans only relevant children. It helps when queries filter on the partition key — e.g. `WHERE nav_date >= '2026-01-01'` touching only Q1/Q2 partitions instead of the whole table. It does nothing for queries that do not constrain the partition key, where it just adds planning overhead.

</details>

<details><summary><b>51.</b> When does partitioning add cost rather than benefit?</summary>

When there are many partitions and queries do not filter on the partition key, the planner must consider every partition, increasing planning time and memory without reducing scanned data. Too-fine partitioning (hundreds or thousands of small partitions) also bloats catalog overhead and can slow plan generation. Partitioning helps bulk pruning, partition-wise joins, and cheap detach/drop of old data; it is not a general index substitute.

</details>

<details><summary><b>52.</b> How does partitioning make "dropping old data" cheap compared with a `DELETE`?</summary>

Dropping an old monthly partition with `DROP TABLE` or `DETACH PARTITION` removes the whole child table in one metadata operation — no row-by-row deletion, no dead tuples, no vacuum aftermath. A `DELETE` of the same rows scans and marks millions of tuples dead, generating WAL and bloat that vacuum must then clean. For a rolling retention policy on trade/NAV history, partition-by-date plus drop-the-oldest is dramatically cheaper.

</details>

<details><summary><b>53.</b> What is the "Postgres until you can't" architect's lens, and what is its central tradeoff?</summary>

It is the principle of running one well-operated PostgreSQL plus extensions to cover roles you might otherwise split across many systems — queue, cache, vector store, time-series, graph, scheduler, small warehouse — keeping everything transactional with your core data. The tradeoff is operational simplicity and consistency at low-to-moderate scale versus the ceiling of a single node: when one workload's scale, latency, or fan-out outgrows Postgres, you graduate just that workload to a specialist and keep the rest. Knowing each extension's crossover point is the architect's skill.

</details>

<details><summary><b>54.</b> Which PostgreSQL extension turns it into a vector database, and what does it add?</summary>

`pgvector` adds a `vector` data type plus distance operators (`<->` L2, `<=>` cosine, `<#>` inner product) and approximate-nearest-neighbour indexes (HNSW and IVFFlat). It lets you store embeddings alongside relational data and run similarity search transactionally, avoiding a separate vector store at low-to-moderate scale. You graduate to a dedicated vector engine only when index size or query fan-out exceeds what one node serves.

</details>

<details><summary><b>55.</b> What does the `pgmq` extension provide and why use it instead of a separate broker?</summary>

`pgmq` implements a message-queue API (send, read with visibility timeout, archive, delete) on top of Postgres tables, giving queue semantics transactionally consistent with your business data. Using it avoids running and securing a separate broker for low-to-moderate throughput, and a message enqueue can commit atomically with the data change that produced it. You move to Kafka or a dedicated broker when throughput, retention, or consumer fan-out outgrows a single node.

</details>

<details><summary><b>56.</b> What does TimescaleDB add to PostgreSQL and for what workload?</summary>

TimescaleDB adds hypertables — automatically partitioned time-series tables — plus time-oriented features like continuous aggregates, retention policies, and compression. It targets high-ingest time-series such as tick data or metrics, keeping them queryable with standard SQL inside Postgres. It is the "time-series DB" role in the one-node story until ingest rate or volume justifies a specialist column store.

</details>

<details><summary><b>57.</b> Which extension gives PostgreSQL cron-style scheduling, and what is a caveat?</summary>

`pg_cron` schedules SQL commands on a cron schedule from within the database, useful for periodic vacuums, rollups, or refreshing materialized views. A caveat is that it runs in a single background worker against one database by default and is not a substitute for a full orchestrator with dependencies, retries, and backfills. For complex pipeline DAGs you still reach for Airflow/ADF; `pg_cron` covers simple in-database housekeeping.

</details>

<details><summary><b>58.</b> What roles do Apache AGE, `pg_duckdb`/Citus, and DBOS play in the "Postgres platform" picture?</summary>

Apache AGE adds an openCypher graph layer (graph DB role); `pg_duckdb` embeds DuckDB for fast columnar analytics and Citus shards Postgres for distributed/analytical scale (small-warehouse role); DBOS provides durable execution of workflows on Postgres. Each lets one Postgres cover a workload you would otherwise add a separate system for, while staying transactional with your data. The discipline is graduating only the workload that outgrows a node, not abandoning Postgres wholesale.

</details>

<details><summary><b>59.</b> Your slow 5-table fund-holdings query's `EXPLAIN ANALYZE` shows the largest `actual time` on a Nested Loop with `loops=3100000` — what is your first hypothesis?</summary>

The nested loop is iterating its inner side three million times, almost certainly because the planner underestimated the outer row count, so it chose a loop where a hash join would be far cheaper. First check the outer node's estimated `rows` against `actual rows` for a large gap, then run `ANALYZE` / raise statistics / add extended statistics so the planner sizes the join correctly. If estimates are accurate but the inner side lacks an index, add the supporting index so each probe is a cheap seek.

</details>

<details><summary><b>60.</b> You added an index but the plan did not change and the query is still slow — what do you check first?</summary>

First confirm the predicate is sargable and the index column order matches the filter/sort; a function-wrapped column or wrong leading column makes the index unusable. Then check selectivity and statistics: if the planner estimates most rows match, it may rightly prefer a seq scan, so `ANALYZE` and re-`EXPLAIN`. Also verify the index actually built (`\d table`), the types match (no implicit cast), and you are testing the same parameter values the planner sees.

</details>

<details><summary><b>61.</b> A query is fast in `EXPLAIN ANALYZE` on your laptop but slow in production — what cache effect explains this and how do you account for it?</summary>

On your laptop the relevant pages are likely warm in `shared_buffers` and the OS cache, so reads are hits; production may hit a cold cache and pay real disk reads. Add `BUFFERS` and look at `shared read` versus `shared hit` to separate I/O from CPU, and consider running on a comparably warmed cache or comparing absolute buffer counts rather than wall-clock time. The fix targets reducing pages touched, which helps regardless of cache temperature.

</details>

<details><summary><b>62.</b> How do you demonstrate the throughput effect of a tuning change, and which tool does the lesson use?</summary>

You run a repeatable benchmark before and after the change and compare transactions-per-second, using `pgbench`, PostgreSQL's bundled load-generator. `pgbench -i` initializes a dataset and `pgbench -c <clients> -j <threads> -T <seconds>` drives concurrent load, reporting TPS. Comparing TPS before and after (on the same warmed system) shows whether an index or rewrite actually improved end-to-end throughput, not just one query's plan.

</details>

<details><summary><b>63.</b> What is the difference between latency (one query's plan) and throughput (`pgbench` TPS), and why measure both?</summary>

Latency is how long a single query takes — what `EXPLAIN ANALYZE` shows — while throughput is how many transactions per second the system sustains under concurrency, what `pgbench` shows. A fix can improve one but harm the other: an index speeds reads but slows writes and adds bloat, lowering write throughput. Measuring both ensures a tuning change that helps a target query does not regress overall capacity.

</details>

<details><summary><b>64.</b> How would you deliberately demonstrate MVCC bloat, as the lesson's "Do" step asks?</summary>

Load a large table, record its size with `pg_total_relation_size()` or `\dt+`, then update every row in a loop (or many times) without vacuuming, and watch the size grow as dead tuples accumulate. Each update creates a new tuple version and leaves the old one dead, so the file expands even though the live row count is unchanged. Then run `VACUUM` and explain that space is now reusable internally (size may not shrink), while `VACUUM FULL` would physically reclaim it.

</details>

<details><summary><b>65.</b> Why doesn't the table file shrink after a plain `VACUUM` even though you removed dead tuples?</summary>

Plain `VACUUM` reclaims dead-tuple space for reuse by future inserts/updates within the same table but only truncates trailing empty pages, so interior free space stays allocated. The file therefore keeps its size and refills as new rows arrive, which is fine for steady-state churn. To actually return space to the OS you need `VACUUM FULL` or `pg_repack`, accepting their locking or operational cost.

</details>

<details><summary><b>66.</b> Pick the right index type for `WHERE isin = 'LU0123456789'` and justify it.</summary>

A B+tree index on `isin` is correct: the predicate is exact equality on a scalar text key, which a B+tree seeks in a few page reads. A hash index would also work for pure equality but offers no range/sort flexibility and historically less tooling support. B+tree also lets the same index serve prefix and ordered lookups later, so it is the safe default.

</details>

<details><summary><b>67.</b> Pick the right index type for `WHERE nav_date BETWEEN ... AND ...` on an append-only 500M-row table and justify it.</summary>

BRIN on `nav_date` is the strong candidate because the table is huge and append-only, so rows are physically clustered by date and block-range min/max pruning is highly effective at a tiny index size. A B+tree would also serve the range but costs far more storage and maintenance on 500M rows. Verify the column's correlation is near 1.0; if updates have scattered the dates, fall back to B+tree or re-cluster.

</details>

<details><summary><b>68.</b> Pick the right index type for `WHERE attributes @> '{"sub_fund":"X"}'` on a `jsonb` column and justify it.</summary>

A GIN index on the `jsonb` column is correct because `@>` is a containment operator over a composite value, exactly what GIN's inverted structure accelerates. A B+tree cannot index arbitrary JSON paths for containment; GIN maps each key/value element to the rows containing it. For a narrower set of paths, a B+tree expression index on a specific extracted field (`(attributes->>'sub_fund')`) can be smaller if you only ever query that one path.

</details>

<details><summary><b>69.</b> Pick the right index type for `WHERE counterparty_tags && ARRAY['UCITS','ESG']` on a `text[]` column and justify it.</summary>

GIN is correct: array overlap (`&&`) and containment (`@>`) are multi-value operators that GIN's inverted index is built for, indexing each array element to its rows. A B+tree indexes the array as an opaque whole and cannot answer element-overlap queries. GIN lets the engine intersect posting lists for the queried elements and fetch only matching rows.

</details>

<details><summary><b>70.</b> What does `pg_stats.correlation` measure and why does it matter for index choice?</summary>

`correlation` is the statistical correlation (from -1 to 1) between a column's logical value order and the physical order of rows on disk, gathered by `ANALYZE`. A value near 1 (or -1) means rows are nearly stored in column order, which makes range scans I/O-cheap and BRIN indexes effective. Near 0 means scattered storage, so range scans and BRIN do many random reads — favoring B+tree or a `CLUSTER` to restore correlation.

</details>

<details><summary><b>71.</b> What does `CLUSTER table USING index` do and what is its main drawback?</summary>

`CLUSTER` physically reorders the table's rows to match the given index's order, improving correlation so range scans and BRIN become efficient. Its drawback is that it takes an `ACCESS EXCLUSIVE` lock and rewrites the table, blocking access during the operation, and the ordering is not maintained automatically as new rows arrive. You re-cluster periodically, or use partitioning to keep data naturally ordered instead.

</details>

<details><summary><b>72.</b> A point lookup uses an index but the plan shows thousands of `Heap Fetches` on an Index Only Scan — what is wrong?</summary>

The index has the columns to answer the query, but many heap pages are not marked all-visible, so the "index-only" scan must visit the heap to check tuple visibility. The usual cause is a heavily updated table that autovacuum has not vacuumed recently enough to update the visibility map. Running `VACUUM` to set all-visible bits (and tuning autovacuum to keep up) restores true index-only behavior and drops the heap fetches.

</details>

<details><summary><b>73.</b> Why is keeping a frequently-updated column out of your indexes a performance decision, not just a style choice?</summary>

Every index that includes a column must be updated when that column changes, generating index bloat and preventing HOT updates (which require no indexed column to change). On a hot, frequently-corrected column like a NAV figure, indexing it forces non-HOT updates that insert new index entries on every change. Leaving it unindexed (or indexing a stable derived key instead) lets updates stay HOT, cutting write amplification and bloat.

</details>

<details><summary><b>74.</b> What is write amplification in PostgreSQL and which two mechanisms contribute most?</summary>

Write amplification is the extra physical writes produced per logical row change. The two big contributors are MVCC (an update writes a whole new tuple plus updates every affected index) and the WAL (the change is logged before the data write, sometimes including full-page images after a checkpoint). Designing for HOT updates, fewer indexes, and appropriate fill factor reduces it.

</details>

<details><summary><b>75.</b> What is full-page-image (FPI) writing in the WAL and why does it spike just after a checkpoint?</summary>

To protect against torn pages (partial 8 KB writes on crash), PostgreSQL logs a full copy of a page the first time it is modified after a checkpoint, not just the row delta. Right after a checkpoint, many pages are touched for the first time, so the WAL temporarily balloons with full-page images. This is why very frequent checkpoints increase WAL volume and I/O, and why `full_page_writes` is left on for safety.

</details>

<details><summary><b>76.</b> What is `fillfactor` and when would you lower it from the default?</summary>

`fillfactor` is the percentage of each page PostgreSQL fills on insert, leaving the rest free; the default is 100 for tables. Lowering it (e.g. to 80) leaves room on each page so updates can stay HOT (new version fits on the same page), reducing index bloat on update-heavy tables. The trade-off is a slightly larger table from the reserved free space, worthwhile when HOT-update rates are high.

</details>

<details><summary><b>77.</b> What is a materialized view and how does it differ from a regular view for a reporting mart?</summary>

A regular view is a stored query re-executed on every access; a materialized view stores the computed result on disk and must be refreshed with `REFRESH MATERIALIZED VIEW`. For an expensive reporting aggregate (e.g. daily fund AUM rollups) the materialized view trades freshness for fast reads. Use `REFRESH ... CONCURRENTLY` (which needs a unique index) to avoid locking readers during the refresh, at the cost of a slower refresh.

</details>

<details><summary><b>78.</b> What is the practical difference between `pg_relation_size`, `pg_table_size`, and `pg_total_relation_size`?</summary>

`pg_relation_size` reports the main data fork of a relation, `pg_table_size` adds TOAST and the free-space/visibility maps, and `pg_total_relation_size` adds all indexes on top. For bloat investigation you typically compare `pg_total_relation_size` over time and against an estimate of live data. They are the standard functions for the lesson's "watch the table size grow" bloat demonstration.

</details>

<details><summary><b>79.</b> How does Azure SQL's planner-hint and isolation culture differ from PostgreSQL, and why care during a migration?</summary>

SQL Server/Azure SQL has a long tradition of explicit query hints (e.g. `OPTION (HASH JOIN)`, index hints) and defaults to read-committed snapshot (RCSI) on Azure SQL, whereas PostgreSQL discourages hints and relies on statistics-driven planning. During a migration, hint-laden SQL Server queries have no direct Postgres equivalent and must be re-expressed as statistics, indexes, or rewrites. Recognizing this prevents porting brittle hints into an engine that deliberately omits them.

</details>

<details><summary><b>80.</b> Why is "read any engine's documentation and predict its behavior" the payoff of this lesson for an architect?</summary>

Once you understand pages, the buffer pool, B+tree/MVCC/WAL mechanics, and planning, vendor-specific features are mostly recombinations of the same primitives under different names. That lets you audit a vendor's claims and infer cost and failure behavior from first principles rather than trusting slideware. For regulated fund-platform selection, that means negotiating with DBAs and vendors on mechanism, not faith.

</details>

<details><summary><b>81.</b> What is the `ctid` of a tuple and why should you not use it as a stable identifier?</summary>

`ctid` is the physical location of a tuple as (block number, offset within block), useful for locating a row on disk. It is not stable: an `UPDATE` moves the row to a new version with a new `ctid`, and `VACUUM FULL`/`CLUSTER` rewrite the whole table, changing every `ctid`. Use a real surrogate key for identity; `ctid` is only for transient, within-transaction tricks.

</details>

<details><summary><b>82.</b> What is TOAST and when does PostgreSQL use it?</summary>

TOAST (The Oversized-Attribute Storage Technique) stores large field values out-of-line in a separate TOAST table, optionally compressed, when a row would otherwise exceed the page size. It triggers automatically for large `text`, `bytea`, `jsonb`, and similar values, keeping the main heap tuple small. The effect on tuning: queries that do not need the large column avoid TOAST I/O, and TOAST has its own storage that counts in `pg_table_size`.

</details>

<details><summary><b>83.</b> A NAV-history query that filters by `fund_id` and `nav_date` is slow despite a single-column index on `nav_date` — what index change helps?</summary>

A multicolumn B+tree index on `(fund_id, nav_date)` (leading with the equality column, then the range column) lets the engine seek to the fund and scan its date range in one structure. With only `nav_date` indexed, the engine still filters every fund's rows for that date range, doing extra work. Column order matters: equality predicates should precede the range predicate in the index key.

</details>

<details><summary><b>84.</b> Why does column order matter in a multicolumn B+tree index?</summary>

A B+tree is ordered by the leading column first, then the next, so it can seek efficiently only on a leading prefix of the key. An index on `(fund_id, nav_date)` serves `fund_id = ?` and `fund_id = ? AND nav_date BETWEEN ...`, but is far less useful for a query filtering only on `nav_date`. Place the columns used for equality first and the range/sort column last to match how queries probe the index.

</details>

<details><summary><b>85.</b> What is a partial index and give a fund-data case where it is the right tool.</summary>

A partial index covers only rows matching a `WHERE` clause in its definition, so it is smaller and cheaper to maintain. For example `CREATE INDEX ... ON orders (order_ref) WHERE status = 'PENDING'` indexes only open orders, which is ideal if queries almost always target pending orders and the pending set is a small fraction. It saves space and write cost compared with indexing the entire, mostly-settled, orders table.

</details>

<details><summary><b>86.</b> What is an expression (functional) index and when do you need one?</summary>

An expression index indexes the result of a function or expression rather than a raw column, e.g. `CREATE INDEX ON securities (upper(ticker))`. You need it when queries filter on a transformed value — `WHERE upper(ticker) = 'IBM'` — which a plain column index cannot serve because the function makes the predicate non-sargable. The expression in the index must match the one in the query exactly for the planner to use it.

</details>

<details><summary><b>87.</b> What does `autovacuum` do automatically, and what two thresholds typically trigger it per table?</summary>

Autovacuum is a background process that runs `VACUUM` and `ANALYZE` on tables that have accumulated enough dead tuples or changes, keeping bloat and stats in check without manual intervention. A table is vacuumed when dead tuples exceed `autovacuum_vacuum_threshold + autovacuum_vacuum_scale_factor * reltuples`, and analyzed under the analogous analyze settings. On large, churn-heavy tables you usually lower the scale factor so it triggers more often relative to size.

</details>

<details><summary><b>88.</b> A large, write-heavy NAV table keeps bloating despite autovacuum — what tuning addresses it?</summary>

The default `autovacuum_vacuum_scale_factor` (0.2) means autovacuum waits until ~20% of a huge table is dead, which on a billion-row table is a vast amount of bloat. Lower the per-table scale factor (or set a fixed threshold), raise `autovacuum_max_workers`/cost limits so vacuum keeps pace, and consider partitioning so each child is vacuumed independently. The goal is to make autovacuum trigger on a sensible absolute amount of dead tuples, not a percentage of a giant table.

</details>

<details><summary><b>89.</b> What is the difference between a logical (table) and physical (block/page) view of data, and why must an architect hold both?</summary>

The logical view is rows, columns, keys, and relationships; the physical view is pages, tuples, indexes on disk, and buffer-pool residency. Performance and failure behavior live at the physical level — an elegant logical model can still be slow if its physical layout causes random I/O or bloat. The architect reasons across both: the logical model for correctness and the physical mechanics for cost and reliability.

</details>

<details><summary><b>90.</b> How do you safely run `EXPLAIN ANALYZE` on an `UPDATE` or `DELETE` without changing data?</summary>

Wrap it in an explicit transaction and roll back: `BEGIN; EXPLAIN (ANALYZE) UPDATE ...; ROLLBACK;`. Because `EXPLAIN ANALYZE` truly executes the statement, omitting the rollback would persist the change. This lets you see the real plan and timings for a write while leaving the data untouched — essential when tuning loaders.

</details>

<details><summary><b>91.</b> What does a `Sort` node spilling to disk look like in a plan, and how do you fix it?</summary>

The `Sort Method` line reads `external merge Disk: <kb>` instead of `quicksort Memory:`, meaning the sort exceeded `work_mem` and spilled to temporary files. Fixes include raising `work_mem` for that session/query, reducing the rows sorted (better filtering or an index that returns data already ordered), or adding a matching index so the sort is avoided. Watch that raising `work_mem` globally multiplies across many concurrent sorts and can exhaust memory.

</details>

<details><summary><b>92.</b> What is `work_mem` and why is setting it too high server-wide risky?</summary>

`work_mem` is the memory a single sort or hash operation may use before spilling to disk; higher values keep operations in memory and faster. The risk is that it is per-operation per-connection, so a complex query with several sorts/hashes across many concurrent sessions can multiply into far more memory than you have. The safer pattern is a modest global default and a higher `SET work_mem` scoped to specific heavy analytical queries.

</details>

<details><summary><b>93.</b> A join chose a hash join that spills to disk on a small server — what knobs and design choices help?</summary>

Raising `work_mem` lets the hash table stay in memory; reducing the build side (filter earlier, project fewer columns) shrinks it; and ensuring accurate statistics prevents the planner from undersizing the hash. If the inputs are already sorted via indexes, a merge join may avoid the memory pressure entirely. As always, confirm with `EXPLAIN (ANALYZE, BUFFERS)` that the spill (temp blocks) actually disappeared.

</details>

<details><summary><b>94.</b> In `BUFFERS` output, what are `temp read`/`temp written`, and what do they indicate?</summary>

`temp` buffers are pages of temporary working data used by sorts, hashes, and materialize nodes that spilled out of `work_mem` to disk. Seeing `temp read`/`temp written` means an operation exceeded its memory budget and is paying disk I/O for intermediate results. The fix is to raise `work_mem` for the query or reduce the data volume being sorted/hashed so it stays in memory.

</details>

<details><summary><b>95.</b> Why can adding an index hurt a write-heavy ingest pipeline, and how do you reason about the tradeoff?</summary>

Every index must be maintained on each insert/update/delete, adding I/O, WAL, and (for updated indexed columns) blocking HOT updates, so more indexes slow writes and increase bloat. On a high-ingest trades loader, an index that helps a rare report can throttle the load path. The architect weighs read benefit against write cost, sometimes building indexes after a bulk load, or using partial/expression indexes to keep maintenance minimal.

</details>

<details><summary><b>96.</b> What is the cost of `CREATE INDEX` versus `CREATE INDEX CONCURRENTLY`, and when do you need the latter?</summary>

A plain `CREATE INDEX` takes a lock that blocks writes to the table while it builds, which is unacceptable on a busy production table. `CREATE INDEX CONCURRENTLY` builds without blocking writes by scanning the table twice and waiting out concurrent transactions, at the cost of a longer build and the risk of leaving an invalid index if it fails. On a 24/7 fund platform you use the concurrent form and then verify the index is valid.

</details>

<details><summary><b>97.</b> How would you diagnose, end to end, a fund-reporting query that "got slow last week" with no schema change?</summary>

Capture `EXPLAIN (ANALYZE, BUFFERS)` and compare estimated vs actual rows to spot stale statistics, then check whether data growth crossed a threshold that flipped the plan (e.g. index scan to seq scan). Look for bloat (`pg_total_relation_size` growth, low autovacuum activity), missing/invalid indexes, and parameter-value skew where a generic plan misfits a specific value. The disciplined order is: reproduce, read the plan and buffers, reconcile estimates with reality, then change one thing and re-measure.

</details>

<details><summary><b>98.</b> Summarize the four-index-type decision an architect should be able to defend on demand for fund data.</summary>

B+tree for scalar equality, ranges, and ordering (ISIN lookups, `(fund_id, nav_date)`); hash only for pure equality where a B+tree is not preferred; GIN for composite/multi-value containment and overlap on arrays, `jsonb`, and full-text (tag/attribute search); and BRIN for very large, naturally-ordered append tables where block min/max pruning works (NAV/trade history by date). The justification always rests on predicate shape and physical correlation, verified with `EXPLAIN (ANALYZE, BUFFERS)` and `pg_stats.correlation`, not on which index happens to exist.

</details>

<details><summary><b>99.</b> What is `pg_stat_statements` and why is it the architect's first stop for finding slow queries?</summary>

`pg_stat_statements` is a contrib extension that aggregates execution statistics per normalized query — total and mean time, calls, rows, and buffer I/O — across the whole server. Instead of guessing or staring at one query, you sort by total time to find the statements that actually dominate the workload, which is often a fast query run a million times rather than one slow report. It is the standard way to prioritize tuning effort, complementing `EXPLAIN (ANALYZE, BUFFERS)` which you then run on the offenders it surfaces.

</details>

<details><summary><b>100.</b> How does the planner decide join order, and what happens when there are many tables to join?</summary>

For a modest number of tables the planner exhaustively considers join orders and algorithms, costing each via cardinality estimates to pick the cheapest. Beyond `geqo_threshold` (default 12 relations) it switches to the genetic query optimizer (GEQO), a heuristic search that samples join orders rather than enumerating all of them, trading optimality for bounded planning time. This is why a query joining many tables can occasionally get a suboptimal order, and why reducing joined tables or pre-aggregating can stabilize plans.

</details>


## Phase 1 · 8.2.1 + 8.2.2 + 8.2.3 Conceptual → logical → physical modeling — 100 self-test questions

<details><summary><b>1.</b> What are the three levels of the conceptual → logical → physical modeling discipline?</summary>

The conceptual model names the business things and their relationships in business language with no keys or types; the logical model adds candidate keys, full attributes, and normalization while staying engine-neutral; the physical model is engine-specific DDL with data types, indexes, partitioning, and constraints. The chain is the architect's signature artifact: each level refines the previous one and is traceable back to it. Skipping a level is how you end up with an `ISIN`-as-primary-key database that cannot survive a corporate action.

</details>

<details><summary><b>2.</b> What belongs in a conceptual data model and what does NOT?</summary>

A conceptual model contains the major business entities (fund, share class, investor, order, NAV) and the relationships between them, expressed in business terms. It deliberately excludes attributes' data types, primary/foreign keys, normalization decisions, and anything engine-specific — those are logical or physical concerns. The test is that a business stakeholder who has never seen a database should be able to read and validate it.

</details>

<details><summary><b>3.</b> What is the "when to stop" rule for conceptual entity modeling?</summary>

You stop adding entities when every distinct business thing the stakeholders talk about is named and no new entity would change the shape of the relationships — roughly one page of entities and relationships. Per DMBOK ch. 5, the conceptual level is about scope and shared vocabulary, not completeness of detail, so resist the urge to add attributes or resolve many-to-many relationships there. Over-modeling at the conceptual level is a common smell: if you are arguing about a foreign key, you have drifted into the logical model.

</details>

<details><summary><b>4.</b> In the fund domain, why is "share class" a separate entity from "fund" rather than an attribute of it?</summary>

A single fund typically issues multiple share classes (e.g. retail vs institutional, distributing vs accumulating, hedged vs unhedged), each with its own `ISIN`, fee schedule, and NAV per share. Modeling share class as its own entity captures the one-to-many relationship and lets each class carry its own attributes; folding it into the fund as an attribute would force repeating-group or multi-valued columns that violate first normal form. This is exactly the kind of entity boundary a conceptual model must get right before any keys are assigned.

</details>

<details><summary><b>5.</b> What is a candidate key?</summary>

A candidate key is any minimal set of attributes whose values uniquely identify each row in a relation, where "minimal" means no attribute can be removed without losing uniqueness. A table can have several candidate keys; you pick one as the primary key and the rest become alternate keys, usually enforced by `UNIQUE` constraints. Identifying all candidate keys is a logical-modeling step that drives normalization, because functional dependencies are defined relative to keys.

</details>

<details><summary><b>6.</b> What is the difference between a natural key and a surrogate key?</summary>

A natural key is a candidate key drawn from real-world business data (an `ISIN`, a passport number, an email), while a surrogate key is a system-generated identifier with no business meaning (an auto-increment integer, a `UUID`, a `BIGINT` from a sequence). Surrogates are stable and opaque, so they survive business-rule changes; natural keys are meaningful but can change, be reissued, or be unknown at insert time. The choice between them is one of the central logical-design decisions you must justify in writing.

</details>

<details><summary><b>7.</b> Why is an `ISIN` an attribute and not a primary key for a security or share class?</summary>

`ISIN`s can be reused or reassigned after a security is delisted, are sometimes unavailable when a record is first created, and a single economic instrument can carry different identifiers across markets — so an `ISIN` is not guaranteed stable or always present, which a primary key must be. Making it the PK welds every foreign key in the database to a value that a corporate action (merger, rename, redomicile) can change, forcing painful cascading updates. The architect's answer is a surrogate primary key with the `ISIN` stored as a `UNIQUE`, indexed business attribute.

</details>

<details><summary><b>8.</b> A colleague proposes `ISIN` as the primary key of the `share_class` table. What is your first objection?</summary>

That `ISIN` is not guaranteed immutable: corporate actions and reissuance can change it, and the PK should never change because every foreign key depends on it. I would propose a surrogate `share_class_id` as the PK and keep `ISIN` as a `UNIQUE NOT NULL` (or `UNIQUE` allowing nulls for not-yet-assigned classes) attribute. This isolates the join graph from business-identifier churn while still enforcing the one-`ISIN`-per-class rule.

</details>

<details><summary><b>9.</b> What is a composite key?</summary>

A composite (compound) key is a candidate or primary key made of two or more columns that together provide uniqueness, because no single column is unique on its own. A classic example is a NAV history table keyed by (`share_class_id`, `nav_date`): neither column alone is unique, but the pair is. Composite keys are common at the logical level but are often replaced by a surrogate at the physical level when the key is wide or referenced by many child tables.

</details>

<details><summary><b>10.</b> What does normalization aim to achieve?</summary>

Normalization organizes columns and tables to minimize redundancy and the update/insert/delete anomalies that redundancy causes, by ensuring each fact is stored in exactly one place. It proceeds through normal forms (1NF, 2NF, 3NF, BCNF, ...) that each forbid a specific class of dependency. The goal at the logical level is a structure where business rules are enforced by keys and constraints rather than by hoping every copy of a fact stays in sync.

</details>

<details><summary><b>11.</b> What does first normal form (1NF) forbid?</summary>

1NF requires every column to hold a single atomic value per row and forbids repeating groups, multi-valued columns, and arrays-as-columns used to dodge a child table. For example, storing three sub-fund `ISIN`s in one comma-separated column violates 1NF; you split them into separate rows of a child table. 1NF is the precondition for all the higher forms, because functional dependencies are only well defined over atomic columns.

</details>

<details><summary><b>12.</b> What does second normal form (2NF) forbid?</summary>

2NF applies to tables with a composite primary key and forbids partial dependencies — where a non-key column depends on only part of the key rather than the whole key. If a NAV-line table keyed by (`order_id`, `line_no`) stores `order_date`, that date depends on `order_id` alone, violating 2NF; it belongs in the `order` table. A table already in 1NF with a single-column key is automatically in 2NF.

</details>

<details><summary><b>13.</b> What does third normal form (3NF) forbid?</summary>

3NF forbids transitive dependencies: a non-key column depending on another non-key column rather than directly on the key. If a `share_class` table stores `fund_name` (which depends on `fund_id`, itself a non-key attribute), that is transitive and `fund_name` belongs in the `fund` table. The informal mnemonic is that every non-key attribute depends on "the key, the whole key, and nothing but the key".

</details>

<details><summary><b>14.</b> What does Boyce-Codd normal form (BCNF) forbid that 3NF allows?</summary>

BCNF strengthens 3NF by requiring that for every non-trivial functional dependency `X → Y`, `X` must be a superkey — closing the loophole where a non-prime attribute determines part of a candidate key. The cases where 3NF and BCNF differ involve overlapping candidate keys, which are rare but real. In practice most well-designed transactional schemas reach BCNF naturally once they are in 3NF.

</details>

<details><summary><b>15.</b> What is a functional dependency, and why does it matter for normalization?</summary>

A functional dependency `A → B` means that for any given value of `A`, the value of `B` is uniquely determined — knowing the `share_class_id` determines the `fund_id`. Normalization is defined entirely in terms of functional dependencies relative to keys: each normal form forbids a particular shape of dependency. You cannot defend a table's normal form without first writing down its functional dependencies.

</details>

<details><summary><b>16.</b> What is denormalization and when is it legitimate?</summary>

Denormalization deliberately reintroduces redundancy — duplicated columns, pre-joined tables, stored aggregates — to improve read performance or simplify queries, accepting the cost of keeping copies in sync. It is legitimate when measured read patterns demand it and the redundancy is documented and controlled (e.g. maintained by triggers or batch jobs), not when it happens by accident. The discipline is that every denormalization must be a recorded, justified decision, never silent drift from a normalized baseline.

</details>

<details><summary><b>17.</b> How should a deliberate denormalization be documented in the model?</summary>

You record which normalized form the table departs from, exactly which redundancy was introduced, the read pattern that justifies it, and the mechanism that keeps the duplicated data consistent. The "Done when" bar for this lesson is being able to name each table's normal form and point to where you denormalized deliberately and why. Undocumented denormalization is indistinguishable from a modeling mistake during review.

</details>

<details><summary><b>18.</b> A reviewer finds the same `fund_name` stored in three tables. What two questions decide whether it is acceptable?</summary>

First: is this a documented, deliberate denormalization with a stated read-pattern justification, or accidental duplication? Second: what mechanism keeps the three copies consistent, and what happens on a rename? If there is no documentation and no sync mechanism, it is an update anomaly waiting to happen and should be normalized back to a single `fund` row that the others reference by `fund_id`.

</details>

<details><summary><b>19.</b> What changes between the logical and physical model regarding keys?</summary>

At the logical level keys are conceptual: you state candidate keys and choose a primary key by attribute set. At the physical level those become concrete DDL — a `BIGINT GENERATED ALWAYS AS IDENTITY` surrogate, a `PRIMARY KEY` constraint, `UNIQUE` constraints for alternate keys, and `FOREIGN KEY` constraints with chosen `ON DELETE`/`ON UPDATE` actions. The physical model also picks index types and storage details the logical model deliberately ignored.

</details>

<details><summary><b>20.</b> At the physical level, why does data-type choice matter beyond just "holding the value"?</summary>

Data types determine storage size, index efficiency, comparison/sort behavior, and what invalid values the engine rejects for free. Choosing `NUMERIC(18,6)` for a NAV instead of `FLOAT` avoids binary rounding errors that are unacceptable in financial calculations; choosing `DATE` instead of `TEXT` for `nav_date` enables range partitioning and correct ordering. Type choice is a physical decision tuned to the target engine, which is why a logical model should not pin it down.

</details>

<details><summary><b>21.</b> Why is `NUMERIC`/`DECIMAL` preferred over `FLOAT`/`DOUBLE PRECISION` for monetary and NAV values in Postgres?</summary>

`NUMERIC` stores exact base-10 values with a defined precision and scale, so sums and comparisons of money are exact, whereas `FLOAT`/`DOUBLE PRECISION` are binary floating point and cannot represent values like `0.1` exactly, producing accumulating rounding errors. In a regulated NAV context those errors can break reconciliation to the cent and fail audit. The cost is that `NUMERIC` arithmetic is slower and the column is larger, which is an acceptable trade for correctness here.

</details>

<details><summary><b>22.</b> What is the difference between `CHAR(n)`, `VARCHAR(n)`, and `TEXT` in Postgres, and which would you use for an `ISIN`?</summary>

`CHAR(n)` is blank-padded to a fixed length, `VARCHAR(n)` enforces a maximum length, and `TEXT` is unbounded; in Postgres there is no performance penalty for `TEXT` versus `VARCHAR`. An `ISIN` is always exactly 12 characters, so `CHAR(12)` documents that fixed width, though many teams use `VARCHAR(12)` plus a `CHECK` constraint to avoid the padding semantics. Either way you add a `CHECK` that enforces the 12-character ISO 6166 format.

</details>

<details><summary><b>23.</b> What is declarative table partitioning in PostgreSQL?</summary>

Declarative partitioning splits one logical table into multiple physical child tables ("partitions") using `CREATE TABLE ... PARTITION BY`, with each partition created via `CREATE TABLE ... PARTITION OF ... FOR VALUES ...`. Postgres routes inserts to the correct partition automatically and can prune irrelevant partitions from query plans. It is a physical-design technique for very large tables like NAV history, introduced as the modern replacement for the old inheritance-plus-trigger approach.

</details>

<details><summary><b>24.</b> What are the three declarative partitioning methods in PostgreSQL?</summary>

Range partitioning (`PARTITION BY RANGE`) splits on non-overlapping value ranges, with lower bound inclusive and upper bound exclusive — ideal for `nav_date`. List partitioning (`PARTITION BY LIST`) assigns explicit key values to each partition, useful for something like fund domicile. Hash partitioning (`PARTITION BY HASH`) spreads rows across partitions by a modulus and remainder for even distribution when no natural range or list exists.

</details>

<details><summary><b>25.</b> Which partitioning method fits a NAV-history table and why?</summary>

Range partitioning on `nav_date` (typically monthly or yearly) fits best, because NAV history grows by date and almost every query filters or aggregates by date range. Range partitions let the planner prune to just the relevant months and make archiving old data a fast `DETACH PARTITION` rather than a huge `DELETE`. This is the canonical example the PostgreSQL partitioning docs use for the design.

</details>

<details><summary><b>26.</b> Show the syntax to declare a range-partitioned NAV table and one monthly partition.</summary>

You declare the parent with `CREATE TABLE nav_history (...) PARTITION BY RANGE (nav_date);` and add a partition with `CREATE TABLE nav_history_2026m06 PARTITION OF nav_history FOR VALUES FROM ('2026-06-01') TO ('2026-07-01');`. The upper bound `'2026-07-01'` is exclusive, so it does not overlap the next month's partition. New rows whose `nav_date` falls in June 2026 are routed to that child table automatically.

</details>

<details><summary><b>27.</b> In PostgreSQL, what constraint must a primary key on a partitioned table satisfy?</summary>

The primary (or unique) key's columns must include all of the partition key columns, and the partition key must not use expressions or function calls. This is because each partition has its own local index that can only enforce uniqueness within itself, so the partition boundaries plus the included key columns are what guarantee global uniqueness. For a `nav_history` partitioned by `nav_date`, the PK must therefore be a composite like (`share_class_id`, `nav_date`), not `share_class_id` alone.

</details>

<details><summary><b>28.</b> A `CREATE TABLE ... PARTITION BY RANGE (nav_date)` fails when you also declare `PRIMARY KEY (share_class_id)`. Why?</summary>

Postgres rejects it because the partition key column `nav_date` is not part of the primary key, and on a partitioned table the unique/primary key must include every partition-key column. The fix is to make the key composite — `PRIMARY KEY (share_class_id, nav_date)` — or to choose a different partition key that is already in the PK. This is a hard limitation of how per-partition indexes enforce uniqueness, not a bug.

</details>

<details><summary><b>29.</b> What is a `DEFAULT` partition and what is the catch when attaching new partitions later?</summary>

A `DEFAULT` partition catches any row whose key matches no defined partition, declared with `CREATE TABLE ... PARTITION OF parent DEFAULT`. The catch is that to `ATTACH` a new partition whose range might already contain rows sitting in the default partition, Postgres must scan the default partition to verify none of those rows belong to the new range, which can be slow and takes a strong lock. Many designs avoid a default partition for time-series tables so future-month partitions attach cheaply.

</details>

<details><summary><b>30.</b> What is the practical difference between `ATTACH PARTITION` and `DETACH PARTITION CONCURRENTLY`?</summary>

`ALTER TABLE ... ATTACH PARTITION` takes only a `SHARE UPDATE EXCLUSIVE` lock on the parent, so it is light, but it validates that incoming rows respect the partition bound. Plain `DETACH PARTITION` requires an `ACCESS EXCLUSIVE` lock that blocks all access, whereas adding `CONCURRENTLY` lowers it to `SHARE UPDATE EXCLUSIVE` so reads and writes continue. For archiving a month of NAV history, `DETACH PARTITION ... CONCURRENTLY` lets you remove old data without an outage.

</details>

<details><summary><b>31.</b> Why is `DETACH PARTITION` a better archival strategy than `DELETE` for old NAV rows?</summary>

`DETACH PARTITION` is a near-instant metadata operation that turns a partition into a standalone table, whereas `DELETE` of millions of rows generates WAL, bloats the table, and requires a `VACUUM` to reclaim space. After detaching you can dump the standalone table to cold storage or `DROP` it cheaply. This is one of the main reasons to range-partition append-only history in the first place.

</details>

<details><summary><b>32.</b> What is partition pruning and what enables it?</summary>

Partition pruning is the planner (and executor) eliminating partitions that cannot contain matching rows, so a query touching only June 2026 reads only that month's partition. It is enabled when the query's `WHERE` clause filters on the partition key with a constant or parameter the planner can compare to partition bounds. Pruning is the main performance payoff of partitioning; a query with no partition-key predicate must scan every partition.

</details>

<details><summary><b>33.</b> How does choosing an index differ at the physical level versus what the logical model says?</summary>

The logical model declares uniqueness and relationships; the physical model decides which of those become indexes and adds non-unique indexes to support query access paths. You add indexes for foreign keys (so joins and cascade checks are fast), for frequent filter/sort columns, and choose the index type — B-tree for ranges and equality, GIN for arrays/JSONB, BRIN for huge naturally-ordered tables. Indexes are pure physical tuning: they change performance, never the logical meaning of the data.

</details>

<details><summary><b>34.</b> Why is a `BRIN` index sometimes a good fit for a large NAV-history table?</summary>

A `BRIN` (Block Range Index) stores summary min/max values per block range rather than per row, so it is tiny and cheap to maintain, and it works well when the data is physically ordered by the indexed column — which `nav_date` typically is in an append-only history. For range scans over date it can prune large swathes of the table at a fraction of a B-tree's size. The trade-off is that `BRIN` is far less effective if the column's physical order is random.

</details>

<details><summary><b>35.</b> On a partitioned table, does `CREATE INDEX` on the parent create a global index?</summary>

No — PostgreSQL has no global indexes; an index on a partitioned table is "virtual" and Postgres creates a matching local index on each partition. The benefit is that each partition's index is independent, so detaching a partition takes its index with it; the cost is that uniqueness can only be enforced per partition unless the partition key is part of the unique constraint. This is why unique constraints on partitioned tables must include the partition key.

</details>

<details><summary><b>36.</b> What is forward engineering in data modeling?</summary>

Forward engineering is generating the physical DDL (and ultimately the database) from a logical or physical model — going model → schema. A modeling tool like DBeaver, erwin, or ER/Studio produces `CREATE TABLE` statements with the types, keys, and constraints the model specifies. It is half of the round-trip; the value is that the running schema is a faithful image of the reviewed model rather than hand-typed drift.

</details>

<details><summary><b>37.</b> What is reverse engineering in data modeling?</summary>

Reverse engineering builds a model by reading an existing database's catalog — going schema → model — so you can diagram and review a database you did not author. Tools such as DBeaver's ERD view or erwin connect to the database and reconstruct entities, columns, keys, and relationships from the system catalog. It is essential for documenting legacy fund-admin systems where the only authoritative artifact is the live schema.

</details>

<details><summary><b>38.</b> What does "round-tripping without drift" mean and why is it the goal?</summary>

Round-tripping means you can forward-engineer a model to DDL, later reverse-engineer that DDL back into a model, and diff the two to confirm they still agree. "Without drift" means the model and the database have not silently diverged — no column added in production that the model lacks, no constraint in the model missing from the database. Keeping them in sync is what makes the model a trustworthy review artifact rather than stale documentation.

</details>

<details><summary><b>39.</b> How would you detect drift between your logical model and the deployed Postgres schema?</summary>

Reverse-engineer the live schema (e.g. in DBeaver) into a model and diff it against your maintained logical model, comparing entities, columns, types, keys, and constraints. Differences flag drift: a column present in production but not the model, or a relationship the model claims that the database does not enforce. The lesson's "Do" step is exactly this — reverse-engineer the physical model and diff against the logical model.

</details>

<details><summary><b>40.</b> What is Crow's Foot notation and what does it express?</summary>

Crow's Foot is an ERD notation where relationship cardinality is drawn at the line ends: a "crow's foot" (three prongs) means "many", a single bar means "one", a circle means "zero/optional", so combinations express minimum and maximum participation. For example a bar-plus-crow's-foot on the child end reads "one and only one ... to many". It is the most widely used notation in practical database modeling and the one you are expected to write fluently.

</details>

<details><summary><b>41.</b> In Crow's Foot notation, how is a mandatory-one-to-many relationship drawn?</summary>

The "one" parent end is marked with a single perpendicular bar (exactly one), and the "many" child end is marked with a crow's foot preceded by a bar to mean "one or more" (mandatory many) or by a circle to mean "zero or more" (optional many). So fund-to-share-class, where a fund must have at least one share class and each share class belongs to exactly one fund, is bar on the fund end and bar-crow's-foot on the share-class end. Reading the symbols at each end gives you both cardinality and optionality.

</details>

<details><summary><b>42.</b> What is IDEF1X notation and how does it differ from Crow's Foot?</summary>

IDEF1X is a formal ERD notation (a U.S. federal standard, common in defense and government data modeling) that distinguishes identifying from non-identifying relationships and uses solid versus dashed lines and rounded versus square-cornered entity boxes to show dependency. Unlike Crow's Foot it encodes whether a child entity's primary key includes the parent's key (identifying = solid line, rounded child box). The lesson asks you to *read* IDEF1X and *write* Crow's Foot, so you need passive fluency in IDEF1X's dependency semantics.

</details>

<details><summary><b>43.</b> In IDEF1X, what is the difference between an identifying and a non-identifying relationship?</summary>

In an identifying relationship the parent's primary key migrates into the child's primary key, making the child existence-dependent on the parent; IDEF1X draws this as a solid line with a rounded-corner (dependent) child entity. In a non-identifying relationship the parent's key becomes a non-key foreign-key attribute in the child, drawn as a dashed line with a square-corner (independent) entity. This distinction is central to IDEF1X and is why it is favored where key-dependency rigor matters.

</details>

<details><summary><b>44.</b> Why must an architect be fluent in more than one modeling notation?</summary>

Different stakeholders and tools speak different notations — a vendor may hand you IDEF1X diagrams, a DBA Crow's Foot ERDs, a BA BPMN — and the architect is the one who reads all of them without a translator. The lesson sets the bar at writing Crow's Foot and reading IDEF1X. Notation is just a rendering of the same underlying entities, keys, and cardinalities, so fluency is about recognizing the same model in different clothes.

</details>

<details><summary><b>45.</b> What is an associative entity (junction table) and when do you introduce one?</summary>

An associative entity resolves a many-to-many relationship into two one-to-many relationships by creating a new entity that holds a foreign key to each side, plus any attributes of the association itself. You introduce it whenever the conceptual model shows a many-to-many — e.g. an investor holding many share classes and a share class held by many investors becomes a `holding` entity. At the logical level this is mandatory, because a relational schema cannot directly represent many-to-many.

</details>

<details><summary><b>46.</b> Why can a conceptual many-to-many relationship not survive into the physical relational model unchanged?</summary>

A relational table cannot store a direct many-to-many link in a single foreign key, so the relationship must be resolved into a junction/associative table carrying one foreign key per side. The junction table's primary key is typically the composite of the two foreign keys (or a surrogate), and it is the natural home for relationship attributes like position quantity or as-of date. Leaving a raw many-to-many in the logical model is an unimplementable model.

</details>

<details><summary><b>47.</b> What is referential integrity and how is it enforced at the physical level?</summary>

Referential integrity is the rule that every foreign-key value must match an existing primary-key value in the referenced table (or be null), so you never point at a non-existent parent. Postgres enforces it with `FOREIGN KEY` constraints, optionally with `ON DELETE`/`ON UPDATE` actions like `RESTRICT`, `CASCADE`, or `SET NULL`. Enforcing it in the database, not just application code, is what guarantees an order can never reference a deleted share class.

</details>

<details><summary><b>48.</b> What does `ON DELETE CASCADE` do, and why would you be cautious with it on fund reference data?</summary>

`ON DELETE CASCADE` automatically deletes child rows when their parent row is deleted, propagating the delete down the relationship. On fund reference data this is dangerous because deleting a fund would silently erase all its share classes, NAV history, and orders — destroying records you are regulated to retain. For reference and historical data you usually prefer `ON DELETE RESTRICT` (or soft-delete flags) so accidental deletes fail loudly.

</details>

<details><summary><b>49.</b> Why is the surrogate-key-versus-natural-key decision recorded "in writing" in this lesson's Done-when criteria?</summary>

Because the architect must be able to state a reason for every surrogate-key choice — including why `ISIN` is not the PK — and an unwritten rationale is unreviewable and forgotten. Writing it down makes the decision auditable, which a regulated fund administrator's governance expects, and forces you to actually have a reason rather than a habit. The bar is that a colleague reading the model can see why each key is what it is.

</details>

<details><summary><b>50.</b> What is the test that the lesson uses to judge whether a logical model is good enough?</summary>

The test is: can you hand the logical model to a colleague and have them implement it without asking you any questions? If they need to ask what a key is, what a relationship means, or what normal form a table is in, the model is underspecified. This is the lesson's primary "Done when" criterion and it forces completeness and clarity at the logical level.

</details>

<details><summary><b>51.</b> Why does the lesson say a logical model should be engine-neutral?</summary>

Because welding the logical model to one engine's types, partitioning, or index syntax means you cannot retarget it and you blur the line between logical meaning and physical tuning. An engine-neutral logical model states entities, keys, attributes, relationships, and normal forms; the choice of `NUMERIC(18,6)` versus another engine's decimal type belongs only in the physical model. Keeping them separate is what lets the same logical design drive Postgres, Snowflake, or Synapse physical models.

</details>

<details><summary><b>52.</b> What is a degenerate dimension's logical-modeling analogue — a degenerate identifier — and how does it relate to keys here?</summary>

A degenerate identifier is a business identifier like an `order_number` that you keep as an attribute for traceability but do not promote to a primary key, because it may not be stable or unique across the whole system. It relates to this lesson's key discipline: like `ISIN`, it is meaningful business data carried as an attribute while a surrogate provides the stable PK. Recognizing which identifiers are decoration versus keys is core to logical key design.

</details>

<details><summary><b>53.</b> Why is "premature surrogate key on every table" itself a modeling smell?</summary>

Adding a surrogate to a table that already has a small, stable, single-column natural key (like a 2-letter country code or a currency `ISO 4217` code) adds a join and an opaque integer for no benefit. The decision should be justified case by case: surrogates earn their place where natural keys are wide, unstable, or absent. The discipline is reasoned key selection, not a blanket rule in either direction.

</details>

<details><summary><b>54.</b> How do you decide whether to store an attribute as a column or promote it to its own entity?</summary>

Promote it to its own entity when it has its own attributes, participates in its own relationships, or repeats across rows — i.e. it is a "thing" not just a "fact about a thing". A fund's domicile is a single coded value, so it can be a column (or a small reference table); a fund's set of distributors each with their own agreements is an entity. The conceptual model should reveal this before keys are assigned.

</details>

<details><summary><b>55.</b> What is a reference (lookup) table and why model coded values that way?</summary>

A reference table holds the allowed values of a coded attribute — currencies, countries, fund types, order statuses — usually with a short code as the key and a human-readable description. Modeling them this way enforces referential integrity on the codes, centralizes the descriptions, and lets you add metadata (active flag, effective dates) per code. It also prevents the data-quality drift you get when free-text values like "EUR", "Euro", and "eur" coexist.

</details>

<details><summary><b>56.</b> At the physical level, why might you choose `GENERATED ALWAYS AS IDENTITY` over a `SERIAL` column in Postgres?</summary>

`GENERATED ALWAYS AS IDENTITY` is the SQL-standard syntax and, with `ALWAYS`, prevents an application from accidentally supplying its own value for the surrogate key, which protects key integrity. `SERIAL` is older Postgres-specific sugar that creates a sequence and a default but does not block manual inserts and has quirkier ownership semantics. For a surrogate primary key you want the stricter, standard `IDENTITY` form.

</details>

<details><summary><b>57.</b> What is the difference between a primary key and a unique constraint at the physical level?</summary>

A primary key is a single chosen candidate key that is `NOT NULL` and uniquely identifies the row, and a table has at most one; a `UNIQUE` constraint enforces uniqueness on an alternate key and may allow nulls (treated as distinct in Postgres). Both create an underlying unique index. You designate the surrogate as the primary key and add a `UNIQUE` constraint on the natural key like `ISIN` so both are enforced.

</details>

<details><summary><b>58.</b> Why might `UNIQUE` on a nullable `ISIN` column behave differently than you expect in Postgres?</summary>

In standard Postgres a `UNIQUE` constraint treats `NULL` values as distinct, so multiple rows with `ISIN IS NULL` are all allowed — useful when a share class exists before its `ISIN` is assigned. If you need at most one null, you would use `NULLS NOT DISTINCT` (available in modern Postgres) or a partial unique index. Knowing this is the difference between "one un-ISIN'd class allowed" and "many" — a real fund-onboarding edge case.

</details>

<details><summary><b>59.</b> How does the conceptual model constrain what the logical model can do?</summary>

The conceptual model fixes the entities and the relationships' cardinality, so the logical model must produce keys and tables that faithfully represent those things and links — it cannot invent or drop a business relationship. If the conceptual model says one investor places many orders, the logical model must give `order` a foreign key to `investor`, not the reverse. Traceability runs downward: each logical element should map to something the conceptual model named.

</details>

<details><summary><b>60.</b> What is the danger of modeling NAV as an attribute of share class rather than as its own time-series entity?</summary>

NAV is a value that changes daily, so storing a single `nav` column on `share_class` keeps only the latest value and throws away the history regulators and investors require. Modeling NAV as its own entity keyed by (`share_class_id`, `nav_date`) preserves the full periodic time series and lets you answer "what was the NAV on this date". This is a conceptual error that, if uncaught, poisons every downstream physical design.

</details>

<details><summary><b>61.</b> Why is (`share_class_id`, `nav_date`) a natural composite candidate key for NAV history?</summary>

Because exactly one official NAV is struck per share class per valuation date, that pair uniquely identifies a NAV record and neither column alone does. It also doubles conveniently as the basis for range partitioning by `nav_date` while still being a valid composite primary key (since the partition key is included). Whether you keep it as the PK or add a surrogate is a physical decision, but the candidate key is clear at the logical level.

</details>

<details><summary><b>62.</b> In a transfer-agency context, why might an investor entity need a surrogate key even though it has identifiers like an account number?</summary>

Account numbers can be reformatted on system migrations, reissued, or differ across the registers an investor holds, so they are not guaranteed stable or globally unique — making them poor primary keys. A surrogate `investor_id` gives a stable internal identity that all the investor's accounts, orders, and holdings can reference unchanged. The account number stays as a `UNIQUE` business attribute for lookup and external reconciliation.

</details>

<details><summary><b>63.</b> What is the relationship between a logical model's normal form and its update anomalies?</summary>

Lower normal forms permit redundant storage of a fact, which creates update anomalies (change it in one place, others go stale), insertion anomalies (cannot record one fact without another), and deletion anomalies (deleting a row loses unrelated facts). Reaching 3NF/BCNF removes the functional-dependency redundancies that cause these. That is the whole point of stating each table's normal form — it tells the reviewer which anomalies are structurally impossible.

</details>

<details><summary><b>64.</b> Give an insertion anomaly example in a poorly normalized fund table.</summary>

If `fund` and `share_class` data live in one table, you cannot record a newly registered fund that has not yet launched any share class without inventing a dummy share-class row, because the share-class columns cannot be null in a meaningful key. Splitting into `fund` and `share_class` lets the fund exist independently of its classes. The anomaly disappears once the transitive/partial dependency is removed.

</details>

<details><summary><b>65.</b> How does an optional (zero-or-one) relationship translate to physical DDL?</summary>

An optional relationship lets the foreign-key column be nullable, so a row may or may not reference the parent — for example an order that has not yet been allocated to a settlement batch has a null `batch_id` — while the `FOREIGN KEY` still validates any non-null value against the parent. A mandatory relationship instead makes that column `NOT NULL`, forcing every child to have a parent. This is how the ERD's cardinality and optionality become enforced database constraints rather than mere drawing.

</details>

<details><summary><b>66.</b> What is a "self-referencing" relationship and where might it appear in fund data?</summary>

A self-referencing (recursive) relationship is a foreign key from a table back to itself, modeling a hierarchy among rows of the same entity. In fund data a master-feeder structure (a feeder fund investing into a master fund) or an umbrella-and-sub-fund hierarchy is naturally a `parent_fund_id` foreign key on the `fund` table. It is the relational way to represent a tree of funds.

</details>

<details><summary><b>67.</b> Why should the physical model's choices be "per target engine" rather than universal?</summary>

Because engines differ in available types, index kinds, partitioning syntax, and performance characteristics — Postgres has `BRIN` and declarative range partitioning, a columnar mart engine wants different storage and clustering. A physical model tuned for Postgres is not optimal or even valid on Snowflake or Synapse. The logical model is shared; the physical model is re-derived for each engine it targets.

</details>

<details><summary><b>68.</b> What is the practical workflow described in the lesson for producing and validating the physical model?</summary>

You write the physical model as Postgres DDL with types, constraints, and declarative partitioning for NAV history, then reverse-engineer that schema in DBeaver and diff the reconstructed model against your logical model. The diff confirms the physical model is a faithful, drift-free implementation of the logical design. It closes the round-trip and is the lesson's hands-on "Do" step.

</details>

<details><summary><b>69.</b> What is a domain (in the relational/data-modeling sense) and how does it relate to data types?</summary>

A domain is the set of permitted values for an attribute — its type plus any constraints, like "a positive `NUMERIC(18,6)`" or "a 12-character `ISIN` matching a checksum pattern". Postgres lets you formalize this with `CREATE DOMAIN`, reusing the same constrained type across many tables. At the physical level the domain becomes a column type plus `CHECK` constraints; conceptually it is the meaning behind the type.

</details>

<details><summary><b>70.</b> How could a `CHECK` constraint help enforce `ISIN` validity at the physical level?</summary>

A `CHECK` constraint can enforce the structural rules of an `ISIN` — exactly 12 characters, first two being an ISO 3166 country code, the rest alphanumeric, and the final digit a Luhn-style check digit over ISO 6166. For example `CHECK (char_length(isin) = 12)` rejects malformed values at write time. Pushing this into the database catches bad reference data at the source rather than discovering it downstream during NAV distribution.

</details>

<details><summary><b>71.</b> Why does the architect care about "the decisions you didn't write down" in a model review?</summary>

Because the riskiest modeling choices — why this is a surrogate key, why this table is denormalized, why NAV history is partitioned this way — are invisible if undocumented, and a reviewer (or a future you, or an auditor) cannot reconstruct the intent. The whole three-level discipline exists to make reasoning reviewable. An undocumented decision is a maintenance landmine, especially in a regulated fund-admin system.

</details>

<details><summary><b>72.</b> A model passes review but production queries are slow on NAV history. Which level is most likely at fault?</summary>

The physical level, since the logical model can be correct while the physical implementation lacks partitioning, the right indexes, or appropriate data types. The first checks are whether `nav_history` is partitioned by `nav_date`, whether queries actually filter on the partition key to allow pruning, and whether foreign-key and filter columns are indexed. Logical correctness and physical performance are independent concerns, which is exactly why the levels are separated.

</details>

<details><summary><b>73.</b> What does it mean that a logical model is "implementation-independent"?</summary>

It means the logical model expresses keys, attributes, relationships, and normal forms without committing to a storage engine, file layout, or index strategy — anyone could implement it on any relational system. Implementation independence is what makes the model a durable communication and review artifact rather than a transcript of one database. The physical model is where independence ends and engine-specific choices begin.

</details>

<details><summary><b>74.</b> How many entities is "too many" at the conceptual level, and how do you tell?</summary>

There is no fixed number, but the signal is that you have started modeling things the business does not name or arguing about attributes and keys — that means you have slid into logical detail. The DMBOK guidance frames the conceptual model as scope and shared vocabulary: a page of the major business things. If stakeholders cannot validate it at a glance, it has too much detail, not too many real entities.

</details>

<details><summary><b>75.</b> Why is "fund" alone insufficient and you typically also need "legal entity" or "umbrella" in a Luxembourg context?</summary>

Luxembourg funds are often umbrella structures (a single legal entity, e.g. a SICAV, containing multiple sub-funds/compartments), so "fund" is ambiguous between the legal wrapper and the sub-fund that strikes a NAV. Modeling the umbrella and sub-fund as related entities captures that one legal entity issues many sub-funds, each with its own share classes and NAVs. Collapsing them loses the structure that drives reporting and ring-fencing of assets.

</details>

<details><summary><b>76.</b> What is the role of a `valid_from`/`valid_to` pair, and is it a logical or physical concern?</summary>

A `valid_from`/`valid_to` pair records the period during which a row's values are correct, enabling temporal/point-in-time queries — it is a logical modeling decision (you are modeling history of an entity) realized with physical date/timestamp columns and constraints. For slowly changing reference data like fund attributes, it lets you answer "what was true as of this date". The columns are physical; the decision to keep history is logical.

</details>

<details><summary><b>77.</b> What is a "weak entity" and how does it relate to IDEF1X identifying relationships?</summary>

A weak entity cannot exist without its parent and its primary key includes the parent's key — a NAV record cannot exist without its share class. In IDEF1X this is exactly an identifying relationship, drawn with a solid line and a rounded-corner (dependent) child box. Recognizing weak entities is what tells you whether to migrate the parent key into the child's primary key.

</details>

<details><summary><b>78.</b> How do you express a one-to-one relationship and when is it appropriate?</summary>

A one-to-one relationship pairs each row of one entity with at most one row of another, physically enforced by a `UNIQUE` `FOREIGN KEY` (or sharing the primary key). It is appropriate to split rarely-used or security-sensitive attributes into a separate table, or to model an optional specialization (e.g. extra attributes only hedged share classes carry). If the two always coexist and are always read together, a one-to-one split may be unnecessary normalization.

</details>

<details><summary><b>79.</b> What is supertype/subtype (generalization) modeling and where does it appear in fund products?</summary>

Supertype/subtype modeling captures "is-a" relationships: a general entity (`security`) with specialized subtypes (`equity`, `bond`, `fund_unit`) that share common attributes but add their own. It appears with heterogeneous fund products where different instrument types share identity and pricing but differ in detail. Physically you implement it as a single table with a type discriminator, a table per subtype, or a shared supertype table with subtype tables linked by the same key.

</details>

<details><summary><b>80.</b> Why is a single huge "wide" table usually the wrong logical model for diverse fund products?</summary>

A wide table forces every product type to carry every other type's columns, leaving most of them null, which obscures which attributes are mandatory for which type and invites data-quality errors. It also typically hides functional dependencies that proper normalization or supertype/subtype modeling would separate. The fix is to model the shared attributes once and the type-specific attributes in their own structures.

</details>

<details><summary><b>81.</b> What does "the partition key must be part of every unique constraint" force you to reconsider about a NAV table's keys?</summary>

It forces you to confirm that `nav_date` (the partition key) is included in the primary/unique key, so a composite like (`share_class_id`, `nav_date`) is required rather than a bare surrogate or `share_class_id` alone. If your logical model assumed a single-column surrogate PK, the physical partitioning decision pushes back and you reconcile the two. It is a concrete case where physical and logical levels must be negotiated, not assumed independent.

</details>

<details><summary><b>82.</b> Why might you NOT partition a table even though it is large?</summary>

Partitioning adds planning overhead and only pays off when queries filter on the partition key (enabling pruning) or when you need partition-level operations like fast archival; a large table queried by arbitrary columns gains little and can even slow down. You also incur the unique-constraint-must-include-partition-key restriction. The decision is driven by the access pattern, so you partition NAV history (date-filtered, archived by date) but not a small dimension table.

</details>

<details><summary><b>83.</b> What is the difference between a "model" and a "schema" in this discipline?</summary>

A model is a deliberately abstracted representation (conceptual, logical, or physical) used for understanding and review; a schema is the concrete catalog of tables, columns, and constraints that exists in a running database. The physical model is the closest to the schema and forward-engineers into it, while the schema reverse-engineers back into a physical model. Keeping the model and schema in sync (no drift) is the whole point of round-tripping.

</details>

<details><summary><b>84.</b> How does naming discipline in the conceptual model pay off later?</summary>

Clear, business-agreed entity names (fund, share class, investor, order, NAV) become the vocabulary for tables, columns, ADRs, and conversations, so consistent naming reduces ambiguity across every downstream artifact. If the conceptual model calls it "share class", the physical table should not surprise readers by calling it `unit_series`. Naming is a governance concern as much as a technical one, especially where multiple teams and regulators read the same model.

</details>

<details><summary><b>85.</b> Why is it dangerous to let the physical model's denormalizations leak back into how people understand the data?</summary>

Because a denormalized physical structure (duplicated `fund_name`, pre-joined reporting table) is a performance artifact, not the source of truth, and treating it as authoritative invites people to update the wrong copy or reason about anomalies as if they were intended. The logical model remains the canonical statement of meaning. This is why denormalizations are documented as departures from the logical baseline, not as the model itself.

</details>

<details><summary><b>86.</b> When reverse-engineering a legacy fund-admin database, what early sign suggests the original design skipped the logical level?</summary>

A telltale sign is business identifiers used directly as primary and foreign keys everywhere — `ISIN`, account numbers, fund codes — with no surrogate keys, so the join graph is welded to mutable business data. You also often see wide tables, repeating-group columns (violating 1NF), and no documented normal forms. These are the failure modes the three-level discipline exists to prevent.

</details>

<details><summary><b>87.</b> What is the value of stating each table's normal form explicitly in the model documentation?</summary>

It tells a reviewer exactly which anomalies are structurally impossible and which redundancies are deliberate, turning "trust me, it's normalized" into a checkable claim. It also surfaces denormalizations as exceptions that must be justified rather than hiding them. The lesson's Done-when bar is naming the normal form of each table and where you denormalized and why.

</details>

<details><summary><b>88.</b> Why does the lesson tie the three-level discipline to "every review you'll run"?</summary>

Because the conceptual/logical/physical chain is the architect's standard lens: you review whether the conceptual model matches the business, whether the logical model's keys and normal forms are sound, and whether the physical model implements them faithfully and performantly. Each review level checks a different class of error, and a model that traces cleanly across all three is the reviewable artifact governance expects. Without the chain, reviews degrade into ad-hoc opinion.

</details>

<details><summary><b>89.</b> How would you justify a surrogate key for a `fund` table in one written sentence?</summary>

"Funds are identified externally by codes and `ISIN`s at the share-class level that can change through corporate actions, so `fund` uses an internal stable surrogate `fund_id` as its primary key, with external identifiers kept as `UNIQUE` business attributes." That sentence states the instability of natural keys, the chosen surrogate, and where the natural keys live. Being able to write exactly this for every table is the lesson's key-justification bar.

</details>

<details><summary><b>90.</b> What is the risk of choosing `nav_date` partitions that are too small (e.g. daily)?</summary>

Daily partitions on a long-lived NAV history can create thousands of partitions, inflating planning time, catalog size, and per-partition index overhead, sometimes hurting more than helping. Conversely, partitions too large (e.g. all-time) defeat pruning and archival. Monthly or yearly partitions are the usual balance for NAV history, chosen to match query and retention patterns.

</details>

<details><summary><b>91.</b> Why is the physical-level choice of `TIMESTAMP WITH TIME ZONE` vs `DATE` for valuation points a meaningful decision?</summary>

A NAV is struck for a valuation *date* (a business day), so `DATE` is usually correct and avoids spurious time-zone arithmetic, whereas event timestamps like order receipt need `TIMESTAMPTZ` to be unambiguous across time zones. Using a timestamp where a date suffices can break range partitioning boundaries and comparisons; using a date where a true instant is needed loses information. Matching the type to the real temporal semantics is a physical-design responsibility.

</details>

<details><summary><b>92.</b> What does "round-trip engineering" buy a regulated organization specifically?</summary>

It gives an auditable, current model that provably matches the deployed database, so questions like "why is NAV history partitioned this way?" can be answered from a reviewed artifact rather than tribal memory. Drift detection means a column added in production without a model change is caught. For a fund administrator under regimes like DORA and UCITS reporting obligations, a trustworthy model is part of demonstrable IT governance.

</details>

<details><summary><b>93.</b> How does normalization interact with the decision to use surrogate keys?</summary>

Normalization is about functional dependencies and is independent of whether keys are natural or surrogate — a fully normalized schema can use surrogates throughout. Surrogates do not "fix" a normalization problem; a table with a surrogate PK can still hide a transitive dependency among its non-key columns. You normalize based on dependencies first, then choose key representation for each resulting table.

</details>

<details><summary><b>94.</b> What is the difference between a candidate key and a superkey?</summary>

A superkey is any set of attributes that uniquely identifies a row, possibly with redundant extra columns; a candidate key is a *minimal* superkey, with no removable attribute. Every candidate key is a superkey, but not every superkey is minimal. Normal-form definitions (especially BCNF's "X must be a superkey") rely on this distinction, so getting it right matters when you defend a table's form.

</details>

<details><summary><b>95.</b> When would deliberate denormalization into a reporting table be the right call for fund data?</summary>

When NAV/holdings reporting queries repeatedly join the same normalized tables under tight SLA, pre-joining them into a denormalized, periodically-refreshed reporting structure can meet performance needs the normalized model cannot. The key is that it is an additional, documented, derived structure refreshed from the normalized source of truth — not a replacement for it. You record the read pattern that justifies it and the refresh mechanism that keeps it consistent.

</details>

<details><summary><b>96.</b> What is the first thing to check when a `FOREIGN KEY` creation fails with a violation error?</summary>

Check that every value in the referencing column already exists in the referenced table's key column (and that the referenced column is itself a primary key or `UNIQUE`), because Postgres validates existing rows when adding the constraint. Orphan rows — a child pointing at a parent that was deleted or never existed — are the usual cause. You either clean the orphans or correct the references before the constraint can be added.

</details>

<details><summary><b>97.</b> Why must the referenced column of a `FOREIGN KEY` be a primary key or have a unique constraint?</summary>

Because a foreign key must point at a uniquely identifiable parent row; if the target column allowed duplicates, "the referenced row" would be ambiguous and referential integrity could not be enforced. Postgres therefore requires the referenced columns to be backed by a primary key or unique constraint. This is why you reference `share_class_id` (the surrogate PK) rather than a non-unique business attribute.

</details>

<details><summary><b>98.</b> How does the three-level discipline help prevent the "ISIN-as-primary-key" failure mode described in the lesson's Why?</summary>

The conceptual level names `ISIN` as a property of a share class, not the share class itself; the logical level identifies it as a candidate/natural key and forces an explicit, written decision about whether it should be the primary key; that decision, made with stability in mind, leads to a surrogate PK with `ISIN` as an attribute. Each level provides a checkpoint where the bad choice would be caught. Skipping the logical key analysis is precisely how the failure slips through.

</details>

<details><summary><b>99.</b> After a corporate action changes a share class's `ISIN`, what should happen in a well-modeled database versus an `ISIN`-keyed one?</summary>

In a well-modeled database the `ISIN` is just an attribute, so you update one column on one `share_class` row and every foreign-key reference (orders, NAV history, holdings) remains valid because they point at the unchanged surrogate `share_class_id`. In an `ISIN`-keyed database you must cascade the change through every referencing table, risking missed references and downtime. This single scenario is the strongest practical argument for the surrogate-key discipline.

</details>

<details><summary><b>100.</b> What is the final self-review test the lesson recommends and why wait a week?</summary>

After a week you re-read the conceptual → logical → physical chain against one question: could a colleague implement it from the logical model alone? Waiting a week removes the author's short-term memory of unstated assumptions, so gaps that were "obvious" at the time now stand out as genuinely missing. It is a cheap way to simulate the outside reviewer the model must ultimately satisfy.

</details>


## Phase 1 · 8.2.4 Dimensional modeling — 100 self-test questions

<details><summary><b>1.</b> What is dimensional modeling and what problem does it solve?</summary>

Dimensional modeling is a design technique that structures data into fact tables (measurements of a business process) and dimension tables (the descriptive context for those measurements), optimized for query understandability and analytical performance rather than transactional write efficiency. It solves the problem that a normalized OLTP schema is hard for analysts to navigate and slow to aggregate, by deliberately denormalizing context into wide, human-readable dimensions. In a fund mart you would model NAV measurements as a fact and fund, share class, investor, and date as dimensions.

</details>

<details><summary><b>2.</b> What is the "grain" of a fact table?</summary>

The grain is the precise definition of what a single row in the fact table represents — the level of detail captured by one measurement event. Declaring the grain in one plain sentence ("one row per fund per share class per valuation date") fixes the meaning of every subsequent column choice. Kimball's first rule is that you declare the grain before you list a single dimension or fact column, because every other modeling decision follows from it.

</details>

<details><summary><b>3.</b> Why does Kimball insist you declare the grain first, before anything else?</summary>

Because the grain determines which dimensions can attach (only dimensions consistent with that level of detail belong) and what each fact column can mean, so deciding it first prevents incoherent designs. If you pick columns first and infer the grain later, you typically end up with a mixed-grain table where some rows are daily and some are monthly, which silently breaks aggregations. Declaring "one row per X per Y per date" up front makes the table reviewable and the SUMs trustworthy.

</details>

<details><summary><b>4.</b> Give the grain of a NAV fact table as a one-sentence declaration.</summary>

"One row per fund, per share class, per valuation date." This says the table captures the official net asset value snapshot at the most atomic reporting level a fund administrator strikes prices at. Any measure on that row — NAV per share, total net assets, shares outstanding — must be true at exactly that fund/share-class/date intersection, and nothing finer or coarser may sneak in.

</details>

<details><summary><b>5.</b> What is the difference between a fact table and a dimension table?</summary>

A fact table stores the numeric measurements of a business process (the "verbs" — amounts, counts, prices) plus foreign keys to dimensions, and it is typically long and narrow with many rows. A dimension table stores the descriptive textual context (the "nouns" — who, what, where, which) used to filter and group, and it is typically short and wide with many attribute columns. Facts are what you aggregate; dimensions are what you slice and label by.

</details>

<details><summary><b>6.</b> What are the three fundamental fact table types in Kimball's taxonomy?</summary>

Transaction fact tables, periodic snapshot fact tables, and accumulating snapshot fact tables. A transaction fact records one row per discrete event as it happens; a periodic snapshot records one row per entity per regular time interval; an accumulating snapshot records one row per workflow instance and updates it as the instance moves through milestones. Every fact table you design should be one of these three — mixing them is a design smell.

</details>

<details><summary><b>7.</b> What is a transaction fact table?</summary>

A transaction fact table has one row for each measurement event at the moment it occurs, such as a single subscription order or a single fee charge. It is the most atomic and flexible grain, capturing the full detail of "something happened" and supporting the widest range of analyses. Its measures are usually fully additive across all dimensions, and rows are inserted but rarely updated.

</details>

<details><summary><b>8.</b> What is a periodic snapshot fact table?</summary>

A periodic snapshot fact table captures the state of a process at regular, predictable intervals — one row per entity per period — even when nothing changed in that period. It answers "what was the state at end of day/month?" rather than "what events occurred?". A daily NAV table is the canonical example: one row per fund/share class for every valuation date, regardless of whether the price moved.

</details>

<details><summary><b>9.</b> Why is a daily NAV table a periodic snapshot rather than a transaction fact?</summary>

Because NAV is not an event that occurs at a random moment — it is a measured state of the fund struck on a regular valuation cadence, so you record one row per fund/share class per valuation date by design. You want a row to exist for every valuation date so a balance is always available for any reporting date, which is the defining behavior of a snapshot, not a transaction log. The measures (NAV per share, total net assets) are point-in-time balances, the hallmark of snapshot facts.

</details>

<details><summary><b>10.</b> What is an accumulating snapshot fact table?</summary>

An accumulating snapshot has one row per instance of a multi-step workflow, and that single row is repeatedly updated as the instance passes each milestone, with multiple date foreign keys (one per milestone) and lag/duration measures. It is built for pipeline processes with a definite beginning and end. A fund subscription lifecycle — order received, traded, settled, units allocated — fits this pattern, with each date column filled in as the order progresses.

</details>

<details><summary><b>11.</b> A measure is "additive". What does that mean and why does it matter?</summary>

An additive measure can be summed correctly across every dimension in the fact table, including time — for example, fee amounts can be added across funds, investors, and months. It matters because additivity is what lets a BI tool roll a fact up along any combination of dimensions without producing nonsense. The richest, easiest-to-use facts are fully additive, which is one reason transaction-grain amounts are so valuable.

</details>

<details><summary><b>12.</b> What is a semi-additive measure? Give a fund example.</summary>

A semi-additive measure can be summed across some dimensions but not across time, because it represents a balance or level rather than a flow. Total net assets and shares outstanding in a NAV snapshot are semi-additive: you can add net assets across share classes on a given date, but adding a fund's net assets across 30 days is meaningless double counting. The correct time aggregation for a balance is usually an average or an end-of-period value, not a SUM.

</details>

<details><summary><b>13.</b> What is a non-additive measure and how do you handle it in a fact table?</summary>

A non-additive measure cannot be summed across any dimension, including across rows, because it is a ratio, percentage, or unit rate — NAV per share and expense ratio are examples. The handling rule is to store the fully additive components (e.g. total net assets and shares outstanding) as facts and let the BI layer compute the ratio after aggregation, rather than storing or summing the ratio directly. Summing NAV-per-share across funds is a classic error this rule prevents.

</details>

<details><summary><b>14.</b> Why is summing "NAV per share" across funds wrong, and what should you store instead?</summary>

NAV per share is a ratio (total net assets divided by shares outstanding), and ratios are non-additive — adding per-share prices across funds produces a number with no meaning. You should store the additive numerator (total net assets) and additive denominator (shares outstanding) as facts, then divide the aggregated numerator by the aggregated denominator at query time. This "aggregate then divide" discipline keeps the ratio correct at every grain.

</details>

<details><summary><b>15.</b> What is a conformed dimension?</summary>

A conformed dimension is a dimension table that means exactly the same thing — same keys, same attributes, same values — when shared across multiple fact tables and business processes. A conformed `dim_fund` lets you join NAV facts, fee facts, and order facts and trust that "Fund A" is the identical entity in all of them. Conformance is what makes a collection of marts behave like one integrated warehouse rather than disconnected silos.

</details>

<details><summary><b>16.</b> What does it mean for two dimensions to be conformed, technically?</summary>

Two dimensions conform when they are either identical, or one is a strict subset (the same keys and a shared subset of attributes at a rolled-up grain) of the other. A monthly summary mart can use a month-grain date dimension that conforms to the daily date dimension as long as the shared attributes match exactly. The test is that a label or attribute used to constrain one fact yields the same result when used against another.

</details>

<details><summary><b>17.</b> What is the enterprise bus matrix?</summary>

The bus matrix is a grid with business processes as rows and conformed dimensions as columns, where each cell is marked when that dimension applies to that process's fact table. It is the master planning and communication artifact of a Kimball warehouse, showing at a glance which marts share which dimensions and in what order to build them. For a fund administrator the rows would be orders, NAV calculation, fee accrual, and transfer agency, with columns for fund, share class, investor, and date.

</details>

<details><summary><b>18.</b> How do you read a row versus a column of the bus matrix?</summary>

A row shows all the conformed dimensions that attach to one business process — effectively the dimensional footprint of that fact table. A column shows every business process that uses a given conformed dimension — revealing where that dimension must be reused identically. Columns with many marks are your highest-value conformed dimensions, because building them once correctly pays off across many marts.

</details>

<details><summary><b>19.</b> For a fund administrator, name the four processes and four conformed dimensions you'd put on the bus matrix.</summary>

Processes (rows): subscription/redemption orders, NAV calculation, fee accrual, and transfer-agency activity. Conformed dimensions (columns): fund, share class, investor, and date. Each process gets its own fact table at its own grain, but all four reference the same four shared dimensions so the marts join cleanly — for example, fee facts and NAV facts both hang off the identical `dim_fund` and `dim_date`.

</details>

<details><summary><b>20.</b> Why is the bus matrix considered an architecture artifact and not just documentation?</summary>

Because it commits the team to a shared set of conformed dimensions before any mart is built, it enforces integration architecturally rather than hoping silos align later. It also sequences delivery: you can build one process's mart at a time (incremental, agile) while guaranteeing each new mart plugs into the same bus of dimensions. In a regulated shop it doubles as a governance map showing which reference data must be mastered once and reused everywhere.

</details>

<details><summary><b>21.</b> What is a slowly changing dimension (SCD)?</summary>

An SCD is a dimension whose descriptive attributes change occasionally over time — like a fund's domicile, name, or investment manager — and the term names the strategies for handling those changes in the dimension table. The core question is whether to overwrite history, preserve it, or something in between. Kimball numbers the standard responses (Type 0 through Type 7), with Types 1, 2, and 3 being the most common.

</details>

<details><summary><b>22.</b> Describe an SCD Type 1 change.</summary>

Type 1 overwrites the old attribute value with the new one in place, keeping no history — the dimension row simply reflects the current truth. It is appropriate for corrections (a misspelled fund name) or attributes where history genuinely does not matter. The gotcha is that any prior report rerun will now show the new value against old facts, because the past version is gone forever.

</details>

<details><summary><b>23.</b> Describe an SCD Type 2 change and the columns it requires.</summary>

Type 2 preserves full history by inserting a new dimension row each time a tracked attribute changes, so the entity has multiple rows over time distinguished by a surrogate key. It requires bookkeeping columns: a `valid_from` date, a `valid_to` date (or null/high-date for the open row), and usually a boolean `is_current` flag. Facts join to whichever row was effective at the fact's date, giving point-in-time-correct context.

</details>

<details><summary><b>24.</b> Describe an SCD Type 3 change.</summary>

Type 3 adds an extra column to hold a single prior value — for example `current_domicile` plus `previous_domicile` — so you can report along either the new or the old categorization without a full history. It is used when only the last change matters and you need to compare "as-is" versus "as-was" side by side. It cannot track an unlimited number of changes the way Type 2 can; it remembers only one prior state.

</details>

<details><summary><b>25.</b> What is an SCD Type 6 and where does its name come from?</summary>

Type 6 is a hybrid combining Types 1, 2, and 3 (1 + 2 + 3 = 6, hence the name), giving you Type 2 history rows plus a Type 1 "current" attribute column on every row, so you can report point-in-time-correct or always-current from the same dimension. Each historical row carries both the value that was effective then and a column overwritten with the latest value. It lets one query pick "as-was" or "as-is" simply by choosing which column to group on.

</details>

<details><summary><b>26.</b> Which SCD type is the default for fund and security reference data, and why?</summary>

SCD Type 2 is the default for fund and security reference data, because regulated reporting must be point-in-time correct: a NAV struck last March must be reportable against the fund's attributes as they stood last March, not as they stand today. Type 2's history rows with `valid_from`/`valid_to` make "as-of" reporting possible, which audit and regulators expect. Overwriting (Type 1) would silently rewrite history and break reconciliations.

</details>

<details><summary><b>27.</b> What is the difference between a natural (business) key and a surrogate key in a dimension?</summary>

A natural key is the identifier the business uses (an ISIN for a share class, an LEI for a legal entity), while a surrogate key is a meaningless integer the warehouse generates as the dimension's primary key. Facts join on the surrogate key, not the natural key. The surrogate is essential for SCD Type 2 because the same natural key (ISIN) appears on multiple history rows, so only an independent surrogate can uniquely identify each version.

</details>

<details><summary><b>28.</b> Why can't you use the ISIN directly as the primary key of an SCD2 fund-share-class dimension?</summary>

Because under SCD Type 2 the same ISIN appears on several rows — one per version of the share class over time — so the ISIN is no longer unique and cannot be the primary key. You instead generate a surrogate integer key that is unique per version, store the ISIN as a natural-key attribute, and have facts reference the surrogate. The ISIN remains indexed so you can look up the right version for a given date.

</details>

<details><summary><b>29.</b> In an SCD2 dimension, what role do `valid_from` and `valid_to` play?</summary>

They define the effective-date window during which that particular version of the row was the current truth: the row applies to any business date `>= valid_from` and `< valid_to` (or `<= valid_to` depending on convention — be consistent). They are the mechanism for point-in-time joins: given a fact date, you select the dimension row whose window contains it. The currently active row typically has `valid_to` set to null or a far-future sentinel like `9999-12-31`.

</details>

<details><summary><b>30.</b> What is the `is_current` flag in an SCD2 dimension and why keep it if you already have `valid_to`?</summary>

`is_current` is a boolean marking the one active version of each natural key, true only for the row whose effective window is still open. It is redundant with `valid_to` but kept as a convenience and performance shortcut: queries that only need today's value filter `WHERE is_current = true` instead of comparing dates against a sentinel. The gotcha is that the flag and the dates must be maintained atomically so they never disagree.

</details>

<details><summary><b>31.</b> Write the join logic for a point-in-time query against an SCD2 dimension.</summary>

You join the fact to the dimension on the natural key AND a date-band predicate, for example `ON f.isin = d.isin AND f.valuation_date >= d.valid_from AND f.valuation_date < d.valid_to`. This picks exactly the dimension version that was effective on the fact's date. For "as-of today" reporting you instead join on the surrogate key the fact already carries, or filter the dimension to `is_current = true`.

</details>

<details><summary><b>32.</b> A point-in-time query returns two dimension rows for one fact. What went wrong?</summary>

The SCD2 effective-date windows overlap — two versions of the same natural key both claim the fact's date — which usually means a load bug left `valid_to` of the old row not closed when the new row opened. The fix is to ensure that when a new version is inserted, the prior row's `valid_to` is set to the new row's `valid_from` so the bands are contiguous and non-overlapping. Half-open intervals (`>= valid_from AND < valid_to`) avoid the boundary double-match.

</details>

<details><summary><b>33.</b> What is a junk dimension?</summary>

A junk dimension is a single dimension table that consolidates several low-cardinality flags and indicators (yes/no flags, small codes) that would otherwise clutter the fact table or spawn many tiny dimensions. It holds one row for each observed combination of those flag values, and the fact carries one foreign key to it. For example, an order fact's "is_first_subscription", "is_in_specie", and "channel" flags can be folded into one `dim_order_flags`.

</details>

<details><summary><b>34.</b> Why use a junk dimension instead of leaving the flags on the fact table?</summary>

Because scattering many narrow flag columns across a huge fact table wastes width and makes the model noisy, while a junk dimension keeps the fact narrow (one FK) and centralizes the flags where they can carry descriptive labels. It also lets you enumerate and constrain on combinations cleanly. You store only the combinations that actually occur, so a junk dimension of a handful of flags stays small.

</details>

<details><summary><b>35.</b> What is a degenerate dimension?</summary>

A degenerate dimension is a dimension key that lives directly in the fact table with no corresponding dimension table, because it has no descriptive attributes of its own — typically an operational transaction identifier. An order number or a SWIFT message reference on an order fact is a degenerate dimension: useful for grouping line items of the same transaction or for drill-back, but there is nothing else to describe about it. It is left as a column on the fact, not modeled as a separate table.

</details>

<details><summary><b>36.</b> Where does an order number belong in a dimensional model, and what is it called?</summary>

It belongs as a column directly on the fact table and is called a degenerate dimension, because the order number identifies a transaction but has no attributes worth putting in a separate dimension table. It still functions as a dimension — you can group all fact rows sharing one order number — but building a one-column `dim_order_number` table would add a pointless join. Keeping it inline preserves the operational drill-back without overhead.

</details>

<details><summary><b>37.</b> How do junk and degenerate dimensions differ?</summary>

A junk dimension is a real, separate table that bundles several unrelated low-cardinality flags/indicators, referenced from the fact by a foreign key. A degenerate dimension is a single operational identifier (like an order number) stored inline on the fact with no separate table because it has no descriptive attributes. One reduces fact-table width by collecting flags into a table; the other accepts a key on the fact precisely because there is nothing to collect.

</details>

<details><summary><b>38.</b> What is the difference between a star schema and a snowflake schema?</summary>

In a star schema each dimension is a single flat, denormalized table joined directly to the fact, producing the characteristic star shape. In a snowflake schema, dimensions are normalized into multiple related tables (a dimension referencing sub-dimension lookup tables), so a single logical dimension spans several joined tables. The star trades storage redundancy for query simplicity and speed; the snowflake trades those away for normalization.

</details>

<details><summary><b>39.</b> Why does Kimball consider snowflaking usually a modeling smell in marts?</summary>

Because snowflaking re-normalizes dimensions back toward an OLTP shape, adding joins that make the model harder for users and BI tools to navigate and often slower, for a storage saving that is negligible against the fact table's size. The dimensional method deliberately denormalizes dimensions for usability and performance, so snowflaking usually signals someone optimizing the wrong thing. The space "wasted" by a flat dimension is trivial compared with the multi-billion-row fact.

</details>

<details><summary><b>40.</b> When is a snowflaked or outrigger dimension actually justified?</summary>

It can be justified for a genuinely shared sub-dimension referenced from another dimension (an "outrigger"), such as a date attribute inside a dimension, or for a very large, sparsely used dimension where normalization meaningfully cuts size or eases maintenance. Even then Kimball treats it as an exception requiring justification, not the default. The bar is: does the join actually buy you integration or material savings, or are you just normalizing out of habit?

</details>

<details><summary><b>41.</b> What is the financial-services "accounts" dimensional pattern Kimball describes?</summary>

In financial services, the account is the central entity many processes hang off, so it becomes a core conformed dimension shared across products and transactions, often with SCD2 history because account attributes change. In a fund context the analogous conformed anchors are the fund, the share class, and the investor account, each modeled as a slowly changing dimension. Transactions (orders, fees, holdings) become facts referencing these account-like dimensions.

</details>

<details><summary><b>42.</b> What does "heterogeneous products" mean in dimensional modeling and why is it tricky?</summary>

Heterogeneous products are different product lines (e.g. equity funds, money-market funds, derivatives) that share some common attributes and measures but each have many product-specific ones, so a single flat fact/dimension would be either too generic or full of nulls. Kimball's solution is a core fact and core dimension holding the common attributes for all products, plus custom fact/dimension extensions per product line for the type-specific detail. This lets you query across all products generically or drill into one line's specifics.

</details>

<details><summary><b>43.</b> What is a "fee fact" and why model fees as their own fact table?</summary>

A fee fact captures fee/charge measurements — management fees, performance fees, distribution fees — typically at transaction or accrual grain, with the amount as an additive measure and foreign keys to fund, share class, investor, and date. Fees are a distinct business process from NAV calculation, so they get their own fact table at their own grain rather than being crammed into the NAV snapshot. Sharing conformed dimensions then lets you join fee facts to NAV facts to compute, say, fees as basis points of net assets.

</details>

<details><summary><b>44.</b> A fee-accrual process and a NAV-calculation process share the same dimensions but have different grains. How do you model them?</summary>

As two separate fact tables, each with its own declared grain (fee accrual perhaps one row per fund/share class/fee-type/accrual date; NAV one row per fund/share class/valuation date), both referencing the same conformed `dim_fund`, `dim_share_class`, and `dim_date`. You never force two different grains into one table. The conformed dimensions are exactly what let you join the two marts when you need fees-over-assets ratios.

</details>

<details><summary><b>45.</b> What does "drill across" mean and what makes it possible?</summary>

Drill-across means querying two or more fact tables (often at different grains) and combining their results on shared dimension attributes — for instance, total net assets from the NAV mart and total fees from the fee mart, grouped by fund and month. It is made possible only by conformed dimensions: each fact is aggregated separately to a common dimensional grain, then the result sets are joined on the conformed labels. You do not join the two fact tables directly; you join their aggregates.

</details>

<details><summary><b>46.</b> Why should you avoid joining two fact tables directly to each other?</summary>

Because fact tables are at different grains and have many rows, a direct fact-to-fact join multiplies rows and produces wrong, inflated measures (a "fan trap" or many-to-many explosion). The correct approach is to aggregate each fact to a common dimensional level independently and then join those aggregates on conformed dimension keys (drill-across). This is a frequent cause of double-counted totals in naive marts.

</details>

<details><summary><b>47.</b> What is a "factless fact table" and give a fund-administration example?</summary>

A factless fact table has no numeric measures; it records that an event or relationship occurred, represented purely by its foreign keys, and you analyze it by counting rows. An example is an eligibility or coverage table recording which share classes are registered for distribution in which countries on which dates — there's no amount, but counting rows answers "how many classes are registered in Luxembourg today?". Event-tracking and coverage scenarios are the two classic uses.

</details>

<details><summary><b>48.</b> What is the role of the date dimension and why is it almost always conformed?</summary>

The date dimension provides rich calendar attributes (day, month, quarter, fiscal period, business-day flag, holiday) so queries can filter and group by meaningful time concepts without date arithmetic in SQL. It is conformed across virtually every process because almost every fact references time, making it the most reused column on the bus matrix. It is a textbook dimension you pre-populate with one row per calendar day rather than deriving on the fly.

</details>

<details><summary><b>49.</b> What is an additive fact's relationship to the "rule" that you should always store the lowest practical grain?</summary>

Storing the lowest (most atomic) grain keeps facts maximally additive and re-aggregatable, because you can always sum atomic rows up to any summary level the business asks for, but you can never split a pre-aggregated row back down. Atomic grain therefore future-proofs the mart against new questions. The cost is more rows, which modern columnar engines like DuckDB handle well, so the bias is toward atomic detail.

</details>

<details><summary><b>50.</b> In dbt + DuckDB, how would you typically materialize a star schema mart's dimensions and facts?</summary>

You write each dimension and fact as a dbt model (a `SELECT` in a `.sql` file) and materialize them as tables via `{{ config(materialized='table') }}` or in `dbt_project.yml`, with staging models feeding dimension and fact models. dbt manages the build order through `ref()` dependencies, so dimensions build before the facts that reference them. DuckDB executes the SQL as the local analytical engine, giving you a versioned, testable star without a server.

</details>

<details><summary><b>51.</b> How would you implement SCD2 logic in dbt?</summary>

dbt provides snapshots: you define a snapshot block with a `unique_key`, a strategy (`timestamp` or `check`), and the columns to watch, and `dbt snapshot` maintains `dbt_valid_from`/`dbt_valid_to` rows automatically on each run. Alternatively you hand-write the SCD2 logic in an incremental model that closes the prior row and inserts a new one when watched attributes change. The snapshot approach is the idiomatic, less error-prone route for fund reference data.

</details>

<details><summary><b>52.</b> What columns does a dbt snapshot add to implement SCD2?</summary>

A dbt snapshot adds `dbt_valid_from` and `dbt_valid_to` (the effective-date window, with `dbt_valid_to` null on the current row), `dbt_scd_id` (a unique hash key per version), and `dbt_updated_at`. These give you the surrogate version key and effective dating that point-in-time joins need. You then join facts to the snapshot on the natural key with a `dbt_valid_from`/`dbt_valid_to` band predicate to get as-of-date attributes.

</details>

<details><summary><b>53.</b> An auditor asks for the NAV report "as it would have read on 2024-03-31, with fund attributes as of that date." How does your model satisfy this?</summary>

You query the NAV periodic-snapshot fact filtered to `valuation_date = '2024-03-31'` and join it to the SCD2 fund dimension on the natural key with `'2024-03-31' >= valid_from AND '2024-03-31' < valid_to`, returning the fund attributes effective on that date rather than today's. Because the snapshot fact preserves the historical NAV and the SCD2 dimension preserves the historical attributes, the report reconstructs point-in-time truth. This is exactly why fund reference data is SCD2.

</details>

<details><summary><b>54.</b> What is a "role-playing dimension" and give a fund-flow example?</summary>

A role-playing dimension is a single physical dimension referenced multiple times from one fact, each reference playing a different semantic role, usually surfaced through SQL views or aliases. The date dimension is the classic case: a subscription order fact may reference the same `dim_date` as order date, trade date, and settlement date simultaneously. You alias the dimension once per role so each foreign key resolves to clearly named columns.

</details>

<details><summary><b>55.</b> What is a "mini-dimension" and when do you split one off?</summary>

A mini-dimension extracts a cluster of rapidly changing or browse-heavy attributes out of a large dimension into its own small dimension, so frequent changes don't bloat the main dimension with SCD2 rows. You split one off when an attribute group changes so often that Type 2 history would explode the parent dimension's row count. The fact then carries a foreign key to both the base dimension and the mini-dimension.

</details>

<details><summary><b>56.</b> What is a "bridge table" and what problem does it solve?</summary>

A bridge table resolves a many-to-many relationship between a fact and a dimension, or within a dimension's hierarchy, by sitting between them and often carrying a weighting/allocation factor. In funds, a multi-manager fund or a portfolio holding multiple instruments needs a bridge so a single fact can fairly allocate across several dimension members. The weighting factor lets you split a measure without double-counting when fanning out the join.

</details>

<details><summary><b>57.</b> Why are many-to-many relationships between facts and dimensions dangerous if modeled naively?</summary>

Because a plain join across a many-to-many relationship multiplies fact rows by the number of related dimension members, inflating any SUM and producing double-counted totals like overstated AUM. A bridge table with allocation weights, applied carefully, lets you either allocate the measure proportionally or report it as an impact without overstating. Recognizing the many-to-many before joining is what prevents the double count.

</details>

<details><summary><b>58.</b> The lesson warns that "ungrained fact tables are where double-counted AUM reports come from." Explain the mechanism.</summary>

If a fact table's grain is undeclared or mixed, rows at different levels of detail coexist (say, both per-share-class and per-fund net-asset rows), so a naive `SUM(total_net_assets)` adds the fund-level rows and the share-class rows that compose them, counting the same assets twice. A single, explicitly declared grain guarantees every row is at the same level so SUMs are exact. The discipline of one-sentence grain declaration is precisely the guard against inflated AUM.

</details>

<details><summary><b>59.</b> How do you decide whether an attribute belongs in a dimension or as a fact?</summary>

Ask whether you primarily filter/group by it (dimension attribute) or aggregate it numerically (fact measure); descriptive, low-churn, used-as-a-label values go in dimensions, while additive numeric measurements go in facts. A value that is numeric but used mainly to constrain (like a credit rating bucket) often becomes a dimension attribute despite being a number. When in doubt, the "do I SUM it or GROUP BY it?" test usually decides.

</details>

<details><summary><b>60.</b> What is a "degenerate" versus "junk" decision for a cluster of order-related flags plus the order number?</summary>

The order number, being a bare identifier with no attributes, stays on the fact as a degenerate dimension; the cluster of small order flags (channel, in-specie, first-subscription) gets folded into a junk dimension referenced by one foreign key. So one order fact row holds the order number inline plus a single junk-dimension key. This keeps the fact narrow while preserving both the operational identifier and the flag combinations.

</details>

<details><summary><b>61.</b> Why should surrogate keys be integers rather than reusing natural business keys?</summary>

Integer surrogate keys are compact, fast to join and index, insulate the warehouse from changes or reformatting of business keys, and crucially allow SCD2 versioning where one natural key maps to many rows. They also provide a stable home for special rows like an "unknown"/"not applicable" member. Reusing a natural key (ISIN, LEI) as the PK breaks the moment you need history or the source reissues the identifier.

</details>

<details><summary><b>62.</b> How do you handle a fact whose dimension value is missing or not yet known at load time?</summary>

You point the fact's foreign key at a special dimension row reserved for "unknown" or "not applicable" (commonly a surrogate key like `-1`) rather than leaving the key null. This keeps the fact-to-dimension join an inner join with no row loss and gives reports an explicit "Unknown" bucket instead of silently dropping facts. Null foreign keys are avoided because they break joins and hide data-quality problems.

</details>

<details><summary><b>63.</b> What is the "centipede fact table" anti-pattern?</summary>

A centipede fact table has too many foreign keys (dozens of "legs"), usually because the designer made a separate dimension for every low-cardinality code instead of grouping flags into junk dimensions or using a proper hierarchy. It signals over-normalized dimensional thinking. The fix is to consolidate correlated low-cardinality attributes into junk dimensions and reconsider whether some "dimensions" are really just attributes.

</details>

<details><summary><b>64.</b> What is the difference between a "transaction" grain and a "snapshot" grain when modeling investor holdings?</summary>

A transaction grain records each subscription/redemption event (units bought or sold) as a row, capturing flows; a snapshot grain records the holding balance per investor/share class at each period end, capturing levels. Flows are fully additive across time; balances are semi-additive (not summable across time). You often build both: a transaction fact for activity analysis and a periodic snapshot for position reporting.

</details>

<details><summary><b>65.</b> Why might you build both a transaction fact and a periodic snapshot for the same process?</summary>

Because they answer different questions cheaply: the transaction fact preserves every flow for detailed activity and audit analysis, while the periodic snapshot precomputes the running balance so position-as-of-date queries don't have to sum the entire transaction history each time. Recomputing balances from transactions for every report is expensive at scale, so the snapshot is a performance and clarity convenience. Kimball calls this a "complementary" snapshot.

</details>

<details><summary><b>66.</b> How do conformed dimensions support incremental, agile warehouse delivery?</summary>

Because the bus matrix fixes conformed dimensions up front, each business process's mart can be built and shipped independently knowing it will plug into the same shared dimensions, so you deliver value one mart at a time without a big-bang build. Later marts reuse the already-built dimensions rather than reinventing them. This is the architectural reason Kimball pairs the bus matrix with incremental delivery.

</details>

<details><summary><b>67.</b> A new fee-mart and the existing NAV-mart both define their own `dim_fund` slightly differently. What is the risk and the fix?</summary>

The risk is non-conformance: "Fund A" might carry different attributes or keys in each mart, so drill-across results disagree and reconciliations fail — exactly the silo problem dimensional modeling exists to prevent. The fix is to build a single conformed `dim_fund` (one definition, one set of surrogate keys) and have both facts reference it. Governance over conformed dimensions is what keeps the marts integrated.

</details>

<details><summary><b>68.</b> What is the practical difference between "as-was" and "as-is" reporting, and which SCD type gives you both at once?</summary>

"As-was" reports facts against the dimension attributes effective at the time of the fact (historical truth), while "as-is" reports the same facts against today's attributes (current restated view). SCD Type 6 (and Type 2 augmented with a current-value column) provides both from a single dimension: group by the historical column for as-was, or the overwritten current column for as-is. Regulators usually want as-was; management dashboards often want as-is.

</details>

<details><summary><b>69.</b> Why might management prefer "as-is" reporting while regulators require "as-was"?</summary>

Management often wants to compare history under today's structure (e.g. current fund groupings) to spot trends consistently, which is as-is restatement. Regulators and auditors require the report to reflect the world as it actually stood at the reporting date — the fund's real domicile, name, and manager then — which is as-was, point-in-time-correct reporting. Supporting both from one SCD2/Type-6 dimension avoids maintaining two models.

</details>

<details><summary><b>70.</b> In a fee fact, why is the fee amount additive but a fee rate (in basis points) not?</summary>

The fee amount is a currency measurement of an actual charge, so it sums correctly across funds, investors, and time — it is fully additive. The fee rate in basis points is a ratio (fee relative to assets), and ratios are non-additive: averaging or summing rates across funds is meaningless. You store the amount as a fact and, if you need an overall rate, divide the summed fees by the summed assets at query time.

</details>

<details><summary><b>71.</b> How would you compute "fees as basis points of average net assets" across the NAV and fee marts?</summary>

Aggregate total fees from the fee fact and average net assets from the NAV snapshot fact independently to a common grain (say fund and month), join the two aggregates on the conformed fund and date dimensions (drill-across), then divide summed fees by average net assets and scale to basis points. You never join the two fact tables row-to-row. The conformed dimensions are what make the aligned join correct.

</details>

<details><summary><b>72.</b> What is the danger of computing an average from a periodic snapshot's semi-additive measure incorrectly?</summary>

If you naively SUM a balance (like net assets) across time and divide by the count, or worse just SUM it, you double-count assets that persist across snapshots and overstate the figure. The correct time aggregation for a balance is an average of the period-end values (or an end-of-period value), respecting its semi-additivity. Mislabeling a balance as additive is a classic source of inflated AUM-over-time figures.

</details>

<details><summary><b>73.</b> How are hierarchies (fund → share class, or country → region) usually represented in a star schema?</summary>

As denormalized attribute columns within a single flat dimension — the fund dimension carries both the share-class attributes and the parent-fund attributes, and a geography dimension carries country plus its region/continent. This avoids the snowflake of separate hierarchy tables and lets users drill up and down by selecting columns. The redundancy is accepted because it keeps queries simple and fast.

</details>

<details><summary><b>74.</b> What is the "audit dimension" pattern and why is it useful in a regulated mart?</summary>

An audit dimension attaches lineage and data-quality metadata to fact rows — load timestamp, source system, ETL batch id, quality flags — via a foreign key, so each measurement carries provenance. In a regulated fund mart this supports traceability requirements: you can show which load produced a given NAV figure and whether it passed quality checks. It turns operational metadata into a queryable dimension rather than buried log entries.

</details>

<details><summary><b>75.</b> Why does Kimball recommend descriptive text values in dimensions rather than cryptic codes?</summary>

Because dimensions are the source of report labels and filter values, spelling out human-readable descriptions ("Luxembourg SICAV", "Management Fee") makes reports self-explanatory and reduces lookups, whereas raw codes force users to memorize meanings. You can keep the operational code as an additional attribute, but the verbose label is what drives usability. Dimensions are deliberately verbose precisely because that is where meaning is presented to users.

</details>

<details><summary><b>76.</b> What is a "step" in an accumulating snapshot for a subscription order, and what measures does it enable?</summary>

Each step is a milestone in the order lifecycle — order received, dealt/traded, settled, units allocated — and each has its own date foreign key on the single order row. With all milestone dates present, you can compute lag measures like days from receipt to settlement, and monitor pipeline bottlenecks. The row is updated as each milestone is reached, which is the defining behavior of the accumulating snapshot.

</details>

<details><summary><b>77.</b> Why is an accumulating snapshot poorly suited to immutable, insert-only storage layers?</summary>

Because its core behavior is updating the same row repeatedly as milestones complete, which clashes with append-only or immutable storage (and with some columnar engines' update costs). On such platforms you typically rebuild affected rows or use merge/upsert patterns, accepting the overhead. If frequent in-place updates are impractical, a transaction fact recording each milestone event may be the better fit.

</details>

<details><summary><b>78.</b> How do you model fund domicile (e.g. a fund redomiciling from one jurisdiction to Luxembourg) so history stays correct?</summary>

Store domicile as an SCD2 attribute on the fund dimension: when the fund redomiciles, close the prior row's `valid_to`, insert a new row with the new domicile and a fresh surrogate key, and keep `is_current` accurate. NAV facts struck before the change still join to the old-domicile row via the date-band predicate, preserving point-in-time truth. This is the textbook reason fund reference data is SCD2.

</details>

<details><summary><b>79.</b> What goes wrong if you model fund domicile as SCD Type 1 in a regulated mart?</summary>

A Type 1 overwrite replaces the old domicile everywhere, so reruns of historical regulatory reports would show the new domicile against NAVs that were actually struck under the old jurisdiction — a misstatement of history. Auditors reconciling prior filings would find the mart disagrees with what was originally reported. This silent history rewrite is exactly why such attributes are SCD2, not Type 1.

</details>

<details><summary><b>80.</b> What is the "snapshot fact has no transactions in a period" situation and how does the snapshot handle it?</summary>

A periodic snapshot records a row for every entity every period regardless of activity, so even a fund with no subscriptions still gets a NAV row each valuation date showing its current balance. This guarantees a value is always available for any reporting date, unlike a transaction fact where a quiet period leaves gaps. The snapshot's completeness is precisely why it suits balance/position reporting.

</details>

<details><summary><b>81.</b> How does the choice of fact type affect whether you can answer "what was the balance on an arbitrary date"?</summary>

A periodic snapshot answers it directly with a single indexed lookup because a balance row exists for every period; a transaction fact answers it only by summing all transactions up to that date, which is correct but expensive and requires a complete event history. Accumulating snapshots track a workflow's state, not periodic balances. Choosing the snapshot type is what makes "balance as of date" cheap.

</details>

<details><summary><b>82.</b> Why is the surrogate key on a fact (pointing to an SCD2 dimension version) sometimes preferable to a date-band join?</summary>

If the ETL resolves and stores the correct SCD2 version's surrogate key on the fact at load time, then as-was reporting is a simple equi-join on the surrogate, avoiding the runtime cost and error risk of a `BETWEEN`-style date-band predicate. The fact "remembers" which version was effective when the event occurred. The trade-off is that you must resolve the version correctly during load and can't easily re-point it later.

</details>

<details><summary><b>83.</b> When loading a fact, how do you resolve which SCD2 dimension surrogate key to assign?</summary>

You look up the dimension by natural key (e.g. ISIN) and select the version whose effective window contains the fact's business date — `WHERE isin = ? AND fact_date >= valid_from AND fact_date < valid_to` — and store that row's surrogate on the fact. This "freezes" the correct historical context onto the fact at load time. Getting this lookup right is the heart of correct SCD2 fact loading.

</details>

<details><summary><b>84.</b> What is the difference between the bus matrix and an actual data model (ERD) of the warehouse?</summary>

The bus matrix is a high-level planning grid of processes against conformed dimensions, with no columns or keys — it scopes and sequences the warehouse. An ERD/star-schema diagram is the detailed physical model showing fact and dimension tables, columns, keys, and joins for a specific mart. The matrix guides which marts to build and how they conform; the star schema is how one of them is actually implemented.

</details>

<details><summary><b>85.</b> How would you justify each dimension in a fund bus matrix as conformed, junk, or degenerate?</summary>

Fund, share class, investor, and date are conformed dimensions because they are shared identically across multiple processes (NAV, fees, orders, TA). An order-flags cluster would be a junk dimension, local to the order fact, bundling small indicators. The order number (or a SWIFT message reference) is a degenerate dimension stored inline on the order fact with no separate table. Classifying each member this way is part of the lesson's "done when" checklist.

</details>

<details><summary><b>86.</b> Where does a LEI fit in a fund-administration dimensional model?</summary>

The LEI (Legal Entity Identifier) is a natural-key attribute on a legal-entity dimension — the fund's management company, the depositary, or a counterparty — used to identify and conform that entity across processes and against external regulatory data. It sits as a descriptive attribute on the relevant dimension, not as a fact. If the entity's attributes change over time, that dimension is SCD2 so the LEI's associated details stay point-in-time correct.

</details>

<details><summary><b>87.</b> Where does an ISIN fit in the model, and at what grain?</summary>

An ISIN identifies a specific security or fund share class, so it is the natural key of the share-class dimension at one-row-per-share-class (or per-version under SCD2) grain. Facts reference the share-class dimension by surrogate key, with the ISIN available as a lookup attribute. Because the same ISIN spans multiple SCD2 versions, it cannot itself be the dimension's primary key.

</details>

<details><summary><b>88.</b> How should a SWIFT message reference on a settlement fact be modeled?</summary>

As a degenerate dimension — an operational identifier stored directly on the fact, since the reference identifies a specific message/transaction but carries no descriptive attributes of its own. It supports drill-back to the operational system and grouping of related fact rows. Building a separate single-column dimension table for it would add a join with no analytical payoff.

</details>

<details><summary><b>89.</b> An EMT/EPT-style regulatory extract needs cost and charge figures per share class per reporting period — how does dimensional modeling serve this?</summary>

You source it from a charges/fees fact at the share-class/period grain joined to conformed share-class and date dimensions (and an SCD2 share-class dimension for point-in-time-correct attributes), aggregating additive charge amounts and computing ratios as aggregate-then-divide. The conformed dimensions guarantee the figures align with the NAV mart for consistency checks. The clean grain prevents the double-counting that would corrupt a regulatory cost disclosure.

</details>

<details><summary><b>90.</b> Why is "declare the grain in one written sentence" a review gate for an architect?</summary>

Because if the modeler cannot state the grain in a single unambiguous sentence, the fact table's meaning is undefined and its aggregations cannot be trusted — the architect literally cannot review the mart. The one-sentence test forces clarity and surfaces mixed-grain mistakes before columns are added. It is the cheapest, highest-leverage correctness check in dimensional design, which is why the lesson elevates it.

</details>

<details><summary><b>91.</b> What is a "transaction-grain" fee fact versus an "accrual-grain" fee fact?</summary>

A transaction-grain fee fact records each individual fee charge event as it is billed, while an accrual-grain fee fact records the daily/periodic accrual amounts that build up to a charge over time. They answer different questions — actual charges versus how the liability accumulated — and may coexist as separate facts. Each must have its grain declared explicitly so accrual rows and charge rows are never summed together.

</details>

<details><summary><b>92.</b> How do you prevent double counting when a fund-of-funds holds positions in underlying funds?</summary>

Recognize the many-to-many/hierarchy and avoid summing parent and child net assets together; use a bridge or allocation approach, or report the fund-of-funds and its underlyings at clearly separated grains so a single SUM never adds the same assets at two levels. Declaring the grain and being explicit about look-through allocation is what stops the inflated AUM. This is a concrete instance of the "ungrained tables double-count AUM" warning.

</details>

<details><summary><b>93.</b> What is the difference between a "snapshot" and an "accumulating snapshot" — do not confuse them.</summary>

A (periodic) snapshot records a fresh row per entity at each regular interval, capturing balances over time, and is insert-only with many rows per entity. An accumulating snapshot records one row per workflow instance and updates that same row as it progresses through milestones, with multiple date keys and lag measures. Periodic = recurring states over time; accumulating = one evolving row per process instance.

</details>

<details><summary><b>94.</b> Why does dimensional modeling deliberately accept data redundancy in dimensions?</summary>

Because the redundancy from denormalizing hierarchies and descriptions into flat dimensions buys query simplicity, performance, and user understandability, which are the goals of an analytical mart, and the storage cost is trivial next to the fact table. Update anomalies, the usual argument against redundancy, are managed by the controlled ETL load rather than by ad-hoc writes. This is the conscious trade that distinguishes dimensional from normalized design.

</details>

<details><summary><b>95.</b> What is the first thing to check when a mart's total AUM report comes back roughly double the expected figure?</summary>

Check the fact table's grain and your join cardinality first: a mixed/undeclared grain or a many-to-many join (e.g. fact-to-fact, or a fund hierarchy joined without allocation) is the usual cause of a doubled total. Verify that one declared grain sentence holds for every row and that you aren't summing parent and child levels together. The lesson explicitly ties doubled AUM to ungrained fact tables.

</details>

<details><summary><b>96.</b> A point-in-time NAV report shows today's fund name for a NAV struck a year ago. What is the modeling defect?</summary>

The fund dimension is SCD Type 1 (overwriting) instead of Type 2, so the historical NAV joins to the current, overwritten attribute row rather than the version effective a year ago. The fix is to make the fund name an SCD2 attribute with effective dating and join on a date-band predicate so the year-old NAV picks up the name that was current then. This is the canonical as-was-versus-as-is failure.

</details>

<details><summary><b>97.</b> Why might a snowflaked dimension actually slow down a self-service BI tool beyond just extra joins?</summary>

Many BI tools and semantic layers assume a star (single table per dimension); a snowflake forces the tool either to pre-join the normalized pieces or to expose multiple tables that confuse business users and can produce wrong aggregations if the user joins them incorrectly. Beyond raw join cost, it degrades usability and increases the chance of fan-trap errors. This usability hit is a core reason Kimball calls snowflaking a smell in marts.

</details>

<details><summary><b>98.</b> How do you choose between SCD Type 2 and Type 3 for a given attribute?</summary>

Use Type 2 when you need the full history of changes and point-in-time-correct joins (most regulated reference data); use Type 3 when only the immediately prior value matters and you want an easy "current vs previous" comparison without history rows. Type 3 cannot track more than one change back, so any attribute that changes repeatedly or needs full audit history must be Type 2. The number of changes you must retain is the deciding factor.

</details>

<details><summary><b>99.</b> What is the role of the "current flag" plus effective dates together in everyday querying?</summary>

The effective dates (`valid_from`/`valid_to`) enable arbitrary as-of-date joins for historical reporting, while the `is_current` flag gives a fast path for "today's value" queries without date arithmetic. Together they let one SCD2 dimension serve both point-in-time and current-state needs efficiently. They must be kept consistent by the load so the open row is the one flagged current.

</details>

<details><summary><b>100.</b> Summarize the dimensional design sequence an architect should follow for a new fund mart.</summary>

First identify the business process; second declare the fact table's grain in one sentence; third pick the dimensions consistent with that grain (reusing conformed ones from the bus matrix); fourth identify the facts (measures) and their additivity. Reference data dimensions like fund and share class are modeled SCD2 for point-in-time correctness, flags are bundled into junk dimensions, operational ids stay as degenerate dimensions, and snowflaking is avoided. Following this order is what produces a reviewable, double-count-proof mart.

</details>


## Phase 1 · 8.5.1 Architecture notations & decision records (C4, ADR) — 100 self-test questions

<details><summary><b>1.</b> What does C4 stand for in the C4 model, and who created it?</summary>

C4 stands for the four hierarchical levels of abstraction: Context, Container, Component, and Code. It was created by Simon Brown as a lightweight, notation-independent way to describe software architecture at different zoom levels. The core idea is that you tell a "map of your code at different scales" story, the way you'd zoom out from a street map to a country map.

</details>

<details><summary><b>2.</b> Name the four levels of the C4 model in order from most zoomed-out to most zoomed-in.</summary>

The order is Context (level 1), Container (level 2), Component (level 3), and Code (level 4). Each level zooms in one step: Context shows the system among its users and neighbours, Container shows the deployable/runnable pieces, Component shows the major building blocks inside one container, and Code shows classes or schema inside one component. You almost never draw all four for the same system.

</details>

<details><summary><b>3.</b> What does a C4 System Context diagram show?</summary>

It shows your software system as a single box in the middle, surrounded by the people (actors) who use it and the other systems it interacts with. It deliberately hides all internal detail so that non-technical stakeholders can see scope and boundaries. For a NAV-calculation system, the context diagram would show the fund accountant, the order-management system, the market-data feed, and the regulator's reporting gateway, but nothing about how NAV is computed inside.

</details>

<details><summary><b>4.</b> What does a C4 Container diagram show, and what level does it sit at?</summary>

The Container diagram is level 2; it zooms into the single system box from the context diagram and shows the separately deployable or runnable units inside it — web apps, APIs, databases, message queues, and scheduled jobs. Every arrow is labelled with the protocol and intent, e.g. "reads EMT files via SFTP" or "publishes NAV events over Kafka". It is the diagram most architecture work stops at because it captures the high-level technology shape without drowning in internal class detail.

</details>

<details><summary><b>5.</b> In C4, what exactly is a "container"? Is it a Docker container?</summary>

No — a C4 container is "an application or a data store; something that needs to be running for the overall system to work", i.e. a runtime boundary around executing code or stored data. It is a logical/architectural unit, not a Docker or OS container; Simon Brown chose the word before Docker popularised it and explicitly warns against conflating them. A single C4 container (say a Spring Boot API) might run inside one Docker container, several, or none — deployment is modelled separately.

</details>

<details><summary><b>6.</b> Give five concrete examples of things that count as C4 containers.</summary>

Examples include a server-side web application (Node.js, ASP.NET, Java EE), a single-page browser application (Angular, React), a mobile app, a database (PostgreSQL, MongoDB), and a serverless function (AWS Lambda, Azure Function). Shell scripts, file systems, blob stores like S3, and message brokers also count. The unifying test is "does this need to be running, or hold state, for the system to work?".

</details>

<details><summary><b>7.</b> What does a C4 Component diagram show, and why is it level 3?</summary>

A Component diagram zooms inside one single container and shows its major structural building blocks — groupings of related functionality behind an interface, such as a "NAV Calculator", an "ISIN Validator", or a "TA Register Loader" — and how they collaborate. It is level 3 because it sits one zoom below the container; you draw one component diagram per container that warrants it, not one for the whole system. Most teams rarely keep these up to date because they drift from the code quickly.

</details>

<details><summary><b>8.</b> What is at C4 level 4 (Code), and why is it usually not hand-drawn?</summary>

Level 4 (Code) shows the implementation of a single component — UML class diagrams, entity-relationship diagrams, or similar. It is usually not hand-drawn because it changes constantly and is far better auto-generated from the codebase by an IDE or tool when actually needed. Most teams skip drawing level 4 entirely and let the source code itself be the level-4 "diagram".

</details>

<details><summary><b>9.</b> Why does C4 say most architecture work stops at the Container level?</summary>

Because Context plus Container together answer the questions stakeholders and reviewers actually ask — what is the system, who uses it, what are its moving parts, and how do they talk — without incurring the maintenance cost of component and code diagrams that drift the moment someone refactors. Container-level diagrams are stable enough to live in a repo and still meaningful months later. Going deeper is justified only for a specific container that is genuinely complex or contentious.

</details>

<details><summary><b>10.</b> What would force you to draw a Component (level 3) diagram for a particular container?</summary>

You drop to component level when one container is internally complex enough that reviewers cannot reason about it from the container diagram alone — e.g. a NAV engine with intricate pricing, accruals, and fee-calculation responsibilities whose internal boundaries are themselves an architectural decision. The trigger is "the interesting decisions now live inside this one box". You draw it only for that container, and only while it stays useful.

</details>

<details><summary><b>11.</b> What are the three supplementary C4 diagram types beyond the four core levels?</summary>

They are the System Landscape diagram, the Dynamic diagram, and the Deployment diagram. The System Landscape shows many systems and their relationships across an enterprise; the Dynamic diagram shows the ordered runtime collaboration for one scenario (like a UML communication diagram); and the Deployment diagram maps containers onto infrastructure nodes. They complement the static Context/Container/Component view rather than replacing it.

</details>

<details><summary><b>12.</b> What does a C4 Deployment diagram add that a Container diagram does not?</summary>

A Deployment diagram maps the logical containers onto the physical or virtual infrastructure they run on — nodes such as Kubernetes pods, VMs, on-prem servers, or cloud regions — including how many instances of each container exist. The Container diagram says what the runnable units are; the Deployment diagram says where and on how much hardware they live. For a regulated fund platform this is where you'd show data residency, e.g. NAV data confined to an EU region.

</details>

<details><summary><b>13.</b> What is a C4 System Landscape diagram useful for in an asset-management firm?</summary>

It gives a bird's-eye view of many systems and how they connect across the whole estate — order management, transfer agency, fund accounting, regulatory reporting, market data — independent of any single system's internals. It is the picture an enterprise architect uses to spot duplicated capabilities or undocumented integrations. It is explicitly a landscape, not a context diagram, because it has no single "system in scope".

</details>

<details><summary><b>14.</b> What is meant by C4 being "notation independent" and "tooling independent"?</summary>

C4 prescribes the abstractions (person, system, container, component) and the zoom levels, but not the shapes, colours, or arrows you must use, and not the tool you draw with. You can render C4 with boxes-and-lines in any tool, or with dedicated tooling like Structurizr. The discipline comes from the abstractions and from giving every element and relationship a clear, complete label, not from a fixed visual language.

</details>

<details><summary><b>15.</b> Why does C4 stress that every element and every arrow must carry an explicit, complete label?</summary>

Because an unlabelled box or a bare arrow forces the reader to guess, and guessing is exactly what an architecture diagram should eliminate. C4 wants each element to say what it is and its core responsibility, and each relationship to say the intent plus the protocol or technology — for example "TA System sends settlement instructions to Custodian via SWIFT MT54x". A diagram a stranger can read without you in the room is the whole point.

</details>

<details><summary><b>16.</b> What is "diagrams-as-code", and what core benefit does it give over a drawing tool?</summary>

Diagrams-as-code means defining the model in a plain-text DSL or markup that a tool renders into the diagram, instead of dragging boxes in a GUI. The core benefit is that the model becomes a versioned text artifact you can diff, review in a pull request, and store next to the code it describes — so the architecture history is captured in Git like everything else. It also means the picture cannot silently drift from the agreed source of truth.

</details>

<details><summary><b>17.</b> Why is a committed `.dsl` or Mermaid file better than a committed `.png` export of the same diagram?</summary>

A `.png` is opaque to version control — a diff just shows "binary changed", you cannot see what moved, and a reviewer cannot comment on a specific line. A text model diffs meaningfully, so a reviewer sees exactly that an arrow's protocol changed from `SFTP` to `HTTPS`, and the change is reviewable in a PR. The export is a build output; the text is the source of truth.

</details>

<details><summary><b>18.</b> What is Structurizr DSL?</summary>

Structurizr DSL is a text-based domain-specific language for defining a software architecture model based on the C4 model, authored in plain `.dsl` files. You describe the model once — people, systems, containers, components, and their relationships — and then declare which views (context, container, component) to render from it. Because it separates the single model from multiple views, every diagram stays consistent with one source of truth.

</details>

<details><summary><b>19.</b> In Structurizr DSL, what are the three main top-level blocks inside a `workspace`?</summary>

Inside `workspace { ... }` the three main blocks are `model`, `views`, and (optionally) `configuration`/`styles`. The `model` block defines the elements and relationships; the `views` block defines which diagrams to generate from that model. Keeping model and views separate is what lets you draw several diagrams (context, container, component) from one definition without duplicating elements.

</details>

<details><summary><b>20.</b> How do you declare a person and a software system in Structurizr DSL?</summary>

You assign them inside the `model` block, e.g. `fundAccountant = person "Fund Accountant"` and `navSystem = softwareSystem "NAV Calculation System"`. The left-hand identifier is a variable you reference later when drawing relationships, and the quoted string is the display name. You can add an optional description as a second quoted argument.

</details>

<details><summary><b>21.</b> In Structurizr DSL, how do you express that one element uses another, and how is the protocol shown?</summary>

You use the `->` operator with a description and an optional technology, e.g. `navSystem -> custodian "Sends settlement instructions" "SWIFT MT54x"`. The first string is the intent shown on the arrow; the second is the technology/protocol. This is the diagrams-as-code equivalent of labelling every arrow, and it diffs cleanly in Git.

</details>

<details><summary><b>22.</b> In Structurizr DSL, how are containers nested under a software system?</summary>

You define them inside the software system's braces, e.g. `navSystem = softwareSystem "NAV" { api = container "NAV API" "REST" "Node.js"; db = container "NAV Store" "" "PostgreSQL" }`. The nesting tells the tool these containers belong to that system, so a container view of `navSystem` automatically shows just those. You then reference the container identifiers (`api`, `db`) in relationships.

</details>

<details><summary><b>23.</b> How do you declare a container view versus a system-context view in Structurizr DSL?</summary>

In the `views` block you write `systemContext navSystem "Context" { include *; autolayout }` for the level-1 view and `container navSystem "Containers" { include *; autolayout }` for level-2. Each view names the element it zooms into and which elements to include; `autolayout` lets the renderer position things. The same model thus produces multiple consistent diagrams.

</details>

<details><summary><b>24.</b> What is Structurizr Lite, and how is it typically run?</summary>

Structurizr Lite is the free, single-workspace version of Structurizr that renders and serves diagrams from a local `workspace.dsl`, typically run as a Docker container that watches the file and shows the diagrams in a browser. It is the recommended FOSS hands-on tool for this lesson because it keeps the model in your repo and re-renders on save. You point it at a directory containing the `.dsl` file and open `http://localhost:8080`.

</details>

<details><summary><b>25.</b> What is Mermaid's C4 support, and what is an important caveat about it?</summary>

Mermaid can render C4 diagrams using directives like `C4Context`, `C4Container`, `C4Component`, `C4Dynamic`, and `C4Deployment`, with syntax modelled on C4-PlantUML. The important caveat is that Mermaid's C4 support is officially experimental — the syntax and behaviour may change in future releases and documentation is provisional until it stabilises. It is attractive because Mermaid renders directly in GitHub/GitLab markdown, but you should pin your tool version.

</details>

<details><summary><b>26.</b> Why might you choose Mermaid C4 over Structurizr for a small repo, and what do you give up?</summary>

Mermaid renders inline in GitHub and GitLab markdown with no extra tooling, so a diagram lives right in the README and reviewers see it in the PR without running anything. What you give up is Structurizr's single-model-many-views consistency: in Mermaid each diagram is written separately, so a context and a container diagram of the same system can silently drift out of sync. For one or two diagrams that is fine; for a large model it is not.

</details>

<details><summary><b>27.</b> In Mermaid C4, how do you declare a person and a system inside a `C4Context` block?</summary>

You use functions such as `Person(accountant, "Fund Accountant", "Calculates NAV")` and `System(nav, "NAV System", "Computes daily NAV")`. Relationships use `Rel(accountant, nav, "uses", "HTTPS")`. The syntax deliberately mirrors C4-PlantUML so existing C4-PlantUML knowledge transfers, but remember it is experimental in Mermaid.

</details>

<details><summary><b>28.</b> What is an Architecture Decision Record (ADR)?</summary>

An ADR is a short document that captures a single significant architectural decision together with its context and consequences, so that future readers understand not just what was decided but why and at what cost. It turns tacit "hallway memory" into a reviewable, auditable artifact. The format was popularised by Michael Nygard's 2011 blog post and is now a widespread lightweight practice.

</details>

<details><summary><b>29.</b> What are the core sections of Michael Nygard's original ADR template?</summary>

They are Title, Status, Context, Decision, and Consequences. Context describes the forces and the situation; Decision states the choice in active voice ("We will..."); Consequences records the resulting trade-offs, both good and bad. The deliberate brevity is the point — short enough that people actually write them.

</details>

<details><summary><b>30.</b> Why does an ADR's "Context" section matter as much as the "Decision" itself?</summary>

Because the context records the forces — constraints, requirements, regulatory pressures, what you knew at the time — that made the decision reasonable, which is exactly what a future reader needs to judge whether it still holds. A decision with no context is just an assertion; a decision with context can be re-evaluated honestly when circumstances change. For a regulated firm the context is also part of the audit trail.

</details>

<details><summary><b>31.</b> What goes in the "Consequences" section of an ADR, and why must the bad ones be included?</summary>

It records the outcomes of the decision — what becomes easier, what becomes harder, and what new constraints or risks are introduced — including the negative ones. The negatives must be there because a list of only upsides is marketing, not an honest decision record, and the trade-offs you accepted are precisely what a reviewer or auditor needs to see. Honest consequences also stop the same trade-off being re-litigated later in ignorance.

</details>

<details><summary><b>32.</b> Why are ADRs deliberately kept short?</summary>

Because length is the enemy of adoption — a one-page ADR gets written and read, while a ten-page design document does not. The goal is to capture the decision, its context, and its consequences with just enough detail to be useful, not to produce exhaustive documentation. Short ADRs accumulate into a navigable decision log over the life of a system.

</details>

<details><summary><b>33.</b> What three (or four) status values describe an ADR's place in its lifecycle?</summary>

The common statuses are Proposed, Accepted, and Superseded, with Deprecated and Rejected also used. Proposed means under review, Accepted means in force, Superseded means a later ADR replaced it, Rejected means it was considered and turned down, and Deprecated means no longer relevant but not directly replaced. The status makes the document's authority explicit at a glance.

</details>

<details><summary><b>34.</b> What is the cardinal rule about editing an ADR once it is Accepted?</summary>

You do not rewrite the substance of an accepted ADR — its decision, context, and consequences are immutable history. If the decision changes, you write a new ADR that supersedes the old one and mark the old one's status as Superseded, leaving its original text intact. This preserves the audit trail of why things were once done a certain way, which slide-decks and edited wikis destroy.

</details>

<details><summary><b>35.</b> Why does "never rewrite history, supersede it" matter especially in a regulated fund administrator?</summary>

Because IT governance and regulators expect an auditable trail showing what was decided, when, by whom, and what later changed it — not a single document that was quietly edited to match today's reality. Superseding leaves both the old and new decisions visible with their statuses, so an auditor asking "why was NAV history partitioned this way in 2024, and why did it change in 2026?" gets a complete answer. Silent edits would look like an attempt to hide the trail.

</details>

<details><summary><b>36.</b> How do you record that ADR-0007 replaces ADR-0003? What changes in each file?</summary>

You leave ADR-0003's body unchanged but set its status to "Superseded by ADR-0007", and you create ADR-0007 with a reference back to "Supersedes ADR-0003". The two-way link is what makes the trail navigable in both directions. ADR-0003 stays in the repo forever as accurate history of a past decision.

</details>

<details><summary><b>37.</b> What is MADR, and what does the acronym stand for in its current version?</summary>

MADR is a popular structured ADR template. As of version 4.0.0 (released 2024-09-17) the acronym stands for "Markdown Architectural Decision Records"; earlier versions expanded it as "Markdown Any Decision Records" before the project refocused on architectural decisions. It adds structure (decision drivers, considered options, pros and cons) on top of Nygard's leaner format.

</details>

<details><summary><b>38.</b> What are the main sections of the full MADR template?</summary>

They are an optional YAML front matter (status, date, deciders), Title, Context and Problem Statement, Decision Drivers (optional), Considered Options, Decision Outcome with justification, Consequences (positive and negative), an optional Confirmation, optional per-option Pros and Cons, and optional More Information. The "Considered Options" plus "Pros and Cons" sections are what distinguish MADR from Nygard's template. MADR also ships "minimal" and "bare" variants for lighter use.

</details>

<details><summary><b>39.</b> What does MADR's "Decision Drivers" section capture, and why is it useful to reviewers?</summary>

Decision Drivers list the criteria and forces that the chosen option had to satisfy — performance, cost, regulatory constraints, operability, vendor lock-in — that the options are then judged against. They are useful to reviewers because they make the evaluation traceable: you can check that the chosen option actually scores well on the drivers the team claimed to care about. Without them, "we chose X" looks arbitrary.

</details>

<details><summary><b>40.</b> What does the MADR front-matter status field typically look like for a superseded record?</summary>

It uses a value like `superseded by ADR-0012`, sitting alongside the other allowed values `proposed`, `rejected`, `accepted`, and `deprecated`. Encoding the superseding link in the status (and in front matter where tooling can parse it) keeps the lifecycle machine-readable. The original record's body is still left intact.

</details>

<details><summary><b>41.</b> What is the standard file-naming convention for MADR/ADR files?</summary>

Files are named `NNNN-title-with-dashes.md`, where `NNNN` is a zero-padded sequential number (e.g. `0001`, `0042`) and the title uses lowercase words separated by dashes. The padding to four digits keeps files sorting correctly up to 9,999 records. For example `0007-partition-nav-history-by-fund-and-month.md`.

</details>

<details><summary><b>42.</b> Why pad the ADR number to four digits (`0001`) rather than using `1`, `2`, `10`?</summary>

Because zero-padding makes the files sort correctly as plain strings in a directory listing or Git tree — `0002` sorts before `0010`, whereas `2` would sort after `10`. It is a small detail that keeps the decision log readable in the exact chronological order decisions were made. Four digits comfortably covers any realistic project.

</details>

<details><summary><b>43.</b> Where, by convention, do ADR files live in a repository?</summary>

The conventional location is a dedicated directory such as `doc/adr/` or `docs/adr/` at the repo root, holding the numbered markdown files. Keeping them in-repo (not in a separate wiki) means the decisions are versioned with the code, reviewed in the same PRs, and travel with a clone. This lesson asks you to set up that `adr/` convention once and reuse it in every capstone.

</details>

<details><summary><b>44.</b> What is `adr-tools`, and what does `adr new "..."` do?</summary>

`adr-tools` is a small command-line helper for managing Nygard-style ADRs; `adr new "Use Kafka for NAV events"` creates the next sequentially numbered markdown file from a template with the status pre-set. It also offers `adr new -s 3 "..."` to create a record that supersedes ADR-0003, automatically updating the old record's status. It is optional — many teams just copy a template by hand — but it removes the friction of numbering and superseding.

</details>

<details><summary><b>45.</b> How would `adr-tools` help you correctly supersede an existing record?</summary>

Running `adr new -s 7 "Replace SFTP ingestion with event streaming"` creates the new numbered ADR and automatically appends "Superseded by" to ADR-0007's status while linking the new one back to it. This automates the two-way link and the immutability convention so you cannot forget to update the old record. The result is a clean, navigable supersession trail.

</details>

<details><summary><b>46.</b> What is a lightweight RFC process, and how does it differ from an ADR?</summary>

An RFC (Request for Comments) is a short proposal document circulated for review and discussion before a decision is made, whereas an ADR records a decision after it has been made. The RFC is the deliberation; the ADR is the outcome. Lightweight RFC processes give a decision the review it needs without a heavyweight committee, and the resulting decision is then captured in an ADR.

</details>

<details><summary><b>47.</b> When does a decision need an RFC step before an ADR records it?</summary>

When the decision is significant, contentious, or affects multiple teams enough that it needs explicit review and buy-in before it is locked in — for example choosing the firm-wide market-data ingestion pattern. A small, local, reversible decision can go straight to an ADR; a large, cross-cutting, hard-to-reverse one benefits from an RFC round first. The RFC reduces the risk of an Accepted ADR being immediately challenged.

</details>

<details><summary><b>48.</b> How do the RFC and ADR artifacts fit together over a decision's life?</summary>

The RFC opens the question and gathers comments while the decision is still Proposed; once consensus forms, the decision is recorded as an Accepted ADR that may reference the RFC for the fuller discussion. The RFC captures the debate; the ADR captures the conclusion and its consequences. Some teams even keep the RFC as the ADR's "More Information" link.

</details>

<details><summary><b>49.</b> What does the phrase "the decisions you didn't write down" mean for a reviewer?</summary>

It refers to implicit architectural choices baked into a diagram or system that were never explicitly recorded — like why a datastore was chosen, why a boundary sits where it does, or why a protocol was selected. A good reviewer hunts for exactly these gaps, because undocumented decisions are the ones that bite later when nobody remembers the rationale. The fix is to surface them as new ADRs.

</details>

<details><summary><b>50.</b> What three things do experienced reviewers look for in an architecture submission?</summary>

They look for clear boundaries (is the system scope and each container's responsibility unambiguous?), correct data flows (does every arrow show the right direction, protocol, and intent?), and the decisions that were made but not written down (the missing ADRs). These map directly onto C4 diagrams plus ADRs. A submission that nails all three is reviewable and auditable.

</details>

<details><summary><b>51.</b> A reviewer says "this arrow has no protocol" on your container diagram. Why does that matter?</summary>

Because an unlabelled arrow hides a real decision and a real integration risk — whether two containers talk over `HTTPS`, `SFTP`, a message queue, or SWIFT changes security, reliability, and latency, and a reviewer cannot assess the design without it. C4's rule that every relationship carries intent plus technology exists precisely to force this out. The fix is to add the protocol, e.g. "publishes NAV events via Kafka".

</details>

<details><summary><b>52.</b> Why are C4 diagrams and ADRs described as "the artifacts that define the architect role in practice"?</summary>

Because they are what make an architect's reasoning reviewable and decisions auditable, rather than living in slide decks and personal memory. The C4 diagrams make the structure legible; the ADRs make the choices and their trade-offs explicit and traceable. In a regulated fund administrator, producing these is much of what distinguishes architecture work from ad-hoc design.

</details>

<details><summary><b>53.</b> Your NAV platform's architecture lives only in a `.pptx` slide deck. What is the concrete risk?</summary>

The risk is that the slides drift from reality, cannot be diffed or reviewed in a PR, and carry no record of why decisions were made — so when an auditor asks why NAV history is partitioned a certain way, the only answer is "ask the person who built it". Slides are an export, not a source of truth, and they lose the decision trail entirely. Moving to in-repo C4-as-code plus ADRs fixes all three problems.

</details>

<details><summary><b>54.</b> For a transfer-agency order flow from EMT file to register, which C4 level best shows the runnable pieces and protocols?</summary>

The Container diagram (level 2). It would show the SFTP ingestion service, the EMT/EPT parser, the order-validation service, the message broker, and the register database as separate containers, with each arrow labelled with its protocol (e.g. "reads EMT file via SFTP", "publishes validated orders via Kafka"). Context (level 1) would hide these pieces, and Component (level 3) would only be needed inside one especially complex container.

</details>

<details><summary><b>55.</b> At the Context level, who are the likely external actors and systems for a fund's NAV-calculation system?</summary>

External actors include the fund accountant and oversight/compliance users; external systems include the order-management/transfer-agency system, the market-data provider, the custodian, the accounting/general-ledger system, and the regulatory-reporting gateway. The context diagram shows the NAV system as one box among these, with labelled relationships, and nothing about its internals. It answers "what is this system and who does it touch?".

</details>

<details><summary><b>56.</b> Write a one-line ADR title (Nygard style) for the decision to partition NAV history by fund and month.</summary>

A good title is short, neutral, and states the decision, e.g. "Partition NAV history by fund and calendar month". The corresponding file would be `0007-partition-nav-history-by-fund-and-month.md`. The Context would record the query and retention forces, the Decision the partitioning scheme, and the Consequences the trade-offs such as cross-fund query cost.

</details>

<details><summary><b>57.</b> A new requirement makes the monthly NAV partitioning scheme wrong. What is the correct ADR action?</summary>

You write a new ADR proposing the replacement scheme, take it through review, mark it Accepted, and set it to "Supersedes ADR-0007"; then you update ADR-0007's status to "Superseded by ADR-00NN" without altering its body. You never edit the original decision's substance. This leaves a clean, auditable trail of both the old rationale and the new one.

</details>

<details><summary><b>58.</b> In C4, what is the difference between a "system" and a "container", using a NAV platform as the example?</summary>

The NAV platform as a whole is one software system at the Context level — the single box stakeholders care about. Its containers are the separately runnable parts inside it: the NAV API, the calculation worker, the PostgreSQL store, the scheduler. Context answers "what is the platform among its neighbours"; Container answers "what does the platform consist of internally".

</details>

<details><summary><b>59.</b> Why can a single Apache Tomcat instance host several C4 containers in dev but separate them in production?</summary>

Because C4 containers are logical runtime/data boundaries, not deployment units — in development you might run several web applications inside one Tomcat for convenience, while in production each runs in its own process or node. The Container diagram models the logical separation; the Deployment diagram models the physical placement. This is exactly why C4 keeps "container" decoupled from infrastructure.

</details>

<details><summary><b>60.</b> What is the relationship between C4's Code level and a UML class diagram?</summary>

A C4 Code diagram is typically a UML class diagram (or ERD) describing the internals of one component. C4 does not invent a new notation for level 4 — it reuses UML and recommends auto-generating it from the source when actually needed, rather than maintaining it by hand. This is why most teams treat the code itself as the level-4 artifact.

</details>

<details><summary><b>61.</b> Why should the architecture model and the ADRs live in the same Git repository as the code where possible?</summary>

Co-locating them means the diagrams-as-code and decision records are versioned, reviewed, and updated in the same pull requests as the code they describe, so they stay in sync and travel with a clone. A reviewer can see a code change and the architecture/ADR change together. Splitting them into a separate wiki is how documentation rots.

</details>

<details><summary><b>62.</b> A teammate edited the body of an Accepted ADR to reflect a new decision. Why is this wrong, and what should they have done?</summary>

It is wrong because it destroys the audit trail — the historical record of what was decided and why is overwritten, so nobody can reconstruct the original rationale or see that a change occurred. They should have written a new ADR superseding the old one and set the old one's status to Superseded, leaving its body untouched. The "never rewrite history, supersede it" rule exists precisely to prevent this.

</details>

<details><summary><b>63.</b> You inherit a system with C4 diagrams but no ADRs. What is the first reviewer instinct?</summary>

To look for the decisions the diagrams imply but never document — why this datastore, why this boundary, why this protocol — because those are "the decisions you didn't write down" and the ones most likely to cause pain later. You would then write retroactive ADRs capturing the rationale you can reconstruct, so future readers are not left guessing. Diagrams show structure; ADRs explain choice.

</details>

<details><summary><b>64.</b> What does "Status: Proposed" on an ADR tell a reader about its authority?</summary>

It tells the reader the decision is still under review and not yet in force, so it should not be relied upon as the current design. Only once it moves to Accepted does it carry authority. Making the status explicit prevents teams from acting on a decision that was merely floated.

</details>

<details><summary><b>65.</b> Why is the active-voice form "We will use Kafka for NAV events" preferred in an ADR's Decision section?</summary>

Active voice states the decision unambiguously as a commitment the team is making, which is clearer and more accountable than passive hedging like "Kafka could be considered". It removes doubt about whether a decision was actually taken. Clarity here is what lets a reader, or an auditor, treat the ADR as a real record rather than a musing.

</details>

<details><summary><b>66.</b> How does diagrams-as-code support code review of architecture changes specifically?</summary>

Because the model is text, a change to it shows up as a normal diff in a pull request — a reviewer sees that a new container was added or an arrow's protocol changed, and can comment inline on the exact line. This brings architecture under the same review discipline as code, instead of being a separate, unreviewed drawing. The diagram render is just the build output of the reviewed text.

</details>

<details><summary><b>67.</b> In a regulated environment, why is an auditable ADR trail more valuable than a single up-to-date design document?</summary>

Because auditors and regulators (under regimes like DORA) want to see what was decided, when, by whom, and how it changed over time — a trail — not just the current state. A single living document shows only "now" and erases the history of "why then". Numbered, superseding ADRs provide exactly the chronological, immutable evidence governance expects.

</details>

<details><summary><b>68.</b> What is the risk of drawing all four C4 levels for every system?</summary>

The main risk is maintenance cost and drift: component and code diagrams change with every refactor, so they go stale fast and then actively mislead readers who trust them. Effort spent maintaining low-value diagrams is effort not spent on the context and container diagrams that actually stay useful. The discipline is to draw only the levels that earn their keep.

</details>

<details><summary><b>69.</b> How would you decide whether a particular architectural choice deserves its own ADR?</summary>

Ask whether the choice is significant (affects structure, cost, security, or compliance), whether it is hard to reverse, and whether a future reader would benefit from knowing why it was made. If yes to those, it warrants an ADR; trivial, local, easily reversed choices do not. The aim is a useful decision log, not a record of every line of code.

</details>

<details><summary><b>70.</b> A `C4Container` diagram in Mermaid renders fine today but breaks after a Mermaid upgrade. What is the likely cause?</summary>

The likely cause is that Mermaid's C4 support is officially experimental, so its syntax and rendering can change between releases without backward-compatibility guarantees. The fix is to pin the Mermaid version your pipeline uses and treat an upgrade as a change to test, not assume. This is a known trade-off of choosing Mermaid C4 for its in-markdown convenience.

</details>

<details><summary><b>71.</b> Your Structurizr Lite container starts but shows no diagrams. What is the first thing to check?</summary>

Check that you pointed Structurizr Lite at the directory actually containing your `workspace.dsl` and that the file parses — a DSL syntax error or a misdirected volume mount is the usual cause of an empty workspace. Structurizr Lite watches that one file and re-renders on save, so confirming the mount and a valid model comes first. Then confirm you are looking at `http://localhost:8080`.

</details>

<details><summary><b>72.</b> In Structurizr DSL, why does defining relationships once in the model save you work across views?</summary>

Because the model holds elements and relationships in one place, and each view simply selects which of them to show — so a relationship you define once appears correctly in the context, container, and any component view that includes its endpoints. You never redraw the same arrow per diagram. This single-model-many-views design is what keeps the diagrams mutually consistent.

</details>

<details><summary><b>73.</b> What is the difference between a C4 Dynamic diagram and a Container diagram?</summary>

A Container diagram is static — it shows what the containers are and which can talk to which. A Dynamic diagram shows the ordered sequence of interactions for one specific scenario, with numbered steps, like "1. order received, 2. validated, 3. NAV recalculated". Use the Dynamic diagram when the runtime flow of a particular use case is what you need to explain.

</details>

<details><summary><b>74.</b> For an order lifecycle from EMT ingestion to register update, which supplementary C4 diagram best shows the step order?</summary>

The Dynamic diagram, because it numbers the interactions in the order they occur — SFTP receive, parse EMT, validate order, publish event, update register — for that one scenario. The Container diagram shows the same pieces but not the sequence. Note that step-by-step business-process detail might also be expressed in BPMN, but within C4 the Dynamic diagram is the right tool.

</details>

<details><summary><b>75.</b> Why is "boundaries" the first thing a reviewer checks on a context or container diagram?</summary>

Because if the system boundary or each container's responsibility is unclear, nothing else on the diagram can be trusted — you cannot judge data flows or decisions when you do not know what is in scope. Clear boundaries are the foundation the rest of the review stands on. A box whose responsibility you cannot state in one sentence is a red flag.

</details>

<details><summary><b>76.</b> How do C4 diagrams and ADRs complement each other rather than overlap?</summary>

C4 diagrams answer "what does the architecture look like" — the structure, boundaries, and flows; ADRs answer "why is it like that" — the decisions, drivers, and trade-offs behind the structure. A diagram without ADRs leaves the reasoning implicit; ADRs without diagrams leave the structure hard to picture. Together they make a design both legible and auditable.

</details>

<details><summary><b>77.</b> What does "Done when" expect you to be able to explain about C4 levels?</summary>

You should be able to explain when to stop at the container level — because context plus container answer most stakeholder and reviewer questions cheaply — and what would force a component diagram, namely one container being internally complex or contentious enough that its internal boundaries are themselves a decision. The skill is justifying the chosen zoom depth, not drawing everything. Stopping at the right level is itself an architectural judgement.

</details>

<details><summary><b>78.</b> What does it mean to "show an ADR pair with the status trail intact"?</summary>

It means presenting two ADRs where the later one is marked "Supersedes ADR-N" and the earlier one is marked "Superseded by ADR-M", with both bodies preserved unedited. The intact trail proves you modelled the lifecycle correctly — history was extended, not rewritten. This is one of the lesson's explicit completion criteria.

</details>

<details><summary><b>79.</b> Why write retroactive ADRs for a system you already understand, as this lesson asks?</summary>

Because it forces you to practise the format, the immutability rule, and especially the supersession lifecycle on a real system whose decisions you can reconstruct, without the pressure of a live debate. Writing two — including one that gets superseded — models the full lifecycle end to end. It also leaves the inherited system better documented than you found it.

</details>

<details><summary><b>80.</b> An ADR's Context says "we must comply with UCITS reporting deadlines". Why does recording such a driver matter later?</summary>

Because it ties the architectural choice to a concrete external constraint, so a future reader knows the decision was driven by a real deadline, not preference — and can re-evaluate it correctly if, say, the regulation changes. Without that recorded driver, someone might "simplify" the design and unknowingly break a compliance obligation. Drivers turn a decision into something safely re-examinable.

</details>

<details><summary><b>81.</b> What is the danger of an architecture diagram that is correct today but never updated?</summary>

A stale diagram is worse than no diagram, because readers trust it and then make decisions on a false picture of the system. Diagrams-as-code mitigates this by living in the repo and being updatable in the same PRs as code changes, but it still requires the discipline to update it. The cheapest diagram to keep current is the container-level one, which is part of why C4 stops there.

</details>

<details><summary><b>82.</b> In C4, can two containers in the same system communicate directly, and how is that shown?</summary>

Yes — direct container-to-container communication is shown as a labelled arrow between them on the container diagram, with the protocol and intent, e.g. "NAV API reads positions from Position Store via JDBC". C4 places no restriction on which containers may talk; the diagram simply records the actual relationships. Every such arrow should carry its technology so the integration is reviewable.

</details>

<details><summary><b>83.</b> How would you represent an external SWIFT messaging dependency in a C4 context diagram?</summary>

SWIFT (or the counterparty reached over SWIFT, such as a custodian) appears as an external system box outside your system boundary, with a labelled relationship like "sends settlement instructions via SWIFT MT54x". It is external because you do not own or deploy it. The label captures both the intent and the messaging standard so the dependency is explicit.

</details>

<details><summary><b>84.</b> Why might "what protocol does this arrow use" be a recurring review question across all your diagrams?</summary>

Because the protocol determines security, reliability, latency, and failure modes, and it is the single most commonly omitted label on architecture diagrams. Reviewers ask it repeatedly because its absence hides real risk — an unencrypted `FTP` versus `SFTP`, or a synchronous call versus an async queue, are very different designs. C4's rule to label every relationship with its technology is a direct response to this.

</details>

<details><summary><b>85.</b> What is the smallest viable ADR you could write, and is it still valuable?</summary>

The smallest viable ADR is essentially Nygard's five sections kept to a few sentences each: a title, status, a paragraph of context, a one-line decision, and a short consequences list. It is still highly valuable because it captures the why and the trade-off, which is what gets lost otherwise. Brevity is a feature — a tiny ADR that exists beats a perfect one that was never written.

</details>

<details><summary><b>86.</b> How does the ADR lifecycle status `Deprecated` differ from `Superseded`?</summary>

`Superseded` means a specific later ADR replaced this decision, so there is a forward link to the new record; `Deprecated` means the decision is no longer relevant or in use but is not directly replaced by a named successor. Both keep the original body intact as history. The distinction tells a reader whether to follow a link to a replacement or simply treat the decision as retired.

</details>

<details><summary><b>87.</b> Why is it useful for an ADR to record options that were considered and rejected (as MADR does)?</summary>

Because the rejected options and the reasons for rejecting them are exactly what stops a future team from re-proposing a path that was already evaluated and ruled out for good reasons. MADR's "Considered Options" plus pros-and-cons sections capture this. It saves rework and makes the chosen option's justification far more convincing than a bare assertion.

</details>

<details><summary><b>88.</b> A capstone submission has great C4 diagrams but reviewers still flag it. What are they most likely flagging?</summary>

They are most likely flagging the missing decisions — the ADRs explaining why the design is the way it is — and possibly unlabelled data flows. Beautiful diagrams still leave "why" implicit, and this lesson's whole point is that diagrams plus ADRs together are the deliverable. The fix is to add ADRs for the key choices the diagrams embody.

</details>

<details><summary><b>89.</b> What is the practical meaning of "ship C4 + ADRs with every capstone from here on without thinking about it"?</summary>

It means the habit becomes automatic: every system you design gets at least a context and container diagram as code in the repo, plus ADRs for its significant decisions, as a standard deliverable rather than an afterthought. The later capstones in the plan enforce this. The point is to internalise the practice now so it is muscle memory by the time the systems get large.

</details>

<details><summary><b>90.</b> Why does C4 deliberately avoid prescribing colours and shapes?</summary>

Because mandating a visual language would make the model harder to adopt and tie it to specific tools, whereas C4's value lies in its abstractions and the discipline of complete labelling, which work in any tool. Teams are free to add their own consistent styling (e.g. a colour per technology) on top. The model is about clear thinking, not a fixed icon set.

</details>

<details><summary><b>91.</b> How does the `model` versus `views` split in Structurizr DSL embody the C4 idea of "one model, many diagrams"?</summary>

The `model` block is the single source of truth for all elements and relationships, while each entry in the `views` block is just a filtered, zoomed projection of that model into a context, container, or component diagram. Because every view draws from the same model, the diagrams cannot contradict each other. This is the structural reason Structurizr keeps multi-level C4 diagrams consistent.

</details>

<details><summary><b>92.</b> When narrating an unfamiliar C4 container diagram cold, what should you read off first?</summary>

First the system boundary and what each container is and is responsible for, then each relationship's direction, intent, and protocol, and finally what external systems or actors it touches. Reading in that order — boundaries, then flows — mirrors exactly what a reviewer checks. If you cannot state a container's responsibility in a sentence, that is the first gap to call out.

</details>

<details><summary><b>93.</b> Why is "data flows" a distinct review concern from "boundaries"?</summary>

Boundaries are about what the pieces are and where their responsibilities start and stop; data flows are about how data and control actually move between them — direction, protocol, and intent on each arrow. A diagram can have crisp boundaries but wrong or missing flows, and vice versa. Reviewers check both because a design needs the boxes and the arrows to be right.

</details>

<details><summary><b>94.</b> How would an ADR help when an auditor asks "why is NAV history partitioned this way?"</summary>

The relevant ADR directly answers it: its Context records the query and retention forces, its Decision states the partitioning scheme, and its Consequences record the trade-offs accepted — all dated and attributable. If the scheme later changed, the superseding ADR shows when and why. This is the difference between an auditable answer and "the person who built it would know".

</details>

<details><summary><b>95.</b> What is the downside of using a heavyweight RFC process for every small decision?</summary>

It creates so much review friction that people stop recording decisions at all, or route around the process, which defeats the purpose. RFCs are for significant, contentious, or cross-cutting decisions; small reversible ones should go straight to a lightweight ADR. Matching the process weight to the decision's stakes is the skill.

</details>

<details><summary><b>96.</b> How can an RFC reduce the chance that an Accepted ADR is immediately challenged?</summary>

By surfacing objections and alternatives during the RFC review phase, before the decision is locked in, so that by the time it becomes an Accepted ADR the major concerns have already been aired and addressed. The ADR then records a decision that already has buy-in. Skipping the RFC on a contentious decision often means re-opening it as an ADR the week after it's accepted.

</details>

<details><summary><b>97.</b> Why store the `adr/` directory convention once and reuse it across all capstones?</summary>

Reusing one convention — location, naming (`NNNN-title.md`), template, and lifecycle rules — means every capstone's decision log looks the same and is instantly navigable, and you stop re-deciding format each time. Consistency is what makes the accumulated body of ADRs across the plan usable as one corpus. It also models the standardisation a real firm's governance imposes.

</details>

<details><summary><b>98.</b> What single sentence captures why this lesson sits at the start of the architecture phase?</summary>

Because C4 diagrams and ADRs are the artifacts through which an architect makes reasoning reviewable and decisions auditable, and every later capstone is expected to ship them — so you build the habit before the systems get complex. They convert design from hallway memory into versioned, reviewable, regulator-ready evidence. Master them now and they become invisible infrastructure for everything that follows.

</details>

<details><summary><b>99.</b> Why does C4 describe itself as "abstraction-first, notation-second"?</summary>

Because the value of the model is the shared set of abstractions — person, software system, container, component — and the disciplined zoom levels, not the boxes-and-arrows style you render them in. If everyone agrees what a "container" means, any tool or notation will communicate; if they don't, even a beautiful diagram misleads. So C4 invests in getting the abstractions and labels right and treats the visual notation as a free choice on top.

</details>

<details><summary><b>100.</b> What is the practical difference between linking an RFC from an ADR versus pasting the whole discussion into the ADR?</summary>

Linking keeps the ADR short and decision-focused while preserving the full deliberation for anyone who wants it, which fits the "short enough that people actually write them" principle; MADR even has a "More Information" section for exactly such links. Pasting the entire thread bloats the record so it stops being read. The rule of thumb is: the ADR records the decision and its consequences, and points to the RFC for the long-form debate.

</details>


## Phase 1 · 1.10.1 Modeling notations overview — 100 self-test questions

<details><summary><b>1.</b> What does the abbreviation UML stand for, and which body maintains it?</summary>

UML stands for Unified Modeling Language, a general-purpose graphical language for visualizing and specifying the structure and behavior of software systems. It is maintained by the Object Management Group (OMG), the same standards body behind BPMN and DMN. The current formal version is UML 2.5.1, released in December 2017.

</details>

<details><summary><b>2.</b> At this lesson's level, what is your goal with UML, BPMN, DMN, ArchiMate, ERD, and C4?</summary>

The explicit goal is reading fluency, not authoring mastery — you must name each notation and narrate what a diagram says when shown one cold. The point is that in a fund-industry workshop the business analyst brings BPMN, the vendor brings ArchiMate, and the DBA brings an ERD, and the architect reads all of them without a translator. Deep authoring practice comes later in Phase 4 (BPM) and Phase 8 (ArchiMate).

</details>

<details><summary><b>3.</b> A UML class diagram shows structure or behavior?</summary>

A UML class diagram shows static structure: the classes (or types/entities) in a system, their attributes and operations, and the relationships between them such as association, generalization, and composition. It answers "what things exist and how are they related" rather than "what happens over time." Behavior over time is the job of UML's interaction diagrams like the sequence diagram.

</details>

<details><summary><b>4.</b> A UML sequence diagram shows structure or behavior?</summary>

A UML sequence diagram shows interaction behavior: how objects or participants exchange messages over time to accomplish a scenario. The vertical axis represents time flowing downward, and horizontal arrows represent messages between lifelines. It answers "in what order do these parties call each other" — for example, how a NAV-calculation service, a pricing feed, and a register are invoked during end-of-day processing.

</details>

<details><summary><b>5.</b> In a UML sequence diagram, what does a vertical dashed line under a participant represent?</summary>

The vertical dashed line is the lifeline, representing the existence of that participant (object, actor, or system) over the duration shown. Time flows downward along the lifeline. A thin rectangle drawn over the lifeline is the activation bar, showing when that participant is actively executing in response to a message.

</details>

<details><summary><b>6.</b> In UML, what is the difference between a solid-arrowhead message and an open-arrowhead message on a sequence diagram?</summary>

A filled (solid) arrowhead conventionally denotes a synchronous message — the sender waits for the call to complete — while an open (line/stick) arrowhead denotes an asynchronous message or a reply. A dashed line with an open arrowhead is typically the return message. These conventions let you read whether a caller blocks, which matters when narrating a NAV pipeline where some feeds are fire-and-forget and others are awaited.

</details>

<details><summary><b>7.</b> What notation would you reach for to describe the class structure of a fund's data model at the object/system level?</summary>

A UML class diagram is the right reading tool for object/system-level structure such as the classes in an application's domain model. However, for a relational database schema specifically, an ERD is the more common and more precise choice. The class diagram shines when the model includes behavior (operations) and object-oriented relationships like inheritance, which a pure ERD does not express.

</details>

<details><summary><b>8.</b> What does BPMN stand for, and who maintains it?</summary>

BPMN stands for Business Process Model and Notation, an OMG standard for modeling business processes as flowcharts that both business and technical stakeholders can read. The current widely-used version is BPMN 2.0.2, published in January 2014, which standardized both the visual notation and an XML serialization. It is the notation a business analyst brings to a fund-operations workshop.

</details>

<details><summary><b>9.</b> What kind of question is BPMN designed to answer?</summary>

BPMN answers "how does this business process flow end to end" — the sequence of activities, decisions, events, and the participants (lanes) that carry them out. It is the natural choice for describing an order lifecycle or a transfer-agency flow, such as how a subscription order moves from an inbound EMT/order file through validation to settlement and register update. It models process, not data structure or static architecture.

</details>

<details><summary><b>10.</b> In BPMN, what is the difference between a task and a sub-process?</summary>

A task is an atomic unit of work in the process — a single activity that is not broken down further at that level of detail. A sub-process is a compound activity that contains its own flow of tasks and can be collapsed (shown as a rounded rectangle with a small plus marker) or expanded inline. Sub-processes let you read a high-level transfer-agency flow first, then drill into, say, the AML-check sub-process.

</details>

<details><summary><b>11.</b> In BPMN, what does a diamond shape (gateway) represent?</summary>

A diamond is a gateway, which controls how the sequence flow diverges or converges — it is the branching and merging logic of the process. An exclusive (XOR) gateway marked with an X takes exactly one outgoing path based on a condition; a parallel (AND) gateway marked with a plus splits into or joins concurrent paths. Reading gateways correctly tells you whether two activities happen in sequence, as alternatives, or in parallel.

</details>

<details><summary><b>12.</b> In BPMN, what do circles represent, and how do start, intermediate, and end events differ visually?</summary>

Circles are events — something that happens during the process. A start event uses a thin single-line circle, an intermediate event uses a double-line circle, and an end event uses a thick single-line circle. Markers inside the circle (an envelope for a message, a clock for a timer) tell you the trigger, such as a message-start event firing when an inbound order file arrives.

</details>

<details><summary><b>13.</b> In BPMN, what is the difference between a pool and a lane?</summary>

A pool represents a participant or organization in the process — for example the transfer agent versus the asset manager — and a message flow (dashed arrow) crosses between pools. A lane is a subdivision within a single pool, used to organize activities by role or system, such as separating the validation team's tasks from the settlement team's. Sequence flow (solid arrow) stays within a pool; only message flow crosses pool boundaries.

</details>

<details><summary><b>14.</b> In BPMN, what is the difference between a sequence flow and a message flow, and how are they drawn?</summary>

A sequence flow is a solid line with a filled arrowhead showing the order of activities within a single pool. A message flow is a dashed line with an open arrowhead showing communication of a message between two separate pools (participants). Confusing the two is a classic reading error: a dashed arrow between the asset manager and the transfer agent is them exchanging a message, not one ordering the other's internal steps.

</details>

<details><summary><b>15.</b> What does DMN stand for, and what is its core idea?</summary>

DMN stands for Decision Model and Notation, an OMG standard whose core idea is to separate decision logic from process flow. Instead of burying complex business rules inside BPMN gateways, you factor them into reusable decision tables and a Decision Requirements Diagram. The current formal version is DMN 1.5, adopted in August 2024, with a 1.6 beta released the following month.

</details>

<details><summary><b>16.</b> Why separate DMN decision logic from a BPMN process flow?</summary>

Separating them keeps each notation readable and each piece independently maintainable: the BPMN process shows the flow, and a single BPMN task or "business rule task" calls out to a DMN decision that holds the rules. When a fund's fee-tier or eligibility rules change, you edit one decision table rather than rewiring gateways across the process. It also lets business users own and audit the rules directly, which matters in a regulated context.

</details>

<details><summary><b>17.</b> What is a DMN decision table, and what are its main parts?</summary>

A DMN decision table is a tabular representation of decision logic with input columns, output columns, and rows of rules. Each row maps a combination of input conditions to an output result, and a hit policy (such as Unique, First, or Collect) governs what happens when multiple rows match. For example, inputs of investor type and investment amount could map to an output fee tier.

</details>

<details><summary><b>18.</b> In a DMN decision table, what does the hit policy control, and what does a "Unique" hit policy require?</summary>

The hit policy controls how the table resolves when zero, one, or several rules match a given input. The Unique hit policy (often abbreviated U) requires that at most one rule matches any input — the rules must not overlap — which makes the table unambiguous and easy to validate. Other policies like First (F), Any (A), or Collect (C) handle overlaps differently, so reading the hit-policy marker is essential to knowing what output to expect.

</details>

<details><summary><b>19.</b> What is a DMN Decision Requirements Diagram (DRD)?</summary>

A DRD is the graph-level view in DMN that shows how decisions depend on one another and on their input data and knowledge sources. Decisions are rectangles, input data are rounded "stadium" shapes, and arrows show information requirements. It lets you read which sub-decisions feed a final decision — for instance, an "eligibility" decision and a "fee tier" decision both feeding a final "accept order" decision.

</details>

<details><summary><b>20.</b> What is FEEL in the context of DMN?</summary>

FEEL stands for Friendly Enough Expression Language, the standard expression language defined by the DMN specification for writing the conditions and computations inside decision tables and boxed expressions. It is designed to be readable by business users while still being unambiguous and executable. Knowing FEEL exists explains why DMN cells can contain ranges and expressions rather than just literal values.

</details>

<details><summary><b>21.</b> What does ArchiMate model, and who maintains it?</summary>

ArchiMate is an enterprise-architecture modeling language maintained by The Open Group, designed to describe and relate the business, application, and technology layers of an enterprise in one coherent language. The current version is ArchiMate 3.2. It is the notation a vendor or enterprise architect brings when they want to show how a business service is realized by applications and underlying infrastructure together.

</details>

<details><summary><b>22.</b> What are the three core layers of ArchiMate?</summary>

The three core layers are the Business layer (business processes, services, actors, and roles), the Application layer (application components and application services), and the Technology layer (nodes, system software, and infrastructure services). ArchiMate uses service orientation and realization relationships to connect concrete elements to more abstract ones across these layers. This layering is exactly what lets one diagram show a fund-accounting business service traced down to the servers that run it.

</details>

<details><summary><b>23.</b> Beyond the three core layers, what additional aspects does ArchiMate 3.x include?</summary>

ArchiMate 3.x adds Motivation elements (stakeholders, drivers, goals, requirements, principles), a Strategy layer (resources, capabilities, courses of action), a Physical layer (equipment, facilities, materials) extending technology, and an Implementation and Migration layer for transition planning. These extensions let the language express not just the current structure but why it exists and how it will change, which suits regulatory-driven transformation programs like a DORA remediation roadmap.

</details>

<details><summary><b>24.</b> What question does ArchiMate answer that BPMN cannot?</summary>

ArchiMate answers "how does our enterprise hang together across business, application, and technology" — it traces a business service down through the applications that realize it to the infrastructure that runs it. BPMN cannot do this; BPMN only models the flow of a single business process and has no concept of the application components or technology nodes underneath. You reach for ArchiMate for landscape and traceability, BPMN for a specific process flow.

</details>

<details><summary><b>25.</b> What does ERD stand for, and what does it model?</summary>

ERD stands for Entity-Relationship Diagram, the classic notation for data modeling — it shows entities (things you store data about), their attributes, and the relationships between them. It is the DBA's and data modeler's primary tool for designing and communicating a relational schema. For example, an ERD for a fund register would show Investor, Holding, Fund, and Transaction entities and the relationships linking them.

</details>

<details><summary><b>26.</b> In ERD crow's-foot notation, how is a many relationship shown, and how is "one"?</summary>

The crow's-foot notation draws the "many" end of a relationship as a three-pronged splayed line (the crow's foot) touching the entity, and the "one" end as a single perpendicular bar. Additional marks show optionality: a circle (O) near the end means zero is allowed, a bar means at least one is required. So a line reading "one bar" at Fund and a "crow's foot with a bar" at Holding reads as "one fund has one-or-many holdings."

</details>

<details><summary><b>27.</b> What does IDEF1X stand for, and where is it still mandated?</summary>

IDEF1X is a data-modeling notation from the IDEF (Integration DEFinition) family, originally developed for the U.S. Air Force ICAM program and standardized as a U.S. federal standard. It is a rigorous, relational-style entity-relationship notation still mandated in some U.S. government and defense data-modeling contexts. Its existence is why a single "ER diagram" can look quite different depending on whether it follows crow's-foot, Barker, or IDEF1X conventions.

</details>

<details><summary><b>28.</b> How does IDEF1X distinguish an independent entity from a dependent entity visually?</summary>

In IDEF1X an independent entity (one whose primary key does not depend on another entity) is drawn as a box with square corners, while a dependent (identifier-dependent) entity is drawn as a box with rounded corners. A dependent entity is one whose primary key includes a foreign key from its parent — for example a Transaction line whose identity depends on the parent Order. Reading the corner shape immediately tells you about identifying relationships.

</details>

<details><summary><b>29.</b> What does C4 stand for, and what are its four levels?</summary>

C4 is a software-architecture diagramming approach whose four levels are Context, Container, Component, and Code — the four C's. Each level zooms in one step: Context shows the system and its external users and systems, Container shows the deployable/runnable units and their technologies, Component shows the components inside a container, and Code shows the lowest-level implementation detail. It gives you a consistent way to describe one software system at increasing zoom.

</details>

<details><summary><b>30.</b> In C4, what does a "container" mean, and why is the term sometimes confusing?</summary>

In C4 a container is a separately runnable or deployable unit that executes code or stores data — for example a web application, an API service, a database, or a message broker. It is confusing because the word collides with Docker/OS containers, but C4 containers are about application boundaries, not virtualization. A C4 container diagram of a fund-data platform would show, say, the ingestion API, the NAV-calculation service, and the Postgres warehouse as separate containers.

</details>

<details><summary><b>31.</b> Which C4 level shows the highest-level view and to whom is it usually shown?</summary>

The System Context diagram is the highest-level C4 view; it shows your software system as a single box surrounded by its users (people) and the external systems it interacts with. It is aimed at the broadest audience, including non-technical stakeholders, because it deliberately hides internal detail. For a fund platform it might show the system, the operations users, and external systems like a SWIFT gateway and a market-data feed.

</details>

<details><summary><b>32.</b> What supplementary diagrams does the C4 model define beyond the four core levels?</summary>

Beyond Context, Container, Component, and Code, C4 defines supplementary diagrams: the System Landscape diagram (multiple systems in a broader enterprise context), the Dynamic diagram (runtime collaboration, similar in spirit to a sequence diagram), and the Deployment diagram (how containers map to infrastructure and environments). These cover questions the static four levels do not, such as runtime behavior and physical deployment.

</details>

<details><summary><b>33.</b> Is C4 a formal notation with fixed symbols like UML or BPMN?</summary>

No — C4 is deliberately notation-independent and tooling-independent; it prescribes the set of abstractions and the hierarchy of diagrams, not a strict shape grammar. You can render C4 with simple boxes and arrows as long as the diagram is self-explanatory with a clear title, key/legend, and meaningful labels. This contrasts with BPMN and UML, which define precise symbols whose meaning you must memorize.

</details>

<details><summary><b>34.</b> Which notation best answers "how does an order get from an EMT file to the register"?</summary>

BPMN is the best fit, because that is a business-process flow question — a sequence of activities, decisions, and handoffs across participants. You would model the inbound EMT/order file arriving as a message start event, validation tasks, gateways for accept/reject, and the register update as the end state. This is exactly the kind of "question to notation" mapping the lesson's cheat sheet is meant to capture.

</details>

<details><summary><b>35.</b> Which notation best answers "what fee tier applies to this investor and amount"?</summary>

DMN is the best fit, because that is decision logic, not process flow — it maps combinations of inputs (investor type, amount) to an output (fee tier) in a decision table. Embedding such rules in a BPMN gateway would be unreadable and hard to maintain, which is precisely why DMN separates decisions from process. The BPMN process would simply invoke the DMN decision at the right step.

</details>

<details><summary><b>36.</b> Which notation best answers "how is our fund-accounting business service realized by applications and infrastructure"?</summary>

ArchiMate is the best fit, because the question spans business, application, and technology layers and asks about realization — exactly what ArchiMate's layered service-oriented model expresses. No other notation in this lesson can trace a business service through the applications that realize it down to the technology that runs it. BPMN, DMN, ERD, and C4 each cover only one slice of that picture.

</details>

<details><summary><b>37.</b> Which notation best answers "what is the relational schema of the investor register"?</summary>

An ERD is the best fit, because schema design — entities, attributes, primary and foreign keys, and cardinalities — is precisely what entity-relationship diagrams express. A UML class diagram could approximate it, but the ERD is the conventional, more precise tool for relational databases. IDEF1X is an alternative ERD dialect you might encounter in stricter or government-adjacent contexts.

</details>

<details><summary><b>38.</b> Which notation best answers "how do the containers of our internal NAV platform fit together"?</summary>

C4, specifically the Container diagram, is the best fit because the question is about the high-level software architecture of one system — its runnable units and the technologies and communications between them. C4 was designed exactly to answer this at a glance for a development team. ArchiMate could also show it but operates at enterprise scope; C4 is lighter-weight and software-focused.

</details>

<details><summary><b>39.</b> You are shown a diagram with rounded-rectangle activities, diamonds, and pools with dashed arrows between them. Which notation is it?</summary>

This is BPMN. Rounded-rectangle activities (tasks), diamond gateways, swimlanes organized into pools, and dashed message flows crossing between pools are all distinctive BPMN constructs. The combination of pools-with-message-flows plus diamonds is the tell, since neither UML nor C4 uses that exact vocabulary.

</details>

<details><summary><b>40.</b> You are shown a diagram with lifelines and horizontal arrows where time flows downward. Which notation is it?</summary>

This is a UML sequence diagram. The defining features are vertical lifelines (often dashed) for participants, time flowing downward, and horizontal message arrows between lifelines in chronological order. Activation bars on the lifelines reinforce the identification. No other notation in this lesson uses a top-to-bottom time axis with lifelines.

</details>

<details><summary><b>41.</b> You are shown boxes connected by lines ending in three-pronged "crow's feet." Which notation is it?</summary>

This is an ERD using crow's-foot notation. The crow's-foot symbol at a relationship end denoting "many," combined with entity boxes listing attributes, is unmistakable. If the boxes instead had rounded versus square corners with no crow's feet, you would suspect IDEF1X rather than crow's-foot ERD.

</details>

<details><summary><b>42.</b> You are shown layered boxes labeled "business," "application," and "technology" with realization arrows. Which notation is it?</summary>

This is ArchiMate. The explicit business/application/technology layering with service-orientation and realization relationships connecting them is ArchiMate's signature. The distinctive element notation (such as the rounded-corner business-process arrow shape and layered color bands) further confirms it.

</details>

<details><summary><b>43.</b> You are shown a simple "boxes and arrows" diagram titled "Container diagram" with technologies labeled on each box. Which notation is it?</summary>

This is a C4 Container diagram. The tells are the explicit C4 level name in the title, plain boxes annotated with their technology choices, people and external systems around the edge, and clearly labeled relationships. Because C4 is notation-independent, the labels and title — not special symbols — are what identify it.

</details>

<details><summary><b>44.</b> A diagram uses a diamond with a plus sign and two outgoing arrows that both proceed. What does it mean in BPMN?</summary>

A diamond with a plus marker is a parallel (AND) gateway, and when used to split it activates all outgoing paths simultaneously — both branches proceed in parallel. Later a matching parallel gateway used as a join waits for all incoming branches before continuing. So this reads as "do both of these activities concurrently," for instance run the AML check and the sanctions check at the same time.

</details>

<details><summary><b>45.</b> A BPMN diamond marked with an "X" splits into three labeled outgoing flows. What does it mean?</summary>

A diamond marked with an X is an exclusive (XOR) gateway, and on a split it selects exactly one of the outgoing flows based on the conditions labeling each path. Only one branch is taken, unlike the parallel gateway. For an order, an XOR gateway might route to "accept," "reject," or "manual review" depending on validation results.

</details>

<details><summary><b>46.</b> In UML, what is the difference between association, aggregation, and composition?</summary>

All three are structural relationships between classes; the difference is ownership strength. A plain association (solid line) just means the classes are related; aggregation (hollow diamond) is a "has-a" whole-part relationship where the part can exist independently; composition (filled diamond) is a stronger whole-part where the part's lifetime is bound to the whole. For example, a Fund composes its NAV-history records (they die with the fund) but merely aggregates the Investors that hold it.

</details>

<details><summary><b>47.</b> In a UML class diagram, what do the symbols at the ends of an association line tell you?</summary>

They tell you multiplicity (cardinality) — how many instances of one class relate to one instance of the other, written as numbers or ranges like `1`, `0..1`, `1..*`, or `*`. They may also carry role names and navigability arrows. Reading `1` at Fund and `0..*` at Holding means one fund can have zero or many holdings, mirroring the cardinality an ERD would express with crow's feet.

</details>

<details><summary><b>48.</b> What does the multiplicity `1..*` mean on a UML association?</summary>

The multiplicity `1..*` means "one or more" — at least one instance and no fixed upper bound. The `*` (or `0..*`) means "zero or more," and `0..1` means "optional, at most one." So an Order with a `1..*` multiplicity to OrderLine means every order must have at least one line, a constraint you would also enforce in the database the ERD describes.

</details>

<details><summary><b>49.</b> How does an ERD relationship cardinality compare to a UML class diagram multiplicity?</summary>

They express the same idea — how many instances relate to how many — but with different notation: ERDs use crow's-foot (or other) symbols at the line ends, while UML uses numeric multiplicities like `1`, `0..1`, and `*`. A crow's foot with a circle equals UML `0..*`; a crow's foot with a bar equals UML `1..*`. Recognizing this equivalence is part of reading both notations without a translator.

</details>

<details><summary><b>50.</b> Why is BPMN described as "executable," and what makes that possible?</summary>

BPMN 2.0 is called executable because the standard defines not only the visual notation but also a precise XML serialization and execution semantics, so compliant process engines can run a BPMN model directly. This means a transfer-agency flow drawn in BPMN can, with the right attributes filled in, be deployed to an engine that orchestrates real tasks. UML and C4, by contrast, are descriptive and not executed by an engine.

</details>

<details><summary><b>51.</b> Can DMN decision tables be executed, and by what?</summary>

Yes — DMN, like BPMN, has standardized execution semantics, and DMN-compliant engines can evaluate decision tables and DRDs at runtime, often using FEEL for the expressions. This lets a fee-tier or eligibility decision be authored as a table and called by a running process. The separation means the rules can be changed and redeployed without altering the surrounding BPMN process.

</details>

<details><summary><b>52.</b> What is the relationship between BPMN and DMN in a typical design?</summary>

They are complementary: BPMN models the process flow and, at a decision point, delegates to DMN rather than encoding complex rules in a gateway. A BPMN "business rule task" invokes a DMN decision, which returns a result the process then acts on. This keeps the BPMN readable and the rules independently maintainable and auditable — valuable when fund rules must be traced for a regulator.

</details>

<details><summary><b>53.</b> Why might an architect prefer C4 over UML for explaining a system to a mixed audience?</summary>

C4 offers a small, consistent set of abstractions (Context, Container, Component, Code) with a clear zoom hierarchy and no specialized symbol grammar to learn, so a mixed business-and-technical audience can follow it quickly. UML is precise but its breadth and strict symbols can overwhelm non-specialists. C4's self-explanatory boxes-and-arrows with explicit legends trade formal rigor for communication clarity.

</details>

<details><summary><b>54.</b> What does a C4 Component diagram show, and what is the common pitfall in keeping it?</summary>

A C4 Component diagram zooms inside one container to show its components — groupings of related functionality — and how they collaborate. The common pitfall is that component-level diagrams drift out of date fastest because they are closest to the code, so many teams generate or maintain only Context and Container diagrams by hand and derive lower levels from code when possible. This is why C4 emphasizes keeping diagrams cheap to produce.

</details>

<details><summary><b>55.</b> What does a C4 Code diagram correspond to, and how often is it drawn?</summary>

The C4 Code diagram is the lowest level, corresponding roughly to a UML class diagram or entity-relationship view of the implementation detail inside a single component. In practice it is rarely drawn by hand because it is volatile and high-effort; when needed it is usually generated from the codebase by an IDE or tool. C4's author recommends most teams stop at the Component level.

</details>

<details><summary><b>56.</b> Why is the lesson's "notation chooser" cheat sheet structured as question to notation to tool?</summary>

Because the architect's real skill is matching the question being asked to the notation that answers it and then to a tool that produces it — not memorizing every symbol of every language. A row reads, for example, "how does an order get from EMT file to register?" to BPMN to a BPMN tool. Building this one page forces you to articulate which question each notation answers and, crucially, which it cannot.

</details>

<details><summary><b>57.</b> Which notation answers "what decision logic applies" and which answers "what is the process flow"?</summary>

DMN answers "what decision logic applies" via decision tables and DRDs, while BPMN answers "what is the process flow" via activities, gateways, and events. The whole point of DMN's existence is to pull the decision logic out of the BPMN flow so each stays clear. In a fund order pipeline, BPMN shows the steps and DMN holds the eligibility and fee rules invoked at one of those steps.

</details>

<details><summary><b>58.</b> Which notation answers "what data do we store and how is it related," and name two dialects of it.</summary>

The ERD (Entity-Relationship Diagram) answers what data is stored and how entities relate, through entities, attributes, keys, and cardinalities. Two common dialects are crow's-foot notation (widely used in commercial tools) and IDEF1X (rigorous, still mandated in some U.S. government/defense contexts). Barker notation is a third dialect you may also encounter.

</details>

<details><summary><b>59.</b> Which two notations in this lesson can both depict runtime interaction over time, and how do they differ?</summary>

The UML sequence diagram and the C4 Dynamic diagram both depict runtime interaction. The sequence diagram is a formal UML notation with lifelines, activation bars, and strict message semantics; the C4 Dynamic diagram is a lighter, notation-independent view that numbers interactions on a Context- or Container-level picture. Use the sequence diagram for rigor, the C4 Dynamic diagram for an accessible runtime walk-through.

</details>

<details><summary><b>60.</b> A vendor's slide shows business processes realized by application components realized by technology nodes. What can you infer about the right phase to study it deeply?</summary>

The slide is ArchiMate, and the lesson explicitly defers deep ArchiMate practice to Phase 8; at this point you only need to read it and name it. The layered realization chain — business to application to technology — is the recognizable signature. Knowing it is ArchiMate lets you engage the vendor on the same terms even before you can author such models yourself.

</details>

<details><summary><b>61.</b> In ArchiMate, what does a "realization" relationship express?</summary>

A realization relationship expresses that a more concrete element realizes (provides the concrete implementation of) a more abstract element — for instance an application component realizes an application service, or an application service realizes a business service. It is the backbone that lets ArchiMate connect the layers vertically. Reading realization arrows is how you trace a business capability down to the system that delivers it.

</details>

<details><summary><b>62.</b> What is the danger of using BPMN gateways to encode complex business rules instead of DMN?</summary>

Encoding complex rules as nested gateways produces a tangled, hard-to-read "gateway spaghetti" process that mixes flow with logic and is painful to change or audit. DMN exists precisely to avoid this by holding the rules in a table the process calls out to. In a regulated fund context, the auditable, single-table form of DMN is far easier to review than rules scattered across branches.

</details>

<details><summary><b>63.</b> What is the difference between a UML use-case diagram and a UML class diagram (awareness)?</summary>

A use-case diagram shows actors and the use cases (goals) a system supports — a high-level "what can users do" view — whereas a class diagram shows the internal static structure of types and their relationships. Use-case diagrams capture functional scope from the user's perspective; class diagrams capture the design's structure. At reading level, recognize the stick-figure actors and ovals of a use-case diagram versus the attribute/operation boxes of a class diagram.

</details>

<details><summary><b>64.</b> When narrating a BPMN diagram cold, what should you identify first?</summary>

First identify the pools and lanes to know who the participants and roles are, then find the start event(s) to know what triggers the process, then trace sequence flow through tasks and gateways to the end event(s). Reading in that order — actors, trigger, flow, outcome — keeps you oriented. For a transfer-agency flow you would say, for example, "the transfer agent's pool starts on receipt of an order message, validates, branches on an XOR gateway, and ends with a register update."

</details>

<details><summary><b>65.</b> When narrating a UML sequence diagram cold, what should you identify first?</summary>

First identify the participants across the top (the lifelines) and the scenario the diagram represents, then read the messages top to bottom to follow the order of interaction, noting synchronous versus asynchronous arrows and any return messages. The downward time axis is the key to narration. You would say, for instance, "the scheduler calls the NAV service, which synchronously requests prices from the feed, then asynchronously notifies the register."

</details>

<details><summary><b>66.</b> When shown an unfamiliar diagram, what three steps does the lesson's self-test prescribe?</summary>

The self-test is to take three unfamiliar diagrams, (1) identify each notation, (2) name it correctly, and (3) narrate what each diagram actually says. This rehearses the real workshop skill of reading a notation cold without a translator. The "Done when" criteria require exactly this: name the notation and read it correctly when shown a diagram cold.

</details>

<details><summary><b>67.</b> Why is recognizing the notation a prerequisite to narrating the diagram?</summary>

Because the same shapes mean different things in different notations — a diamond is a gateway in BPMN but a decision in a flowchart, a box can be a class, an entity, a container, or an ArchiMate element. Until you know which language you are reading, you cannot reliably interpret the symbols. Naming the notation first is what prevents you from mis-narrating a vendor's ArchiMate as if it were a C4 diagram.

</details>

<details><summary><b>68.</b> Where do the authoritative specifications for UML, BPMN, and DMN live, and what should you read at this stage?</summary>

They live on the OMG website at omg.org under the respective spec pages (UML, BPMN, DMN). At this stage you read only the intro/overview sections of each spec plus one example diagram each — not the full multi-hundred-page documents. The aim is reading fluency and one worked example per notation, captured into your reference folder.

</details>

<details><summary><b>69.</b> Where is the authoritative source for ArchiMate, and for C4?</summary>

ArchiMate's authoritative source is The Open Group's ArchiMate specification and overview pages (opengroup.org / pubs.opengroup.org), with the current version being 3.2. C4's authoritative source is c4model.com, the site maintained by the model's creator. ERD/IDEF1X grounding for this lesson comes from the DAMA-DMBOK, chapter 5.

</details>

<details><summary><b>70.</b> What is the first deliverable of the lesson's "Do" steps?</summary>

The first deliverable is to collect one example diagram of each notation — UML, BPMN, DMN, ArchiMate, ERD/IDEF1X, and C4 — drawn from the spec intros and c4model.com, into a single reference folder. Having a concrete example of each in one place is what makes the notations recognizable later. It is the raw material for the cheat sheet and the cold-reading self-test.

</details>

<details><summary><b>71.</b> What must each row of the one-page "notation chooser" cheat sheet contain?</summary>

Each row maps a question to a notation to a tool, and must include a fund-industry example question. For instance: "how does an order get from EMT file to register?" to BPMN to a BPMN tool. Adding the fund-flavored question per row is one of the explicit "Done when" criteria, ensuring the sheet is grounded in your real domain.

</details>

<details><summary><b>72.</b> Why does the lesson stress that the architect reads BA, vendor, and DBA diagrams "without a translator"?</summary>

Because in fund-industry workshops different roles bring different notations — the BA brings BPMN, the vendor brings ArchiMate, the DBA brings an ERD — and the architect is the one person expected to read all of them. Needing a translator slows decisions and cedes authority. The lesson's reading-fluency goal is precisely to make you that fluent reader across notations.

</details>

<details><summary><b>73.</b> Which notation is the natural home for "order lifecycle" and "transfer-agency flows" per the syllabus?</summary>

BPMN is named in the syllabus as the executable business-process notation for the order lifecycle and transfer-agency flows. These are sequences of activities, decisions, and handoffs — exactly process-flow questions. You would model them as BPMN processes with events, tasks, gateways, and lanes for the responsible teams.

</details>

<details><summary><b>74.</b> How does a UML class diagram differ from an ERD even though both can show entities and relationships?</summary>

A UML class diagram can include behavior (operations/methods) and object-oriented relationships such as inheritance and composition, and it models classes in a software design. An ERD focuses purely on data — entities, attributes, keys, and cardinalities — and maps naturally to a relational schema. For database design the ERD is conventional and precise; for object-model design the class diagram fits better.

</details>

<details><summary><b>75.</b> What does it mean that a notation "answers some questions but not others," and give an example with C4 and DMN.</summary>

It means each notation has a defined scope and using it outside that scope produces a poor or impossible diagram. C4 answers "how is this one software system structured" but cannot express business decision logic; DMN answers "what is the decision rule" but cannot show software containers or deployment. The cheat sheet's value is recording both the question each notation answers and the ones it cannot.

</details>

<details><summary><b>76.</b> In BPMN, what does an envelope marker inside a start-event circle indicate?</summary>

An envelope marker inside a start event indicates a message start event — the process is triggered by the arrival of a message. In a fund pipeline this typically models the inbound order or EMT file arriving and kicking off the transfer-agency process. Other markers, like a clock, would indicate a timer start (e.g., a scheduled end-of-day run).

</details>

<details><summary><b>77.</b> What is a "boundary event" in BPMN at a reading level?</summary>

A boundary event is an event attached to the edge of an activity that can interrupt or branch off from it when triggered — for example a timer on a task that fires if the task runs too long, or an error event that catches a failure. You read it as "while this activity runs, if X happens, take this alternate path." It lets a process model exceptions like a timeout on waiting for a settlement confirmation.

</details>

<details><summary><b>78.</b> Why is image pinning unrelated here — what's the genuine cross-notation risk when reading a diagram with no legend?</summary>

The genuine risk is misidentifying the notation or the cardinality because, without a legend, the same shape (a box, a diamond, a line end) is ambiguous across notations. C4 explicitly requires every diagram to carry a title and key/legend for exactly this reason. When reading a legend-less diagram, your first job is to infer the notation from distinctive constructs before trusting any symbol's meaning.

</details>

<details><summary><b>79.</b> How would you model "should this subscription order be accepted" cleanly across BPMN and DMN?</summary>

Model the order's journey as a BPMN process — receive order, validate, settle, update register — and at the validation step place a BPMN business rule task that invokes a DMN "accept order" decision. The DMN decision's DRD might combine an eligibility decision and a fee-tier decision, each a table evaluated with FEEL. This keeps the flow readable in BPMN and the rules auditable in DMN, ideal for a regulated transfer-agency setting.

</details>

<details><summary><b>80.</b> What is the ArchiMate notion of a "service," and why is it central?</summary>

In ArchiMate a service is an externally visible unit of functionality that an element exposes to others, defined at each layer (business service, application service, technology service). It is central because ArchiMate is service-oriented: higher layers consume the services that lower layers provide, and realization relationships connect them. This is what lets a business service be traced to the application and technology services that deliver it.

</details>

<details><summary><b>81.</b> When would IDEF1X be the mandated notation rather than crow's-foot ERD?</summary>

IDEF1X is mandated chiefly in certain U.S. federal and defense data-modeling environments where it is the prescribed standard, owing to its origin in the Air Force ICAM program and its later federal standardization. In commercial and fund-industry settings, crow's-foot or Barker notation is far more common. Knowing IDEF1X exists prevents you from being thrown when a government-adjacent system delivers models in that dialect.

</details>

<details><summary><b>82.</b> What is a DRD "knowledge source," and what does it represent?</summary>

In a DMN Decision Requirements Diagram, a knowledge source represents the authority or origin of the decision logic — a person, document, regulation, or policy that the decision must comply with. It is drawn as a shape with a wavy bottom edge and connected to decisions by an authority requirement. For a fund decision, a knowledge source might be the UCITS eligibility rules or the fund prospectus that governs the logic.

</details>

<details><summary><b>83.</b> Why does the lesson place this notations overview before Phase 4 (BPM) and Phase 8 (ArchiMate)?</summary>

Because reading fluency across all the notations is a prerequisite to going deep on any one of them: Phase 4 dives into BPM/BPMN and Phase 8 practices ArchiMate, and both assume you can already recognize and read the surrounding notations. Establishing the map first prevents later phases from stalling on "what am I even looking at." It also makes you immediately useful in mixed workshops well before the deep phases.

</details>

<details><summary><b>84.</b> A diagram has stick-figure actors connected to ovals inside a system boundary box. Which notation and what does it show?</summary>

This is a UML use-case diagram; the stick figures are actors and the ovals are use cases representing goals the system supports, with the box marking the system boundary. It answers "who uses the system and for what" at a high level, not how it is built. Recognize it as distinct from a sequence diagram (which has lifelines and a time axis).

</details>

<details><summary><b>85.</b> What is the practical difference between "reading" a notation and "authoring" one, as this lesson frames it?</summary>

Reading means you can look at someone else's diagram, name the notation, and correctly narrate what it says; authoring means you can produce correct, well-formed diagrams from scratch. This lesson targets reading only, because in workshops you mostly consume others' diagrams. Authoring fluency in BPMN and ArchiMate is built later, deliberately, in Phases 4 and 8.

</details>

<details><summary><b>86.</b> Which notation would a DBA most likely bring to a fund-data workshop, and what would it show?</summary>

A DBA would most likely bring an ERD, showing the relational schema — entities like Fund, Investor, Holding, and Transaction, their attributes and keys, and the cardinalities between them. It answers what data is stored and how it is related, the DBA's core concern. As the architect you must read it fluently alongside the BA's BPMN and the vendor's ArchiMate.

</details>

<details><summary><b>87.</b> What is the risk of treating a C4 diagram as if it follows a strict symbol standard?</summary>

Because C4 is notation-independent, two C4 diagrams of the same system may use different shapes and colors, so assuming a fixed symbol grammar leads you to over-read meaning into styling. What carries meaning in C4 is the level (Context/Container/Component), the labels, the relationships, and the legend — not the specific box shape. Read the title and key first to know which level and conventions apply.

</details>

<details><summary><b>88.</b> How do BPMN message flows help you read an inter-organization fund process?</summary>

Message flows (dashed arrows crossing pools) show the messages exchanged between separate organizations — for example the asset manager sending an order to the transfer agent, and the transfer agent returning a confirmation. Following them tells you who communicates what to whom, independent of each party's internal steps (sequence flow). This is essential for reading multi-party flows like subscription, redemption, and settlement.

</details>

<details><summary><b>89.</b> Why is DMN's separation of logic especially valuable in a DORA/regulated context?</summary>

Because regulators and auditors need to see and verify decision rules clearly, and a self-contained DMN decision table is far easier to inspect, version, and trace than rules buried in process branches or code. DMN also lets business and compliance owners review the logic directly. This auditability and changeability aligns with DORA's emphasis on governance and traceability of automated decisions.

</details>

<details><summary><b>90.</b> What does a "lane" tell you that a "task" alone does not in BPMN?</summary>

A lane tells you which role, team, or system is responsible for the tasks placed inside it, adding the "who" to the "what." A task alone says an activity happens; the lane it sits in says who performs it. So reading lanes lets you say, for example, that validation is the operations team's task while final approval sits in the compliance lane.

</details>

<details><summary><b>91.</b> How can you tell a UML class diagram from a C4 Code diagram if both show classes?</summary>

You often cannot tell purely from the shapes, because a C4 Code diagram is typically rendered as a UML class (or ER) diagram — C4 borrows existing notations at that level. The distinguishing context is the diagram's stated level and its place in a C4 hierarchy; a Code diagram is labeled as such and zooms into one C4 component. Absent that framing, treat class-box-with-attributes-and-operations as UML.

</details>

<details><summary><b>92.</b> What is the minimum each diagram should carry so that a cold reader can interpret it, per C4's guidance?</summary>

Per C4, every diagram should have a clear, descriptive title, a key/legend explaining the notation and any colors or shapes, and meaningful labels on both elements and relationships. This makes the diagram self-explanatory to someone seeing it for the first time. The principle generalizes: a legend-less diagram forces the reader to guess the notation, which is exactly the failure mode this lesson trains you to avoid.

</details>

<details><summary><b>93.</b> In ArchiMate, what is the Motivation extension used to capture?</summary>

The Motivation elements capture the "why" behind an architecture: stakeholders, drivers, assessments, goals, outcomes, principles, requirements, and constraints. They let a model justify why elements exist and what they must satisfy, linking architecture to business intent. In a regulated program you might model a DORA requirement as a driver and trace it to the application changes that satisfy it.

</details>

<details><summary><b>94.</b> What does the Implementation and Migration layer add to an ArchiMate model?</summary>

It adds elements for planning change — work packages, deliverables, implementation events, plateaus (stable intermediate states), and gaps — so the model can express the transition from a current to a target architecture. This turns ArchiMate from a static snapshot into a roadmap. It is how you would show, for instance, the phased migration of a fund-accounting platform to a new application landscape.

</details>

<details><summary><b>95.</b> Summarize the one-line scope of each of the six notations in this lesson.</summary>

UML covers system structure (class) and interaction behavior (sequence); BPMN covers executable business-process flow; DMN covers decision logic separated from flow; ArchiMate covers business, application, and technology layers in one enterprise language; ERD/IDEF1X covers data modeling and relational schema; and C4 covers software architecture at four zoom levels. Each answers a distinct question, and the architect's skill is matching question to notation.

</details>

<details><summary><b>96.</b> Why is "narrate what the diagram says" a better test of fluency than "name the notation"?</summary>

Naming proves only recognition, whereas narrating proves you can actually decode the symbols into meaning — read the flow, the cardinalities, the layers, or the rules. The lesson's "Done when" deliberately requires both: name it and read it correctly. Being able to walk a stakeholder through an unfamiliar BPMN or ArchiMate diagram on the spot is the real workshop capability.

</details>

<details><summary><b>97.</b> If a single diagram tried to show process flow, decision rules, data schema, and infrastructure at once, what would be wrong?</summary>

It would violate the principle that each notation answers a bounded set of questions — cramming process (BPMN), rules (DMN), data (ERD), and infrastructure (ArchiMate/C4) into one diagram makes all of them unreadable. The correct approach is separate, linked diagrams in the right notation for each concern, as DMN's split from BPMN exemplifies. Recognizing this is part of choosing notations well, the heart of the cheat-sheet exercise.

</details>

<details><summary><b>98.</b> In a UML class diagram, what does a hollow triangle arrowhead pointing to one class mean?</summary>

A hollow (unfilled) triangle arrowhead denotes generalization — inheritance — pointing from the subclass to its superclass; it reads "is a kind of." For instance an EquityFund and a BondFund class might both generalize to a Fund superclass, sharing its attributes and operations. Do not confuse it with the open stick arrowhead used for navigation or the diamonds used for aggregation and composition.

</details>

<details><summary><b>99.</b> How does an ISIN-keyed instrument reference data model illustrate the difference between an ERD and a BPMN diagram?</summary>

An ERD of instrument reference data shows the static structure — an Instrument entity keyed by ISIN, related to Issuer, Currency, and Price entities with their cardinalities — answering "what do we store and how is it related." A BPMN diagram instead shows the process of how that ISIN gets onboarded, enriched, and validated over time, answering "what happens in what order." The same fund-data domain needs both: the ERD for the schema and the BPMN for the workflow that populates it.

</details>

<details><summary><b>100.</b> How would you use these notations together to document an end-to-end fund subscription, naming each?</summary>

Use BPMN for the subscription process flow across the asset manager and transfer-agent pools; DMN for the eligibility and fee-tier decisions invoked within it; an ERD for the register schema the process writes to; ArchiMate to show the business service realized by the applications and infrastructure; and C4 to detail the internal software architecture of your own platform. Each notation answers its own question, and together they form a coherent, role-readable picture.

</details>


## Phase 1 · 9.1.3 Local data sandboxes — 100 self-test questions

<details><summary><b>1.</b> What is a "local data sandbox" in the context of this study plan, and why does the whole four-year lab depend on it?</summary>

It is a reproducible, self-contained data stack you can stand up on your own laptop with one command, typically a `docker-compose.yml` describing services like Postgres, MinIO, and an analytical engine. The lab depends on it because every capstone builds on the assumption that a stranger can clone the repo and get the identical stack running; a stack only you can bring up is a stack nobody can trust or review. The discipline of a one-command, reproducible stack is the same discipline that later makes your Azure environments reviewable.

</details>

<details><summary><b>2.</b> What does the `docker compose up` command do at a high level?</summary>

It reads the `docker-compose.yml` (and any override files) in the current directory, creates the declared networks and volumes if missing, pulls or builds the images, and starts every defined service as containers in dependency order. By default it runs in the foreground and streams logs; adding `-d` runs the stack detached in the background. It is the single command that turns a declarative file into a running multi-container stack.

</details>

<details><summary><b>3.</b> What is a Compose "service" versus a "container"?</summary>

A service is the declarative definition in `docker-compose.yml` — an image, ports, environment, volumes, and dependencies — describing how one logical component should run. A container is a concrete running instance of that service; one service usually maps to one container but can be scaled to several replicas. The distinction matters because you reason and version the service definition, while Compose manages the container instances for you.

</details>

<details><summary><b>4.</b> What does `depends_on` express in a Compose file?</summary>

`depends_on` declares that one service depends on another, which controls the order in which Compose starts and stops containers — the dependency is started before the dependent and stopped after it. In short form it is just a list of service names; in long form each dependency carries a `condition`. It is the primary tool for expressing the startup graph of your stack.

</details>

<details><summary><b>5.</b> With the short-form `depends_on`, what exactly does Compose guarantee about startup?</summary>

Short-form `depends_on` only guarantees that the dependency container is created and started before the dependent — it is equivalent to the `service_started` condition. It does NOT wait for the dependency's application to be ready to accept connections; Postgres can be "started" while its server is still initialising. This gap is the single most common source of flaky stacks and is exactly why healthchecks exist.

</details>

<details><summary><b>6.</b> What does Compose explicitly NOT guarantee, even with `depends_on` set?</summary>

Compose does not guarantee that the dependency's service inside the container is actually ready — only that the container process has started. It does not wait for a database to finish recovery, a port to start listening, or an HTTP endpoint to return 200. To gate on real readiness you must add a `healthcheck` and use the `service_healthy` condition, and even then your application should still tolerate transient connection failures.

</details>

<details><summary><b>7.</b> What are the three valid `condition` values in the long-form `depends_on` syntax?</summary>

They are `service_started`, `service_healthy`, and `service_completed_successfully`. `service_started` waits only for the container to start; `service_healthy` waits until the dependency's healthcheck reports healthy; `service_completed_successfully` waits for the dependency to run to a successful exit (exit code 0). You choose the condition that matches what "ready" actually means for that dependency.

</details>

<details><summary><b>8.</b> When would you use the `service_completed_successfully` condition?</summary>

You use it when a dependency is a one-shot job rather than a long-running service — for example a migration or seed container that must finish before the app starts. Compose waits for that container to exit with code 0 before starting the dependent. If the job exits non-zero, the dependent is not started, which is the desired fail-fast behaviour.

</details>

<details><summary><b>9.</b> Write the long-form `depends_on` block that makes a `loader` service wait for `postgres` to be healthy.</summary>

You write `depends_on:` then under `loader`, `postgres:` with `condition: service_healthy`. Concretely the loader's block reads `depends_on:` followed by an indented `postgres:` then `condition: service_healthy`. This makes Compose hold the loader until the Postgres healthcheck passes, not merely until its container starts.

</details>

<details><summary><b>10.</b> What is the practical difference between `service_started` and `service_healthy` for a data loader?</summary>

`service_started` releases the loader the instant the database container starts, which is often before Postgres is accepting connections, so the loader's first connection attempt fails. `service_healthy` releases the loader only after the database's healthcheck succeeds, meaning the server is actually ready. A loader needs `service_healthy` because it connects and runs SQL immediately, with no built-in patience for a not-yet-ready server.

</details>

<details><summary><b>11.</b> Why is being able to explain `service_started` versus `service_healthy` a "Done-when" criterion for this lesson?</summary>

Because it is the conceptual crux of reliable local stacks: knowing that "container started" is not "service ready" is what separates a stack that comes up cleanly every time from one that races and fails intermittently. The lesson's acceptance test asks you to articulate why a loader specifically needs `service_healthy`. If you can explain it, you understand both Compose's ordering guarantees and their limits.

</details>

<details><summary><b>12.</b> What is a Compose `healthcheck` and what problem does it solve?</summary>

A `healthcheck` is a command Compose runs periodically inside a container to determine whether the service is actually ready and functioning, marking the container `healthy`, `unhealthy`, or `starting`. It solves the readiness-versus-started gap: without it, `depends_on` can only know the container launched, not that the app works. A healthcheck turns a vague "it's up" into a testable signal other services can gate on.

</details>

<details><summary><b>13.</b> What are the main keys inside a Compose `healthcheck` block?</summary>

The keys are `test` (the command to run), `interval` (how often to run it), `timeout` (how long each run may take), `retries` (consecutive failures before `unhealthy`), `start_period` (a grace window during which failures don't count against `retries`), `start_interval` (a faster probe cadence during that grace window), and `disable` (turn off an inherited healthcheck). Together they let you tune both how readiness is measured and how forgiving the startup window is.

</details>

<details><summary><b>14.</b> What does the `test` key in a healthcheck specify, and what forms can it take?</summary>

`test` specifies the command Compose runs to judge health; a zero exit means healthy, non-zero means failing. It can be a string (run via the shell, equivalent to `CMD-SHELL`) or a list whose first element is `CMD` (run directly, no shell) or `CMD-SHELL` (run through the shell). Using the list `CMD` form avoids shell-quoting surprises, while `CMD-SHELL` is convenient when you need shell features like pipes or variable expansion.

</details>

<details><summary><b>15.</b> What healthcheck `test` command is conventional for a Postgres service?</summary>

The conventional probe is `pg_isready`, typically `pg_isready -U <user> -d <db>`, which returns exit code 0 only when the server is accepting connections. It ships with the Postgres image, so no extra tooling is needed. Some teams instead run a trivial `psql -c 'SELECT 1'` for a stronger check that the database actually answers queries, not just that the listener is up.

</details>

<details><summary><b>16.</b> What does the `start_period` key do, and why does it matter for databases?</summary>

`start_period` defines an initial grace window after the container starts during which failing healthchecks do not count toward the `retries` limit and do not mark the container `unhealthy`. It matters for databases because first-boot initialisation (creating data directories, running init scripts) can legitimately take many seconds, and you don't want those expected early failures to flip the container to `unhealthy`. A successful probe during the grace period immediately marks the container healthy.

</details>

<details><summary><b>17.</b> What is the role of `retries` in a healthcheck?</summary>

`retries` is the number of consecutive failed probes required before Compose marks the container `unhealthy` (after the `start_period`). It debounces transient failures so a single hiccup doesn't fail the service, while still catching a genuinely broken one. For example `retries: 5` with `interval: 5s` means roughly 25 seconds of sustained failure before the container is declared unhealthy.

</details>

<details><summary><b>18.</b> A dependent service never starts and Compose reports the dependency as `unhealthy` — what is the first thing to check?</summary>

First run the dependency's healthcheck `test` command yourself inside the container, e.g. `docker compose exec postgres pg_isready -U postgres`, to see what it actually returns. A common cause is a wrong username or database name in the probe so it always exits non-zero, or a `start_period` too short for first-boot init. Inspect `docker inspect --format '{{json .State.Health}}' <container>` to read the recorded failure output.

</details>

<details><summary><b>19.</b> How do you see a container's current health status from the CLI?</summary>

Run `docker ps`, which shows the health state in parentheses in the `STATUS` column, such as `Up 30 seconds (healthy)` or `(health: starting)`. For the full probe history and the last few outputs, use `docker inspect` and read the `.State.Health` object. `docker compose ps` similarly surfaces health for the stack's services.

</details>

<details><summary><b>20.</b> Why should application code still retry connections even when you use `service_healthy`?</summary>

Because a healthcheck only samples readiness at intervals, and there is always a small window — and edge cases like a database briefly rejecting connections under load or restart — where the dependency can be momentarily unavailable. Healthchecks reduce races but do not eliminate them, so robust apps wrap their initial connection in a short retry-with-backoff loop. Compose's own docs recommend designing services to be resilient to dependency unavailability rather than relying solely on startup order.

</details>

<details><summary><b>21.</b> What is a Docker named volume and why prefer it for stateful services?</summary>

A named volume is Docker-managed persistent storage with a stable name (declared under top-level `volumes:` and mounted into a container), whose lifecycle is independent of any single container. You prefer it for stateful services like Postgres or MinIO because data survives `docker compose down` and container recreation, and Docker manages its location and permissions. It is the canonical way to keep a database's data directory durable across stack restarts.

</details>

<details><summary><b>22.</b> What is the difference between a named volume, an anonymous volume, and a bind mount?</summary>

A named volume has an explicit name and is managed by Docker in its storage area; an anonymous volume is the same but with a random name Docker assigns when you don't name it, making it easy to orphan; a bind mount maps a specific host path directly into the container. Named volumes are best for service state (portable, managed), bind mounts are best for injecting source code or config from the host. Relying on anonymous volumes for state is a smell because they are hard to track and easy to lose.

</details>

<details><summary><b>23.</b> Why is putting every stateful service on a named volume a "Done-when" requirement for this lesson?</summary>

Because reproducibility and durability both depend on it: state on a named volume survives container recreation, and the explicit declaration makes it obvious where each service's data lives. The acceptance criterion asks you to show every stateful service mapped to a named volume so there is no hidden, ephemeral, or host-coupled state. A stack with un-named or accidental state is one you cannot reliably tear down and rebuild.

</details>

<details><summary><b>24.</b> What happens to a named volume when you run `docker compose down` versus `docker compose down -v`?</summary>

Plain `docker compose down` stops and removes the containers and the default network but preserves named volumes, so your database data is still there next time. Adding `-v` (or `--volumes`) also removes the named volumes declared in the Compose file, deleting that state. The `-v` flag is what you use deliberately to get a truly clean slate for reproducibility testing.

</details>

<details><summary><b>25.</b> How do you mount a named volume into the Postgres data directory in Compose?</summary>

You declare a top-level `volumes:` entry such as `pgdata:` and, under the Postgres service, add a `volumes:` mapping `pgdata:/var/lib/postgresql/data`. The left side is the named volume, the right side is the container path Postgres uses for its data. This keeps the database files durable and lets you wipe them on demand with `docker compose down -v`.

</details>

<details><summary><b>26.</b> What is a Compose network and what does Compose create by default?</summary>

A Compose network is a Docker virtual network that connects the stack's containers so they can reach each other by service name. By default, Compose creates a single network for the project and attaches every service to it, so `postgres` can be reached at the hostname `postgres` on its container port. This default makes intra-stack DNS "just work" without you wiring anything up.

</details>

<details><summary><b>27.</b> How do containers in the same Compose stack address each other?</summary>

They use the service name as a DNS hostname on the shared network — for example an app connects to Postgres at host `postgres` and port `5432`, not `localhost`. Compose runs an embedded DNS resolver that maps service names to container IPs. This is why your application's connection string inside the stack uses `postgres:5432`, while from your host you'd use `localhost` and a published port.

</details>

<details><summary><b>28.</b> Why might you define multiple, isolated networks per stack rather than using the single default?</summary>

To segment traffic and enforce isolation — for instance keeping a database on an internal-only network unreachable from outside, while the app sits on both that network and a front-facing one. Isolated networks per stack also prevent accidental cross-talk between unrelated projects running on the same host. The lesson frames "isolated networks per stack" as part of treating each sandbox as a self-contained unit.

</details>

<details><summary><b>29.</b> What does publishing a port (`ports: "5432:5432"`) actually do, and how does it differ from `expose`?</summary>

`ports` maps a container port to a host port so the service is reachable from your laptop (host `localhost:5432`), punching through to the outside of the stack. `expose` only documents/opens a port to other containers on the same network without binding it on the host. For a database you often only need inter-container access, so exposing without publishing reduces your host's attack surface.

</details>

<details><summary><b>30.</b> What is image pinning and why does the lesson insist on it?</summary>

Image pinning means referencing an image by an exact, immutable identifier — a specific version tag like `postgres:16.3` or, better, a content digest — instead of a moving target like `latest`. The lesson insists on it because reproducibility across machines and across months requires that everyone pulls the identical bits; `latest` silently drifts and breaks the "same numbers on a clean clone" guarantee. Pinning is what makes the stack a fixed, auditable artifact.

</details>

<details><summary><b>31.</b> Why is `postgres:latest` dangerous in a Compose file meant to be reproducible?</summary>

`latest` is a mutable tag that points to whatever the maintainers most recently pushed, so two people pulling on different days can get different major versions with incompatible behaviour or on-disk formats. Your stack then "works on my machine" and fails on a clean clone, defeating the whole point of a reproducible sandbox. Pin to an explicit version (and ideally a digest) so the stack reproduces identically.

</details>

<details><summary><b>32.</b> What is the difference between pinning by tag and pinning by digest?</summary>

A tag like `postgres:16.3` is human-readable but still mutable — the maintainer can re-push a new image under the same tag. A digest like `postgres@sha256:<hash>` is content-addressed and absolutely immutable: it always refers to byte-for-byte the same image. Tags are convenient and usually sufficient; digests give the strongest reproducibility guarantee and are preferred for audited or regulated environments.

</details>

<details><summary><b>33.</b> How do you find the digest of an image you have pulled?</summary>

Run `docker image inspect <image> --format '{{index .RepoDigests 0}}'`, which prints the `repository@sha256:...` digest reference. You can then copy that into your Compose file in place of the tag. `docker images --digests` also lists digests alongside tags for a quick overview.

</details>

<details><summary><b>34.</b> Why is "show every image pinned to a specific version tag" an explicit acceptance criterion?</summary>

Because unpinned images are the quietest way a reproducible stack rots: nothing visibly changes in your file, yet the behaviour drifts as upstream tags move. Requiring a visible, specific tag on every image makes the reproducibility contract auditable at a glance during review. It mirrors the same governance you'll later apply to pinned dependencies and infrastructure versions.

</details>

<details><summary><b>35.</b> How does image pinning relate to the regulated fund-administration context this plan targets?</summary>

In a regulated context like Luxembourg fund administration under DORA and UCITS/AIFMD oversight, you must be able to demonstrate exactly which software versions produced a given NAV or report, often years later for audit. Pinned images (ideally by digest) make the computing environment itself reproducible and auditable, so a recomputed NAV can be tied to an unambiguous toolchain. Unpinned `latest` images would make that provenance claim impossible to defend.

</details>

<details><summary><b>36.</b> What is Testcontainers and what core idea does it embody?</summary>

Testcontainers is a set of libraries (Java, Python, Go, and others) that let your test code programmatically start, configure, and tear down real Docker containers — a real Postgres, Kafka, or MinIO — for the duration of a test. The core idea is programmatic, throwaway infrastructure: instead of mocking a database or relying on a shared one, each test run spins up genuine ephemeral services and disposes of them automatically. It moves the reproducible-stack discipline from `docker-compose.yml` into the test lifecycle itself.

</details>

<details><summary><b>37.</b> How does Testcontainers differ from a `docker-compose.yml` development stack?</summary>

A Compose stack is a declarative, long-lived environment you bring up by hand for development; Testcontainers is imperative and ephemeral, created and destroyed by your test code within a single test run. Compose is for "give me a dev environment to work against"; Testcontainers is for "give this one test a clean, real dependency and throw it away after." They are complementary: Compose for the dev sandbox, Testcontainers for hermetic integration tests.

</details>

<details><summary><b>38.</b> Why does Testcontainers usually map service ports to random host ports?</summary>

Because tests must be able to run in parallel and on CI without colliding on fixed ports, Testcontainers binds each container to an ephemeral random host port and exposes a method to look it up at runtime. Your test asks the container object for its mapped port and host rather than hard-coding `5432`. This makes tests robust against other processes and concurrent test runs holding well-known ports.

</details>

<details><summary><b>39.</b> What guarantees does Testcontainers give about cleanup of containers it starts?</summary>

It tears down containers at the end of the test/lifecycle, and it ships a companion reaper (commonly called Ryuk) that watches the test session and removes leftover containers, networks, and volumes even if the test process crashes or is killed. This prevents orphaned infrastructure from accumulating across runs. The promise is that what a test starts, the framework reliably cleans up.

</details>

<details><summary><b>40.</b> In a regulated fund pipeline, what is a concrete use of Testcontainers?</summary>

You can write an integration test that spins up a throwaway Postgres, applies your migrations, loads a small set of ISIN-keyed securities and a NAV row, runs the loader, and asserts the resulting row counts and checksums — then disposes of the container. Because the database is real and ephemeral, the test exercises actual SQL, constraints, and types rather than mocks, and leaves no shared state behind. That gives high confidence the loader behaves correctly before it ever touches a shared environment.

</details>

<details><summary><b>41.</b> What is DuckDB and how is it architecturally different from Postgres?</summary>

DuckDB is an embedded, in-process analytical (OLAP) database that runs as a library inside your application or query tool, storing data in a single file (or in memory). Postgres, by contrast, is a separate server process you connect to over a socket and is optimised for transactional (OLTP) workloads. The key difference is that DuckDB needs no service to manage — you import a library and open a file — whereas Postgres needs a running daemon.

</details>

<details><summary><b>42.</b> What does "DuckDB as a zero-infra warehouse" mean, and when does a file beat a service?</summary>

It means using DuckDB's single file plus its in-process engine to do analytical querying without standing up any server, network, or container — no infrastructure to operate. A file beats a service when the data fits comfortably on one machine, the workload is single-user analytics or batch transforms, and you value zero operational overhead and trivial reproducibility over multi-user concurrency. For a local lab building a reporting mart, a `.duckdb` file is often simpler and faster than running a warehouse service.

</details>

<details><summary><b>43.</b> Why might you include DuckDB in a Compose stack at all if it needs no server?</summary>

Usually you don't run it as a long-running Compose service; it more often appears as a library used by a Python loader or a dbt run inside a one-shot container. When it does appear in the stack, it is as the analytical engine a transform step uses against a mounted volume, not as a daemon with a port. The point of the lesson is recognising when the right answer is a file (DuckDB) rather than another service.

</details>

<details><summary><b>44.</b> What is DuckDB's concurrency model for writers?</summary>

DuckDB is single-writer at the file level: only one process may open the database in read-write mode at a time, using MVCC and optimistic concurrency control within that process. Multiple threads inside that single process can write, but two threads editing the same row trigger a conflict error on the second. For multiple processes to read simultaneously, they must all open the file read-only, during which no process may write.

</details>

<details><summary><b>45.</b> A second tool fails to open a `.duckdb` file with a lock/conflict error while your loader is running — why?</summary>

Because DuckDB allows only one read-write process at a time on a database file; your loader holds the read-write lock, so a second writer is refused. The fix is either to let the loader finish, or to have the second process open the file in read-only mode (which is allowed only if no writer holds it). This single-writer constraint is the trade-off for DuckDB's zero-infra simplicity.

</details>

<details><summary><b>46.</b> Why is DuckDB a natural fit for the Phase-1 capstone's reporting mart?</summary>

The capstone builds a dimensional mart (a NAV periodic-snapshot star and an SCD2 fund dimension) as dbt models, which is a single-user, batch analytical workload that fits on one machine. DuckDB gives columnar OLAP performance with literally zero infrastructure to stand up, so a stranger can reproduce the mart by running dbt against a file. It stands in for a cloud warehouse like Synapse or Snowflake in the local lab without the operational weight.

</details>

<details><summary><b>47.</b> What is the recommended way to test that your stack is truly reproducible?</summary>

Test from a fresh clone on a clean Docker: prune existing images and volumes, clone the repo, and run `docker compose up`, timing it until every service reports healthy. This removes any reliance on cached images or leftover state that only exists on your machine. The lesson's bar is a clean, healthy stack in under two minutes from that fresh state.

</details>

<details><summary><b>48.</b> What does `docker compose up` doing in the foreground versus `-d` change about your workflow?</summary>

In the foreground, Compose attaches to and streams all container logs and stays in control of your terminal until you `Ctrl-C`, which is ideal for watching a stack come up and diagnosing startup. With `-d` (detached), it starts the stack in the background and returns your prompt, which you'd use once the stack is known-good or in scripts. For first reproducibility testing, running in the foreground lets you watch healthchecks flip to healthy.

</details>

<details><summary><b>49.</b> What is the difference between `docker compose down` and `docker compose stop`?</summary>

`docker compose stop` halts the running containers but leaves them, the network, and volumes in place so you can `start` them again quickly. `docker compose down` removes the containers and the default network entirely (volumes are kept unless you add `-v`), returning closer to a clean slate. You use `stop` to pause work and `down` to tear the stack down.

</details>

<details><summary><b>50.</b> What does `docker compose ps` show you?</summary>

It lists the containers belonging to the current Compose project with their state, published ports, and — when healthchecks are defined — their health status. It is the quickest way to confirm which services are up, healthy, or unhealthy for this stack specifically. Unlike `docker ps`, it is scoped to the project defined by your Compose file.

</details>

<details><summary><b>51.</b> How do you view the logs of just one service in a Compose stack?</summary>

Run `docker compose logs <service>`, optionally with `-f` to follow in real time and `--tail N` to limit history. For example `docker compose logs -f postgres` streams the database's startup output, which is where you'd look to see why a healthcheck is failing. Scoping to one service keeps the output readable in a multi-service stack.

</details>

<details><summary><b>52.</b> What is the purpose of the Compose `project name`, and how is it set?</summary>

The project name namespaces all of a stack's resources — containers, the default network, and volume prefixes — so multiple stacks can coexist on one host without colliding. By default it is derived from the directory name; you can override it with `-p`/`--project-name` or the `COMPOSE_PROJECT_NAME` environment variable, or `name:` at the top of the file. Distinct project names are what let you run two copies of a similar stack side by side.

</details>

<details><summary><b>53.</b> Why does running the same `docker-compose.yml` from two differently named directories create two independent stacks?</summary>

Because Compose derives the project name from the directory by default, and the project name prefixes the volume, network, and container names. Two directories yield two project names, hence two isolated sets of resources that don't share state. To force them to be the same stack you would set an explicit shared project name.

</details>

<details><summary><b>54.</b> What does the `restart` policy on a service control, and how does it differ from `depends_on: restart`?</summary>

A service-level `restart` policy (`no`, `always`, `on-failure`, `unless-stopped`) tells the container runtime whether to relaunch a container after it exits or the daemon restarts. The `restart: true` under a `depends_on` entry is different: it tells Compose to restart the dependent service after it updates the dependency during a Compose operation, excluding runtime auto-restarts. One governs crash recovery; the other governs reaction to dependency updates.

</details>

<details><summary><b>55.</b> What is the difference between the Compose `environment` key and an `.env` file?</summary>

The `environment` key sets variables inside a service's container at runtime. The `.env` file in the project directory provides values for variable interpolation in the Compose file itself (e.g. `image: postgres:${PG_VERSION}`) and is read automatically by Compose. They operate at different layers: `.env` parameterises the file; `environment` configures the container.

</details>

<details><summary><b>56.</b> Why should secrets like `POSTGRES_PASSWORD` not be hard-coded directly in a committed `docker-compose.yml`?</summary>

Because the file is version-controlled and shared, a hard-coded credential leaks into history and to anyone with repo access, which is unacceptable in a regulated environment. Instead reference an environment variable or use Docker/Compose secrets so the value comes from an uncommitted `.env` or a secret store. For a throwaway local sandbox a dummy password is fine, but the habit of externalising secrets should be built early.

</details>

<details><summary><b>57.</b> What is the role of `docker compose config`?</summary>

`docker compose config` renders and validates the fully-merged, interpolated configuration — applying overrides, `.env` substitution, and defaults — and prints the canonical result. It is the fastest way to catch a YAML or interpolation error and to see exactly what Compose will run, including which image tags resolved. Running it before `up` turns silent config drift into a visible diff.

</details>

<details><summary><b>58.</b> How do Compose override files (e.g. `docker-compose.override.yml`) work?</summary>

Compose automatically merges `docker-compose.override.yml` on top of the base `docker-compose.yml`, letting you layer local or environment-specific changes (extra ports, mounts, debug settings) without editing the base. You can also pass multiple files explicitly with `-f base.yml -f prod.yml`, applied left to right. This keeps a clean, shared base while allowing per-context customisation.

</details>

<details><summary><b>59.</b> A service comes up but your host cannot connect to it on the expected port — what are the first two things to check?</summary>

First confirm the `ports` mapping actually publishes the container port to the host (e.g. `"5432:5432"`), since without it the service is only reachable from inside the stack. Second confirm the service is bound inside the container to `0.0.0.0` rather than `127.0.0.1`, and that you are connecting to `localhost` on the host-side port. `docker compose ps` and `docker compose logs` quickly reveal whether the container is even listening.

</details>

<details><summary><b>60.</b> Inside the stack, an app's connection string uses `localhost:5432` and fails — why, and what is the fix?</summary>

Inside a container, `localhost` refers to that container itself, not the database container, so the app is dialling a port nothing is listening on. The fix is to use the database's service name as the host, e.g. `postgres:5432`, which Compose's DNS resolves to the right container. `localhost` only works from your laptop against a published port, not for inter-container traffic.

</details>

<details><summary><b>61.</b> What does it mean that Compose creates and removes resources idempotently on repeated `up`?</summary>

On `docker compose up`, Compose reconciles desired state with what exists: it reuses already-correct containers, networks, and volumes, and only (re)creates what changed. Running `up` again on an unchanged file is largely a no-op rather than a duplication. This reconciliation is part of why a Compose file behaves as a declarative description of the stack rather than a one-shot script.

</details>

<details><summary><b>62.</b> Why does the lesson tell you to `docker system prune` before timing a fresh `docker compose up`?</summary>

Pruning removes cached images, stopped containers, dangling volumes, and networks so the timed run starts from a genuinely clean state, like a stranger's machine. Without pruning, your local image cache hides slow or missing pulls and masks reproducibility problems. The honest test of "under two minutes from a fresh clone" requires that nothing is pre-warmed.

</details>

<details><summary><b>63.</b> What is the risk of `docker system prune -a --volumes` and when should you use it?</summary>

`prune -a --volumes` removes all unused images (not just dangling ones) and all unused volumes, which can delete data and large images you'd have to re-pull. You use it deliberately when you want a maximally clean slate to validate reproducibility, accepting the time cost of re-pulling. Run it knowing it can wipe state and is not reversible, so never on a machine holding data you need.

</details>

<details><summary><b>64.</b> How do healthchecks make the under-two-minutes acceptance test meaningful?</summary>

Because the criterion is "healthy," not merely "started," the timer only stops when every service's healthcheck passes — a real readiness signal. Without healthchecks you could only measure container launch, which says nothing about whether the stack is usable. Healthchecks turn the timing test into a measure of true end-to-end readiness.

</details>

<details><summary><b>65.</b> What is the difference between a Compose healthcheck and a Kubernetes liveness/readiness probe at the concept level?</summary>

Both periodically run a command/request to judge whether a container is ready or alive, but Compose has a single `healthcheck` whose state feeds `depends_on` ordering on one host. Kubernetes splits the idea into separate readiness probes (gate traffic) and liveness probes (trigger restarts) across a cluster. The underlying concept — probe for actual readiness rather than assuming "started means ready" — is identical, which is why mastering Compose healthchecks transfers upward.

</details>

<details><summary><b>66.</b> Why is YAML indentation a common cause of Compose failures, and how do you guard against it?</summary>

YAML uses indentation to define structure, so a mis-indented key silently lands under the wrong parent (e.g. a `healthcheck` becoming a sibling of `services` instead of a service), changing meaning without an obvious error. Guard against it by running `docker compose config` to render the merged result and confirm keys sit where you intend. Consistent two-space indentation and a linting editor catch most cases before runtime.

</details>

<details><summary><b>67.</b> What does the top-level `volumes:` declaration do versus a per-service `volumes:` mapping?</summary>

The top-level `volumes:` block declares named volumes that Compose should create and manage for the project. The per-service `volumes:` list mounts those named volumes (or bind paths) into specific containers at specific paths. You need both: one declares the volume exists, the other attaches it where the service writes data.

</details>

<details><summary><b>68.</b> Why is it a problem to store database data on a bind mount to a host path in a sandbox meant to be portable?</summary>

A bind mount couples the stack to a specific host filesystem layout and permissions, so it behaves differently across machines and OSes and breaks the "clone and run anywhere" promise. Named volumes are managed by Docker and portable, so the same Compose file works on another laptop without path assumptions. Bind mounts are great for source code, but state should live on named volumes.

</details>

<details><summary><b>69.</b> How does running on native Ubuntu rather than Docker Desktop on macOS/Windows affect volume performance?</summary>

On native Linux, Docker uses the host kernel directly, so bind-mount and volume I/O is native-speed; on macOS/Windows, Docker Desktop runs a Linux VM and bind mounts cross a virtualised filesystem boundary that can be markedly slower. This is one reason the lab assumes native Ubuntu — the local stack is faster and behaves closer to production Linux. Named volumes are less affected than bind mounts, but the native-Linux path is simplest and fastest.

</details>

<details><summary><b>70.</b> On the native-Ubuntu laptop, why does `docker compose` (the plugin) replace the old `docker-compose` (the script)?</summary>

Compose v2 is implemented as a Docker CLI plugin invoked as `docker compose` (a subcommand), whereas the legacy `docker-compose` was a separate standalone Python binary that is now end-of-life. The v2 plugin is the current, maintained implementation and is what you install on Ubuntu via the `docker-compose-plugin` package. Scripts and habits should use the space-separated `docker compose` form.

</details>

<details><summary><b>71.</b> What does the Compose specification's top-level `name:` key set, and why might you commit it?</summary>

The top-level `name:` sets the project name explicitly in the file itself, overriding the directory-derived default. Committing it makes the project name deterministic regardless of what directory someone clones into, which keeps volume and network names stable across machines. That stability aids reproducibility and avoids accidentally creating duplicate stacks.

</details>

<details><summary><b>72.</b> Why is pinning the Compose file format / spec version less of a concern than it used to be?</summary>

Older Compose required a top-level `version:` key (e.g. `'3.8'`) that gated which features were available, and mismatches caused confusion. The current Compose Specification is versionless — the `version` field is deprecated and ignored — so you simply use the features the installed Compose supports. Reproducibility now hinges on pinning your image tags and your Compose/Docker versions, not a schema version string.

</details>

<details><summary><b>73.</b> How do you confirm which Compose version a fresh machine has, and why does it matter for reproducibility?</summary>

Run `docker compose version` to print the installed Compose plugin version. It matters because newer healthcheck keys like `start_interval` or certain `depends_on` conditions require a recent enough Compose, so a stack that relies on them can silently behave differently on an older install. Documenting a minimum Compose/Docker version in the README is part of making the stack reproducible.

</details>

<details><summary><b>74.</b> What is MinIO and why is it in the lab's standard stack?</summary>

MinIO is an S3-API-compatible object storage server you can run locally in a container, giving you a stand-in for cloud object storage like Azure Blob or AWS S3. It is in the stack so the lab can practise object-store patterns — landing raw files, partitioned data lakes — using the same S3 API you'd use in the cloud, but free and local. It makes the local sandbox a faithful, zero-cost rehearsal for cloud storage.

</details>

<details><summary><b>75.</b> What does a sensible MinIO healthcheck probe, and why not just rely on the container starting?</summary>

A MinIO healthcheck typically curls its readiness/health endpoint (for example `/minio/health/live`) and treats a non-200 as failing, so dependents only start once the object store actually answers. Relying on container start would let a loader try to create buckets before MinIO is listening, causing connection-refused errors. The healthcheck closes that race exactly as it does for Postgres.

</details>

<details><summary><b>76.</b> In the Phase-1 capstone stack, why is a "placeholder service" included in the Compose file from the start?</summary>

The capstone tells you to write the `docker-compose.yml` you'll grow for all four years, so a placeholder reserves the shape — a third service slot, its network attachment, and its dependency wiring — that later phases will fill (a Spark worker, an Airflow scheduler, etc.). Establishing the pattern now means future additions slot into an already-disciplined file. It also forces you to practise dependency and healthcheck wiring beyond just one database.

</details>

<details><summary><b>77.</b> How would you wire a loader so it runs once after both Postgres and MinIO are ready, then exits?</summary>

Define the loader as a service with `depends_on` listing `postgres` and `minio` each with `condition: service_healthy`, give it a `restart: "no"` policy, and have its command run the load and exit. Compose holds the loader until both dependencies' healthchecks pass, then runs it to completion. Downstream services can gate on the loader with `condition: service_completed_successfully` if they must wait for the data to be loaded.

</details>

<details><summary><b>78.</b> Why does the capstone require the loader to produce identical end state when run twice (idempotency), and how does the sandbox support testing that?</summary>

Regulated fund pipelines must be safely re-runnable — a retried load after a failure must not double-count orders or NAV rows — so the loader uses a natural dedup key (order refs) and converges to the same state. The sandbox supports testing this by letting you wipe to a clean slate (`down -v`), run the loader twice, and compare committed row counts and checksums. The reproducible stack is what makes that two-run evidence trustworthy.

</details>

<details><summary><b>79.</b> What is a checksum-based acceptance test, and why is the reproducible stack a prerequisite for it?</summary>

It is asserting that the data produced (e.g. table row counts plus a hash of key columns) matches a committed expected value, proving the load is deterministic. The reproducible stack is a prerequisite because the same numbers can only be guaranteed if everyone runs the identical images, schema, and seed against the identical engine. Without pinned images and managed state, the checksum could differ for environmental reasons rather than real data changes.

</details>

<details><summary><b>80.</b> How does the discipline of a reproducible local sandbox map to building "reviewable" Azure environments later?</summary>

The same instinct — declare every dependency, pin every version, externalise state, and make the whole thing reproducible from a clean start — is exactly what makes a cloud environment auditable via infrastructure-as-code. Compose teaches the muscle memory locally for free before you apply it to Bicep/Terraform and Azure resources. A reviewer trusts an environment they can rebuild identically, whether it's a laptop stack or a subscription.

</details>

<details><summary><b>81.</b> Why does the lesson describe Compose fluency as "the substrate for every capstone"?</summary>

Because every later capstone assumes a one-command, reproducible stack underneath it, so if you can't author and bring up a clean Compose stack, you can't reliably run or hand off any of the projects. Compose is the common floor on which Postgres, MinIO, DuckDB, and future services stand. Mastering it once pays off in every subsequent phase.

</details>

<details><summary><b>82.</b> What is the difference between `service_healthy` gating and simply adding a `sleep` before the dependent starts?</summary>

`service_healthy` waits exactly as long as needed for the dependency to actually report ready, no more and no less, and fails fast if it never does. A fixed `sleep` is a guess: too short and you still race, too long and you waste time on every startup, and it never adapts to a slow machine. Healthcheck gating is the correct, adaptive mechanism; sleeps are a fragile anti-pattern.

</details>

<details><summary><b>83.</b> A loader gated on `service_healthy` still occasionally fails its first query — what subtle cause should you consider?</summary>

Consider that the Postgres healthcheck may be passing on the default `postgres` database while your application database or required tables aren't ready yet, or init scripts are still running. `pg_isready` returns healthy as soon as the server accepts connections, which can precede your schema being fully created. Strengthen the healthcheck to probe the actual target database/object, or have the loader retry briefly.

</details>

<details><summary><b>84.</b> How can you make a Postgres healthcheck check the specific database the loader will use?</summary>

Point `pg_isready` at the target with `-d <yourdb>` and the right `-U <user>`, so it only reports healthy when that database accepts connections, e.g. `pg_isready -U appuser -d fundref`. For an even stronger guarantee, use `psql -U appuser -d fundref -c 'SELECT 1'` so the probe confirms the server can actually execute a query against that database. This narrows the readiness signal to what the loader truly needs.

</details>

<details><summary><b>85.</b> What does `docker compose pull` do and why might you run it separately?</summary>

`docker compose pull` fetches the images referenced by the stack without starting anything, so you can pre-download (or refresh) images in a controlled step. Running it separately lets you measure or warm pull time, verify that pinned tags/digests resolve, and detect a missing image before `up`. It also lets CI cache images between the pull and the run.

</details>

<details><summary><b>86.</b> What is the difference between `docker compose run` and `docker compose up` for a one-off task?</summary>

`docker compose up` starts the whole stack (or named services) as long-running containers per the file; `docker compose run <service>` starts a single service with a one-off command, attached, and respects its `depends_on` but is meant for ad-hoc execution like a migration or a shell. `run` is handy for invoking a tool against the stack without redefining it as a permanent service. By default `run` also doesn't publish the service's ports unless you pass `--service-ports`.

</details>

<details><summary><b>87.</b> Why might you set `pull_policy` or use digests instead of relying on whatever is cached locally?</summary>

Because a locally cached image under a tag can be stale relative to the registry, so two machines with the same tag but different cache states diverge. Pinning by digest forces byte-identical content, and an explicit `pull_policy: always` (or pulling fresh) avoids silently running an old cached layer. For strict reproducibility, digests remove cache ambiguity entirely.

</details>

<details><summary><b>88.</b> How does declaring resources (volumes/networks) explicitly in the file aid teardown and cleanup?</summary>

Because the resources are named and owned by the project, `docker compose down` knows exactly which network to remove, and `down -v` knows precisely which named volumes to delete, leaving no orphans. Implicit or anonymous resources are harder to track and tend to accumulate as cruft. Explicit declarations make both setup and teardown deterministic.

</details>

<details><summary><b>89.</b> What is a sign that your "reproducible" stack actually has hidden machine-specific state?</summary>

It works on your machine but a teammate or a clean clone gets different data, errors, or counts — classic symptoms of leftover named volumes, a bind mount to a local path, or a cached image. The test is to `down -v`, prune, and run from a fresh clone; if the result changes, hidden state existed. Eliminating that gap is the entire point of the volumes/pinning discipline.

</details>

<details><summary><b>90.</b> Why might you keep your database on an internal-only network with no published port in a more security-conscious stack?</summary>

To ensure the database is reachable only by other services in the stack and never directly from the host or outside, shrinking the attack surface — useful when the stack handles sensitive fund data. The app service bridges the internal database network and any external-facing network. In regulated contexts, minimising exposed ports is a defensible default even in a sandbox.

</details>

<details><summary><b>91.</b> How does the LEI/ISIN-keyed reference data in the capstone benefit from a reproducible loader and stack?</summary>

Reference data keyed by ISIN (securities) and tied to LEIs (legal entities) must be loaded consistently so that downstream NAV and reporting joins are stable; a reproducible loader guarantees the same keys and relationships every run. Because the stack is pinned and state-managed, anyone can reproduce the exact reference set and verify joins resolve. This consistency is what lets the capstone's point-in-time and SCD2 queries be trusted.

</details>

<details><summary><b>92.</b> Why is "a stranger can run `docker compose up && uv run load.py` from the README and get the same numbers" the ultimate acceptance test?</summary>

Because it operationalises reproducibility end to end: the stack comes up identically (pinned images, named volumes, healthchecked ordering) and the loader produces deterministic data, verified by matching numbers. It removes every "works on my machine" excuse and proves the sandbox is a shared, trustworthy artifact. This is the same standard you will be held to when handing off real fund-administration pipelines.

</details>

<details><summary><b>93.</b> How does `uv run load.py` fit into the sandbox, and why `uv` rather than bare `python`?</summary>

`uv run load.py` executes the loader inside a `uv`-managed, reproducible Python environment resolved from the project's lockfile, so dependencies are pinned just like the Docker images. Using `uv` rather than bare `python`/`pip` guarantees the same package versions on every machine, extending reproducibility from the container layer into the Python layer. It mirrors image pinning: deterministic dependencies are the rule, not whatever happens to be installed.

</details>

<details><summary><b>94.</b> Why is it better for the loader to connect to Postgres via the published host port when run from the host, but via the service name when run as a container?</summary>

From the host, the loader reaches Postgres through the port published on `localhost`, because the host is outside the Compose network. When the loader itself runs as a container on the stack's network, it must use the service name `postgres` because that is how Compose DNS resolves the database, and `localhost` would mean the loader's own container. Choosing the right host depends on where the loader executes relative to the network boundary.

</details>

<details><summary><b>95.</b> What does it mean that Compose `up` will recreate a container when its configuration changes, and why is that desirable?</summary>

When you edit a service's image tag, environment, or mounts, the next `up` detects the diff and replaces the old container with one reflecting the new config, rather than leaving stale settings running. This is desirable because it keeps the running stack faithful to the declared file — the file remains the source of truth. It is the reconciliation behaviour that makes Compose declarative rather than a fire-and-forget script.

</details>

<details><summary><b>96.</b> A teammate reports your stack "takes forever to come up" while yours is instant — what reproducibility-relevant explanation is most likely?</summary>

Most likely your images are already cached locally while theirs must be pulled fresh, so your timing hides the real cold-start cost; the pinned tags are correct but the pull dominates on a clean machine. Confirm by pruning and timing from cold yourself. The lesson's prune-then-time discipline exists precisely to surface this difference.

</details>

<details><summary><b>97.</b> Why should a healthcheck command be cheap and side-effect-free?</summary>

Because it runs repeatedly on the configured `interval` for the life of the container, an expensive or stateful probe adds load and can itself cause flakiness or false unhealthies under contention. A good probe is a quick liveness check like `pg_isready` or a lightweight `SELECT 1`, not a heavy query or a write. Cheap, idempotent probes give a reliable signal without perturbing the service.

</details>

<details><summary><b>98.</b> How do you decide between adding a service to the Compose stack versus using DuckDB-as-a-file for an analytical need?</summary>

Ask whether the workload needs multi-user concurrency, network access, or to run continuously — if yes, a service (e.g. Postgres or a warehouse) is justified; if it is single-user batch analytics that fits on one machine, a DuckDB file avoids the operational cost entirely. The lesson frames this as "when a file beats a service": prefer the file when it removes infrastructure without losing what you need. Every avoided service is one less thing to pin, healthcheck, and operate.

</details>

<details><summary><b>99.</b> What is the relationship between this lesson's Compose skills and Phase 0's Docker module?</summary>

This lesson (9.1.3) builds directly on the container fundamentals from Phase 0's module 0.5, moving from single-container basics to orchestrating a multi-service, healthchecked, volume-backed stack. Phase 0 taught what a container and image are; here you compose them into a reproducible system. The progression is deliberate: container literacy first, then Compose fluency as the substrate for every capstone.

</details>

<details><summary><b>100.</b> Summarise the minimal checklist that makes a Compose-based local sandbox trustworthy and reproducible.</summary>

Every image is pinned to a specific tag (ideally a digest); every stateful service writes to a named volume; every dependent gates on `service_healthy` via a real healthcheck, not just `service_started`; and the whole stack comes up clean and healthy from a fresh clone on pruned Docker, with the Python layer pinned via `uv`. Validate it by running from cold and confirming the loader yields identical row counts and checksums on a second run. If a stranger gets the same numbers from the README, the sandbox is trustworthy.

</details>
