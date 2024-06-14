#  Pyrofork - Telegram MTProto API Client Library for Python
#  Copyright (C) 2022-present Mayuri-Chan <https://github.com/Mayuri-Chan>
#
#  This file is part of Pyrofork.
#
#  Pyrofork is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrofork is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrofork.  If not, see <http://www.gnu.org/licenses/>.

import pyrogram
from pyrogram import raw
from pyrogram import types


class GetStickerSet:
    async def get_sticker_set(
        self: "pyrogram.Client",
        set_short_name: str
    ) -> "types.StickerSet":
        """Get info about a stickerset.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            set_short_name (``str``):
               Stickerset shortname.

        Returns:
            :obj:`~pyrogram.types.StickerSet`: On success, the StickerSet information is returned.

        Example:
            .. code-block:: python

                await app.get_sticker_set("mypack1")
        """
        r, _ = await self._get_raw_stickers(
            raw.types.InputStickerSetShortName(
                short_name=short_name
            )
        )
        return r


    async def _get_raw_stickers(
        self: "pyrogram.Client",
        sticker_set: "raw.base.InputStickerSet"
    ) -> "types.StickerSet":
        """Internal Method.

        Parameters:
            sticker_set (:obj:`~pyrogram.raw.base.InputStickerSet`):

        Returns:
            List of :obj:`~pyrogram.types.Sticker`: A list of stickers is returned.

        Raises:
            ValueError: In case of invalid arguments.
        """
        sticker_set = await self.invoke(
            raw.functions.messages.GetStickerSet(
                stickerset=sticker_set,
                hash=0
            )
        )
        r = types.List([
            await types.Sticker._parse(
                self, doc, {type(a): a for a in doc.attributes}
            ) for doc in sticker_set.documents
        ])
        return r, sticker_set.set
