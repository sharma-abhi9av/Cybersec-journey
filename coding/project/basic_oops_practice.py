class Target:
    def __init__(self, username, ip_address):
        self.username = username
        self.ip_address = ip_address
    def recon_summary(self):
        print(f">>> TARGET ACQUIRED: {self.username} at IP: {self.ip_address} <<<")
target_one = Target("admin", "10.10.10.1")
target_one.recon_summary()
