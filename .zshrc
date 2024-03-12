# -*- mode: sh -*-

HISTSIZE="10000"
SAVEHIST="10000"

HISTFILE="$HOME/.zsh_history"
mkdir -p "$(dirname "$HISTFILE")"

setopt HIST_FCNTL_LOCK
setopt HIST_IGNORE_DUPS
unsetopt HIST_IGNORE_ALL_DUPS
setopt HIST_IGNORE_SPACE
unsetopt HIST_EXPIRE_DUPS_FIRST
setopt SHARE_HISTORY
unsetopt EXTENDED_HISTORY
setopt autocd

# flutter config
export PATH=/opt/flutter/bin:$PATH

#aliases
source $HOME/.alias

# Basic auto/tab complete:
autoload -U compinit
zstyle ':completion:*' menu select
# Auto complete with case insenstivity
zstyle ':completion:*' matcher-list '' 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=*' 'l:|=* r:|=*'
zmodload zsh/complist
compinit
_comp_options+=(globdots)# Include hidden files.

#vi mode
bindkey -v
export KEYTIMEOUT=1
bindkey "^?" backward-delete-char
# Change cursor shape for different vi modes.
function zle-keymap-select {
  if [[ ''${KEYMAP} == vicmd ]] ||
     [[ $1 = 'block' ]]; then
     echo -ne '\e[1 q'
  elif [[ ''${KEYMAP} == main ]] ||
       [[ ''${KEYMAP} == viins ]] ||
       [[ ''${KEYMAP} = ' ' ]] ||
       [[ $1 = 'beam' ]]; then
       echo -ne '\e[5 q'
  fi
}
zle -N zle-keyma p-select

#zsh plugins
source /usr/share/zsh/plugins/zsh-history-substring-search/zsh-history-substring-search.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.plugin.zsh 
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# FZF
[ -f /usr/share/fzf/completion.zsh ] && source /usr/share/fzf/completion.zsh
[ -f /usr/share/fzf/key-bindings.zsh ] && source /usr/share/fzf/key-bindings.zsh
export FZF_DEFAULT_OPS="--extended"
export FZF_CTRL_T_COMMAND="$FZF_DEFAULT_COMMAND"

# Starship Prompt
eval "$(starship init zsh)"
