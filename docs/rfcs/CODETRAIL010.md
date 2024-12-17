# RFC-010: Codetrail Configuration Command

## Metadata

- **Author(s):** @mochams
- **Status:** Draft
- **Created:** 2024-12-08
- **Last Updated:** 2024-12-07
- **Related Issues:** N/A

## Summary

The `config` command manages local repository configuration settings in `Codetrail`. It provides a way to read and write configuration values essential for repository operation, such as user identity and repository-specific settings.

## Background and Motivation

A version control system needs to maintain configuration settings to identify users and customize repository behavior. The config command is crucial as it's typically the second step after initialization, allowing users to set their identity and repository preferences.

## Terminology

- **Local Config**: Configuration settings specific to a single repository
- **Entry**: A key-value pair in the configuration file
- **Config Section**: A group of related config entries (e.g., user.\*)

## Objectives

- Provide a mechanism to set and get configuration values
- Store configuration in a human-readable format
- Support hierarchical configuration keys (sections and subsections)
- Enable listing of all configuration values
- Support basic data types (strings, integers, booleans)

## Non-Objectives

- Global configuration support (future enhancement)
- System-wide configuration
- Configuration templates
- Configuration includes/imports
- Environment variable overrides

## Proposal

### Command Interface

```bash
# Set a config value
codetrail config set <key> <value>

# Get a config value
codetrail config get <key>

# List all config values
codetrail config list

# Remove a config value
codetrail config unset <key>

# Edit a config value
codetrail config edit <key> <new value>
```

### Design

#### Configuration File Structure

```ini
[user]
    name = John Doe
    email = john@example.com
[core]
    ignorecase = false
    autocrlf = input
```

#### Data Structures

1. Configuration File `.codetrail/config`

   - Plain text file
   - INI-style format
   - Sections denoted by [section] i.e user and core
   - Key-value pairs under sections

2. Key Format
   - Section.key (e.g., user.name)

#### Sections Supported

##### User

This section contains user profile information. Variables include: `name` and `email`.

##### Core

This section holds the core configuration required for functionality. Variables are still to be determined and will be outlined in a future RFC.

### Algorithm

1. Reading Configuration:
   - Parse config file into sections
   - Split keys by dots to navigate sections
   - Return value if found, None if not

2. Writing Configuration:
   - Parse key into section and name
   - Create section if it doesn't exist
   - Update or create key-value pair
   - Write entire config back to file

3. Listing Configuration:
   - Read entire config file
   - Format each entry as section.key=value
   - Sort alphabetically by section and key

### Error Handling

- Missing config file error: When the configuration file is missing
- Invalid section: Error message listing valid sections

## Examples

### Example 1: Setting User Identity

```bash
# Set user name
python -m codetrail config set user.name "John Doe"
# Expected output: None (success)

# Set email
python -m codetrail config set user.email "john@example.com"
# Expected output: None (success)
```

### Example 2: Reading Configuration

```bash
# Read user name
python -m codetrail config get user.name
# Expected output: John Doe

# List all settings
python -m codetrail config list
# Expected output:
# user.name=John Doe
# user.email=john@example.com
# core.ignorecase=false
```

## Alternatives Considered

### JSON Format

- Description: Store config in JSON format
- Pros:
  - Native parsing in Python
  - Type safety
- Cons:
  - Less human-readable
  - More complex for manual editing
- Why rejected: INI format is more user-friendly and traditional in VCS

## Migration Plan

N/A - Initial implementation

## Success Criteria

### Functional Requirements

- Successfully store and retrieve configuration values
- Maintain file format integrity
- Handle all basic operations (get, set, list, unset)
- Preserve file comments and formatting
- Validate input values

### Non-Functional Requirements

- Operations complete in under 50ms
- Clear error messages
- Human-readable file format
- Backward compatible with future enhancements

## Future Considerations

1. Global configuration support
2. Configuration value type validation
3. Multi-value support
4. Configuration includes
5. Environment variable overrides

## Questions and Open Issues

N/A

## References

1. [Git Config Documentation](https://git-scm.com/docs/git-config)
2. [INI File Format](https://en.wikipedia.org/wiki/INI_file)
