# c2-ec2-netutils
c2-ec2-netutils contains a set of utilities for managing elastic network interfaces on CROC Cloud EC2.

##### Supported versions:
 - Debian 8 and greater
 - Ubuntu 18.04 and greater

##### Preconfig
   * Ubuntu:
        
Allow metadata in udev.service:
   ```  
    /lib/systemd/system/udev.service
    IPAddressAllow=169.254.169.254
   ```
   * Debian:

Remove configurations for an interfaces other than eth0 in the default configuration```/etc/network/interfaces```.

Add ```source  /etc/network/interfaces.d/*``` in the default configuration.
 