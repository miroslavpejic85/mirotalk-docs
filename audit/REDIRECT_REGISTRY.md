# Redirect registry

Every changed public URL must be recorded here before implementation. Redirects must be permanent, one hop, preserve query strings where appropriate, and be tested in the production delivery layer.

| Old URL | New URL | Status | Implementation | Removal date | Verification |
| --- | --- | --- | --- | --- | --- |
| `/license/licensing-options/` | `/license/` | Ready for production Nginx install | Exact-match `301` rules in `deploy/nginx/redirects.conf`; client-side HTML fallback retained until live verification | Not scheduled | Nginx 1.18 syntax and local responses verified for both slash forms and query preservation; live endpoint remains `200` until the include is installed and Nginx is reloaded |

## Rules

1. Do not remove an old public URL without an approved replacement and redirect.
2. Prefer edge or server `301` responses over HTML or JavaScript redirects.
3. Keep redirecting URLs out of navigation and mark them `noindex`.
4. Verify the deployed response code, destination, query handling, and absence of redirect chains.
5. Add a removal date only after traffic and inbound-link review.