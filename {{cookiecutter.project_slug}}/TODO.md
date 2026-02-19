# Project TODOs

## Code Improvements
- [x] **CORS Configuration**: Update `app/main.py` to read `allow_origins` from `settings.BACKEND_CORS_ORIGINS` instead of hardcoding `["*"]`.
- [x] **Dockerfile**: Verify `Dockerfile` exists and is optimized for production (multi-stage build).
- [x] **Health Check**: Confirm `app/api/health.py` is fully implemented.

## Cookiecutter Template Conversion
Steps to convert this scaffold into a reusable Cookiecutter template:

1. [ ] **Setup Directory**: Create a new folder `fastapi-template`.
2. [ ] **JSON Config**: Create `cookiecutter.json` in the new folder with variables:
   - `project_name`
   - `project_slug`
   - `postgres_user`, `postgres_password`, `postgres_db`
   - `app_port`
3. [ ] **Move Source**: Copy the current project content into `fastapi-template/{{cookiecutter.project_slug}}/`.
4. [ ] **Templatize Files**:
   - `app/core/config.py`: Replace hardcoded app name and DB creds with `{{ cookiecutter.variable }}`.
   - `README.md`: Update title and description.
   - `docker-compose.yml`: Parameterize ports and env vars.
5. [ ] **Cleanup Hook**: Add `hooks/post_gen_project.py` to remove the `.git` directory after generation.