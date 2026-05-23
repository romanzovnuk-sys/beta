from telethon import events
import requests
import os

MODULES_DIR = "modules"


def register(bot):

    @bot.on(events.NewMessage(pattern=r"\.dlmod (.+)"))
    async def dlmod(event):

        url = event.pattern_match.group(1)

        try:

            r = requests.get(url)

            if r.status_code != 200:

                return await event.reply(
                    "❌ Download error"
                )

            name = url.split("/")[-1]

            if not name.endswith(".py"):

                return await event.reply(
                    "❌ Not python module"
                )

            path = os.path.join(
                MODULES_DIR,
                name
            )

            with open(path, "wb") as f:

                f.write(r.content)

            await event.reply(
                f"✅ Module downloaded: `{name}`"
            )

        except Exception as e:

            await event.reply(
                f"❌ Error:\n`{e}`"
            )
