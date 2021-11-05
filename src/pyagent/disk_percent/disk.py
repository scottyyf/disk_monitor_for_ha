#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File:
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2019, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
import os
from pyha.AgentBase import AgentBase
from pyha.HaLog import logging


class disk(AgentBase):

    def __init__(self, opts):
        super(disk, self).__init__(opts)
        self._opts = opts
        self._name = self._opts.get_rsc_name()
        self._rsc_id = self._opts.get_rsc_id()
        self._mount_point = self._opts.get_option('mountpoint')
        if ',' in self._mount_point:
            self._mount_point = [
                p.strip() for p in self._mount_point.split(',')]
        else:
            self._mount_point = [self._mount_point]
        self._percent = self._opts.get_option('percent')

    def _is_mount_point(self, mp):
        return os.path.ismount(mp)

    def _get_disk_used_percent(self, mp):
        vfs = os.statvfs(mp)
        used = vfs.f_blocks - vfs.f_bfree
        ret = round(used * 100.00 / vfs.f_blocks, 2)
        return ret

    def start(self):
        return self.status()

    def status(self):
        ret = 0
        for mp in self._mount_point:
            if not self._is_mount_point(mp):
                logging.error(
                    '{0} is not a mountpoint in resource {1}'.format(
                        mp, self._name))
                ret = 1
                continue

            percent = self._get_disk_used_percent(mp)
            if percent >= float(self._percent):
                logging.error(
                    'mountpoint {0} for resource {1} used {2}, out of user '
                    'designed: {3}'.format(mp, self._name,
                                           percent, self._percent))
                ret = 1

        return ret

    def check_env(self):
        for mp in self._mount_point:
            if not self._is_mount_point(mp):
                return 1

            ret = self._get_disk_used_percent(mp)
            if ret >= float(self._percent):
                return 1

        return 0

    def alive(self):
        return self.status()

    def stop(self):
        return 0

