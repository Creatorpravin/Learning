#!/bin/bash

cd /home/chiefnet/ChiefNet/

RequirementFile=CPE/requirements.txt

activate()
{ 
    source VirtualEnvironment/bin/activate; 
}

if [ -f $RequirementFile ]; then
    activate

    pip install -r $RequirementFile

    pipStatus=$?
    if [ $pipStatus == 0 ];then
        logger -s "pip installed success"
    else
        logger -s "pip installed failed"
    fi

    deactivate

    exit $pipStatus
fi
