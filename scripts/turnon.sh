#!/bin/bash

rm -f tmp.root

for mean in 0 10 20; do

  for reso in 5 15 30 50 90; do

    ./turnon.py -m ${mean} -r ${reso} -o tmp.root

  done
  unset -v reso

done
unset -v mean
