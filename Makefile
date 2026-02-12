help_a:
    @echo "Makefile commands"
    @echo " install - установка зависимостей"
    @echo " run_test - запустить автотесты"
    @echo " test_only - запустить автотесты только один автотест с меткой only"
    @echo " linter - запустить проверку кода"

install:
    pip install -r requiremets.txt

run_test:
    python -m pytest -v

linter:
    black .
    isort .
    flake8