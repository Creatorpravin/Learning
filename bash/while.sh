#!/bin/bash

count=1
var="Exited"
while [ "$count" -le 5 ]; do
    echo "Count is $count"
    
    if [ "$var" == "Exited" ]; then
        echo "Breaking the loop"
        break
    fi

    count=$((count + 1))
done

echo "Loop finished"
