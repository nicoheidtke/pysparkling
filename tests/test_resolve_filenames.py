import os
from pysparkling.fileio import File
from nose.plugins.skip import SkipTest


def test_local_1():
    filenames = File.resolve_filenames(
        'tests/*'
    )
    assert 'tests/test_resolve_filenames.py' in filenames


def test_local_2():
    filenames = File.resolve_filenames(
        'tests/test_resolve_filenames.py'
    )
    assert (len(filenames) == 1 and
            'tests/test_resolve_filenames.py' == filenames[0])


def test_s3_1():
    if not os.getenv('AWS_ACCESS_KEY_ID'):
        raise SkipTest

    filenames = File.resolve_filenames(
        's3n://aws-publicdatasets/common-crawl/'
        'crawl-data/CC-MAIN-2015-11/warc.paths.*'
    )
    print(filenames)
    assert ('s3n://aws-publicdatasets/common-crawl/'
            'crawl-data/CC-MAIN-2015-11/warc.paths.gz' in filenames)


if __name__ == '__main__':
    test_local_1()
    test_local_2()
    test_s3_1()
