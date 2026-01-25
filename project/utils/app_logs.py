"""
Sistema de logging simples e eficaz para SmartTools.
"""

import logging
from pathlib import Path
from datetime import datetime


def setup_logger(
    name: str = "smarttools",
    level: int = logging.INFO,
    log_dir: str = "logs"
) -> logging.Logger:
    """
    Configura logger com arquivo rotativo por data.
    
    Args:
        name: Nome do logger
        level: Nível de log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_dir: Diretório para salvar logs
        
    Returns:
        Logger configurado
    """
    logger = logging.getLogger(name)
    
    # Evitar duplicação de handlers
    if logger.handlers:
        return logger
    
    logger.setLevel(level)
    
    # Formato: Data/Hora - Nível - [Arquivo:Linha] - Mensagem
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Handler para console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # Handler para arquivo
    try:
        # Criar diretório de logs
        log_path = Path(log_dir)
        log_path.mkdir(exist_ok=True)
        
        # Nome do arquivo: smarttools_YYYYMMDD.log
        log_filename = f"smarttools_{datetime.now().strftime('%Y%m%d')}.log"
        file_path = log_path / log_filename
        
        file_handler = logging.FileHandler(file_path, encoding='utf-8')
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
    except Exception as e:
        logger.warning(f"Não foi possível criar arquivo de log: {e}")
    
    return logger


# Logger global da aplicação
app_logger = setup_logger()


# Funções de conveniência
def info(msg: str):
    """Log informativo."""
    app_logger.info(msg)


def warning(msg: str):
    """Log de aviso."""
    app_logger.warning(msg)


def error(msg: str):
    """Log de erro."""
    app_logger.error(msg)


def exception(msg: str):
    """Log de exceção com stack trace."""
    app_logger.exception(msg)