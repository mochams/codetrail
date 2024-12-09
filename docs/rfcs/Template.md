# RFC Template

````markdown
# RFC-XXX: Title of RFC

## Metadata

- **Author(s):** [Your name]
- **Status:** [Draft | In Review | Accepted | Implemented | Rejected]
- **Created:** [YYYY-MM-DD]
- **Last Updated:** [YYYY-MM-DD]
- **Related Issues:** [Links to related GitHub issues]

## Summary

[A brief (2-3 sentences) explanation of what this RFC proposes. This should be
clear enough that someone familiar with the project can understand the core idea
without reading further.]

## Background and Motivation

[Explain the context and why this change is important. What problem does it solve?
Why is now the right time to solve it?]

## Terminology

[Define any technical terms or acronyms that might be unfamiliar to readers.]

## Objectives

[List the specific goals this proposal aims to achieve. These should be measurable
and concrete.]

- Objective 1
- Objective 2
- ...

## Non-Objectives

[Explicitly list what this proposal is NOT trying to solve to prevent scope creep
and clarify boundaries.]

- Non-objective 1
- Non-objective 2
- ...

## Proposal

[Detailed description of the proposed changes. This is the meat of the RFC.]

### Command Interface

[If applicable, describe the command-line interface and arguments.]

```bash
command [arguments] <options>
```

### Design

[Technical details about how this will work.]

### Data Structures

[If applicable, describe any new data structures or modifications to existing ones.]

### Algorithm

[If applicable, describe the algorithm or process in detail.]

### Error Handling

[How will errors be handled and reported?]

## Examples

[Provide concrete examples of how this feature will be used.]

### Example 1: [Basic Usage]

```bash
# Example command
# Expected output
```

### Example 2: [Advanced Usage]

```bash
# Example command
# Expected output
```

## Alternatives Considered

[What other approaches were considered? Why were they rejected?]

### Alternative 1

- Description
- Pros
- Cons
- Why rejected

## Migration Plan

[If applicable, how will existing users/data be migrated to the new system?]

## Success Criteria

[How will we know this change is successful?]

### Functional Requirements

[What must the implementation do?]

### Non-Functional Requirements

[Performance, security, usability requirements]

## Future Considerations

[What future extensions or changes might be needed?]

## Questions and Open Issues

[List any unresolved questions or issues that need discussion.]

## References

[Links to relevant documentation, similar implementations, or background material.]
````

## Each section serves a specific purpose:

1. **Metadata**: Tracks the RFC's lifecycle and ownership
2. **Summary**: Provides quick understanding for readers
3. **Background**: Establishes context and justification
4. **Terminology**: Ensures clear communication
5. **Objectives/Non-Objectives**: Sets clear scope boundaries
6. **Proposal**: Contains the main technical content
7. **Examples**: Shows practical usage
8. **Alternatives**: Demonstrates thorough analysis
9. **Success Criteria**: Defines completion metrics
10. **Future Considerations**: Anticipates future needs
11. **Questions**: Acknowledges uncertainties
12. **References**: Provides additional context
