#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2013 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.

import ziggurat_foundations.models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension

from sqlalchemy_mptt import mptt_sessionmaker

DBSession = scoped_session(mptt_sessionmaker(
    sessionmaker(extension=ZopeTransactionExtension())))
Base = declarative_base()
ziggurat_foundations.models.DBSession = DBSession