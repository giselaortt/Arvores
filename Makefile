cov:
	pytest --cov


cov 2-3:
	pytest --cov-report term-missing --cov=2-3-tree


cov bst:
	pytest --cov-report term-missing --cov=binary-search-tree


cov avl:
	pytest --cov-report term-missing --cov=avl


