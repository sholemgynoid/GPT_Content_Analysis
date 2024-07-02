#!/usr/bin/python
# -*- coding: utf-8 -*-

from ffmpy import FFmpeg
import datetime
import subprocess


# def scalettarai_to_mp3(
#         filename: str,
#         link: str,
#         output_directory: str = '',
#         index: str = '',
#         start_time: str = '00:00:00.0',
#         end_time: str = '01:00:00.0',
#         extension: str = 'mp3'
# ):

def mov_to_flac(
        filename: str,
        input_directory: str = '',
        output_directory: str = '',
        index: str = '',
        start_time: str = '00:00:00.0',
        end_time: str = '01:00:00.0',
        extension: str = 'mov') -> str:
    """

    :type input_directory: object
    """
    if index == '':
        pass
    else:
        filename = filename_upgrade(filename, start_time, index)

    print('Calling ffmpeg procedure to convert {0} file to .flac'.format(filename))
    ff = FFmpeg(
        global_options={'-v quiet -stats'},
        inputs={'{0}{1}{2}'.format(input_directory, filename, extension): None},
        outputs={
            '{0}{1}.flac'.format(output_directory,
                                 filename + index): '-ss {0} -t {1} -q:a 0 -filter:a "atempo=1" -ar 16000 -ac 1 -map a'.format(
                start_time, end_time)}
    )

    # print (ff.cmd)
    # 'ffmpeg -i 8304_20171123_2000_Rai2.mov -ss 00:00:00.0 -t 00:35:00.0 -q:a 0 -ar 16000 -ac 1 -map a prova_TG2.flac'

    ff.run()

    return '{0}.flac'.format(filename + index)


def filename_upgrade(
        filename: str,
        start_time: str,
        index: str):
    """

    :param filename:
    :param start_time:
    :param index:
    :return:
    """

    file_time = filename[14:18]
    file_time = file_time[0:2] + ':' + file_time[2:5]

    t1 = datetime.datetime.strptime(file_time, '%H:%M:%S.%f').time()
    t2 = datetime.datetime.strptime(start_time, '%H:%M:%S.%f').time()

    td1 = datetime.timedelta(hours=t1.hour, minutes=t1.minute)
    td2 = datetime.timedelta(hours=t2.hour, minutes=t2.minute)
    td3 = datetime.timedelta(hours=0, minutes=int(index))

    td4 = td1 + td2 + td3

    ts = str(td4)
    ts = ts[:-3]
    ts = ts[0:1] + ts[2:3]

    return filename[1:13] + ts + filename[19:]
