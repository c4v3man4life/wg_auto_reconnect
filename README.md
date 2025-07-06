# wg_auto_reconnect
WireGuard Auto-reconnect Script

This repository contains a simple script that manages the WireGuard connection on your Raspberry Pi and ensures it starts on boot. The script automatically attempts to reconnect the WireGuard VPN if the connection is lost, providing a reliable and continuous VPN connection for your device. Purpose

The WireGuard Auto-reconnect script serves to address the issue of intermittent or dropped WireGuard VPN connections on your Raspberry Pi. By running this script, you can ensure that your Raspberry Pi stays connected to the WireGuard network and automatically attempts to reestablish the VPN connection if it is lost. Usage

    Script Setup

    Save the provided script in a file named wg_auto_reconnect.sh. Make the script executable by running the following command:

    bash

    chmod +x wg_auto_reconnect.sh

    Manual Testing

    Test the script manually by running it in the foreground with the following command:

    bash

    ./wg_auto_reconnect.sh

    Observe if the script correctly reconnects when the WireGuard service is temporarily stopped.

    Automatic Start on Boot

    To set up the script to automatically start on boot, the script needs to be configured as a service using systemd.

    Create a new service unit file:

    bash

sudo nano /etc/systemd/system/wg_auto_reconnect.service

Add the following content to the service unit file:

ini

[Unit] Description=WireGuard Auto-reconnect After=network.target

[Service] Type=simple ExecStart=/path/to/your/script/wg_auto_reconnect.sh

[Install] WantedBy=multi-user.target

Replace /path/to/your/script with the actual path to your wg_auto_reconnect.sh script.

Save the file and enable the service:

bash

sudo systemctl enable wg_auto_reconnect

    Reboot

    After setting up the service, reboot your Raspberry Pi to ensure the WireGuard Auto-reconnect script starts automatically on boot.

Customization

Please note that this script is a basic example and may require customization to suit your specific network configuration and security considerations. For instance, you may want to adjust the WireGuard interface name (wg0) and IP range (10.10.10.0/24) to match your setup.

Remember to be cautious when using this script and ensure that you have the necessary permissions and access rights for any network scanning and connectivity tasks that the script performs.

If needed, you can enhance the script by adding error handling, logging, or additional functionality as per your requirements. Disclaimer

This script is intended for educational and illustrative purposes. Always exercise caution and obtain proper authorization before conducting any network scanning or connectivity tasks. Unauthorized scanning of networks is illegal and unethical. The script should be used responsibly and in compliance with applicable laws and regulations.
