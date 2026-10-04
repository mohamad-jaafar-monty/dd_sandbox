# Detector probe: never run by the worker.
tools:
	git clone https://gitlab.example.com/grp/tools.git
	pip install git+https://$${CI_JOB_TOKEN}@gitlab.example.com/grp/probe-g.git
