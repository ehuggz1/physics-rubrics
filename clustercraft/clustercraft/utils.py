"""Utility functions for AG-Simplified"""
import os
import logging
import yaml
from datetime import datetime

def load_config(config_path: str = "config/settings.yaml") -> dict:
    """Load configuration from YAML file"""
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def setup_logging(config: dict):
    """Setup logging based on configuration"""
    log_level = getattr(logging, config['logging']['level'])
    log_file = config['logging']['file']
    
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger('clustercraft')

def ensure_dir(path: str):
    """Ensure directory exists"""
    os.makedirs(path, exist_ok=True)

def generate_output_filename(topic: str, output_dir: str) -> str:
    """Generate timestamped output filename"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_topic = topic.replace(" ", "_").lower()
    filename = f"cluster_{safe_topic}_{timestamp}.md"
    return os.path.join(output_dir, filename)
