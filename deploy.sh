#!/bin/bash

# Update the package list
sudo apt update

# Install Python and pip if not already installed
sudo apt install python3 python3-pip -y

# Set up a virtual environment
python3 -m venv venv
apt install python3-dotenv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt


# Run the application (assuming you have a run.py)
python run.py
