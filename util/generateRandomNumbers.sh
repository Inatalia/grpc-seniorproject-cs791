#!/bin/bash
gcc number_generator.c
mkdir -p ./randomNumbers
rm -f ./randomNumbers/*
./a.out
rm a.out
mv *.numbers ./randomNumbers/
