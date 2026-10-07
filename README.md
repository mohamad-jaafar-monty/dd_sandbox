# dd_sandbox
## Detector probe

The files below exist only to exercise the DevDox coverage scan's private-source detector. None of them is used by the install: the worker installs from `requirements.txt` alone, clones without submodules, and never runs tox, make or GitLab CI. A coverage scan of this repository must pause and list 22 cards, one per address (the same address in two files is one card):

| File | Form | Expected card |
|---|---|---|
| requirements.txt | git URL (the real private dependency) | github.com/mohamad-jaafar-monty/dd_sandbox_models, Token saved |
| requirements-detector-probe.txt | git URL with a scheme | gitlab.example.com/grp/probe-a |
| requirements-detector-probe.txt | ssh scheme | gitlab.example.com/grp/probe-b |
| requirements-detector-probe.txt | `${GIT_TOKEN}` placeholder | gitlab.example.com/grp/probe-c, code expects `${GIT_TOKEN}` |
| requirements-detector-probe.txt | token embedded in the URL | gitlab.example.com/grp/probe-d, Token is in the code |
| requirements-detector-probe.txt | domain with a port | nexus.example.com/repository/pypi/simple, username and token |
| requirements-detector-probe.txt | IPv4 address | 10.0.0.5/repository/pypi/simple, username and token |
| requirements-detector-probe.txt | single label with a port | nexus/repository/pypi/simple, username and token |
| requirements-detector-probe.txt | localhost | localhost/simple, username and token |
| requirements-detector-probe.txt | underscore in the host | my_nexus.example.com/simple, username and token |
| pip.conf | registry in a config file | artifactory.example.com/artifactory/api/pypi/pypi-remote/simple |
| tox.ini and Pipfile `[[source]]` | the same registry in two files | pypi.internal.example.com/simple, one card |
| Pipfile `[packages]` | git dependency in TOML | gitlab.example.com/grp/probe-e |
| .gitmodules | scp form `git@host:path` | bitbucket.org/team/probe-f, username and token |
| Makefile | plain `git clone` | gitlab.example.com/grp/tools |
| Makefile | `${CI_JOB_TOKEN}` placeholder | gitlab.example.com/grp/probe-g |
| .gitlab-ci.yml | token placeholder on a registry URL | gitlab.example.com/api/v4/projects/123/packages/pypi/simple |
| .gitlab-ci.yml | `github:org/repo` shorthand | github.com/acme/probe-i |
| .npmrc | npm registry and `//host/:_authToken=${NPM_TOKEN}` | one card, npm.example.com, code expects `${NPM_TOKEN}` |
| go.mod | Go module path | gitlab.example.com/grp/probe-j and github.com/acme/probe-k |
| requirements-long-line.txt | a normal line after an over-long one | github.com/acme/probe-after-long-line |

Must not appear: `pypi.org`, `files.pythonhosted.org`, `golang.org/x/text`, and the commented-out line in requirements-detector-probe.txt.

## Skip probes

Four things the detector must pass over and report under "Skipped while reading", not as cards:

| File | Why it is skipped |
|---|---|
| requirements-long-line.txt, line 2 | line longer than 4000 characters (its address, probe-long-line, must not appear) |
| constraints-oversize.txt | file larger than 1 MB |
| constraints-linked.txt | symlink to a file |
| linked-ci | symlink to a directory |
