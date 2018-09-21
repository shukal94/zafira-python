import enum


class TestStatus(enum.Enum):
    UNKNOWN = 'UNKNOWN',
    IN_PROGRESS = 'IN_PROGRESS',
    PASSED = 'PASSED',
    FAILED = 'FAILED',
    SKIPPED = 'SKIPPED',
    ABORTED = 'ABORTED'

