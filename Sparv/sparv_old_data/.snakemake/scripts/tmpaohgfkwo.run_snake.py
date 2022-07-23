
######## snakemake preamble start (automatically inserted, do not edit) ########
import sys; sys.path.extend(['/home/sebson/.local/lib/python3.7/site-packages', '/home/sebson/.local/lib/python3.7/site-packages/sparv/core']); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05X\x10\x00\x00\x00source/text2.txtq\x06a}q\x07(X\x06\x00\x00\x00_namesq\x08}q\tX\x12\x00\x00\x00_allowed_overridesq\n]q\x0b(X\x05\x00\x00\x00indexq\x0cX\x04\x00\x00\x00sortq\reh\x0ccfunctools\npartial\nq\x0ecbuiltins\ngetattr\nq\x0fcsnakemake.io\nNamedlist\nq\x10X\x0f\x00\x00\x00_used_attributeq\x11\x86q\x12Rq\x13\x85q\x14Rq\x15(h\x13)}q\x16X\x05\x00\x00\x00_nameq\x17h\x0csNtq\x18bh\rh\x0eh\x13\x85q\x19Rq\x1a(h\x13)}q\x1bh\x17h\rsNtq\x1cbubX\x06\x00\x00\x00outputq\x1dcsnakemake.io\nOutputFiles\nq\x1e)\x81q\x1f(X\x19\x00\x00\x00sparv-workdir/text2/@textq X\x1e\x00\x00\x00sparv-workdir/text2/text/@spanq!e}q"(h\x08}q#h\n]q$(h\x0ch\reh\x0ch\x0eh\x13\x85q%Rq&(h\x13)}q\'h\x17h\x0csNtq(bh\rh\x0eh\x13\x85q)Rq*(h\x13)}q+h\x17h\rsNtq,bubX\x06\x00\x00\x00paramsq-csnakemake.io\nParams\nq.)\x81q/(X\x0b\x00\x00\x00text_importq0X\x05\x00\x00\x00parseq1}q2(X\n\x00\x00\x00source_dirq3csparv.util.classes\nSource\nq4)\x81q5}q6h3X\x06\x00\x00\x00sourceq7sbX\x06\x00\x00\x00prefixq8X\x00\x00\x00\x00q9X\x08\x00\x00\x00encodingq:X\x05\x00\x00\x00UTF-8q;X\x12\x00\x00\x00keep_control_charsq<\x89X\t\x00\x00\x00normalizeq=X\x03\x00\x00\x00NFCq>X\x03\x00\x00\x00docq?csparv.util.classes\nDocument\nq@X\x05\x00\x00\x00text2qA\x85qB\x81qCuNX\x05\x00\x00\x00text2qD\x89N\x89e}qE(h\x08}qF(X\x0b\x00\x00\x00module_nameqGK\x00N\x86qHX\x06\x00\x00\x00f_nameqIK\x01N\x86qJX\n\x00\x00\x00parametersqKK\x02N\x86qLX\x0b\x00\x00\x00export_dirsqMK\x03N\x86qNh?K\x04N\x86qOX\r\x00\x00\x00use_preloaderqPK\x05N\x86qQX\x06\x00\x00\x00socketqRK\x06N\x86qSX\x0f\x00\x00\x00force_preloaderqTK\x07N\x86qUuh\n]qV(h\x0ch\reh\x0ch\x0eh\x13\x85qWRqX(h\x13)}qYh\x17h\x0csNtqZbh\rh\x0eh\x13\x85q[Rq\\(h\x13)}q]h\x17h\rsNtq^bhGh0hIh1hKh2hMNh?hDhP\x89hRNhT\x89ubX\t\x00\x00\x00wildcardsq_csnakemake.io\nWildcards\nq`)\x81qahDa}qb(h\x08}qcX\x03\x00\x00\x00docqdK\x00N\x86qesh\n]qf(h\x0ch\reh\x0ch\x0eh\x13\x85qgRqh(h\x13)}qih\x17h\x0csNtqjbh\rh\x0eh\x13\x85qkRql(h\x13)}qmh\x17h\rsNtqnbh?hDubX\x07\x00\x00\x00threadsqoK\x01X\t\x00\x00\x00resourcesqpcsnakemake.io\nResources\nqq)\x81qr(K\x01K\x01e}qs(h\x08}qt(X\x06\x00\x00\x00_coresquK\x00N\x86qvX\x06\x00\x00\x00_nodesqwK\x01N\x86qxuh\n]qy(h\x0ch\reh\x0ch\x0eh\x13\x85qzRq{(h\x13)}q|h\x17h\x0csNtq}bh\rh\x0eh\x13\x85q~Rq\x7f(h\x13)}q\x80h\x17h\rsNtq\x81bhuK\x01hwK\x01ubX\x03\x00\x00\x00logq\x82csnakemake.io\nLog\nq\x83)\x81q\x84}q\x85(h\x08}q\x86h\n]q\x87(h\x0ch\reh\x0ch\x0eh\x13\x85q\x88Rq\x89(h\x13)}q\x8ah\x17h\x0csNtq\x8bbh\rh\x0eh\x13\x85q\x8cRq\x8d(h\x13)}q\x8eh\x17h\rsNtq\x8fbubX\x06\x00\x00\x00configq\x90}q\x91(X\x0c\x00\x00\x00run_by_sparvq\x92\x88X\x05\x00\x00\x00debugq\x93\x89h?]q\x94X\t\x00\x00\x00log_levelq\x95X\x07\x00\x00\x00warningq\x96X\x0e\x00\x00\x00log_file_levelq\x97h\x96hRNhT\x89X\x07\x00\x00\x00targetsq\x98]q\x99X\r\x00\x00\x00export_corpusq\x9aahoK\x01X\n\x00\x00\x00log_serverq\x9bX\t\x00\x00\x00127.0.0.1q\x9cM\xc5\x94\x86q\x9duX\x04\x00\x00\x00ruleq\x9eX\x12\x00\x00\x00text_import::parseq\x9fX\x0f\x00\x00\x00bench_iterationq\xa0NX\t\x00\x00\x00scriptdirq\xa1X:\x00\x00\x00/home/sebson/.local/lib/python3.7/site-packages/sparv/coreq\xa2ub.'); from snakemake.logging import logger; logger.printshellcmds = False; __real_file__ = __file__; __file__ = '/home/sebson/.local/lib/python3.7/site-packages/sparv/core/run_snake.py';
######## snakemake preamble end #########
"""Script used by Snakemake to run Sparv modules."""

import importlib.util
import logging
import sys

from pkg_resources import iter_entry_points

from sparv.core import log_handler, paths
from sparv.core import registry
from sparv.util import SparvErrorMessage

custom_name = "custom"
plugin_name = "plugin"

# The snakemake variable is provided automatically by Snakemake; the below is just to please the IDE
try:
    snakemake
except NameError:
    from snakemake.script import Snakemake
    snakemake: Snakemake


def exit_with_error_message(message, logger_name):
    """Log error message and exit with non-zero status."""
    error_logger = logging.getLogger(logger_name)
    if snakemake.params.doc:
        message += f"\n\n(document: {snakemake.params.doc})"
    error_logger.error(message)
    sys.exit(123)


class StreamToLogger:
    """File-like stream object that redirects writes to a logger instance."""

    def __init__(self, logger, log_level=logging.INFO):
        self.logger = logger
        self.log_level = log_level

    def write(self, buf):
        self.logger.log(self.log_level, buf.rstrip())


# Import module
modules_path = ".".join(("sparv", paths.modules_dir))
module_name = snakemake.params.module_name

use_preloader = snakemake.params.use_preloader
preloader_busy = False

if use_preloader:
    from sparv.core import preload
    import socket
    sock = None
    try:
        if snakemake.params.force_preloader:
            sock = preload.connect_to_socket(snakemake.params.socket)
        else:
            # Try to connect to the preloader and fall back to running without it if it's unavailable
            sock = preload.connect_to_socket(snakemake.params.socket, timeout=True)
            sock.settimeout(0.5)
            # Ping preloader to verify that it's free
            preload.send_data(sock, preload.PING)
            response = preload.receive_data(sock)  # Timeouts if busy
            sock.settimeout(None)
    except (BlockingIOError, socket.timeout) as e:
        use_preloader = False
        preloader_busy = True
        if sock is not None:
            sock.close()

if not use_preloader:
    # Import custom module
    if module_name.startswith(custom_name):
        name = module_name[len(custom_name) + 1:]
        module_path = paths.corpus_dir.resolve() / f"{name}.py"
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
    else:
        try:
            # Try to import standard Sparv module
            module = importlib.import_module(".".join((modules_path, module_name)))
        except ModuleNotFoundError:
            # Try to find plugin module
            entry_points = dict((e.name, e) for e in iter_entry_points(f"sparv.{plugin_name}"))
            entry_point = entry_points.get(module_name)
            if entry_point:
                entry_point.load()
            else:
                exit_with_error_message(
                    f"Couldn't load plugin '{module_name}'. Please make sure it was installed correctly.", "sparv")


# Get function name and parameters
f_name = snakemake.params.f_name
parameters = snakemake.params.parameters

log_handler.setup_logging(snakemake.config["log_server"],
                          log_level=snakemake.config["log_level"],
                          log_file_level=snakemake.config["log_file_level"])
logger = logging.getLogger("sparv")
logger.info("RUN: %s:%s(%s)", module_name, f_name, ", ".join("%s=%s" % (i[0], repr(i[1])) for i in
                                                             list(parameters.items())))

# Redirect any prints to logging module
old_stdout = sys.stdout
old_stderr = sys.stderr
module_logger = logging.getLogger("sparv.modules." + module_name)
sys.stdout = StreamToLogger(module_logger)
sys.stderr = StreamToLogger(module_logger, logging.WARNING)

if not use_preloader:
    if preloader_busy:
        logger.info("Preloader busy; executing without preloader")
    # Execute function
    try:
        registry.modules[module_name].functions[f_name]["function"](**parameters)
        if snakemake.params.export_dirs:
            logger.export_dirs(snakemake.params.export_dirs)
    except SparvErrorMessage as e:
        # Any exception raised here would be printed directly to the terminal, due to how Snakemake runs the script.
        # Instead we log the error message and exit with a non-zero status to signal to Snakemake that
        # something went wrong.
        exit_with_error_message(e.message, "sparv.modules." + module_name)
    except Exception as e:
        logger.exception("An error occurred while executing:")
        sys.exit(123)
    finally:
        # Restore printing to stdout and stderr
        sys.stdout = old_stdout
        sys.stderr = old_stderr
else:
    try:
        preload.send_data(sock, (f"{module_name}:{f_name}", parameters, snakemake.config))
        response = preload.receive_data(sock)
        if isinstance(response, SparvErrorMessage):
            exit_with_error_message(response.message, "sparv.modules." + module_name)
        elif isinstance(response, BaseException):
            exit_with_error_message(str(response), "sparv.modules." + module_name)
        elif response is not True:
            exit_with_error_message("An error occurred while using the Sparv preloader.",
                                    f"sparv.modules.{module_name}")
    finally:
        sock.close()
        sys.stdout = old_stdout
        sys.stderr = old_stderr
