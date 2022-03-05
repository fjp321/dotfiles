" Call in vim plugged
let data_dir = has('nvim') ? stdpath('data') . '/site' : '~/.vim'
if empty(glob(data_dir . '/autoload/plug.vim'))
  silent execute '!curl -fLo '.data_dir.'/autoload/plug.vim --create-dirs  https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

" Call plugs in
call plug#begin()
Plug 'scrooloose/syntastic'
Plug 'kien/rainbow_parentheses.vim'
Plug 'jiangmiao/auto-pairs'
Plug 'omnisharp/omnisharp-vim'
call plug#end()
