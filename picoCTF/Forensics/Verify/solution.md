# Solution
SSH into the server with the given password
`ssh -p 51350 ctf-player@rhea.picoctf.net`

To check the has of every file in the directory use sha256sum files/*, and grep for the file with the checksum 467a10447deb3d4e17634cacc2a68ba6c2bb62a6637dad9145ea673bf0be5e02
`sha256sum files/* | grep 467a10447deb3d4e17634cacc2a68ba6c2bb62a6637dad9145ea673bf0be5e02`

Finally, to get the flag decrypt the file with the correct hash
`./decrypt.sh files/c6c8b911`