# -*- coding: utf-8 -*-

# Copyright(C) 2011 Laurent Bachelier
#
# This file is part of weboob.
#
# weboob is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# weboob is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with weboob. If not, see <http://www.gnu.org/licenses/>.


from weboob.tools.test import BackendTest
from .paste import PastebinPaste

class PastebinTest(BackendTest):
    BACKEND = 'pastebin'

    def test_get_paste(self):
        p = self.backend.get_paste('7HmXwzyt')
        self.backend.fillobj(p, ('title', 'contents'))
        assert p.title == 'plop'
        assert p.page_url == 'http://pastebin.com/7HmXwzyt'
        assert p.contents == 'prout'

    def test_post(self):
        p = PastebinPaste(None, title='ouiboube', contents='Weboob Test')
        self.backend.post_paste(p)
        assert p.id
        assert p.title == 'ouiboube'
        assert p.id in p.page_url
