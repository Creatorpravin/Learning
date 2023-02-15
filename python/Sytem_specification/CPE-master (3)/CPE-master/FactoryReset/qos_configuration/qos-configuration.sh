#!/bin/sh

tc qdisc del dev enp1s0 root handle 1:0 hfsc > /dev/null
tc qdisc del dev enp2s0 root handle 1:0 hfsc > /dev/null
tc qdisc del dev tun0 root handle 1:0 hfsc > /dev/null
tc qdisc del dev tun1 root handle 1:0 hfsc > /dev/null
tc qdisc del dev tun2 root handle 1:0 hfsc > /dev/null
tc qdisc del dev tun3 root handle 1:0 hfsc > /dev/null
tc qdisc del dev tun4 root handle 1:0 hfsc > /dev/null
