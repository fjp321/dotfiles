" needs curl and git

" Install vim-plug if not found
if empty(glob('~/.vim/autoload/plug.vim'))
  silent !curl -fLo ~/.vim/autoload/plug.vim --create-dirs
      \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  endif

  " Run PlugInstall if there are missing plugins
autocmd VimEnter * if len(filter(values(g:plugs), '!isdirectory(v:val.dir)'))
  \| PlugInstall --sync | source $MYVIMRC
  \| endif

call plug#begin()

Plug 'sheerun/vim-polyglot'
Plug 'sainnhe/everforest'
Plug 'yggdroot/indentline'

call plug#end()

" everforest configuration

if has('termguicolors')
  set termguicolors
endif

set background=dark

let g:everforest_background='hard'

let g:everforest_better_performance='hard'

colorscheme everforest
