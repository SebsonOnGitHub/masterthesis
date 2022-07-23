
######## snakemake preamble start (automatically inserted, do not edit) ########
import sys; sys.path.extend(['/home/sebson/.local/lib/python3.7/site-packages', '/home/sebson/.local/lib/python3.7/site-packages/sparv/core']); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05(X+\x00\x00\x00sparv-workdir/text3/segment.token/misc.wordq\x06X\'\x00\x00\x00sparv-workdir/text3/segment.token/@spanq\x07X*\x00\x00\x00sparv-workdir/text3/segment.sentence/@spanq\x08XH\x00\x00\x00/home/sebson/.local/share/sparv/models/stanza/pos/sv_talbanken_tagger.ptq\tXF\x00\x00\x00/home/sebson/.local/share/sparv/models/stanza/sv_talbanken.pretrain.ptq\nXF\x00\x00\x00/home/sebson/.local/share/sparv/models/stanza/lem/sv_suc_lemmatizer.ptq\x0bXH\x00\x00\x00/home/sebson/.local/share/sparv/models/stanza/dep/sv_talbanken_parser.ptq\x0cXF\x00\x00\x00/home/sebson/.local/share/sparv/models/stanza/sv_talbanken.pretrain.ptq\rX<\x00\x00\x00/home/sebson/.local/share/sparv/models/stanza/resources.jsonq\x0ee}q\x0f(X\x06\x00\x00\x00_namesq\x10}q\x11X\x12\x00\x00\x00_allowed_overridesq\x12]q\x13(X\x05\x00\x00\x00indexq\x14X\x04\x00\x00\x00sortq\x15eh\x14cfunctools\npartial\nq\x16cbuiltins\ngetattr\nq\x17csnakemake.io\nNamedlist\nq\x18X\x0f\x00\x00\x00_used_attributeq\x19\x86q\x1aRq\x1b\x85q\x1cRq\x1d(h\x1b)}q\x1eX\x05\x00\x00\x00_nameq\x1fh\x14sNtq bh\x15h\x16h\x1b\x85q!Rq"(h\x1b)}q#h\x1fh\x15sNtq$bubX\x06\x00\x00\x00outputq%csnakemake.io\nOutputFiles\nq&)\x81q\'(X,\x00\x00\x00sparv-workdir/text3/segment.token/stanza.msdq(X,\x00\x00\x00sparv-workdir/text3/segment.token/stanza.posq)X/\x00\x00\x00sparv-workdir/text3/segment.token/stanza.ufeatsq*X1\x00\x00\x00sparv-workdir/text3/segment.token/stanza.baseformq+X0\x00\x00\x00sparv-workdir/text3/segment.token/stanza.depheadq,X4\x00\x00\x00sparv-workdir/text3/segment.token/stanza.dephead_refq-X/\x00\x00\x00sparv-workdir/text3/segment.token/stanza.deprelq.e}q/(h\x10}q0h\x12]q1(h\x14h\x15eh\x14h\x16h\x1b\x85q2Rq3(h\x1b)}q4h\x1fh\x14sNtq5bh\x15h\x16h\x1b\x85q6Rq7(h\x1b)}q8h\x1fh\x15sNtq9bubX\x06\x00\x00\x00paramsq:csnakemake.io\nParams\nq;)\x81q<(X\x06\x00\x00\x00stanzaq=X\x08\x00\x00\x00annotateq>}q?(X\x07\x00\x00\x00out_msdq@csparv.util.classes\nOutput\nqA)\x81qB}qC(X\x04\x00\x00\x00nameqDX\x18\x00\x00\x00segment.token:stanza.msdqEX\r\x00\x00\x00original_nameqFX\x12\x00\x00\x00<token>:stanza.msdqGX\x04\x00\x00\x00rootqHcpathlib\nPosixPath\nqI(X\x01\x00\x00\x00/qJX\x04\x00\x00\x00homeqKX\x06\x00\x00\x00sebsonqLX\t\x00\x00\x00DocumentsqMX\x06\x00\x00\x00ExjobbqNX\x05\x00\x00\x00SparvqOtqPRqQX\x03\x00\x00\x00docqRX\x05\x00\x00\x00text3qSX\x03\x00\x00\x00clsqTX\t\x00\x00\x00token:msdqUX\x0b\x00\x00\x00descriptionqVX0\x00\x00\x00Part-of-speeches with morphological descriptionsqWubX\x07\x00\x00\x00out_posqXhA)\x81qY}qZ(hDX\x18\x00\x00\x00segment.token:stanza.posq[hFX\x12\x00\x00\x00<token>:stanza.posq\\hHhI(hJhKhLhMhNhOtq]Rq^hRhShTX\t\x00\x00\x00token:posq_hVX\x13\x00\x00\x00Part-of-speech tagsq`ubX\t\x00\x00\x00out_featsqahA)\x81qb}qc(hDX\x1b\x00\x00\x00segment.token:stanza.ufeatsqdhFX\x15\x00\x00\x00<token>:stanza.ufeatsqehHhI(hJhKhLhMhNhOtqfRqghRhShTX\x0c\x00\x00\x00token:ufeatsqhhVX \x00\x00\x00Universal morphological featuresqiubX\x0c\x00\x00\x00out_baseformqjhA)\x81qk}ql(hDX\x1d\x00\x00\x00segment.token:stanza.baseformqmhFX\x17\x00\x00\x00<token>:stanza.baseformqnhHhI(hJhKhLhMhNhOtqoRqphRhShTX\x0e\x00\x00\x00token:baseformqqhVX\x14\x00\x00\x00Baseform from StanzaqrubX\x0b\x00\x00\x00out_depheadqshA)\x81qt}qu(hDX\x1c\x00\x00\x00segment.token:stanza.depheadqvhFX\x16\x00\x00\x00<token>:stanza.depheadqwhHhI(hJhKhLhMhNhOtqxRqyhRhShTX\r\x00\x00\x00token:depheadqzhVX!\x00\x00\x00Positions of the dependency headsq{ubX\x0f\x00\x00\x00out_dephead_refq|hA)\x81q}}q~(hDX \x00\x00\x00segment.token:stanza.dephead_refq\x7fhFX\x1a\x00\x00\x00<token>:stanza.dephead_refq\x80hHhI(hJhKhLhMhNhOtq\x81Rq\x82hRhShTX\x11\x00\x00\x00token:dephead_refq\x83hVX3\x00\x00\x00Sentence-relative positions of the dependency headsq\x84ubX\n\x00\x00\x00out_deprelq\x85hA)\x81q\x86}q\x87(hDX\x1b\x00\x00\x00segment.token:stanza.deprelq\x88hFX\x15\x00\x00\x00<token>:stanza.deprelq\x89hHhI(hJhKhLhMhNhOtq\x8aRq\x8bhRhShTX\x0c\x00\x00\x00token:deprelq\x8chVX \x00\x00\x00Dependency relations to the headq\x8dubX\x04\x00\x00\x00wordq\x8ecsparv.util.classes\nAnnotation\nq\x8f)\x81q\x90}q\x91(hDX\x17\x00\x00\x00segment.token:misc.wordq\x92hFX\x0c\x00\x00\x00<token:word>q\x93hHhI(hJhKhLhMhNhOtq\x94Rq\x95hRhSX\x04\x00\x00\x00sizeq\x96NubX\x05\x00\x00\x00tokenq\x97h\x8f)\x81q\x98}q\x99(hDX\r\x00\x00\x00segment.tokenq\x9ahFX\x07\x00\x00\x00<token>q\x9bhHhI(hJhKhLhMhNhOtq\x9cRq\x9dhRhSh\x96NubX\x08\x00\x00\x00sentenceq\x9eh\x8f)\x81q\x9f}q\xa0(hDX\x10\x00\x00\x00segment.sentenceq\xa1hFX\n\x00\x00\x00<sentence>q\xa2hHhI(hJhKhLhMhNhOtq\xa3Rq\xa4hRhSh\x96NubX\t\x00\x00\x00pos_modelq\xa5csparv.util.classes\nModel\nq\xa6)\x81q\xa7}q\xa8(hDXH\x00\x00\x00/home/sebson/.local/share/sparv/models/stanza/pos/sv_talbanken_tagger.ptq\xa9hFh\xa9hHhI(hJhKhLhMhNhOtq\xaaRq\xabubX\x12\x00\x00\x00pos_pretrain_modelq\xach\xa6)\x81q\xad}q\xae(hDXF\x00\x00\x00/home/sebson/.local/share/sparv/models/stanza/sv_talbanken.pretrain.ptq\xafhFh\xafhHhI(hJhKhLhMhNhOtq\xb0Rq\xb1ubX\t\x00\x00\x00lem_modelq\xb2h\xa6)\x81q\xb3}q\xb4(hDXF\x00\x00\x00/home/sebson/.local/share/sparv/models/stanza/lem/sv_suc_lemmatizer.ptq\xb5hFh\xb5hHhI(hJhKhLhMhNhOtq\xb6Rq\xb7ubX\t\x00\x00\x00dep_modelq\xb8h\xa6)\x81q\xb9}q\xba(hDXH\x00\x00\x00/home/sebson/.local/share/sparv/models/stanza/dep/sv_talbanken_parser.ptq\xbbhFh\xbbhHhI(hJhKhLhMhNhOtq\xbcRq\xbdubX\x12\x00\x00\x00dep_pretrain_modelq\xbeh\xa6)\x81q\xbf}q\xc0(hDXF\x00\x00\x00/home/sebson/.local/share/sparv/models/stanza/sv_talbanken.pretrain.ptq\xc1hFh\xc1hHhI(hJhKhLhMhNhOtq\xc2Rq\xc3ubX\x0e\x00\x00\x00resources_fileq\xc4h\xa6)\x81q\xc5}q\xc6(hDX<\x00\x00\x00/home/sebson/.local/share/sparv/models/stanza/resources.jsonq\xc7hFh\xc7hHhI(hJhKhLhMhNhOtq\xc8Rq\xc9ubX\x07\x00\x00\x00use_gpuq\xca\x88X\n\x00\x00\x00batch_sizeq\xcbM\x88\x13X\x13\x00\x00\x00max_sentence_lengthq\xccK\xfaX\x0c\x00\x00\x00cpu_fallbackq\xcd\x89uNX\x05\x00\x00\x00text3q\xce\x89N\x89e}q\xcf(h\x10}q\xd0(X\x0b\x00\x00\x00module_nameq\xd1K\x00N\x86q\xd2X\x06\x00\x00\x00f_nameq\xd3K\x01N\x86q\xd4X\n\x00\x00\x00parametersq\xd5K\x02N\x86q\xd6X\x0b\x00\x00\x00export_dirsq\xd7K\x03N\x86q\xd8hRK\x04N\x86q\xd9X\r\x00\x00\x00use_preloaderq\xdaK\x05N\x86q\xdbX\x06\x00\x00\x00socketq\xdcK\x06N\x86q\xddX\x0f\x00\x00\x00force_preloaderq\xdeK\x07N\x86q\xdfuh\x12]q\xe0(h\x14h\x15eh\x14h\x16h\x1b\x85q\xe1Rq\xe2(h\x1b)}q\xe3h\x1fh\x14sNtq\xe4bh\x15h\x16h\x1b\x85q\xe5Rq\xe6(h\x1b)}q\xe7h\x1fh\x15sNtq\xe8bh\xd1h=h\xd3h>h\xd5h?h\xd7NhRh\xceh\xda\x89h\xdcNh\xde\x89ubX\t\x00\x00\x00wildcardsq\xe9csnakemake.io\nWildcards\nq\xea)\x81q\xebX\x13\x00\x00\x00sparv-workdir/text3q\xeca}q\xed(h\x10}q\xeeX\x03\x00\x00\x00docq\xefK\x00N\x86q\xf0sh\x12]q\xf1(h\x14h\x15eh\x14h\x16h\x1b\x85q\xf2Rq\xf3(h\x1b)}q\xf4h\x1fh\x14sNtq\xf5bh\x15h\x16h\x1b\x85q\xf6Rq\xf7(h\x1b)}q\xf8h\x1fh\x15sNtq\xf9bhRh\xecubX\x07\x00\x00\x00threadsq\xfaK\x01X\t\x00\x00\x00resourcesq\xfbcsnakemake.io\nResources\nq\xfc)\x81q\xfd(K\x01K\x01e}q\xfe(h\x10}q\xff(X\x06\x00\x00\x00_coresr\x00\x01\x00\x00K\x00N\x86r\x01\x01\x00\x00X\x06\x00\x00\x00_nodesr\x02\x01\x00\x00K\x01N\x86r\x03\x01\x00\x00uh\x12]r\x04\x01\x00\x00(h\x14h\x15eh\x14h\x16h\x1b\x85r\x05\x01\x00\x00Rr\x06\x01\x00\x00(h\x1b)}r\x07\x01\x00\x00h\x1fh\x14sNtr\x08\x01\x00\x00bh\x15h\x16h\x1b\x85r\t\x01\x00\x00Rr\n\x01\x00\x00(h\x1b)}r\x0b\x01\x00\x00h\x1fh\x15sNtr\x0c\x01\x00\x00bj\x00\x01\x00\x00K\x01j\x02\x01\x00\x00K\x01ubX\x03\x00\x00\x00logr\r\x01\x00\x00csnakemake.io\nLog\nr\x0e\x01\x00\x00)\x81r\x0f\x01\x00\x00}r\x10\x01\x00\x00(h\x10}r\x11\x01\x00\x00h\x12]r\x12\x01\x00\x00(h\x14h\x15eh\x14h\x16h\x1b\x85r\x13\x01\x00\x00Rr\x14\x01\x00\x00(h\x1b)}r\x15\x01\x00\x00h\x1fh\x14sNtr\x16\x01\x00\x00bh\x15h\x16h\x1b\x85r\x17\x01\x00\x00Rr\x18\x01\x00\x00(h\x1b)}r\x19\x01\x00\x00h\x1fh\x15sNtr\x1a\x01\x00\x00bubX\x06\x00\x00\x00configr\x1b\x01\x00\x00}r\x1c\x01\x00\x00(X\x0c\x00\x00\x00run_by_sparvr\x1d\x01\x00\x00\x88X\x05\x00\x00\x00debugr\x1e\x01\x00\x00\x89hR]r\x1f\x01\x00\x00X\t\x00\x00\x00log_levelr \x01\x00\x00X\x07\x00\x00\x00warningr!\x01\x00\x00X\x0e\x00\x00\x00log_file_levelr"\x01\x00\x00j!\x01\x00\x00h\xdcNh\xde\x89X\x07\x00\x00\x00targetsr#\x01\x00\x00]r$\x01\x00\x00X\r\x00\x00\x00export_corpusr%\x01\x00\x00ah\xfaK\x01X\n\x00\x00\x00log_serverr&\x01\x00\x00X\t\x00\x00\x00127.0.0.1r\'\x01\x00\x00M5\x90\x86r(\x01\x00\x00uX\x04\x00\x00\x00ruler)\x01\x00\x00X\x10\x00\x00\x00stanza::annotater*\x01\x00\x00X\x0f\x00\x00\x00bench_iterationr+\x01\x00\x00NX\t\x00\x00\x00scriptdirr,\x01\x00\x00X:\x00\x00\x00/home/sebson/.local/lib/python3.7/site-packages/sparv/corer-\x01\x00\x00ub.'); from snakemake.logging import logger; logger.printshellcmds = False; __real_file__ = __file__; __file__ = '/home/sebson/.local/lib/python3.7/site-packages/sparv/core/run_snake.py';
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
