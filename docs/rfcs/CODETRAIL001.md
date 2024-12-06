# RFC-001: Codetrail Initialize Command

## Metadata

- **Author(s):** @mochams
- **Status:** Implemented
- **Created:** 2024-12-07
- **Last Updated:** 2024-12-07
- **Related Issues:** N/A

## Summary

The `init` command creates a new `Codetrail` repository in a specified directory, establishing the basic directory structure and configuration files necessary for version control. It implements safety checks to prevent nested repositories and provides clear feedback to users.

## Background and Motivation

A version control system needs a way to initialize its data structures and configuration. The `init` command is the first step in using `Codetrail`, making it a foundational feature. Git's `init` command serves as inspiration, but we've chosen to implement additional safety features and a simpler initial structure.

## Terminology

- **Repository**: A directory containing version-controlled files and the `.codetrail` directory
- **Working Directory**: The directory where the repository is initialized
- **Repository Root**: The `.codetrail` directory containing all version control data

## Objectives

1. Create a new repository with minimal but sufficient structure
2. Prevent nested repositories to avoid confusion and conflicts
3. Maintain proper file permissions and directory structure
4. Provide clear feedback to users about the initialization process
5. Handle error cases gracefully with informative messages

## Non-Objectives

- Creating bare repositories (repositories without working directories)
- Implementing repository templates
- Supporting custom hooks
- Remote repository initialization

## Proposal

### Command Interface

```bash
codetrail init [path]
```

Where `path` is an optional argument defaulting to the current directory.

### Design

#### Repository Structure

The command creates the following structure:

```
<repository_root>/
├── .codetrail/
│   ├── HEAD          # Points to current branch (initially master)
│   ├── config        # Local repository configuration
│   ├── description   # Repository description file
│   ├── objects/      # Will store all repository objects
│   └── refs/
│       ├── heads/    # Branch references
│       └── tags/     # Tag references
```

### Algorithm

1. Validate target path
2. Check for existing repositories in parent directories
3. Check for existing repositories in child directories
4. Create repository directory structure
5. Initialize required files with default content
6. Set appropriate permissions

### Error Handling

- `ExistingRepositoryError`: When repository exists in parent/child directories
- `NotADirectoryError`: When target path exists but isn't a directory
- All errors logged with descriptive messages

## Examples

### Example 1: Basic Usage

```bash
# Initialize in current directory
python -m codetrail init
# Expected output: Initialized new repository at /current/path/.codetrail
```

### Example 2: Custom Path

```bash
# Initialize in specific directory
python -m codetrail init /path/to/repo
# Expected output: Initialized new repository at /path/to/repo/.codetrail
```

## Alternatives Considered

### Git's Approach

- Description: Follow Git's exact implementation
- Pros:
  - Familiar to users
  - Battle-tested design
- Cons:
  - More complex than needed
  - Allows nested repositories
- Why rejected: Chose simpler approach focused on safety and clarity

### Single Directory Structure

- Description: Put all files in repository root
- Pros:
  - Simpler structure
  - Easier to implement
- Cons:
  - Clutters working directory
  - Deviates from VCS conventions
- Why rejected: Clean separation of concerns is more important

## Implementation Plan

1. Core Repository Class (1 day)
   - Basic directory structure
   - File management methods
2. Safety Checks (1 day)
   - Parent/child repository detection
   - Path validation
3. Command Line Interface (1 day)
   - Argument parsing
   - Error handling

## Migration Plan

N/A - This is the first implementation.

## Success Criteria

### Functional Requirements

- Repository structure created correctly
- All necessary files initialized with correct content
- Proper permissions set
- No nested repositories allowed
- Clear error messages for all failure cases

### Non-Functional Requirements

- Command completes in under 100ms
- Memory usage under 50MB
- Clear, informative logging
- Consistent with project style guide

## Future Considerations

1. Support for bare repositories
2. Repository templates
3. Custom initial branch names
4. Extended configuration options
5. Hook scripts support

## Questions and Open Issues

1. Should we support custom initial branch names?
2. Do we need to implement repository templates in the future?
3. How should we handle permissions on different operating systems?

## References

1. [Git Init Documentation](https://git-scm.com/docs/git-init)
2. [Git Repository Layout](https://git-scm.com/docs/gitrepository-layout)
