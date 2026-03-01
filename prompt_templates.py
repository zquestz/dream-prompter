#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Prompt Template management for Dream Prompter plugin
Handles loading, saving, and managing prompt templates with prefix/main/suffix
"""

import json
import os
from typing import Dict, List, Optional
from settings import get_config_file

TEMPLATES_FILE_NAME = "dream-prompter-templates.json"


class PromptTemplate:
    """Represents a prompt template with prefix, main, and suffix sections"""
    
    def __init__(self, name: str, prefix: str = "", main: str = "", suffix: str = ""):
        self.name = name
        self.prefix = prefix
        self.main = main
        self.suffix = suffix
    
    def get_full_prompt(self) -> str:
        """Combine prefix, main, and suffix into a complete prompt"""
        parts = []
        if self.prefix.strip():
            parts.append(self.prefix.strip())
        if self.main.strip():
            parts.append(self.main.strip())
        if self.suffix.strip():
            parts.append(self.suffix.strip())
        return " ".join(parts)
    
    def to_dict(self) -> Dict[str, str]:
        """Convert template to dictionary for JSON serialization"""
        return {
            "name": self.name,
            "prefix": self.prefix,
            "main": self.main,
            "suffix": self.suffix,
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> "PromptTemplate":
        """Create template from dictionary"""
        return cls(
            name=data.get("name", ""),
            prefix=data.get("prefix", ""),
            main=data.get("main", ""),
            suffix=data.get("suffix", ""),
        )


def get_templates_file() -> str:
    """Get path to templates file (same directory as config file)"""
    config_file = get_config_file()
    config_dir = os.path.dirname(config_file)
    return os.path.join(config_dir, TEMPLATES_FILE_NAME)


def load_templates() -> Dict[str, PromptTemplate]:
    """Load all templates from file
    
    Returns:
        Dictionary mapping template names to PromptTemplate objects
    """
    templates = {}
    try:
        templates_file = get_templates_file()
        if os.path.exists(templates_file):
            with open(templates_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                for template_data in data.get("templates", []):
                    template = PromptTemplate.from_dict(template_data)
                    templates[template.name] = template
    except (OSError, PermissionError) as e:
        print(f"Failed to read templates file: {e}")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in templates file: {e}")
    except Exception as e:
        print(f"Unexpected error loading templates: {e}")
    
    return templates


def save_templates(templates: Dict[str, PromptTemplate]) -> None:
    """Save all templates to file
    
    Args:
        templates: Dictionary mapping template names to PromptTemplate objects
    """
    try:
        templates_file = get_templates_file()
        data = {
            "templates": [template.to_dict() for template in templates.values()]
        }
        
        with open(templates_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        
        # Set file permissions on Unix-like systems
        import platform
        if platform.system() != "Windows":
            os.chmod(templates_file, 0o600)
            
    except (OSError, PermissionError) as e:
        print(f"Failed to save templates: {e}")
    except Exception as e:
        print(f"Unexpected error saving templates: {e}")


def save_template(template: PromptTemplate) -> None:
    """Save or update a single template
    
    Args:
        template: PromptTemplate to save
    """
    templates = load_templates()
    templates[template.name] = template
    save_templates(templates)


def delete_template(template_name: str) -> None:
    """Delete a template by name
    
    Args:
        template_name: Name of template to delete
    """
    templates = load_templates()
    if template_name in templates:
        del templates[template_name]
        save_templates(templates)


def get_template_names() -> List[str]:
    """Get list of all template names
    
    Returns:
        Sorted list of template names
    """
    templates = load_templates()
    return sorted(templates.keys())


def get_template(template_name: str) -> Optional[PromptTemplate]:
    """Get a template by name
    
    Args:
        template_name: Name of template to retrieve
        
    Returns:
        PromptTemplate if found, None otherwise
    """
    templates = load_templates()
    return templates.get(template_name)
