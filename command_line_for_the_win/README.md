# Command line for the win

## STEPS TO USE THE SFTP CL TOOL

1. Open commqnd prompt in local machine
2. Connect local machine to remote server i.e sandbox environment (Ubuntu)
using command sftp <remote-username>@<remote-host-id> and
enter password when prompted.
3. Check if successfully entered the sftp interface, should see the prompt `sftp>`.   
4. Navigate to dir containing the screenshots in local system using `lcd`.
5. Upload the screenshot files into the remote server, i.e
`/root/alx-aystem_engineering-devops/command_line_for_the_win/` using `put` command
6. `put <screenshot files>` `/root/alx-aystem_engineering-devops/command_line_for_the_win/`.
7. Navigate to the remote dir i.e `/root/alx-aystem_engineering-devops/command_line_for_the_win/`
 and check if the screenshot files uploaded successfully using `ls` command.
8. Exit from `sftp` interface using `exit` or `bye`.
