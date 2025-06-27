#! /bin/bash
#
# Updates `saltbox-bridge-messages` commit hash to current in requirements.
# Run from outer repo e. g.:
#
#   $ cd ~/sources/satlbox-core/
#   $ ../saltbox-bridge-messages/bin/update_saltbox_bridge_messages_requirements.sh
#

set -e

local_requirements_basename='local_requirements.txt'

local_requirements_file=$(find . -name "$local_requirements_basename")
saltbox_bridge_messages_dir=$(dirname "$(dirname "$0")")

pushd "$saltbox_bridge_messages_dir" > /dev/null
last_hash=$(git log -n 1 --pretty='format:%H')
popd > /dev/null

sed --in-place "s/\(saltbox-bridge-messages @ .*@\).*/\1${last_hash}/" "$local_requirements_file"

git diff "$local_requirements_file"
