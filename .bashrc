#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# aliases
alias deploy-juice='sudo docker pull bkimminich/juice-shop && sudo docker run --rm -p 3000:3000 bkimminich/juice-shop'
alias ls='ls --color=auto'
alias ll='ls -la'
alias internet='ping -c 6 www.wikipedia.org; echo; nmcli connection show'
alias pytop='bpytop'

sh_str=$SHELL

# shell prefix
export PS1="\[\033[38;5;11m\]\u\[$(tput sgr0)\]\[\033[38;5;10m\] at \h\[$(tput sgr0)\]\[\033[38;5;14m\] in \w\[$(tput sgr0)\]\[\033[38;5;12m\] using $(echo ${sh_str:5}) \v \[$(tput sgr0)\]\[\033[38;5;13m\]\$(git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/')\[$(tput sgr0)\]\n\[$(tput sgr0)\]\[\033[38;5;9m\]\\$\[$(tput sgr0)\] \[$(tput sgr0)\]"

export PATH="/home/fjp/.local/bin:"${PATH}

# key env vars
source .envrc

