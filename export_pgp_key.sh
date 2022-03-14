#!/bin/bash

KEY=$1

if [ -z $KEY ]; then
    echo "Missing key parameter!"
    exit 1
fi

if [[ $(gpg --list-keys | grep $KEY -o) != $KEY ]];
then
    echo "Key not found! Look at gpg --list-keys"
    exit 1
fi

rm pubkey.gpg 2>/dev/null
rm keys.asc 2>/dev/null

gpg --output pubkey.gpg --export $KEY && \
gpg --output - --export-secret-key $KEY | \
    cat pubkey.gpg - | \
    gpg --armor --output keys.asc --symmetric --cipher-algo AES256 | \
rm pubkey.gpg

