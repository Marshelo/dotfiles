set number
set numberwidth=1
set mouse=r
set clipboard=unnamed
set showcmd
set ruler
set encoding=utf-8
set showmatch
set sw=2
set relativenumber
syntax enable
set tabstop=2
set autoindent
set laststatus=2
set bg=dark

set nocompatible
filetype plugin on
syntax on

call plug#begin('~/.vim/plugged')

" ## Plugins ##
" For bosses like me B)
Plug 'vimwiki/vimwiki'
" Syntax
Plug 'sheerun/vim-polyglot' "A wide programing languaje syntax support

" Status Bar
Plug 'maximbaz/lightline-ale'
Plug 'itchyny/lightline.vim'

" Themes
Plug 'morhetz/gruvbox'
Plug 'shinchu/lightline-gruvbox.vim'

" Autocomplete
Plug 'neoclide/coc.vim', {'branch': 'release'}

" Typing
Plug 'jiangmiao/auto-pairs' "pair (, [, {, ' and ''
Plug 'tpope/vim-surround' "wrap selected text with a character

" IDE
Plug 'easymotion/vim-easymotion' "Move fast searching 2 characters with space + s
Plug 'scrooloose/nerdtree' "Navigate between directories in a tree
" Plug 'christoomey/vim-tmux-navigator'
Plug 'mhinz/vim-signify' "Diff saved file with the current file
Plug 'yggdrrot/indentline' "Show a line for tabs
Plug 'scrooloose/nerdcommenter' "Comment the current line

Plug 'lervag/vimtex'

call plug#end()

colorscheme gruvbox
let g:gruvbox_contrast_dark = "hard"
let NERDTreeQuitOnOpen=1

let mapleader=" "

nmap <Leader>s <Plug>(easymotion-s2)
nmap <Leader>nt :NERDTreeFind<CR>

" My commands
" Latex
command! CompileLatex w | execute '!mkdir -p aux && pdflatex -output-directory=aux ' . @%
command! CompileLatexVerbose w | execute '!alacritty -e fish -c "mkdir -p aux && pdflatex -output-directory=aux ' . @% . ' && read -p \"echo \n\nPress Enter to close this window...\"" &'
" command! CompileLatexVerbose w | execute 'new | 0read !mkdir -p aux && pdflatex -output-directory=aux ' . @% " This open new pane to output the shell text but is not so good with the input
cnoreabbrev compile CompileLatex
cnoreabbrev compilev CompileLatexVerbose
cnoreabbrev latex CompileLatex
cnoreabbrev latexv CompileLatexVerbose
command! OpenPDF execute '!zathura aux/' . expand('%:r') . '.pdf &'
cnoreabbrev pdf OpenPDF<Esc>


" Short Cuts and Key bindings
nmap S gg
nmap Z G
" Tabs
nmap <a-a> gT
nmap <a-x> gt
nmap <a-s> :execute 'buffer ' . ((bufnr("%")+len(getbufinfo({'buflisted':1}))-2)%len(getbufinfo({'buflisted':1})) + 1)<return>
nmap <a-z> :execute 'buffer ' . (bufnr("%")%len(getbufinfo({'buflisted':1})) + 1)<return>

" Latex
nmap ,mm :CompileLatex<CR><Esc>
nmap ,wm :CompileLatexVerbose<CR><Esc>


