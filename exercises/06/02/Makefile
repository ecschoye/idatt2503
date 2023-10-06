.PHONY: install run

# Function to check if a command exists
check-command = $(shell command -v $(1) 2> /dev/null)

# Check for bun or npm and set the appropriate command variables
BUN := $(call check-command,bun)
NPM := $(call check-command,npm)

# Default install target
install:
ifdef BUN
	@echo "Using bun to install dependencies."
	bun install
else ifdef NPM
	@echo "Using npm to install dependencies."
	npm install
else
	@echo "Neither bun nor npm found. Please install one of them."
	exit 1
endif

# Default run target
run: install
ifdef BUN
	@echo "Using bun to run the application."
	bun run serve & bun run server.js
else ifdef NPM
	@echo "Using npm to run the application."
	npm run serve & npm run server.js
else
	@echo "Neither bun nor npm found. Please install one of them."
	exit 1
endif
