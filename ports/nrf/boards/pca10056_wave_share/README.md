# First cmds

cd micropython
make -C mpy-cross

cd micropython/ports/nrf
make submodules BOARD=pca10056_wave_share


# history cmds    
    make BOARD=pca10056_wave_share SD=s140 sd
    
    make BOARD=pca10056_wave_share SD=s140 sd -f Makefile -f vars.mk d-OBJCOPY 
    make -f Makefile -f vars.mk d-OBJCOPY 
    
    make BOARD=pca10056_wave_share MICROPY_VFS_FAT=1 flash

    rm -rf build-pca10056_wave_share
    rm -rf build-pca10056_wave_share-s140



# make and downlaod 
// download softdevice s140 and applet at the same time 
make BOARD=pca10056_wave_share SD=s140 MICROPY_VFS_FAT=1 DEBUG=1 sd
// download applet only.       
make BOARD=pca10056_wave_share SD=s140 MICROPY_VFS_FAT=1 DEBUG=1 flash 


