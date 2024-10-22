from telethon import Button

from ._handler import new_cmd


@new_cmd(pattern="start")
async def _start(msg):
    if not msg.is_private:
        return await msg.reply("Hi, I'm alive ~>_<~")
    caption = """
    Hi <b><a href="tg://user?id={}">{}</a></b>, I'm Valeri.
    I'm a bot that can help you with some stuff.
    check out my <code>/help</code> section to see what I can do for you."""
    await msg.reply(
        caption.format(msg.sender_id, msg.sender.first_name),
        parse_mode="html",
        buttons=buttons,
    )

@new_cmd(pattern="help")
async def _help(msg):
    await msg.reply("""Here is the help menu
    Commands
    /ariadl
    /ariadelall
    /cancel
    /ariastatus
    /ariapause
    /ariaresume
    /gpt
    /dalle
    /ping
    /ls
    /cd
    /rm
    /upl
    /ul
    /setthumb
    /series
    /resetthumb
    /dl
    /auth
    /unauth
    /update
    /restart
    /speedtest
    /eval
    /bash
    /exec
    /request
    /ext
    /info
    /gem
    /math
    /weather
    /ud
    /pinterest
    /gif
    /fake
    /wiki
    /id
    /paste
    /tl
    /movie
    /dog
    /song
    /animate
    /color
    /edit
    /itos
    /kang
    /kangemoji
    /cup
    /teradl""", buttons=help_menu)



