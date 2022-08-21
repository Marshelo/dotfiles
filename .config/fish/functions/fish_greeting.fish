# Defined in /usr/share/fish/functions/fish_greeting.fish @ line 1
function fish_greeting
    if not set -q fish_greeting
        set messages "chanchulín" "chuchetumare" "poto" "???" "!!!" "wena po olvidona"
        set message $messages[(random 1 (count $messages))]
        # set style (random 1 4)
        set style (random 1 9)
        switch $style
            case 1
                cowthink $message
            case 2
                toilet $message -f pagga -F border | lolcat
            case 3
                toilet $message -f pagga -F border # use for limit wide -w 28
            case 4 # Bandera de chile con dialogo
                set messages "Wena chuchetumare" "wena watón"
                set message $messages[(random 1 (count $messages))]

                echo
                set_color normal -b normal
                echo "           ($message)"

                set_color blue
                echo -n "  █"
                set_color white -b blue
                echo -n " "
                set_color blue
                echo -n
                set_color white
                echo -n "█████"
                set_color normal -b normal
                echo " /"

                set_color red -b normal
                echo "  ████████"
            case 5 # Bandera de chile gritando
                set messages "Wena chuchetumare" "C-H-III, L-EEE"
                set message $messages[(random 1 (count $messages))]

                echo
                set_color normal -b normal
                echo "          ¡¡$message!!"

                set_color blue
                echo -n "  █"
                set_color white -b blue
                echo -n " "
                set_color blue
                echo -n
                set_color white
                echo -n "█████"
                set_color normal -b normal
                echo " /"

                set_color red -b normal
                echo "  ████████"

            case 6 # Dialogo de bandera con respuesta
                # messages and answers arrays must have the same index length
                set messages "CHORISOPAIPA" "Wena po"
                set answers "NADA MEJOR QUE UN CHORIPAN METIO EN UNA SOPAIPA" "Wena po olvidona"
                set randomNum (random 1 (count $messages))
                set message $messages[$randomNum]
                set answer $answers[$randomNum]

                echo
                set_color normal -b normal
                echo "           ($message)"

                set_color blue
                echo -n "  █"
                set_color white -b blue
                echo -n " "
                set_color blue
                echo -n
                set_color white
                echo -n "█████"
                set_color normal -b normal
                echo " /"

                set_color red -b normal
                echo "  ████████"
                echo

                set_color white -b normal
                toilet -f future " $answer"

            case 7 # Grito de bandera con respuesta
                # messages and answers arrays must have the same index length
                set messages "C-H-III, L-EEE" "C-H-III, L-EEE"
                set answers "CHIIIII, LEEEEE." "CHI CHI CHI, LE LE LE, VIVA CHILE"
                set randomNum (random 1 (count $messages))
                set message $messages[$randomNum]
                set answer $answers[$randomNum]

                echo
                set_color normal -b normal
                echo "          ¡¡$message!!"

                set_color blue
                echo -n "  █"
                set_color white -b blue
                echo -n " "
                set_color blue
                echo -n
                set_color white
                echo -n "█████"
                set_color normal -b normal
                echo " /"

                set_color red -b normal
                echo "  ████████"
                echo

                set_color white -b normal
                toilet -f future " $answer"
            case 8

            case 9

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