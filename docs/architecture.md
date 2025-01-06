# Zentri AI Architecture

Zentri AI is designed as a modular, extensible framework for building code analysis agents. The architecture promotes scalability, reusability, and ease of integration with various platforms and workflows.

## High-Level Overview

The core components of Zentri AI are structured into the following layers:

1. **Agent Core**: Manages the lifecycle of agents, including initialization, task execution, and result aggregation.
2. **Analyzer Modules**: Perform specific code analysis tasks such as linting, complexity analysis, and dependency graph generation.
3. **Integrations**: Provide connectors to platforms like GitHub, GitLab, or local repositories for seamless analysis workflows.
4. **User Interface** (Future Scope): A planned component for a graphical or command-line interface to interact with agents and visualize results.

---

## Core Components

### 1. Zentri Agent Core

The central hub that orchestrates the analysis workflow:

- **Initialization**: Configures the environment and loads necessary modules.
- **Task Management**: Delegates tasks to specific analyzer modules based on user input or default configuration.
- **Result Handling**: Aggregates and formats results for output or integration.

Key file: `zentri_agent.py`

---

### 2. Analyzer Modules

Analyzer modules are pluggable components responsible for different types of code analysis. These include:

- **Lint Checker**: Ensures code adheres to best practices and coding standards.
- **Complexity Analyzer**: Identifies hotspots in the codebase that may require refactoring.
- **Dependency Analyzer**: Maps out dependencies within the project to detect potential issues or bottlenecks.

Each module is located in the `src/analyzer/` directory and implements a common interface for consistency.

---

### 3. Integrations

Integrations allow Zentri AI to connect with external systems and repositories:

- **GitHub Connector**: Fetches repositories and PRs for analysis.
- **GitLab Connector**: Similar functionality for GitLab.
- **Local Integration**: Allows analysis of local projects without an external repository.

Integrations are located in `src/integrations/`.

---

### 4. Planned: User Interface

Future versions of Zentri AI aim to provide a user-friendly interface:

- **CLI Enhancements**: Add interactive prompts and detailed output customization.
- **Web Dashboard**: A web-based tool for managing agents, configuring analysis, and viewing results.

---

## Data Flow

1. **Input**: Zentri AI accepts input as a repository URL or a local file path.
2. **Processing**: The Agent Core dispatches tasks to the relevant analyzer modules.
3. **Output**: Results are returned in a standardized JSON format or displayed via the CLI.

---

## Extensibility

Developers can extend Zentri AI by:

- Adding new analyzer modules by implementing the common interface.
- Creating custom integrations for new platforms.
- Enhancing the Agent Core with additional functionality.

For detailed steps on contributing, see the [CONTRIBUTING.md](../CONTRIBUTING.md).

---

**Zentri AI's architecture ensures adaptability and scalability, empowering developers to tackle complex codebases efficiently.**
