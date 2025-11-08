# Picolas DDOS Tool

## Overview

Picolas DDOS Tool is a powerful Distributed Denial of Service (DDoS) tool designed to test the resilience of networks, servers, and other devices against DDoS attacks. This tool is for educational purposes and should be used responsibly.

## Features

- **Multiple Attack Types**: Supports various DDoS attack methods, including UDP, TCP, and HTTP floods.
- **Customizable Targets**: Allows specification of target IP addresses and ports.
- **User-Friendly Interface**: Easy-to-use command-line interface for configuring and launching attacks.
- **Banner Customization**: Supports custom banners for a personalized experience.

## Installation

### Prerequisites

- Python 3
- Required Python packages: `requests`, `pyfiglet`

### Steps

1. **Clone the Repository**

```bash
   git clone https://github.com/TuUsuario/PicolasDDOSTool.git
   cd PicolasDDOSTool
```

```bash
python picolas_ddos_tool.py
```

Options
Website Domain: Attack a specific website by entering the domain name.
IP Address: Attack a specific IP address by entering the IP and port number.
About: Displays information about the tool.
Exit: Exits the tool.
Banner
The tool supports a custom banner. You can replace the default banner with your own by modifying the print_banner function in the picolas_ddos_tool.py file. The current banner is hosted on Catbox and can be viewed here.

Examples
Attacking a Website
```bash
python picolas_ddos_tool.py
```
Follow the on-screen instructions to enter the website domain.

Attacking an IP Address
sh
python picolas_ddos_tool.py
Follow the on-screen instructions to enter the IP address and port number.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
