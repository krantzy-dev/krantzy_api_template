# copier-python-api-template

[Copier](https://copier.readthedocs.io/) template for scaffolding FastAPI services: uv,
SQLAlchemy + Alembic, ruff, pytest, Docker, and a release-please-driven CI/CD setup.

This is the template's own README. It is **not** copied into generated projects, the
generated project gets its own `README.md` (rendered from `README.md.jinja`).

> **Note:** GitHub Actions are disabled for this repository (Settings → Actions → General).
> `.github/workflows/*` here are the workflows that ship *into generated projects*, not
> workflows meant to run against the template itself. Running them here would fail, since
> files like `pyproject.toml.jinja` aren't valid until rendered.

## Usage

```bash
copier copy git+https://github.com/krantzy/krantzy_api_template.git my-new-project
```

Pin to a specific tag if you don't want the latest template state:

```bash
copier copy --vcs-ref v0.1.0 git+https://github.com/krantzy/krantzy_api_template.git my-new-project
```

To pull in template updates on an already-generated project:

```bash
cd my-new-project
copier update
```

## Questions asked

| Variable                           | Purpose                                                              |
| ---------------------------------- | -------------------------------------------------------------------- |
| `project_name`                   | Human-readable name                                                  |
| `project_slug`                   | Package / directory slug                                             |
| `project_description`            | One-liner, used in`pyproject.toml` and the FastAPI title           |
| `author_name` / `author_email` | Author metadata for`pyproject.toml`                                |
| `python_version`                 | 3.11 / 3.12 / 3.13, drives`.python-version` and Docker base images |
| `db_name`                        | Postgres DB name (test DB is derived as`<db_name>_test`)           |
| `use_docker_compose`             | Whether to include`docker-compose.yml`                             |
| `github_owner`                   | Used to build`ghcr.io/<owner>/<slug>` image tags in CI             |

## Structure

- `src/{routes,services,repositories,schemas,models,load_data}` — layered app structure
- `src/config.py`, `database.py`, `exceptions.py`, `exception_handlers.py`, `logging_config.py`
- `alembic/` — wired to `src/config.py` and `src/models.Base`
- `.github/workflows/ci.yml` — lint + test on push/PR
- `.github/workflows/release-please.yml` — versioning, changelog, Docker build & push, `uv.lock` sync
- `Dockerfile` — multi-stage, uv builder → slim runtime
- `tests/integration/conftest.py` — savepoint-based DB session isolation per test

## Versioning this template

Tag releases normally; Copier reads Git tags (SemVer preferred) to resolve `--vcs-ref` and
to detect updates for `copier update`:

```bash
git commit -m "feat: add health probes"
git tag v0.1.0
git push origin main --tags
```

## Roadmap

- Helm chart for Kubernetes deployment
- Default authentication flow
- External secret management option
