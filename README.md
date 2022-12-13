# pipfile-no-wildcards

Pre-commit which makes your commit fail when your Pipfile contains a wildcard (dev-)dependency.

# Sample

Sample `.pre-commit-config.yaml`

```yaml
- repo: https://github.com/wimvdc/pre-commit-pipfile-no-wildcards
  rev: v0.1.0
  hooks:
    - id: pipfile-no-wildcards
```
