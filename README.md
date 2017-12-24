# **keepass2password-store**

keepass2password-store is a python script to convert a `csv` file from
KeePass into a `password-store database`

It will create a password-store database where the first line is the
password.  The second line is `Username:`  username.  The third line
is `URL:` the.url.  Then a line with `Notes:`, followed by the notes
field from KeePass.

# Assumptions

The user will be shown a list of keys in the *GnuPG keyring*.  It assumes
that the GnuPG files are in `~/.gnupg`.

The user chooses the key to use for the encryption and the database files
are encrypted with that key.

# Example

One argument is required and that is the *csv* file to convert.  For example,

`keepass2password-store ~/.password-store`
<br />

# Dependencies

password-store2keepass requires `os`, `sys`, `csv`, and `gnupg`.
