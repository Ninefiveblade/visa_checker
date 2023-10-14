import colorlog

formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red",
    },
)

logger = colorlog.getLogger(__name__)

logger.setLevel(colorlog.INFO)
console_handler = colorlog.StreamHandler()
console_handler.setLevel(colorlog.DEBUG)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
