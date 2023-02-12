import ftplib
# Connect FTP Server
ftp_server = ftplib.FTP('185.116.162.93','cansat@secure-iot.ir','aEGQZ5X7t')
 
# force UTF-8 encoding
ftp_server.encoding = "utf-8"
 
# Enter File Name with Extension
filename = "1.jpg"
 
# Read file in binary mode
with open(filename, "rb") as file:
    # Command for Uploading the file "STOR filename"
    ftp_server.storbinary(f"STOR {filename}", file)


print('http://secure-iot.ir/cansat/{}'.format(filename))
# Close the Connection
ftp_server.quit()