" set leader key
let g:mapleader = "\<space>"

syntax enable                           " Enables syntax highlighing
set hidden                              " Required to keep multiple buffers open multiple buffers
" set nowrap                              " Display long lines as just one line
filetype indent plugin on
set autoindent
set wildmenu                            " Better completion
set encoding=utf-8                      " The encoding displayed
set pumheight=10                        " Makes popup menu smaller
set fileencoding=utf-8                  " The encoding written to file
set ruler              			            " Show the cursor position all the time
set cmdheight=1                         " More space for displaying messages
set iskeyword+=-                      	" treat dash separated words as a word text object"
set mouse=a                             " Enable your mouse
set splitbelow                          " Horizontal splits will automatically be below
set splitright                          " Vertical splits will automatically be to the right
set t_Co=256                            " Support 256 colors
set conceallevel=0                      " So that I can see `` in markdown files
set tabstop=4                           " Insert 4 spaces for a tab
set expandtab
set shiftwidth=4                        " Change the number of space characters inserted for indentation
set smartindent                         " Makes indenting smart
set autoindent                          " Good auto indent
set number                              " Line numbers
set cursorline                          " Enable highlighting of the current line
" set background=dark                     " tell vim what the background color looks like
" set showtabline=2                       " Always show tabs
set laststatus=2                        " Always display statusline 
set showcmd
set noshowmode                          " We don't need to see things like -- INSERT -- anymore
set nobackup                            " This is recommended by coc
set nowritebackup                       " This is recommended by coc
set updatetime=300                      " Faster completion
set timeoutlen=500                      " By default timeoutlen is 1000 ms
set formatoptions-=cro                  " Stop newline continution of comments
" set clipboard=unnamedplus               " Copy paste between vim and everything else
set ignorecase                          " Case insensitive search
set smartcase
"set autochdir                           " Your working directory will always be the same as your working directory

au! BufWritePost $MYVIMRC source %      " auto source when writing to init.vm alternatively you can run :source $MYVIMRC

" You can't stop me
cmap w!! w !sudo tee %

"MAPING
" Map Y to act like D and C, i.e. to yank until EOL, rather than act as yy
map Y y$

" Map <C-L> (redraw screen) to also turn off search highlighting until the next search
nnoremap <C-M> :nohl<CR><C-L>

" toggle nerdtree
nnoremap <space>n :NERDTreeToggle<CR>

" persistent undo
if has('persistent_undo')
  set undodir=$HOME/.cache/nvim/undo
  set undofile
endif

" split movement keys
nnoremap <leader>j <C-W><C-J>
nnoremap <leader>k <C-W><C-K>
nnoremap <leader>l <C-W><C-L>
nnoremap <leader>h <C-W><C-H>
nnoremap <leader>wv <C-W><C-V>
nnoremap <leader>ws <C-W><C-S>
nnoremap <leader>wc <C-W><C-C>

" Copy to clipboard
vnoremap  <leader>y  "+y
nnoremap  <leader>Y  "+yg_
nnoremap  <leader>y  "+y
nnoremap  <leader>yy  "+yy

" Paste from clipboard
nnoremap <leader>p "+p
nnoremap <leader>P "+P
vnoremap <leader>p "+p
vnoremap <leader>P "+P
 
" pair syntax
inoremap " ""<left>
"inoremap ' ''<left>
inoremap ( ()<left>
inoremap [ []<left>
inoremap { {}<left>
inoremap {<CR> {<CR>}<ESC>O
inoremap {;<CR> {<CR>};<ESC>O
