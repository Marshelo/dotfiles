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

call plug#begin('~/.vim/plugged')

" ## Plugins ##
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

call plug#end()

colorscheme gruvbox
let g:gruvbox_contrast_dark = "hard"
let NERDTreeQuitOnOpen=1

let mapleader=" "

nmap <Leader>s <Plug>(easymotion-s2)
nmap <Leader>nt :NERDTreeFind<CR>


