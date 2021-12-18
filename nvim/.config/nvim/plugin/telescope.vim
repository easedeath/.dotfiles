lua << EOF
require('telescope').setup{
  pickers = {
    git_files = {
      theme = "dropdown",
    }
  },
}
EOF

nnoremap <leader>fg <cmd>Telescope live_grep<cr>
nnoremap <leader>fb <cmd>Telescope buffers<cr>
nnoremap <leader>fh <cmd>Telescope help_tags<cr>
nnoremap <C-p> <cmd>Telescope git_files<cr>
