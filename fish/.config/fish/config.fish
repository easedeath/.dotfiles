#--------CUSTOM FUNCTIONS---------------

function bluers
    systemctl restart bluetooth.service
end

function com
    g++ $argv[1] && ./a.out && rm a.out 
end


function conf
    set val $argv[1]

    if [ $val = "fish" ]
        nvim ~/.config/fish/config.fish
    
    else if [ $val = "starship" ]
        nvim ~/.config/starship.toml
    
    else if [ $val = "qtile" ]
        nvim ~/.config/qtile/config.py
    
    else if [ $val = "alacritty" ]
        nvim ~/.config/alacritty/alacritty.yml

    else if [ $val = "picom" ]
        nvim ~/.config/picom/picom.conf

    else if [ $val = "vim" ]
        nvim ~/.config/nvim/init.vim
    else
        echo Not in the config list!!
    end
end

# Base16 Shell
if status --is-interactive
    set BASE16_SHELL "$HOME/.config/base16-shell/"
    source "$BASE16_SHELL/profile_helper.fish"
end


#----------------------------- BASICS -----------------------------------
set fish_greeting                      # Supresses fish's intro message
set TERM "xterm-256color"              # Sets the terminal type

set EDITOR "nvim"                      #Sets Editor to neovim
set VISUAL "nvim"

#theme_gruvbox "dark" "hard"
set fish_color_normal '#88C0D0'
set fish_color_autosuggestion '#B48EAD'
set fish_color_qouted '#EBCB8B'
set fish_color_command '#8FBCBB'
set fish_color_error '#BF616A'
set fish_color_param '#88C0D0'
set fish_color_keyword '#D8DEE9'

#----------------------------- ALIASES --------------------------------

#----DIRECTORY CHANGE
alias ..='cd ..' 
alias ...='cd ../..'

alias vim='nvim'
alias mv='mv -i'
alias rm='rm -rfi'

#----LS OUTPUT
alias ls='exa -F --color=always --group-directories-first' # my preferred listing
alias la='exa -a --color=always --group-directories-first'  # all files and dirs
alias ll='exa -l --color=always --group-directories-first'  # long format
alias lt='exa -aT --color=always --group-directories-first' # tree listing
#alias tmux="TERM=screen-256color-bce tmux" #base16 colors

# pacman and yay
alias docker='sudo docker'
alias pacman='sudo pacman'
alias yay=paru
alias pacsyu='sudo pacman -Syyu'                 # update only standard pkgs
alias yaysua='paru -Sua --noconfirm'              # update only AUR pkgs
alias yaysyu='paru -Syu --noconfirm'              # update standard pkgs and AUR pkgs
alias unlock='sudo rm /var/lib/pacman/db.lck'    # remove pacman lock
alias cleanup='sudo pacman -Rns (pacman -Qtdq)'  # remove orphaned packages
#alias python='python3'

# adding flags
alias df='df -h'                          # human-readable sizes
alias free='free -m'                      # show sizes in MB

#-----MISC

alias ew='~/Downloads/eww/target/release/eww'


alias fetch='~/Public/fm6000 -c=bright_red -n -m=7 -g=7 -l=16'
alias cf='rm -rf ~/CP && mkdir ~/CP' #competetive coding :)
alias loff='xrandr --output eDP1 --off' #turns off laptop screen :)
alias lonn='xrandr --output eDP1 --auto'
#-----GREP COLOR
alias grep='grep --color=auto'
colorscript -e crunchbang-mini 

starship init fish | source
export PATH="$HOME/.emacs.d/bin:$PATH"


#--------JAYDA KA BACha----------
#alias qb64="bash /home/puffc0rn/Downloads/qb64/run_qb64.sh"
alias fl="cd /home/puffc0rn/ZZZ/JAY/Github/10_FLASK_PROJECTS/Project_10_Online_Shopping_Site;export FLASK_DEBUG=1;flask run"
alias qb64="bash /home/strawhat54/Downloads/qb64/run_qb64.sh"
alias eww="./eww"