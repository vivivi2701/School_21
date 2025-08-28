# Report

## Part 1: Installation of the OS
- **Command Output:**
	![Ubuntu 20.04.6 LTS \n \l](file:/home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/Screenshot_20250119_191454.png)
	*Screenshot of the command output showing the Ubuntu version.*

## Part 2: Creating a user
- **Command to Create User:**
	`sudo useradd 'adm_user' -g adm`
- **Output of `/etc/passwd`:**
	![Create User Command](file://home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/Screenshot_20250119_195347.png)
	*Screenshot showing the new user in the `/etc/passwd` file.*

## Part 3: Setting up the OS network
	![timedatectl](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/3/Screenshot_20250119_204146.png)
	*timedatectl*
	(file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/3/Screenshot_20250119_204654.png)
	*set-hostname*

	(file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/3/Screenshot_20250119_204919.png)
	*link show*

	(file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/3/Screenshot_20250119_205115.png)
	*address show*

	(file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/3/Screenshot_20250119_205609.png)
	*ip route*

	(file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/3/Screenshot_20250119_205817.png)
	*ifconfig.me*

	(file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/3/Screenshot_20250119_212040.png)
	*netplan/01-netcfg.yaml*

	(file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/3/Screenshot_20250119_212147.png)
	*applying*

	(file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/3/Screenshot_20250119_212225.png)
	*process of applying*

	(file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/3/Screenshot_20250119_212251.png)
	*results*

	(file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/3/Screenshot_20250119_212334.png)
	*finding inet*

	(file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/3/Screenshot_20250119_212841.png)
	`ping 1.1.1.1`
	and
	(file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/3/Screenshot_20250119_212925.png)
	`ping ya.ru`:
	successful ping results with "0% packet loss".
- **Explanation for `lo` Interface:**
	`The "lo" interface represents the loopback interface, which is used for internal communication within the host.`
- **DHCP Explanation:**
	`DHCP stands for Dynamic Host Configuration Protocol. It is used to dynamically assign IP addresses and other network configuration parameters to devices on a network.`

## Part 4: OS Update
- **Updating:**
	![update](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/4/Screenshot_20250119_213135.png)
	![sudo apt update](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/4/Screenshot_20250119_213520.png)
	![processing...](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/4/Screenshot_20250119_213558.png)
	![version before updating](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/4/Screenshot_20250119_215443.png)
	![UPDATING IS DONE!](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/4/Screenshot_20250119_220852.png)
	*Screenshots showing the results of successful updates*
	`sudo apt upgrade -y , sudo apt full-upgrade -y , sudo apt autoremove --purge -y`

## Part 5: Using the sudo command
    ![allowing recently added new user to use command 'sudo'](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/5/Screenshot_20250120_170633.png)
- **Purpose of `sudo`:**
	The `sudo` command allows a permitted user to execute a command as the superuser or another user, as specified by the security policy.
- **Changed Hostname:**
	![Changed Hostname](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/5/Screenshot_20250120_171145.png)
	*Screenshot showing the changed hostname.*

## Part 6: Installing and configuring the time service
- **Current Time:**
	![Current Time](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/6/Screenshot_20250120_171659.png)
	*Screenshot showing the current time of the time zone.*
- **NTP Synchronization:**
	![NTP Synchronization](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/6/Screenshot_20250120_171730.png)
	*Screenshot showing `NTPSynchronized=yes` in the command output.*

## Part 7: Installing and using text editors
- **VIM Editor Installation:**
	![VIM Editor](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/7/Screenshot_20250120_172109.png)
	*Screenshot showing the Successful installation of VIM.*
- **NANO Editor Installation:**
	![NANO Editor](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/7/Screenshot_20250120_172212.png)
	*Screenshot showing the the Successful installation of NANO.*
- **JOE Editor Installation:**
	![JOE Editor](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/7/Screenshot_20250120_172244.png)
	*Screenshot showing the Successful installation of Joe Editor*
- **Exit with Changes Saved:**
	- VIM: `:wq`
	- NANO: `Ctrl+O, Enter, Ctrl+X`
	- JOE: `Ctrl(^)KX`
- **Exit without Saving Changes:**
	- VIM: `:q!`
	- NANO: `Ctrl+X, N`
	- JOE: `Ctrl(^)C, y`
- **Search and Replace:**
	- VIM: `:%s/nickname/21 School 21/g`
	- NANO: `Ctrl+\ (search), Ctrl+T (replace)`
	- JOE: `(Ctrl)^KF-Enter (then, follow the instructions on the screen)`
	![Writing my nickname(rymundzu) into a new vim-file](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/7/Screenshot_20250120_173657.png)
	![Writing my nickname (rymundzu) into a new nano-file](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/7/Screenshot_20250120_173726.png)
	![Writing my rymundzu nickname into a new Joe-file](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/7/Screenshot_20250120_173759.png)
	![Changing my nickname string to `21 School 21` without saving any changes in vim-file](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/7/Screenshot_20250120_174026.png)
	![Changing my nickname string to `21 School 21` without saving any changes in nano-file](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/7/Screenshot_20250120_174136.png)
	![Changing my nickname string to `21 School 21` without saving any changes in joe-file](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/7/Screenshot_20250120_174206.png)

## Part 8: Installing and basic setup of the SSHD service
- **SSHD Process:**
	![Installatin of ssh-server](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/8/Screenshot_20250120_175439.png)
	![Already Active SSH](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/8/Screenshot_20250120_175534.png)
	![Changing Port from 22 to 2022](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/8/Screenshot_20250120_175650.png)
	*Screenshots show the SSHD process.*
- **Netstat Output:**
	![Netstat Output](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/8/Screenshot_20250120_182830.png)
	*Screenshot showing the netstat output with `tcp 0 0.0.0.0:2022 0.0.0.0:* LISTEN`.*
- **Explanation of `ps` Command:**
	The `ps` command is used to display information about active processes. The keys used in the command are:
	- `aux`: Show all processes for all users.
- **Explanation of `netstat` Command:**
	The `netstat` command is used to display network connections, routing tables, interface statistics, masquerade connections, and multicast memberships. The keys used in the command are:
	- `-t`: Show TCP connections.
	- `-a`: Show all connections.
	- `-n`: Show numerical addresses instead of resolving hostnames.
	`The address 0.0.0.0 has several meanings in networking protocols:`
		`Unbound address: Used to denote all available interfaces on a host. When a server listens on 0.0.0.0, it means that it accepts connections on all available IP addresses.`
		`No address: In some contexts, 0.0.0.0 can represent the absence of a specific address or a default value.`
		`Routing: In routing, 0.0.0.0 can be used as a "default route." This means that if there is no specific route to a destination address, traffic will be sent via this route.`

## Part 9: Installing and using the top, htop utilities
- **Top Command Output:**
	- Uptime: `18:34:26 up 8 min`
	- Number of Authorized Users: `1 user`
	- Average System Load: `0.10, 0.02, 0.00`
	- Total Number of Processes: `173 total`
- **CPU Load:**
	- User Space: `1.5%` (next screenshot)
	- System Space: `1963,8 total`
	- Idle: `97.6%`
- **Memory Load:** (next screenshot)
	- Total Memory: `1963.8 MiB`
	- Free Memory: `520.6 MiB`
	- Used Memory: `523.3 MiB`
	- Buff/Cache: `919.9 MiB`
- **PID of Process with Highest Memory Usage:** `1387` (3.7%)
- **PID of Process Taking Most CPU Time:** `1387` (`code`, 1.3% CPU, 0:13.36 cumulative time)
- **Htop Command Output:**
	![Htop Output](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/9/Screenshot_20250120_184549.png)
	*Screenshot showing the htop output sorted by PID, PERCENT_CPU, PERCENT_MEM, TIME.*

## Part 10: Using the fdisk utility
- **Fdisk Output:**
	- **Hard Disk Name:** `/dev/mapper/ubuntu--vg-ubuntu--lv`
	- **Capacity:** `24 GiB`
	- **Number of Sectors:** `50323456`
	- **Swap Size:** `Not available in the output`
	![Output of sudo fdisk -l](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/10/Screenshot_20250120_185345.png)

## Part 11: Using the df utility
- **Df Command Output:**
	- **Partition Size:** `/dev/mapper/ubuntu--vg-ubuntu--lv` 24590672 1K-blocks
	- **Space Used:** `7465252`
	- **Space Free:** `15850952`
	- **Percentage Used:** `33%`
	- **Measurement Unit:** `GiB(1K-blocks)`
- **Df -Th Command Output:**
	- **Partition Size:** `/dev/sda2`
	- **Space Used:** `216MiB`
	- **Space Free:** `1.6G`
	- **Percentage Used:** `12%`
	- **File System Type** `ext4`
	`(file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/11/Screenshot_20250120_210030.png)`
## Part 12: Using the du utility
- **Du Command Output:**
	![Du Output (including the size of all Contents for /var/log)](/src/images/PART_12/12.0.png)
	*Screenshot showing the size of /home, /var, /var/log folders, including the size of all Contents for /var/log.*

## Part 13: Installing and using the ncdu utility
- **Ncdu Command Output:**
	![Ncdu Output /var](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/13/Screenshot_20250120_202421.png)
	![Ncdu Output /home](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/13/Screenshot_20250120_202459.png)
	![Ncdu Output /var/log](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/13/Screenshot_20250120_202520.png)
	*Screenshot showing the size of /home, /var, /var/log folders.*

## Part 14: Working with system logs
- **Last Successful Login:**
	- Time: `Jan 20 20:25:35`
	- User Name: `admuser-hostname`
	- Login Method: `ssh2`
- **SSHD Service Restart:**
	`(file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/14/Screenshot_20250120_202802.png)`
	`(file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/14/Screenshot_20250120_202835.png)`
	`(file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/14/Screenshot_20250120_202856.png)`
	![SSHD Restart](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/14/Screenshot_20250120_203644.png)
	*Screenshot showing the SSHD service restart message.*

## Part 15: Using the CRON job scheduler and uptiming each 2 minutes
- **Adding Cron Task:**
	![CRON Task Adding](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/15/Screenshot_20250120_204435.png)
					  `(file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/15/Screenshot_20250120_204553.png)`
- **CRON Job Execution:**
	![Uptiming every 2 minutes](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/15/Screenshot_20250120_204712.png)
	*Screenshot shows the result of successful uptiming every two minutes*
- **List of Current CRON Jobs and Cron Job Execution at all:**
	![CRON Jobs](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/15/Screenshot_20250120_204840.png)
	*Screenshot showing the list of current CRON jobs.*
- **List of Current CRON Jobs After Removal:**
	![CRON Jobs After Removal](file:///home/rymundzu/PROJECTS/D01_Linux-1/src/pictures/15/Screenshot_20250120_205133.png)
	*Screenshot showing the empty list of current CRON jobs after removal.*
