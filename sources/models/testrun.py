from sources.models.enums import Initiator, DriverMode
from sources.dto import DTO


class TestRun:
    """
    Stores data about test run
    """
    def __init__(self, id, test_suite_id, job_id, build_number, driver_mode=DriverMode.METHOD_MODE.value,
                 started_by=Initiator.SCHEDULER.value):
        self.__id = id
        self.__test_suite_id = test_suite_id
        self.__job_id = job_id
        self.__build_number = build_number
        self.__started_by = started_by
        self.__driver_mode = driver_mode

        self.__dto = DTO(id=self.__id,
                         testSuiteId=self.__test_suite_id,
                         jobId=self.__job_id,
                         buildNumber=self.__build_number,
                         driverMode=self.__driver_mode,
                         startedBy=self.__started_by)

    @property
    def dto(self):
        return self.__dto

    @property
    def id(self):
        return self.__id

    @property
    def test_suite_id(self):
        return self.__test_suite_id

    @test_suite_id.setter
    def test_suite_id(self, test_suite_id):
        self.__test_suite_id = test_suite_id

    @property
    def job_id(self):
        return self.__job_id

    @job_id.setter
    def job_id(self, job_id):
        self.__job_id = job_id

    @property
    def build_number(self):
        return self.__build_number

    @build_number.setter
    def build_number(self, build_number):
        self.__build_number = build_number

    @property
    def started_by(self):
        return self.__started_by

    @started_by.setter
    def started_by(self, started_by):
        self.__started_by = started_by

    @property
    def driver_mode(self):
        return self.__driver_mode

    @driver_mode.setter
    def driver_mode(self, driver_mode):
        self.__driver_mode = driver_mode

