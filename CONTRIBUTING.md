## Contributing

Thanks for your interest in contributing! Please follow these quick guidelines:

1. Create a virtual environment and install dependencies from `requirements.txt`.
2. Use `black` and `isort` for formatting. Consider installing `pre-commit`.
3. Keep notebooks clean: run all cells top‑to‑bottom; avoid large outputs.
4. Place new notebooks under `notebooks/` with a clear numeric prefix.
5. Save figures to `reports/figures/` and avoid committing large binaries.
6. Describe changes clearly in the PR and include before/after visuals if relevant.

### Pre-commit (optional)
```
pre-commit install
pre-commit run --all-files
```

