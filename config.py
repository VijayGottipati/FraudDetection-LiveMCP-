#!/usr/bin/env python3
"""
Configuration file for the financial data streaming application
"""

import os
from typing import Dict, Any, List

class Config:
    """Configuration class for the application"""
    
    # Lenses MCP Configuration
    LENSES_MCP_URL = os.getenv('LENSES_MCP_URL', 'ws://108.129.193.220:8080')
    LENSES_ENVIRONMENT = os.getenv('LENSES_ENVIRONMENT', 'financial-data')
    
    # Kafka Configuration
    KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092').split(',')
    KAFKA_GROUP_ID = os.getenv('KAFKA_GROUP_ID', 'financial-data-streamer')
    
    # Topics Configuration
    TOPICS = {
        'credit_card': 'credit-card-transactions',
        'paypal': 'paypal-transactions'
    }
    
    # Consumer Configuration
    CONSUMER_CONFIG = {
        'auto_offset_reset': 'latest',
        'enable_auto_commit': True,
        'consumer_timeout_ms': 1000,
        'max_poll_records': 100,
        'session_timeout_ms': 30000,
        'heartbeat_interval_ms': 10000
    }
    
    # Processing Configuration
    BATCH_SIZE = int(os.getenv('BATCH_SIZE', '100'))
    PROCESSING_DELAY = float(os.getenv('PROCESSING_DELAY', '0.1'))
    METRICS_INTERVAL = int(os.getenv('METRICS_INTERVAL', '60'))
    
    # Fraud Detection Configuration
    FRAUD_THRESHOLDS = {
        'high_amount_cc': 1000.0,
        'high_amount_pp': 2000.0,
        'frequent_transactions': 10,
        'account_age_threshold': 30
    }
    
    # Logging Configuration
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'kafka_stream.log')
    
    # External Systems Configuration
    WEBHOOK_URL = os.getenv('WEBHOOK_URL', '')
    DATABASE_URL = os.getenv('DATABASE_URL', '')
    
    @classmethod
    def get_kafka_config(cls) -> Dict[str, Any]:
        """Get Kafka configuration dictionary"""
        return {
            'bootstrap_servers': cls.KAFKA_BOOTSTRAP_SERVERS,
            'consumer_config': cls.CONSUMER_CONFIG
        }
    
    @classmethod
    def get_topics_list(cls) -> List[str]:
        """Get list of topics to consume"""
        return list(cls.TOPICS.values())
    
    @classmethod
    def validate_config(cls) -> bool:
        """Validate configuration"""
        required_vars = [
            'LENSES_MCP_URL',
            'LENSES_ENVIRONMENT',
            'KAFKA_BOOTSTRAP_SERVERS'
        ]
        
        for var in required_vars:
            if not getattr(cls, var):
                print(f"Error: {var} is not set")
                return False
        
        return True

# Environment-specific configurations
class DevelopmentConfig(Config):
    """Development configuration"""
    LOG_LEVEL = 'DEBUG'
    PROCESSING_DELAY = 0.05

class ProductionConfig(Config):
    """Production configuration"""
    LOG_LEVEL = 'INFO'
    PROCESSING_DELAY = 0.1
    BATCH_SIZE = 500

class TestConfig(Config):
    """Test configuration"""
    LOG_LEVEL = 'DEBUG'
    PROCESSING_DELAY = 0.01
    BATCH_SIZE = 10

# Configuration factory
def get_config(env: str = None) -> Config:
    """Get configuration based on environment"""
    if env is None:
        env = os.getenv('ENVIRONMENT', 'development')
    
    configs = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'test': TestConfig
    }
    
    return configs.get(env, DevelopmentConfig)()
