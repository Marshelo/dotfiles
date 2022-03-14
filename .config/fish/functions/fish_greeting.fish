# Defined in /usr/share/fish/functions/fish_greeting.fish @ line 1
function fish_greeting
    if not set -q fish_greeting
        set option (random 1 6)
        switch $option
            case 1
                toilet "Welcome" -w 28 -f pagga -F border | lolcat
            case 2
                timeout --foreground 2s cmatrix
            case 3
                sl -ledw3
                clear
            case 4
                timeout --foreground 2s asciiquarium
            case 5
                sl -ew3
                clear
            case 6
                cowthink "???"
        end
    end

  if set -q fish_private_mode
        set -l line (_ "fish is running in private mode, history will not be persisted.")
        if set -q fish_greeting[1]
            set -g fish_greeting $fish_greeting\n$line
        else
            set -g fish_greeting $line
        end
    end

  # The greeting used to be skipped when fish_greeting was empty (not just undefined)
  # Keep it that way to not print superfluous newlines on old configuration
  test -n "$fish_greeting"
    and echo $fish_greeting
end