# Run the development server
serve:
    uv run python blog.py

# Build the static site
build:
    uv run python blog.py build

# Run linting
lint:
    uv run ruff check .

# Run linting with auto-fix
lint-fix:
    uv run ruff check --fix .

# Format code
format:
    uv run ruff format .

# Run both linting and formatting
check: lint format

# Clean build directory
clean:
    rm -rf build/

# Full rebuild (clean + build)
rebuild: clean build

