# Starting work with repo
```bash
$ ln -sv $(pwd)/pre-push $(pwd)/.git/hooks/
```

enables project check before git pushes

## Git Push all project types requirements:
* tagged commit
* repo contains .gitignore
* tracked .gitignore
* tracked project/


## Python project
### Required in repo
* requiremets.txt
* pyproject.toml [example](./pyproject.toml), must contains:
    * [tool.black]
    * [tool.coverage.run]
    * [tool.coverage.report]
    * [tool.mypy]
    * [tool.pytest.ini\_options]
* .gitignore, must contains:
    * venv (virtual environment dir)
    * .venv (virtual environment dir)
    * .coverage (coverage files)
    * coverage.xml (coverage files)
    * .pytest\_cache (pytest cache)
    * .mypy\_cache (mypy cache)
    * \_\_pycache\_\_ (python cache)
    * .python-version (pyenv file)

### Git Push requirements
* requirements.txt, must contains:
    * pytest
    * coverage[toml]
    * mypy
    * black
* .gitignore must contains (written above)
* must passes black check (not formattings must be required)
* must passes pytest check (all test must be passed)
* must passes coverage check (fail if [tool.coverage.report] contains fail\_under)
* must passes mypy check
* tracked requirements.txt


# TODO:
- [x] python project support
- [ ] golang project support
- [ ] clever python project support (have problems with pre-push success with uncommited files)
