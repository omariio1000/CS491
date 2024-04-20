**Odin ID:** nassar
# 1
![The Linux Command Line](TLCL-19.01.pdf.png "The Linux Command Line")

![Adventures with the Linux Command Line with the Linux Command Line](AWTLCL-21.10.pdf "fundamentals")

![The Linux Development Platform](0130091154.pdf "The Linux Development Platform")

# 2
![fundamentals](fundamentals.png "fundamentals")

# 3
![modules](modules.png "modules")

# 4
## a
`zgrep "password" /usr/share/wordlists/rockyou.txt`

3959 results

## b
`zgrep -i "password" /usr/share/wordlists/rockyou.txt`

4690 results

## c
`zgrep -P "\b[0-9]{3}$" /usr/share/wordlists/rockyou.txt`

18429 results

Not able to do without anchor

## d
`zgrep -P "^(?:[^0-9]*[0-9]){3}[^0-9]*$" /usr/share/wordlists/rockyou.txt`

1009587 results

# 5
## a
`find . -type f -name "*.py" -exec sed -i 's/from this\.that import/from that import/g' {} +`

## b
`sed -n '312,345p' filename`

## c
`sudo sed -i 's/^#PasswordAuthentication yes PasswordAuthentication no/' /etc/ssh/sshd_config`

# 6
## a 
`objdump` disassembles the file and shows the headers used and all the assembly code for all the functions. This can be configured with options.

## b
`nm` shows all the symbols from the file. It can also be configured with options.

## b
`readelf` shows information about one or more ELF format object files. It can also be configured with options.

# 7
```
activate_env() {
    local env_path="$1"
    if [[ -z "$env_path" ]]; then
        echo "Usage: activate_env <path_to_env_directory>"
        return 1
    fi

    local activate_script=$(find "$env_path" -type f -name "activate" -path "*/bin/activate" | head -n 1)
    if [[ -n "$activate_script" ]]; then
        source "$activate_script"
        echo "Activated virtual environment in $(dirname $(dirname $activate_script))"
    else
        echo "No activate script found in '$env_path'"
        return 1
    fi
}

```

# 8
## a
The `grep -Ev $(...)` portion is designed to exclude lines containing any user names from `/etc/passwd`. This is useful for filtering out system or regular user processes to focus on processes run by users not normally present in the `passwd` file—potentially highlighting unauthorized or unexpected user activities.

## b
An alias in Unix/Linux is a shorthand or a nickname for a command or a series of commands. It allows a user to customize, shorten, or simplify command sequences. Aliases are often defined in the shell's configuration files like .`bashrc` or `.zshrc` to increase productivity or enhance usability.

## c
Yes, the `awk '{print $1}'` can be replaced with cut `-d' ' -f1`

`ps -efH --no-header | cut -d' ' -f1 | ...`

The reverse is also true; cut can be replaced by `awk` since `awk` is more powerful and can handle more complex text processing tasks than cut.


## d
`paste` is typically used to merge lines of files side by side. However, for this pipeline, replacing Python might involve a different approach since `paste` itself doesn't inherently filter or format input like Python. But you can simplify the Python command by directly using `paste` to streamline combining lines:

`grep -Ev $(cut -f1 -d':' /etc/passwd | paste -sd'|' -)`

Here, `paste -sd'|' -` takes the output of `cut`, which lists user names line by line, and merges them into a single line separated by `|`. This can then be fed into `grep` directly, replacing the Python script used for joining strings.