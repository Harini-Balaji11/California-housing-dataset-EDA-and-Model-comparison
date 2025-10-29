report:
	@mkdir -p reports
	jupyter nbconvert --to html --output reports/eda_report.html "notebooks/01_eda_california_housing.ipynb"

.PHONY: report

