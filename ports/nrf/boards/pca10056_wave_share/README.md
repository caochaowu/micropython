+    rm -rf build-pca10056
+    make flash
+    make BOARD=pca10056 SD=s140 sd
+    make BOARD=pca10056 SD=s140 sd -f Makefile -f vars.mk d-OBJCOPY 
+    make -f Makefile -f vars.mk d-OBJCOPY 


+     make BOARD=pca10056 MICROPY_VFS_FAT=1 flash
+     make BOARD=pca10056 MICROPY_VFS_FAT=1 DEBUG=1 flash
