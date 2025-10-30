# How to release

For project maintainers

1. Update the version number in `pyproject.toml`
2. `poetry check`
3. `git commit`
4. `git tag v$version HEAD`
5. `git push`
6. `git push --tags`
7. Go to https://github.com/ISDuBA/isduba-python-client/releases and create a new release from the tag
8. `poetry build`
9. `poetry upload` or `twine upload dist/...`
