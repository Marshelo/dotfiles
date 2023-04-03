if status is-interactive
    # Commands to run in interactive sessions can go here
end

export VISUAL=vim

alias dotfiles="git --git-dir $HOME/.dotfiles/ --work-tree $HOME"
alias ls="exa --group-directories-first"
alias tre="exa -T"

## Run StarShip promt ##
starship init fish | source
fish_add_path /home/shelo/.cargo/bin
