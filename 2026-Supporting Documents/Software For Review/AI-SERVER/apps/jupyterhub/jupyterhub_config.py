c = get_config()

c.JupyterHub.bind_url = "http://0.0.0.0:8000"
c.JupyterHub.authenticator_class = "dummy"
c.Authenticator.admin_users = {"admin"}
c.Spawner.default_url = "/lab"

# Replace DummyAuthenticator before production:
# c.JupyterHub.authenticator_class = "oauthenticator.generic.GenericOAuthenticator"

c.JupyterHub.log_level = "INFO"
