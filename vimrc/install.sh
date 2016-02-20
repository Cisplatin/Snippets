# A shady script to set-up my vim configuartion. Current bash processes will
# not be updated, so make sure to restart bash.

# Set up the .vimrc file
cp vimrc ~/.vimrc

# Get the most recent version of vim
# http://stackoverflow.com/questions/7211820/update-built-in-vim-on-mac-os-x
sudo mkdir -p /opt/local/bin
cd ~
git clone https://github.com/vim/vim.git
cd vim
./configure --prefix=/opt/local
make
sudo make install
echo 'PATH=/opt/local/bin:$PATH' >> ~/.bash_profile
rm -rf ~/vim

# Install pathogen for next-level plugin management
mkdir -p ~/.vim/autoload ~/.vim/bundle && \
curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim
