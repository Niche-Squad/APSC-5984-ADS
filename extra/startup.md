# Start-up files

- [Start-up files](#start-up-files)
  - [Bash](#bash)
    - [~/.bash\_profile](#bash_profile)
    - [~/.bashrc](#bashrc)
    - [~/.bash\_logout](#bash_logout)
  - [Synchronizing the course repository automatically](#synchronizing-the-course-repository-automatically)
    - [Build your own start-up files](#build-your-own-start-up-files)
    - [Example of .bash\_profile](#example-of-bash_profile)
  - [Update the start-up environment](#update-the-start-up-environment)


## Bash

### ~/.bash_profile

This file is executed for login shells.

### ~/.bashrc

This file is executed for interactive non-login shells.

### ~/.bash_logout

This file is executed when a login shell exits.

## Synchronizing the course repository automatically

### Build your own start-up files

Open Linux terminal, and let's create a file called `.bash_profile` in your home directory (`~`):

```bash
code ~/.bash_profile
```

This will create a file called `.bash_profile` in your home directory and open it in VS Code.

Now, we can define what to do automatically when you open a terminal. For example, we can add the following lines to the file:

```bash
# Sync the course repository automatically
cd ~/APSC-5984-ADS # Change the directory to the course repository
git fetch upstream
git merge upstream/main --no-edit --allow-unrelated-histories
git push
cd ~
```

You can also add aliases to the folders you frequently work on

```bash
# change WD
export ADS="/home/niche/APSC-5984-ADS"
alias toADS="cd $ADS"
# equivalent to `cd /home/niche/APSC-5984-ADS`

# other commands
alias l="ls -lht"
alias ll="ls -l"
alias la="ls -a"
```

### Example of .bash_profile

```bash
cd ~/OneDrive\ -\ Virginia\ Tech

# alias
export profile="/Users/niche/.bash_profile"
export arc1="tinkercliffs1.arc.vt.edu"
alias arc="ssh $arc1"

# Github
alias pull="git pull origin master"
push() {
    git add .
    git rm -r --cache *.DS_Store
    git commit -m "${1}"
    git push
}

# inspect data
alias nrow="awk 'END{print NR}'"
alias ncol="awk 'NR==1{print NF}'"
alias shape="awk 'END{print NR, NF}'"
alias peek="awk NR==2,NR==${2}+1{print} ${1}"

# tasks/analysis
alias l="ls -lht"
alias ol="tail *.log"
alias o="tail *.out"
alias t="top -d 1"

# environment
conda activate tf
```

## Update the start-up environment

You can activate the `.bash_profile` by opening a new terminal or by the command:

```bash
source ~/.bash_profile
```
