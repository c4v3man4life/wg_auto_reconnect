import os
import subprocess

def create_wg_auto_reconnect_script():
    script_content = '''#!/bin/bash

# Function to check WireGuard connection status
function check_wireguard_connection() {
    wg show wg0 | grep -q "peer"
    return $?
}

# Function to attempt reconnection
function attempt_reconnect() {
    echo "WireGuard connection is down. Attempting to reconnect..."
    wg-quick up wg0
    sleep 5
}

# Main loop
while true; do
    if check_wireguard_connection; then
        echo "WireGuard connection is up."
    else
        attempt_reconnect
    fi
    sleep 60   # Adjust the interval (in seconds) to check the connection status
done
'''

    script_path = '/opt/src/wg_auto_reconnect.sh'
    with open(script_path, 'w') as file:
        file.write(script_content)

    # Make the script executable
    os.chmod(script_path, 0o755)

def create_systemd_service():
    service_content = '''[Unit]
Description=WireGuard Auto-reconnect
After=network.target

[Service]
Type=simple
ExecStart=/opt/src/wg_auto_reconnect.sh

[Install]
WantedBy=multi-user.target
'''

    service_path = '/etc/systemd/system/wg_auto_reconnect.service'
    with open(service_path, 'w') as file:
        file.write(service_content)

def setup_wireguard_auto_reconnect():
    # Step 1: Create the wg_auto_reconnect.sh script
    create_wg_auto_reconnect_script()

    # Step 2: Create the systemd service unit file
    create_systemd_service()

    # Step 3: Enable the service
    subprocess.run(['sudo', 'systemctl', 'enable', 'wg_auto_reconnect'])

    print("WireGuard auto-reconnect setup complete!")

if __name__ == "__main__":
    setup_wireguard_auto_reconnect()

