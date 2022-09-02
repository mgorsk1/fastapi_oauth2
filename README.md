# Fast API with Oauth2 Proxy

This is a minimal example of adding OAuth2 Proxy Authentication (Keycloak provider) to your FastAPI microservice.

This approach 'hides' original FastAPI backend behind OAuth2 proxy, which handles communication with Keycloak and passes
access token to your API after successful login.

## Prerequisites

Add to your `/etc/hosts`:

```text
127.0.0.1 keycloak
127.0.0.1 oidc
```
