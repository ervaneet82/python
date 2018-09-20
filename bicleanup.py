"""
Delete the dataset from hdfs and localfilesystem which have been processed.
"""

import subprocess
import os
import logging
import argparse
from datetime import datetime, timedelta

class BICleanup():
    """
      Define Class
    """

    def __init__(self, no_of_days=7):
    # Create the Logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.no_of_days = no_of_days

    # Create the Handler for logging data to a file
        logger_handler = logging.FileHandler('python_logging.log')
        logger_handler.setLevel(logging.DEBUG)

    # Create a Formatter for formatting the log messages
        logger_formatter = logging.Formatter(
            '%(name)s : %(levelname)s : %(pathname)s : %(asctime)s - %('
            'message)s')

    # Add the Formatter to the Handler
        logger_handler.setFormatter(logger_formatter)

    # Add the Handler to the Logger
        self.logger.addHandler(logger_handler)
        self.logger.info('Completed configuring logger()!')


    def calculate_date(self):
        """
        Calculate the date number of days ago.
        :param number: number of days
        :return:
        """
        days_ago = datetime.now() - timedelta(days=self.no_of_days)
        return days_ago.strftime("%Y%m%d")

    def delete_dataset(self, dataset):
        """
         It will delete the dataset from hdfs path and
         localfilesystem as well.
         :param dataset:
         :return:
        """
        rm_hdfs_archive_datasets = subprocess.Popen(
            [HDFS_BIN, 'dfs', '-rm', '-r', '-f', '-skipTrash', os.path.join(
                HDFS_ARCHIVE_PATH, self.calculate_date(), dataset)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        remove_hdfs_dir_output = rm_hdfs_archive_datasets.communicate()
        self.logger.info(remove_hdfs_dir_output)
        os.rmdir(os.path.join(LOCAL_DATASET_PATH, self.calculate_date(), dataset))

    def cleanup(self):
        """
        Checks whether the dataset is present in path/<date>/dataset
        like voice, sms, etc. Call the delete_dataset function
        :return:
         """
        for dataset in DATASETS:
            list_hdfs_archive_dir = subprocess.Popen([HDFS_BIN, 'dfs', '-ls',
                                                      os.path.join(
                                                          HDFS_ARCHIVE_PATH,
                                                          self.calculate_date(), dataset)],
                                                     stdout=subprocess.PIPE,
                                                     stderr=subprocess.PIPE)
            hdfs_list_output = list_hdfs_archive_dir.communicate()
            self.logger.info(hdfs_list_output)
            if list_hdfs_archive_dir.returncode == 0 and \
              os.path.join(LOCAL_DATASET_PATH, self.calculate_date(), dataset):
                self.delete_dataset(dataset)
            else:
                self.logger.error("{} doesn't exist on HDFS".format(dataset))


if __name__ == "__main__":
    parser = argparse.ArgumentParser("The files from hdfs and localfilesystem in "
                                     "ANZ cluster")
    parser.add_argument("--days", help="Number of days ago to delete the "
                                       "datasets", type=int)
    args = parser.parse_args()

    DATASETS = ['cell_info', 'invoice', 'recharge', 'subs_info_post', 'tac',
                'data_post', 'dbal', 'payment', 'subs_info_pre', 'vas', 'sms',
                'data_pre', 'voice']

    HDFS_BIN = "/usr/bin/hdfs"
    HDFS_ARCHIVE_PATH = "<>"
    LOCAL_DATASET_PATH = "<>"
    LOG_FILENAME = "bi_deletion_status.log"


    BI = BICleanup(no_of_days=args.days)
    BI.cleanup()
