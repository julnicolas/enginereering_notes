# Install A Plugin With Vundle

Let's take the `vim-surround` plugin from github as an example.

Add the following in your `.vimrc` file between `call vundle#begin` and
`call vundle#end`:

```
Plugin 'tpope/vim-surround'
```

Then type:
- `:wq`
- `vim ~/.vimrc`
- `:PluginInstall`

