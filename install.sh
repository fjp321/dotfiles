# emerge packages needed for configs
emerge -qv --autounmask=y --autounmask-write=y --autounmask-continue=y x11-wm/bspwm x11-misc/sxhkd x11-misc/polybar x11-terms/kitty media-fonts/jetbrains-mono
# get jetbrains
bash getjet.sh JetBrainsMono
