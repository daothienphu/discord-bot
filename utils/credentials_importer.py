class CredentialsImporter():
    def __init__(self):
        self.Credentials = {}

    def GetCredentials(self, credentialsPath: str) -> dict:
        """Extract all the credentials from a 'credentials.txt' file"""
   
        with open(credentialsPath, 'r') as f:
            raw = f.readlines()
            for line in raw:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    self.Credentials[key] = value
        return self.Credentials