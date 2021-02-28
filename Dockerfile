FROM  python:latest

EXPOSE 5000

RUN pip3 install flask flask_cors flask_bcrypt flask_mysqldb

RUN python3 server.py

# RUN chmod +x /var/lib/Peterest_api/entryPoint.sh

# ENTRYPOINT ["/var/lib/Peterest_api/entryPoint.sh"]