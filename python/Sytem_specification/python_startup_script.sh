#!/bin/bash

apt install python3.10-venv

python3 -m venv VirEnv

activate()
{
VirEnv/bin/activate
}

activate

python3 main.py

read -n 1 -p " "

