import enum


class TestStatus(enum.Enum):
    UNKNOWN = 'UNKNOWN',
    IN_PROGRESS = 'IN_PROGRESS',
    PASSED = 'PASSED',
    FAILED = 'FAILED',
    SKIPPED = 'SKIPPED',
    ABORTED = 'ABORTED'


class Initiator(enum.Enum):
    SCHEDULER = 'SCHEDULER'
    UPSTREAM_JOB = 'UPSTREAM_JOB'
    HUMAN = 'HUMAN'

class DriverMode(enum.Enum):
    METHOD_MODE = "METHOD_MODE"
    CLASS_MODE = "CLASS_MODE"
    SUITE_MODE = "SUITE_MODE"