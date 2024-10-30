# Complete Guide to Using nix-shell

## Windows special instructions - linux and macos should skip this section.
if you dont have WSL2, or are unsure if you have WSL2, it is a good idea to follow this official microsoft guide to set it up: https://learn.microsoft.com/en-us/windows/wsl/install

After that is done you can run `sudo apt install neofetch` and then run `neofetch` to see if you have WSL2 installed and set up properly.

We are now assuming you have entered a WSL2 terminal.
If you have WSL2 set up properly, you should now clone the moodle repository or your own fork of it inside of a wsl folder. (this is because leaving it inside of a windows folder has serious performance issues.)

```bash
cd ~
git clone (your fork of moodle)
cd (your fork of moodle)
```

## Installing Nix
To properly install nix you need to go to this website https://nixos.org/download/ and follow the instructions for your operating system. (linux, macos, or windows)


## Understanding nix-shell Basics
- How to use nix-shell
Just go to the root of your moodle repository and run `nix-shell` and it will automatically set up the environment + the database for you.


## Troubleshooting
- If you are having issues make sure to read the FAQ below.
- If the FAQ didnt help then message Diego or mantarias on discord.


## FAQ
### General - Any command shown here should be run from within an active nix-shell environment.
- what ports do i use? Database: 3306, Moodle: 8000, Adminer: 8080
- How do i run phpunit tests? Run `runit`. This will set up and run phpunit tests for you. Be aware that the first run might take a while.
- How do i quickly set up moodle after deleting config.php. Just run `create_config`. This will set up the config.php for you.
- How do i run CodeSniffer? Run `sniffit`. This will run the codesniffer for you.
- How do i run CodeSniffer so it automatically fixes errors for me? Make sure to run sniffit first, and then run `fixit`. This will run the codesniffer fixer for you. Keep in mind this can only fix some errors.
- How do i reset the database? Exit nix-shell by writing `exit`, then delete the mariadb_data folder and run `nix-shell` again.
- I cant open adminer (localhost:8080) what do i do? It is likely that you already have mariadb running on this port, so you need to make sure it is disabled, and then re-run `nix-shell`
### WSL2
- My performance is bad how do i fix it? Make sure you have WSL2 set up properly, and that you are running the moodle repository from within a WSL folder. (see windows special instructions above)

### MacOS
- Mac is not completely ready yet, either ask diego or wait for this guide to be finished with macos.
