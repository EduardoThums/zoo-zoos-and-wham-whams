#!/bin/bash

KEY=$1
KEY_FILE=$2

if [ -z $KEY ]; then
    echo "Missing key"
    exit 1
fi

if [ -z $KEY_FILE ]; then
    echo "Missing key file"
    exit 1
fi

gpg --output - $KEY_FILE | gpg --import

echo "Press trust and then 5. Press enter to continue:"
read

gpg --edit-key $KEY

