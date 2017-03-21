#!/bin/bash
gcc unicode_generator.c
mkdir -p ./unicodeString
rm -f ./unicodeString/*
./a.out
rm a.out
mv *.unicode ./unicodeString/
