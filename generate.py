from jinja2 import Environment, select_autoescape, FileSystemLoader
from faker import Faker
from config import Config
from util.logger import logger
from util.engine import Engine
from util.helper.jinja_functions import datetimeformat
from util.helper.helper import mkdir


OUTPUT_DIR = "output"


if '__main__' == __name__:
    # force_download = len(sys.argv) > 1 and '-f' in sys.argv
    # dry = len(sys.argv) > 1 and ('-d' in sys.argv or '--dry-run' in sys.argv)
    # load_only = len(sys.argv) > 1 and ('-l' in sys.argv or '--load-only' in sys.argv)
    # force_cache = len(sys.argv) > 1 and ('-c' in sys.argv or '--cache-only' in sys.argv)
    #
    # logger.logger.info(f"%s => %s => %s => %s", force_download, dry, load_only, force_cache)

    mkdir(OUTPUT_DIR)

    _jinja = Environment(
        loader=FileSystemLoader("data/templates"), autoescape=select_autoescape()
    )
    _jinja.filters['datetimeformat'] = datetimeformat

    Engine(
        cfg=Config.load_settings("settings.yaml"),
        names=Config.load_names("data/names.json"),
        ages=Config.load_ages("data/population-pyramid.csv"),
        terminology=Config.load_terminology(terminology_dir="data/terminology", weights_dir="data/weights"),
        output_dir=OUTPUT_DIR,
        log=logger.logger,
        jinja=_jinja,
        faker=Faker(["ar_SA", "en_UK"]),
    ).run()


