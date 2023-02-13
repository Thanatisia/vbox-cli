# vbox manager

Welcome to VBox Manager (Title WIP), 
a Cross-Platform CLI utility/application written in Python/Rust (To Be Decided) to streamline VirtualBox CLI Operations in an all-in-one environment.

## Basics
### VirtualBox (VBox) built-in commands and CLI functionality
- VBoxHeadless commands
    > These are the actual VBoxHeadless commands
    - Synopsis/Syntax
        ```console
        vboxmanage [actions] {options} <arguments
        ```
    - Parameters
        - Options
            - With Arguments
                + --startvm [virtual-machine-name] : Start the specified virtual machine; Equivalent to 'vbox-cli headless start vm'

- VBoxManage commands
    > These are the actual VBoxManage commands
    - Synopsis/Syntax
        ```console
        vboxmanage [actions] {options} <arguments
        ```
    - Parameters
        - Actions
            - internalcommands [command] {options} <arguments> : Execute a command within a virtual machine; Executes 'vboxmanage internalcommands'
                - Commands
                    - createrawvmdk : Create a new raw VMDK image file to map a Virtual Machine to the USB Drive (.vmdk file); Equivalent to 'vbox-cli manage create vmdk'
                        - Options
                            - With Arguments
                                + -filename [path/to/vmdk/file.vmdk] : Specify the output file name of the .vmdk raw virtual machine disk image file
                                + -rawdisk [physical-drive] : Specify the Physical Drive you wish to mount
                                    - Format:
                                        - Windows
                                            + You can refer to either Disk (Partition) Management or diskpart to get the drive number
                                            ```
                                            \\.\PhysicalDrive[drive_number]
                                            ```
                                        - Linux
                                            + Use 'lsblk' or 'sudo fdisk -l' to get the device name/drive name
                                            + Format: /dev/sdX
                            - Flags
            - createhd : Create a hard disk for a Virtual Machine; Equivalent to 'vbox-cli manage create hd'
                - Options
                    - With Arguments
                        - --filename [path/to/hard/disk/file.{vdi|vhd}] : Specify the output file name for the target hard disk you wish to create
                        - --format [hard-disk-format] : Specify the format/type of the Hard disk to create
                            - Hard Disk Formats
                                + VDI : Virtual Disk Image
                                + VHD : Virtual Hard Disk
                        - --size [size] : Set the total storage space of the Hard Disk; Syntax: n{MB|MiB|GB|GiB}
                            - Size Examples
                                + 80000 : 80GB = 1024MiB * 80
                    - Flags
            - createvm {options} : Create a new Virtual Machine with the options provided; Equivalent to 'vbox-cli manage create vm'
                - Options
                    - With Arguments
                        + --basefolder [directory-to-root-folder] : Set the base/root directory of the Virtual Machine data location
                        + --name [name-of-virtual-machine]        : Set the name of the virtual machine 
                        + --ostype [os-type]                      : Set the type of the Operating System
                            - OS Types
                                + Debian_64 : Debian 64-bit
                    - Flags
                        + --register : To Register the Virtual Machine with your Oracle VM VirtualBox Installation
            - modifyhd [hard drive name (*.vdi)] {options} : Modify VHD/VDI Image Files (the Virtual Machine Hard Drive); Equivalent to 'vbox-cli manage modify {hd|hard-drive}
                - Positionals
                    + hard drive name : Specify the hard drive name; i.e. virtualmachine.vdi | virtualmachine.vhd
                - Options
                    + --resize [size] : Specify the new size of the hard drive to resize to; Format: N{GIB|GB|MiB|MB}
            - modifyvm [virtual-machine-name] {options} : Modify an existing Virtual Machine; Equivalent to 'vbox-cli manage modify vm'
                - Positionals
                    + virtual-machine-name : Specify the name of the target Virtual Machine
                - Options
                    + --boot(n) [boot-type] : Set the Boot Order of your bootloader; What types to run first
                        - boot types:
                            + dvd
                            + disk
                        - Examples:
                            + --boot1 dvd --boot2 disk --boot3 none --boot4 none : Set system to look for a DVD first before proceeding to look for disk (if failed)
                    + --ioapic {on|off} : Enable/Disable Input-Output Advanced Programmable Interrupt Controllers (IO APIC)
                    + --memory {ram-memory} : Set your Memory (RAM)
                    + --vram {vram-size} : Set your Virtual Memory to allocate (Optional)
                    + --vrde {on|off} : Enable/Disable Virtual Remote Desktop Environment
                    + --vrdemulticon {on|off} : Enable/Disable Virtual Remote Desktop Environment Multicon
                    + --vrdeport [port_number] : Set VRDE Port Number
            - storageattach [virtual-machine-name] {options} : Attach a Storage Device to an existing Virtual Machine; Equivalent to 'vbox-cli manage storage attach' 
                - Positionals
                    + virtual-machine-name : Specify the name of the target Virtual Machine
                - Options
                    + --storagectl "Storage Controller Name" : Set the Storage Controller to use with the Virtual Machine
                    + --port [port_number] : Set Port Number for the storage device (start from 0)
                    + --device [device_number] : Set Device Number for the Storage Device (start from 0)
                    - --type [storage_medium_type] : Set the type of storage
                        - Examples:
                            + cddrive : CD Drive
                            + dvddrive : DVD Drive
                            + hdd : Hard Disk Drive
                    + --medium [path-to-image-or-file] : Set the path to the Image or Storage File to attach with the Storage Controller of the attached Virtual Machine (.vmdk/.vdi/.iso files etc.) 
            - storagectl [virtual-machine-name] {options} : Modify/Create Storage Controller
                - Positionals
                    + virtual-machine-name : Specify the name of the target Virtual Machine
                - Options
                    + --name [Storage Controller Name] : Specify the name of the Storage Controller to control/add/modify/manage
                    - --add [Storage Type to Add] : Specify the type for the new storage device you wish to add to the target Storage Controller
                        - Storage Types:
                            + ide : For IDE
                            + sata : For SATA
                    - --controller [Storage Controller] : Specify the type for the target Storage Controller
                        - Storage Controllers:
                            + PIIX4
                            + IntelAhci

## Setup
### Pre-Requisites
- Generate Virtual Environment
    ```console
    python -m venv [virtual-environment-folder-name]
    ```

- Source into Virtual Environment
    - Using Linux
        ```console
        source [virtual-environment-folder-name]/bin/activate
        ```
    - Using Windows
        ```console
        .\[virtual-environment-folder-name]\Scripts\activate
        ```

- Updating Python-pip
    ```console
    python -m pip install --upgrade pip
    ```

- Installing Dependencies
    - Using python-pip
        ```console
        python -m pip install -Ur Requirements.txt
        ```

### Dependencies
+ rust/python
- Python-PIP
    + virtualbox
    + argparse
+ make

### Obtaining
- Clone the repository
    ```console
    git clone https://github.com/Thanatisia/vbox-cli
    ```

### Compiling/Build System
- Build the source code using Makefile
    ```console
    make build
    ```

### Installation
- Install the script from system using Makefile
    ```console
    sudo make install
    ```

### Uninstall
- Remove the script from system using Makefile
    ```console
    sudo make uninstall
    ```

### Cleanup
- Remove all temporary objects generated during compilation/build/make process using Makefile
    ```console
    make clean
    ```

## Documentation
### Synopsis/Syntax
```console
vbox-cli {options} [positionals {suboptions}] <arguments>
```

### Parameters
- Positionals
    - headless [actions] {options} <arguments> : Run VBoxHeadless commands; Handles VirtualBox functionality such as starting the virtual machine from the terminal
        - Actions
            - start
                + vm [virtual-machine-name] {options} : Start a virtual machine; Executes 'vboxheadless --startvm [virtual-machine-name]'
                    - Positionals
                        + virtual-machine-name : Set the name of the target Virtual Machine to start
    - manage [action] {options} <arguments> : Run VBoxManage commands; Manage the Virtual Machine
        - Actions
            - attach [target] {options}
                - Target
                    - hd [virtual-machine-name] {options} : Attaches a new hard drive to the Virtual Machine; Specifically Executes 'vboxmanage storageattach --type hdd'
                         - Positionals
                            + virtual-machine-name : Specify the name of the target Virtual Machine
                        - Options
                            + --storagectl "Storage Controller Name" : Set the Storage Controller to use with the Virtual Machine
                            + --port [port_number] : Set Port Number for the storage device (start from 0)
                            + --device [device_number] : Set Device Number for the Storage Device (start from 0)                       
                            + --medium [path-to-image-or-file] : Set the path to the Image or Storage File to attach with the Storage Controller of the attached Virtual Machine (.vmdk/.vdi/.iso files etc.) 
                    - storage [virtual-machine-name] {options} : Attach a new storage to a storage controller; Executes 'vboxmanage storageattach'
                        - Positionals
                            + virtual-machine-name : Specify the name of the target Virtual Machine
                        - Options
                            + --storagectl "Storage Controller Name" : Set the Storage Controller to use with the Virtual Machine
                            + --port [port_number] : Set Port Number for the storage device (start from 0)
                            + --device [device_number] : Set Device Number for the Storage Device (start from 0)
                            - --type [storage_medium_type] : Set the type of storage
                                - Examples:
                                    + cddrive : CD Drive
                                    + dvddrive : DVD Drive
                                    + hdd : Hard Disk Drive
                            + --medium [path-to-image-or-file] : Set the path to the Image or Storage File to attach with the Storage Controller of the attached Virtual Machine (.vmdk/.vdi/.iso files etc.) 
            - control [target] {options}
                - Target
                    - storage [virtual-machine-name] {options} : Selects and Controls a target storage controller; Executes 'vboxmanage storagectl'
                        - Positionals
                            + virtual-machine-name : Specify the name of the target Virtual Machine
                        - Options
                            + --name [Storage Controller Name] : Specify the name of the Storage Controller to control/add/modify/manage
                            - --add [Storage Type to Add] : Specify the type for the new storage device you wish to add to the target Storage Controller
                                - Storage Types:
                                    + ide : For IDE
                                    + sata : For SATA
                            - --controller [Storage Controller] : Specify the type for the target Storage Controller
                                - Storage Controllers:
                                    + PIIX4
                                    + IntelAhci
            - create [target] {options}
                - Target
                    - hd {options} : Create a hard disk for a Virtual Machine; Executes 'vboxmanage createhd'
                        - Options
                            - With Arguments
                                - -f [path/to/hard/disk/file.{vdi|vhd}] | --filename [path/to/hard/disk/file.{vdi|vhd}] : Specify the output file name for the target hard disk you wish to create
                                - -t [hard-disk-format] | --format [hard-disk-format] : Specify the format/type of the Hard disk to create
                                    - Hard Disk Formats
                                        + VDI : Virtual Disk Image
                                        + VHD : Virtual Hard Disk
                                - -s [size] | --size [size] : Set the total storage space of the Hard Disk; Syntax: n{MB|MiB|GB|GiB}
                                    - Size Examples
                                        + 80000 : 80GB = 1024MiB * 80
                            - Flags
                    - vm {options} : Create a new Virtual Machine with the options provided; Executes 'vboxmanage createvm'
                        - Options
                            - With Arguments
                                + -b [directory-to-root-folder] | --basefolder [directory-to-root-folder] : Set the base/root directory of the Virtual Machine data location
                                + -n [name-of-virtual-machine]  | --name [name-of-virtual-machine]        : Set the name of the virtual machine 
                                + -o [os-type]                  | --ostype [os-type]                      : Set the type of the Operating System
                                    - OS Types
                                        + Debian_64 : Debian 64-bit
                            - Flags
                                + -r | --register : To Register the Virtual Machine with your Oracle VM VirtualBox Installation
                    - vmdk {options} : Shortcut to 'vboxmanage internalcommands createrawvmdk'; Create a new raw VMDK image file to map a Virtual Machine to the USB Drive (.vmdk file)
                        - Notes
                            + The VMDK raw image file will hold the path of the bootable USB drive within VirtualBox
                            + Helps VirtualBox to recognize the USB drive as a normal Virtual Disk Drive when available
                        - Options
                            - With Arguments
                                + -f [path/to/vmdk/file.vmdk] | -filename [path/to/vmdk/file.vmdk] : Specify the output file name of the .vmdk raw virtual machine disk image file
                                + -r [physical-drive]  | -rawdisk [physical-drive] : Specify the Physical Drive you wish to mount
                                    - Format:
                                        - Windows
                                            + You can refer to either Disk (Partition) Management or diskpart to get the drive number
                                            ```
                                            \\.\PhysicalDrive[drive_number]
                                            ```
                                        - Linux
                                            + Use 'lsblk' or 'sudo fdisk -l' to get the device name/drive name
                                            + Format: /dev/sdX
                            - Flags
            - modify [target] {options}
                - Modify Targets
                    + hd [hard drive name (*.vdi)] {options} | hard-drive [hard drive name (*.vdi)] {options} : Modify VHD/VDI Image Files (the Virtual Machine Hard Drive); Executes 'vboxmanage modifyhd'
                        - Positionals
                            + hard drive name : Specify the hard drive name; i.e. virtualmachine.vdi | virtualmachine.vhd
                        - Options
                            + --resize [size] : Specify the new size of the hard drive to resize to; Format: N{GIB|GB|MiB|MB}
                    + vm [virtual-machine-name] {options} : Modify an existing Virtual Machine; Executes 'vboxmanage modifyvm'
                        - Positionals
                            + virtual-machine-name : Specify the name of the target Virtual Machine
                        - Options
                            + --boot(n) [boot-type] : Set the Boot Order of your bootloader; What types to run first
                                - boot types:
                                    + dvd
                                    + disk
                                - Examples:
                                    + --boot1 dvd --boot2 disk --boot3 none --boot4 none : Set system to look for a DVD first before proceeding to look for disk (if failed)
                            + --ioapic {on|off} : Enable/Disable Input-Output Advanced Programmable Interrupt Controllers (IO APIC)
                            + --memory {ram-memory} : Set your Memory (RAM)
                            + --vram {vram-size} : Set your Virtual Memory to allocate (Optional)
                            + --vrde {on|off} : Enable/Disable Virtual Remote Desktop Environment
                            + --vrdemulticon {on|off} : Enable/Disable Virtual Remote Desktop Environment Multicon
                            + --vrdeport [port_number] : Set VRDE Port Number
- Optionals
    - With Arguments
        + -e [path/to/virtualbox] | --executable [path/to/virtualbox] : Specify custom path to VirtualBox directory
    - Flags
        - -g {options} | --get-properties {options} : Get properties and details/specifications of a Virtual Machine
            - Options
                - virtual-machine-name [vm-name] : Get details for a specific Virtual Machine Name 
                    - Parameter
                        - vm-name : Specify the target Virtual Machine
                            + Default: Get all Virtual Machines listed row-by-row
                - keyword [keyword]
                    - Parameters
                        - keyword : Specify the target property to search and filter
                            - Property/Detail/Specification Keywords
                                + distribution : Get Distribution for the Virtual Machine; Default: Get Distributions for all Virtual Machines seperated by ',' delimiter
                            - Default: Get all Properties/Details
        + -l  | --list : List all existing Virtual Machines each in a new line
        - -lf [filter-category] {argument} | --list-filtered [filter-category] {argument} : List specific Virtual Machines (Filtered by Categories)
            - Filter Categories
                + vm-name [contains-this-keyword] : Filter by VM name
                + dist [distribution] : Filter by Distribution; 
        + -t  | --tui : Run in Terminal User Interface (TUI) mode; Type in commands manually
        + -h  | --help : Display this verbose help message

### Usage
- Create
    1. Create a Virtual Machine
        ```console
        vbox-cli manage create vm -n "new_vm" -o "Arch_64" -r -b ~/Desktop
        ```
    2. Create a new Hard Disk
        + Filename: ~/Desktop/hard-disks/disk.vhd
        + Size: 50GiB
        + Format: Virtual Hard Disk (VHD)
        ```console
        vbox-cli manage create hd -f ~/Desktop/hard-disks/disk.vhd -t VHD -s 50GiB
        ```
    3. Create a USB Virtual Machine Disk Image File (.vmdk)
        ```console
        vbox-cli manage create vmdk -filename ~/Desktop/vmdk/file.vmdk -rawdisk /dev/sdX
        ```
- Modify
    1. Modify Virtual Machine Hard Drive (VHD/VDI)
        - Resize
            ```console
            vbox-cli manage modify {-hd | --hard-drive} {-r | --resize} xGiB
            ```
- Attach
    1. Attach a storage device to an existing Virtual Machine
        ```console
        vbox-cli manage attach storage "Virtual-Machine" {options}
        ```
- Virtual Machine Control
    1. Start a Virtual Machine
        ```console
        vbox-cli headless start vm
        ```

- General
    + Display this verbose help message
        ```console
        vbox-cli -h
        ```
    - Windows
        + Specify custom VirtualBox directory
            ```batchdos
            vbox-cli -e "%HOMEDIR%\Desktop\path\to\VBox" {actions]
            ```
    - Terminal User Interface (TUI)
        - Examples
            ```console
            vbox-cli -t
            ---------------------
            # System will request for user to enter an action to execute
            # These actions are the VBox utilities (VBoxManage, VBoxHeadless etc)
            Available Actions:
                - vboxmanage
                - vboxheadless
            Action > [vboxmanage | vboxheadless | ...]
            
            # System will request for user to enter options to parse to the action
            # Options will change depending on the action provided.
            # User to type in the keyword 'exit' to stop the Options
            Available Options:
                - 
                - 
            Options : 
            - Option-1
            - Option-2
            ...

            # System will process the command 
            # by combining the command and its parameters

            # System will execute command
            ```
    - List Virtual Machine names in Standard Output
        - List All
            ```console
            ### Input ###
            vbox-cli -l

            ### Output ###
            # VM_1
            # VM_2
            # VM_3
            # VM_4
            # ...
            ```
        - List Filtered by Categories
            - By Distribution
                + List all Debian Virtual Machines
                    ```console
                    vbox-cli -lf dist "Debian"
                    ```
                + List all ArchLinux Virtual Machines
                    ```console
                    vbox-cli -lf dist "Arch"
                    ```
            - By Virtual Machine Name Keyword
                + List all Virtual Machines with names containing "contains-this-keyword"
                    ```console
                    vbox-cli -lf vm-name "contains-this-keyword"
                    ```
    - Get Properties/Details of a Virtual Machine
        - Get all Properties/Details for all Virtual Machines
            ```console
            vbox-cli -g
            ```

        - Get all Properties/Details for a Virtual Machine
            ```console
            vbox-cli -g virtual-machine-name "Virtual_Machine" 
            ```

        - Get the Distribution for a Virtual Machine
            ```console
            vbox-cli -g virtual-machine-name "Virtual_Machine" keyword "distribution"
            ```

## References

## Resources

## Remarks
