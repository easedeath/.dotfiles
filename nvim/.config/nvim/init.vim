filetype plugin on

call plug#begin('~/.vim/plugged')

Plug 'nvim-lua/plenary.nvim'

" MAKING LIFE EASIER
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}  
Plug 'nvim-treesitter/playground'
Plug 'nvim-telescope/telescope.nvim' " oh yeah

" AUTOCOMPLETE BABY
Plug 'neovim/nvim-lspconfig'
Plug 'williamboman/nvim-lsp-installer'
Plug 'hrsh7th/nvim-compe'
Plug 'hrsh7th/vim-vsnip'

" GIT STUFF
Plug 'airblade/vim-gitgutter' 
Plug 'tpope/vim-fugitive' 
Plug 'ap/vim-css-color' 

" MISCS
Plug 'Raimondi/delimitMate' 
Plug 'tomtom/tcomment_vim'

"EYE CANDY
Plug 'arcticicestudio/nord-vim' " nord colorscheme
Plug 'machakann/vim-highlightedyank'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'folke/todo-comments.nvim'

" LANGAUGE STUFF
Plug 'rust-lang/rust.vim' 
Plug 'rhysd/vim-clang-format' 
Plug 'dag/vim-fish' 
Plug 'cespare/vim-toml' 

call plug#end()

let g:rustfmt_autosave = 1

let mapleader = " "

autocmd FileType c ClangFormatAutoEnable
autocmd FileType cpp ClangFormatAutoEnable

colorscheme nord

