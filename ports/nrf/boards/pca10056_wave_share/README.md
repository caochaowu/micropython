    
# history cmds    
    make BOARD=pca10056 SD=s140 sd
    
    make BOARD=pca10056 SD=s140 sd -f Makefile -f vars.mk d-OBJCOPY 
    make -f Makefile -f vars.mk d-OBJCOPY 
    
    make BOARD=pca10056 MICROPY_VFS_FAT=1 flash

    rm -rf build-pca10056
    rm -rf build-pca10056-s140

# make and downlaod 
// download softdevice s140 and applet at the same time 
    make BOARD=pca10056 SD=s140 MICROPY_VFS_FAT=1 DEBUG=1 sd
// download applet only.       
    make BOARD=pca10056 SD=s140 MICROPY_VFS_FAT=1 DEBUG=1 flash 


