# emerge packages needed for configs
emerge -qv --autounmask=y --autounmask-write=y --autounmask-continue=y x11-wm/bspwm x11-misc/sxhkd x11-misc/polybar x11-terms/kitty neofetch
cp -R .config/* $HOME/.config
cd $HOME
mkdir git && cd git

# clone and patch dmenu
git clone https://git.suckless.org/dmenu
cd dmenu/
sudo make clean
git branch lineheight
git checkout lineheight
wget https://tools.suckless.org/dmenu/patches/line-height/dmenu-lineheight-5.0.diff
patch -p1 < dmenu-lineheight-5.0.diff
rm dmenu-lineheight-5.0.diff
git add --all
git commit -m "line height patchy"
git checkout master
git merge lineheight
make
sudo make install
