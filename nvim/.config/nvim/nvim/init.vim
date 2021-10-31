set nocompatible

let g:rustfmt_autosave = 1
noremap <Up> <NOP>
noremap <Down> <NOP>
noremap <Left> <NOP>
noremap <Right> <NOP>


"set termguicolors

set number
" set cursorline
set backspace=indent,eol,start
set showmode
set relativenumber
set mouse=a
set scrolloff=8
"set laststatus=2
filetype plugin indent on
set tabstop=4
set shiftwidth=2
set expandtab
set hidden

set smartcase
set encoding=utf-8

set shell=/bin/bash

let mapleader = " "

set undofile
set undodir=~/.config/nvim/undodir

call plug#begin('~/.vim/plugged')
Plug 'ap/vim-css-color'

Plug 'ambv/black'

Plug 'Raimondi/delimitMate'

Plug 'nvim-treesitter/nvim-treesitter'
Plug 'nvim-treesitter/playground'

Plug 'nvim-lua/plenary.nvim'
Plug 'nvim-telescope/telescope.nvim'

Plug 'neovim/nvim-lspconfig'
Plug 'hrsh7th/nvim-compe'

Plug 'hrsh7th/vim-vsnip'
Plug 'kabouzeid/nvim-lspinstall'
"Plug 'nvim-lua/completion-nvim'

Plug 'rust-lang/rust.vim' " rust for vim
Plug 'rhysd/vim-clang-format' " clang format
Plug 'editorconfig/editorconfig-vim' " proper code pattern
Plug 'machakann/vim-highlightedyank'

Plug 'itchyny/lightline.vim' " statusline

Plug 'scrooloose/nerdtree' " ls
Plug 'scrooloose/nerdcommenter'

Plug 'arcticicestudio/nord-vim' " nord colorscheme

Plug 'dag/vim-fish' " fish support for vim
Plug 'cespare/vim-toml' "TOML support for vim

" Initialize plugin system
call plug#end()

"if !has('gui_running')
"  set t_Co=256
"endif


nnoremap <leader>ff <cmd>Telescope find_files<cr>
nnoremap <leader>fg <cmd>Telescope live_grep<cr>
nnoremap <leader>fb <cmd>Telescope buffers<cr>
nnoremap <leader>fh <cmd>Telescope help_tags<cr>


" Lightline
let g:lightline = {
      \ 'colorscheme': 'nord',
      \ 'active': {
        \   'left': [ [ 'mode', 'paste' ],
        \             [ 'readonly', 'filename', 'modified' ] ],
        \   'right': [ [ 'lineinfo' ],
        \              [ 'percent' ],
        \              [ 'fileencoding', 'filetype' ] ],
        \ },
        \ 'component_function': {
          \   'filename': 'LightlineFilename'
          \ },
          \ }
function! LightlineFilename()
  return expand('%:t') !=# '' ? @% : '[No Name]'
endfunction

autocmd FileType c ClangFormatAutoEnable
autocmd FileType cpp ClangFormatAutoEnable

let g:clang_format#auto_format_on_insert_leave = 1


noremap <Tab> :bn<CR>
noremap <S-Tab> :bp<CR>
noremap <Leader><Tab> :Bw<CR>
noremap <Leader><S-Tab> :Bw!<CR>
noremap <C-t> :tabnew split<CR>

inoremap <silent><expr> <C-Space> compe#complete()
inoremap <silent><expr> <CR>      compe#confirm({ 'keys': "\<Plug>delimitMateCR", 'mode': '' })
inoremap <silent><expr> <C-e>     compe#close('<C-e>')
inoremap <silent><expr> <C-f>     compe#scroll({ 'delta': +4 })
inoremap <silent><expr> <C-d>     compe#scroll({ 'delta': -4 })

set completeopt=menuone,noselect
let g:compe = {}
let g:compe.enabled = v:true
let g:compe.autocomplete = v:true
let g:compe.debug = v:false
let g:compe.min_length = 1
let g:compe.preselect = 'enable'
let g:compe.throttle_time = 80
let g:compe.source_timeout = 200
let g:compe.resolve_timeout = 800
let g:compe.incomplete_delay = 400
let g:compe.max_abbr_width = 100
let g:compe.max_kind_width = 100
let g:compe.max_menu_width = 100
let g:compe.documentation = v:true

let g:compe.source = {}
let g:compe.source.path = v:true
let g:compe.source.buffer = v:true
let g:compe.source.calc = v:true
let g:compe.source.nvim_lsp = v:true
let g:compe.source.nvim_lua = v:true
let g:compe.source.vsnip = v:true
let g:compe.source.ultisnips = v:true
let g:compe.source.luasnip = v:true
let g:compe.source.emoji = v:true

lua << EOF
local nvim_lsp = require('lspconfig')

-- Use an on_attach function to only map the following keys
-- after the language server attaches to the current buffer
local on_attach = function(client, bufnr)
local function buf_set_keymap(...) vim.api.nvim_buf_set_keymap(bufnr, ...) end
local function buf_set_option(...) vim.api.nvim_buf_set_option(bufnr, ...) end

-- Enable completion triggered by <c-x><c-o>
buf_set_option('omnifunc', 'v:lua.vim.lsp.omnifunc')

-- Mappings.
local opts = { noremap=true, silent=true }

-- See `:help vim.lsp.*` for documentation on any of the below functions
buf_set_keymap('n', 'gD', '<cmd>lua vim.lsp.buf.declaration()<CR>', opts)
buf_set_keymap('n', 'gd', '<cmd>lua vim.lsp.buf.definition()<CR>', opts)
buf_set_keymap('n', 'K', '<cmd>lua vim.lsp.buf.hover()<CR>', opts)
buf_set_keymap('n', 'gi', '<cmd>lua vim.lsp.buf.implementation()<CR>', opts)
buf_set_keymap('n', '<C-k>', '<cmd>lua vim.lsp.buf.signature_help()<CR>', opts)
buf_set_keymap('n', '<space>wa', '<cmd>lua vim.lsp.buf.add_workspace_folder()<CR>', opts)
buf_set_keymap('n', '<space>wr', '<cmd>lua vim.lsp.buf.remove_workspace_folder()<CR>', opts)
buf_set_keymap('n', '<space>wl', '<cmd>lua print(vim.inspect(vim.lsp.buf.list_workspace_folders()))<CR>', opts)
buf_set_keymap('n', '<space>D', '<cmd>lua vim.lsp.buf.type_definition()<CR>', opts)
buf_set_keymap('n', '<space>rn', '<cmd>lua vim.lsp.buf.rename()<CR>', opts)
buf_set_keymap('n', '<space>ca', '<cmd>lua vim.lsp.buf.code_action()<CR>', opts)
buf_set_keymap('n', 'gr', '<cmd>lua vim.lsp.buf.references()<CR>', opts)
buf_set_keymap('n', '<space>e', '<cmd>lua vim.lsp.diagnostic.show_line_diagnostics()<CR>', opts)
buf_set_keymap('n', '[d', '<cmd>lua vim.lsp.diagnostic.goto_prev()<CR>', opts)
buf_set_keymap('n', ']d', '<cmd>lua vim.lsp.diagnostic.goto_next()<CR>', opts)
buf_set_keymap('n', '<space>q', '<cmd>lua vim.lsp.diagnostic.set_loclist()<CR>', opts)
buf_set_keymap('n', '<space>f', '<cmd>lua vim.lsp.buf.formatting()<CR>', opts)

end

-- Use a loop to conveniently call 'setup' on multiple servers and
-- map buffer local keybindings when the language server attaches
local servers = { 'pyright', 'rust_analyzer', 'ccls' }
for _, lsp in ipairs(servers) do
  nvim_lsp[lsp].setup {
    on_attach = on_attach,
    flags = {
      debounce_text_changes = 150,
      }
    }
end
EOF


lua << EOF

vim.lsp.handlers["textDocument/publishDiagnostics"] = vim.lsp.with(
vim.lsp.diagnostic.on_publish_diagnostics, {
  virtual_text = true,
  signs = true,
  update_in_insert = true,
  }
)

local capabilities = vim.lsp.protocol.make_client_capabilities()
capabilities.textDocument.completion.completionItem.snippetSupport = true
capabilities.textDocument.completion.completionItem.resolveSupport = {
  properties = {
    'documentation',
    'detail',
    'additionalTextEdits',
    'update_in_insert'
    }
  }

require'lspconfig'.rust_analyzer.setup {
  capabilities = capabilities,
  }

require'lspconfig'.pyright.setup {
  capabilities = capabilities,
  }

require'lspconfig'.ccls.setup {
  capabilities = capabilities,
  }

require'lspconfig'.tsserver.setup {
  capabilities = capabilities,
  }

require'lspconfig'.gopls.setup {
  capabilities = capabilities,
  }
EOF

lua require'nvim-treesitter.configs'.setup { highlight = { enable = true } }


let g:NERDCreateDefaultMappings = 1

" Add spaces after comment delimiters by default
let g:NERDSpaceDelims = 1

" Use compact syntax for prettified multi-line comments
let g:NERDCompactSexyComs = 1



colorscheme nord


set noshowmode  " to get rid of thing like --INSERT--
set noshowcmd  " to get rid of display of last command

" MUST HAVEEEEE

" keeping it centered
nnoremap n nzzzv
nnoremap N Nzzzv
nnoremap J mzJ`z

" Undo Break Points
inoremap , ,<c-g>u
inoremap . .<c-g>u
inoremap ? ?<c-g>u

"Jumplist Mutations
nnoremap <expr> j (v:count > 5 ? "m'"  . v:count : "") . 'j'
nnoremap <expr> k (v:count > 5 ? "m'"  . v:count : "") . 'k'

" Moving Text

inoremap <c-k> <esc>:m .-2<CR>==i
inoremap <c-j> <esc>:m .+1<CR>==i

vnoremap J :m '>+1<CR>gv=gv
vnoremap K :m '<-2<CR>gv=gv

nnoremap <leader>j :m .+1<CR>==
nnoremap <leader>k :m .-2<CR>==

