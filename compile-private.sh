#!/bin/bash
set -euo pipefail

# Helper to print usage
usage() {
    echo "Usage: $0 <domain>"
    echo "Example: $0 cisco"
    exit 1
}

if [ $# -ne 1 ]; then
    usage
fi

DOMAIN="$1"
TEMP_DIR="_temp_archive"
SOURCE_FILE="resume-${DOMAIN}.tex"
OUTPUT_NAME="akshit_mehta_resume_${DOMAIN}"

# 1. Clone private repository
echo "Cloning private archive repository..."
gh repo clone BriskAM/resume-archive "$TEMP_DIR"

# 2. Check if template exists
if [ ! -f "${TEMP_DIR}/${SOURCE_FILE}" ]; then
    echo "Error: Template ${SOURCE_FILE} not found in the private archive."
    rm -rf "$TEMP_DIR"
    exit 1
fi

# 3. Copy template to root
cp "${TEMP_DIR}/${SOURCE_FILE}" .

# 4. Cleanup clone directory immediately
rm -rf "$TEMP_DIR"

# 5. Compile the resume (which will use .env if present)
echo "Compiling ${SOURCE_FILE}..."
if python3 main.py "${SOURCE_FILE}" "${OUTPUT_NAME}"; then
    echo "Success! Compiled PDF written to ${OUTPUT_NAME}.pdf"
else
    echo "Compilation failed."
fi

# 6. Delete the copied source file so it's not committed by accident
rm -f "${SOURCE_FILE}"
