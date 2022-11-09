#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# aliases
alias deploy-juice='sudo docker run --rm -p 3000:3000 bkimminich/juice-shop'
alias ls='ls --color=auto'
alias ll='ls -la'

# shell prefix
export PS1="\[\033[38;5;12m\]\u \[\033[38;5;10m\]at \h\[\033[38;5;11m\] in \w\[\033[38;5;9m\] using bash \v\[\033[38;5;13m\] \$(git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/')\n\\$ "

export PATH="/home/fjp/.local/bin:"${PATH}

# key env vars
source .envrc

