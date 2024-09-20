import paramiko

def send_file_via_ssh(hostname, port, username, password, local_file_path, remote_file_path):
    # Create an SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the remote server
        ssh.connect(hostname, port=port, username=username, password=password)
        
        # Use SFTP to transfer the file
        sftp = ssh.open_sftp()
        sftp.put(local_file_path, remote_file_path)
        sftp.close()

        print(f"File '{local_file_path}' successfully transferred to '{remote_file_path}'.")

    except Exception as e:
        print(f"Failed to transfer file: {e}")

    finally:
        # Close the SSH connection
        ssh.close()

# Example usage
send_file_via_ssh(
    hostname='your.remote.server',
    port=22,
    username='your_username',
    password='your_password',
    local_file_path='/path/to/local/file.txt',
    remote_file_path='/path/to/remote/file.txt'
)
