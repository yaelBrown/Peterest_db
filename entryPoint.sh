#!/bin/bash
echo "Running server entryPoint.sh"
echo ""
echo "[01/02] Server: Installing pip packages"
pip3 install flask flask_cors flask_bcrypt flask_mysqldb
echo ""
echo "[02/02] Server: Running Application"
python3 server.py