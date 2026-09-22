# Platform Workflows

Reusable GitHub Actions workflows for Bambis-Lab. The library uses least-privilege permissions, bounded runtimes, full-SHA pinned external actions, and no paid third-party services.

## Runner policy

- `general`: lightweight HA/config/infrastructure validation.
- `build`: Android, Docker and portable Swift builds.
- `blackglass + isolated`: BlackGlass-only workloads; no `universal` label is assigned.
- Apple/Xcode jobs remain on GitHub-hosted macOS where Xcode is required.
- Public-repository policy/security/SBOM jobs default to GitHub-hosted Ubuntu.

## Reusable workflows

`repo-policy`, `security`, `python-ci`, `node-ci`, `android-ci`, `swift-portable-ci`, `apple-xcode-ci`, `ha-config-ci`, `docker-ci`, `blackglass-ci`, `sbom`, and `release` are callable via `workflow_call`.

`release.yml` only validates and uploads an artifact. It does not publish a GitHub Release or deploy production systems. Deployment remains behind a separate user approval gate.
