# Skill authoring best practices

Source: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices  
Retrieved: 2026-11-13

> Learn how to write effective Skills that Claude can discover and use successfully.  
> For conceptual background on how Skills work, see [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).

## Core principles

### Concise is key

The [context window](https://platform.claude.com/docs/en/build-with-claude/context-windows) is a public good. Your Skill shares the context window with everything else Claude needs, including:

* The system prompt
* Conversation history
* Other Skills’ metadata
* Your actual request

Not every token in your Skill has an immediate cost. At startup, only the metadata (name and description) from all Skills is pre-loaded. Claude reads `SKILL.md` only when the Skill becomes relevant, and reads additional files only as needed. However, being concise in `SKILL.md` still matters: once Claude loads it, every token competes with conversation history and other context.

**Default assumption:** Claude is already very smart

Only add context Claude doesn’t already have. Challenge each piece of information:

* “Does Claude really need this explanation?”
* “Can I assume Claude has this information?”
* “Does this paragraph justify its token cost?”

**Good example: Concise** (approximately 50 tokens):

```markdown
## Extract PDF text

Use pdfplumber for text extraction:

```python
import pdfplumber

with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```
```

**Bad example: Too verbose** (approximately 150 tokens):

```markdown
## Extract PDF text

PDF (Portable Document Format) files are a common file format that contains
text, images, and other content. To extract text from a PDF, you'll need to
use a library. There are many libraries available for PDF processing, but
pdfplumber is recommended because it's easy to use and handles most cases well.
First, you'll need to install it using pip. Then you can use the code below...
```

The concise version assumes Claude already has information about PDFs and how libraries work.

### Set appropriate degrees of freedom

Match the level of specificity to the task’s fragility and variability.

**High freedom** (text-based instructions): Use when multiple approaches are valid, decisions depend on context, and heuristics guide the approach.

**Medium freedom** (pseudocode or scripts with parameters): Use when a preferred pattern exists, some variation is acceptable, and configuration affects behavior.

**Low freedom** (specific scripts, few or no parameters): Use when operations are fragile and error-prone, consistency is critical, or a specific sequence must be followed.

**Analogy:** Think of Claude as a robot exploring a path:

* **Narrow bridge with cliffs on both sides:** there’s only one safe way forward. Provide specific guardrails and exact instructions (low freedom).
* **Open field with no hazards:** many paths lead to success. Give general direction and trust Claude to find the best route (high freedom).

### Test with all models you plan to use

Skills act as additions to models, so effectiveness depends on the underlying model. Test your Skill with all the models you plan to use it with.

**Testing considerations by model:**

* **Claude Haiku** (fast, economical): Does the Skill provide enough guidance?
* **Claude Sonnet** (balanced): Is the Skill clear and efficient?
* **Claude Opus** (powerful reasoning): Does the Skill avoid over-explaining?

What works perfectly for Opus might need more detail for Haiku. If you plan to use your Skill across multiple models, aim for instructions that work well with all of them.

## Skill structure

The `SKILL.md` frontmatter requires two fields:

* `name`
  * Maximum 64 characters
  * Must contain only lowercase letters, numbers, and hyphens
  * Cannot contain XML tags
  * Cannot contain reserved words: `anthropic`, `claude`
* `description`
  * Must be non-empty
  * Maximum 1,024 characters
  * Cannot contain XML tags
  * Should describe what the Skill does and when to use it

### Naming conventions

Use consistent naming patterns. Consider **gerund form** (verb + -ing) for Skill names, because it clearly describes the activity or capability the Skill provides.

Remember that the `name` field must use lowercase letters, numbers, and hyphens only.

**Good naming examples (gerund form):**

* `processing-pdfs`
* `analyzing-spreadsheets`
* `managing-databases`
* `testing-code`
* `writing-documentation`

**Avoid:**

* Vague names: `helper`, `utils`, `tools`
* Overly generic: `documents`, `data`, `files`
* Reserved words: `anthropic-helper`, `claude-tools`
* Inconsistent patterns within your skill collection

### Writing effective descriptions

The `description` field makes Skill discovery possible and should include both what the Skill does and when to use it.

* **Always write in third person.** The description is injected into the system prompt, and inconsistent point-of-view can cause discovery problems.
* Be specific and include key terms: include both what the Skill does and specific triggers/contexts for when to use it.

**Good:** “Processes Excel files and generates reports”  
**Avoid:** “I can help you process Excel files”  
**Avoid:** “You can use this to process Excel files”

### Progressive disclosure patterns

* Keep the `SKILL.md` body under 500 lines for optimal performance.
* Split content into separate files when approaching this limit.
* Keep references one level deep from `SKILL.md`.
* For reference files longer than 100 lines, include a table of contents at the top.

### Avoid deeply nested references

Keep references one level deep from `SKILL.md`. All reference files should link directly from `SKILL.md` to ensure Claude reads complete files when needed.

### Structure longer reference files with a table of contents

For reference files longer than 100 lines, include a table of contents at the top so Claude can see the full scope of available information even when previewing with partial reads.

## Workflows and feedback loops

### Use workflows for complex tasks

Break complex operations into clear, sequential steps. For particularly complex workflows, provide a checklist that Claude can copy into its response and check off as it progresses.

### Implement feedback loops

**Common pattern:** Run validator → fix errors → repeat.

This pattern greatly improves output quality.

## Content guidelines

### Avoid time-sensitive information

Don’t include information that will become outdated; use an “old patterns” section for historical context instead.

### Use consistent terminology

Choose one term and use it throughout the Skill.

## Common patterns

### Template pattern

Provide templates for output format. Match the level of strictness to your needs: strict templates for API responses/data formats; flexible guidance when adaptation is useful.

### Examples pattern

For Skills where output quality depends on seeing examples, provide input/output pairs.

### Conditional workflow pattern

Guide Claude through decision points with clear creation vs. editing branches.

## Evaluation and iteration

### Build evaluations first

Create evaluations BEFORE writing extensive documentation. This ensures your Skill solves real problems rather than documenting imagined ones.

### Develop Skills iteratively with Claude

Work with one Claude instance to create a Skill and another (with the Skill loaded) to test it in real tasks. Iterate based on observed behavior rather than assumptions.

### Observe how Claude navigates Skills

Pay attention to unexpected exploration paths, missed connections, overreliance on certain sections, and ignored content. Iterate based on these observations.

## Anti-patterns to avoid

### Avoid Windows-style paths

Always use forward slashes in file paths, even on Windows.

### Avoid offering too many options

Don’t present multiple approaches unless necessary; provide a default with an escape hatch.

## Advanced: Skills with executable code

### Solve, don’t defer

Handle error conditions in scripts rather than deferring to Claude.

### Provide utility scripts

Pre-made scripts are more reliable, save tokens/time, and ensure consistency.

### Use visual analysis

When inputs can be rendered as images, have Claude analyze them.

### Create verifiable intermediate outputs

Use the “plan-validate-execute” pattern for complex, open-ended tasks.

### Package dependencies

List required packages in your `SKILL.md` and verify availability in the code execution environment.

### Runtime environment

Skills run in a code execution environment with filesystem access. Use forward slashes, descriptive file names, and progressive disclosure through on-demand file reads.

### MCP tool references

Use fully qualified tool names: `ServerName:tool_name`.

### Avoid assuming tools are installed

Explicitly install required packages before use.

## Technical notes

### YAML frontmatter requirements

The `SKILL.md` frontmatter requires `name` and `description` fields with specific validation rules:

* `name`: Maximum 64 characters, lowercase letters/numbers/hyphens only, no XML tags, no reserved words.
* `description`: Maximum 1,024 characters, non-empty, no XML tags.

### Token budgets

Keep the `SKILL.md` body under 500 lines for optimal performance. If content exceeds this, split it into separate files.

## Checklist for effective Skills

Before sharing a Skill, verify:

### Core quality

* [ ] Description is specific and includes key terms
* [ ] Description includes both what the Skill does and when to use it
* [ ] `SKILL.md` body is under 500 lines
* [ ] Additional details are in separate files (if needed)
* [ ] No time-sensitive information (or in “old patterns” section)
* [ ] Consistent terminology throughout
* [ ] Examples are concrete, not abstract
* [ ] File references are one level deep
* [ ] Progressive disclosure used appropriately
* [ ] Workflows have clear steps

### Code and scripts

* [ ] Scripts solve problems rather than defer to Claude
* [ ] Error handling is explicit and helpful
* [ ] No “voodoo constants” (all values justified)
* [ ] Required packages listed in instructions and verified as available
* [ ] Scripts have clear documentation
* [ ] No Windows-style paths (all forward slashes)
* [ ] Validation/verification steps for critical operations
* [ ] Feedback loops included for quality-critical tasks

### Testing

* [ ] At least three evaluations created
* [ ] Tested with Haiku, Sonnet, and Opus
* [ ] Tested with real usage scenarios
* [ ] Team feedback incorporated (if applicable)

## Next steps

* [Get started with Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart)
* [Use Skills in Claude Code](https://code.claude.com/docs/en/skills)
* [Use Skills with the API](https://platform.claude.com/docs/en/build-with-claude/skills-guide)
