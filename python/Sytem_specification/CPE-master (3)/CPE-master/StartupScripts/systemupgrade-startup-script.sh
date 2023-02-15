#!/bin/bash

# Deactivate the virtual environment
deactivate

# Set root directory to the CPE application
cd /home/chiefnet/ChiefNet/SystemUpgrade

# Kill the current instance of CPE application
kill $(cat SystemUpgrade-application.pid)

# Activate the virtual environment
activate()
{ source ../SystemUpgradeVirtualEnv/bin/activate; }
activate

# Run CPE application
python main.py
   