# Steps to install and configure `tor` on Ubuntu 16.04.

## Installing tor in the system

### Install latest stable version
* Create a new 'sources' file for tor repository and open it:

    ```bash
    sudo nano /etc/apt/sources.list.d/tor.list
    ```
* Paste this content in that file, save and close it.
    ```bash
    deb http://deb.torproject.org/torproject.org xenial main
    deb-src http://deb.torproject.org/torproject.org xenial main
    ```
* Run these commands from bash shell
    ```bash
    gpg --keyserver keys.gnupg.net --recv A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89
    gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | sudo apt-key add -
    apt update
    apt install tor deb.torproject.org-keyring
    ```

### Install system repo version
* Run this command from bash shell
    ```bash
    sudo apt-get install tor
    ```

## Running/configuring tor to listen control signals on port 9051

### As a service
* Open the file `/etc/tor/torrc` with super user privileges and un-comment the following line.
    ```
    ControlPort 9051
    ```
* Grant read privileges to user for the file `/var/run/tor/control.authcookie`
    ```bash
    sudo chmod +r /var/run/tor/control.authcookie
    ```
* Restart tor daemon
   ```bash
   sudo systemctl restart tor.service
   ```

### Run tor from shell
* Check whether tor is running. If running, stop it.
* Run the following command from bash shell
    ```bash
    tor --controlport 9051
    ```
