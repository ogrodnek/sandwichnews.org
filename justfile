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

# Create a new blog post
new slug:
    #!/usr/bin/env bash
    set -euo pipefail
    YEAR=$(date +%Y)
    MONTH=$(date +%m)
    DAY=$(date +%d)
    DATETIME=$(date +%Y-%m-%dT%H:%M:%S)
    DIR="pages/posts/${YEAR}/${MONTH}/${DAY}"
    FILE="${DIR}/{{slug}}.md"
    IMAGES_DIR="static/images/posts/${YEAR}/${MONTH}/${DAY}"
    mkdir -p "${DIR}"
    cat > "${FILE}" << EOF
    title:
    date: ${DATETIME}
    tags: []

    EOF
    echo "Created ${FILE}"
    echo "Images: ${IMAGES_DIR}"

