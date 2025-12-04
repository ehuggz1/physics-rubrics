# Customizing Prompts with Jinja2 Templates

AG-Simplified uses [Jinja2](https://jinja.palletsprojects.com/) templates for easy prompt customization without modifying code.

## Template Files

### 1. System Instruction ([system_instruction.md](file:///e:/EVHGH/physics-rubrics/ag-simplified/templates/system_instruction.md))
Contains the core instructions for the LLM, including:
- Role definition (Physics Teacher and Exam Creator)
- Cluster structure requirements
- Three-dimensional framework details

**When to edit**: Modify this to change the overall behavior or add new requirements.

### 2. Cluster Prompt ([cluster_prompt.j2](file:///e:/EVHGH/physics-rubrics/ag-simplified/templates/cluster_prompt.j2))
The main prompt template that combines:
- System instruction
- Context (loaded Standards/PLDs)
- Stimulus (user input)

**When to edit**: Modify this to change how context and stimulus are presented to the LLM.

## Available Variables

Templates have access to the following variables:

| Variable | Type | Description |
|----------|------|-------------|
| `system_instruction` | string | Content from `system_instruction.md` |
| `context` | string | Loaded Standards and PLDs |
| `stimulus` | string | User-provided scenario |

## Example Customizations

### Adding a Specific Output Format
Edit `cluster_prompt.j2`:
```jinja2
Please generate a Physics Cluster in the following JSON format:
{
  "stimulus": "{{ stimulus }}",
  "questions": [...]
}
```

### Changing the Tone
Edit `system_instruction.md`:
```markdown
You are a friendly and encouraging Physics Teacher...
```

### Adding Constraints
Edit `cluster_prompt.j2`:
```jinja2
IMPORTANT: Generate exactly 2 questions, no more, no less.
```

## Testing Changes

After editing templates, test with a dry run:
```bash
python main.py --topic "Forces" --stimulus "Your test scenario" --dry-run
```

This will show the generated prompt without calling the LLM.
