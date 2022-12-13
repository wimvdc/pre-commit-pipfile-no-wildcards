# pipfile-no-wildcards

Pre-commit which makes your commit fail when your Pipfile contains a wildcard (dev-)dependency.

# Example

Sample `.pre-commit-config.yaml`

```yaml
- repo: https://github.com/wimvdc/pre-commit-pipfile-no-wildcards
  rev: v0.1.0
  hooks:
    - id: pipfile-no-wildcards
```

## Arguments

If for some reason your Pipfile is not located in the root of your project, you can specify the path to your Pipfile using the `args` argument.

```yaml
- repo: https://github.com/wimvdc/pre-commit-pipfile-no-wildcards
  rev: v0.1.0
  hooks:
    - id: pipfile-no-wildcards
      args: [-pf=foo/bar/Pipfile]
```
