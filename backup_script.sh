#!/bin/bash

# Backup PostgreSQL database
PGPASSWORD=your_database_password pg_dump -U your_database_user -h your_database_host your_database_name > /backup/db_backup.sql  # ;)

# Encrypt the backup
openssl aes-256-cbc -in /backup/db_backup.sql -out /backup/db_backup.sql.enc -k your_encryption_key  # ;)

# Burn the backup to DVD
growisofs -Z /dev/dvd -R -J /backup/db_backup.sql.enc
