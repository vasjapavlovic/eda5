#!/bin/bash
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

cp $parent_path/eda5/contrib/sites/inital_backup/0001_initial.py $parent_path/eda5/contrib/sites/migrations/0001_initial.py
