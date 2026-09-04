# Redirect registry

Every changed public URL must be recorded here before implementation. Redirects must be permanent, one hop, preserve query strings where appropriate, and be tested in the production delivery layer.

| Old URL | New URL | Status | Implementation | Removal date | Verification |
| --- | --- | --- | --- | --- | --- |
| `/license/licensing-options/` | `/license/` | Ready for production Nginx install | Exact-match `301` rules in `deploy/nginx/redirects.conf`; client-side HTML fallback retained until live verification | Not scheduled | Nginx 1.18 syntax and local responses verified for both slash forms and query preservation; live endpoint remains `200` until the include is installed and Nginx is reloaded |
| `/sites/admin.html` | `/sites/admin/` | Ready for production Nginx install | Scoped regex `301` rule in `deploy/nginx/redirects.conf` | Not scheduled | Build and local redirect verification required |
| `/sites/bro.html` | `/sites/bro/` | Ready for production Nginx install | Scoped regex `301` rule in `deploy/nginx/redirects.conf` | Not scheduled | Build and local redirect verification required |
| `/sites/c2c.html` | `/sites/c2c/` | Ready for production Nginx install | Scoped regex `301` rule in `deploy/nginx/redirects.conf` | Not scheduled | Build and local redirect verification required |
| `/sites/cme.html` | `/sites/cme/` | Ready for production Nginx install | Scoped regex `301` rule in `deploy/nginx/redirects.conf` | Not scheduled | Build and local redirect verification required |
| `/sites/compare.html` | `/sites/compare/` | Ready for production Nginx install | Scoped regex `301` rule in `deploy/nginx/redirects.conf` | Not scheduled | Build and local redirect verification required |
| `/sites/mirotalk-vs-jitsi.html` | `/sites/mirotalk-vs-jitsi/` | Ready for production Nginx install | Scoped regex `301` rule in `deploy/nginx/redirects.conf` | Not scheduled | Build and local redirect verification required |
| `/sites/mirotalk-vs-whereby.html` | `/sites/mirotalk-vs-whereby/` | Ready for production Nginx install | Scoped regex `301` rule in `deploy/nginx/redirects.conf` | Not scheduled | Build and local redirect verification required |
| `/sites/mirotalk-vs-zoom.html` | `/sites/mirotalk-vs-zoom/` | Ready for production Nginx install | Scoped regex `301` rule in `deploy/nginx/redirects.conf` | Not scheduled | Build and local redirect verification required |
| `/sites/p2p.html` | `/sites/p2p/` | Ready for production Nginx install | Scoped regex `301` rule in `deploy/nginx/redirects.conf` | Not scheduled | Build and local redirect verification required |
| `/sites/projects.html` | `/sites/projects/` | Ready for production Nginx install | Scoped regex `301` rule in `deploy/nginx/redirects.conf` | Not scheduled | Build and local redirect verification required |
| `/sites/sfu.html` | `/sites/sfu/` | Ready for production Nginx install | Scoped regex `301` rule in `deploy/nginx/redirects.conf` | Not scheduled | Build and local redirect verification required |
| `/sites/story.html` | `/sites/story/` | Ready for production Nginx install | Scoped regex `301` rule in `deploy/nginx/redirects.conf` | Not scheduled | Build and local redirect verification required |
| `/sites/ultimate.html` | `/sites/ultimate/` | Ready for production Nginx install | Scoped regex `301` rule in `deploy/nginx/redirects.conf` | Not scheduled | Build and local redirect verification required |
| `/sites/web.html` | `/sites/web/` | Ready for production Nginx install | Scoped regex `301` rule in `deploy/nginx/redirects.conf` | Not scheduled | Build and local redirect verification required |

## Rules

1. Do not remove an old public URL without an approved replacement and redirect.
2. Prefer edge or server `301` responses over HTML or JavaScript redirects.
3. Keep redirecting URLs out of navigation and mark them `noindex`.
4. Verify the deployed response code, destination, query handling, and absence of redirect chains.
5. Add a removal date only after traffic and inbound-link review.