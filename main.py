from import_main import *
from telethon.tl.custom import Button
from utilities_as import Utilities


bot = TelegramClient('bot', API_ID, API_HASH)
utils = Utilities()
bot.parse_mode = 'html'


@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    if isinstance(event.peer_id, PeerUser):
        keyboard_buttons = [
            Button.text('📲 Меню', resize=True, single_use=True),
        ]

        await bot.send_message(
            entity=event.peer_id,
            message='Привіт, нажми кнопку \'Меню\'',
            buttons=keyboard_buttons)


@bot.on(events.NewMessage(pattern='📲 Меню'))
async def start(event):
    if isinstance(event.peer_id, PeerUser):
        inline_buttons = ReplyInlineMarkup(
            [
                KeyboardButtonRow(
                    [
                        KeyboardButtonCallback(
                            text='📝 Комунальні послуги загальна сума',
                            data=b'summa'
                        )
                    ]
                ),
                KeyboardButtonRow(
                    [
                        KeyboardButtonCallback(
                            text='🚰 Вода',
                            data=b'w'
                        ),
                        KeyboardButtonCallback(
                            text='💡 Світло',
                            data=b'l'
                        )
                    ]

                ),
                KeyboardButtonRow(
                    [
                        KeyboardButtonCallback(
                            text='🏡 Жек',
                            data=b'j'
                        ),
                        KeyboardButtonCallback(
                            text='🔥 Газ',
                            data=b'g'
                        )
                    ]

                ),
                KeyboardButtonRow(
                    [
                        KeyboardButtonCallback(text='🛜 Інтернет', data=b'i')
                    ]
                )
            ]
        )

        await bot.send_message(
            entity=event.peer_id,
            message='Вибери кнопку для отримання суми оплати',
            buttons=inline_buttons)


@bot.on(events.CallbackQuery(data='summa'))
async def summa(event):
    async def summ_func():
        a = await utils.gas()
        b = await utils.jek()
        c = utils.internet()
        d = utils.light()
        e = utils.water()
        res = round((a + b + c + d + e), 2)
        return str(res)
    message = await event.respond(f'<i>⬇️ Отримуємо дані... ⬇️</i>')
    summ = await summ_func()
    await bot.edit_message(message, f'<b><i>📝 - Загальна сума до оплати {str(summ)} грн.</b></i>')


@bot.on(events.CallbackQuery(data='w'))
async def water(event):
    message = await event.respond(f'<i>⬇️ Отримуємо дані... ⬇️</i>')
    w = utils.water()
    await bot.edit_message(message, f'<b><i>🚰 - До оплати за воду {str(w)} грн.</i></b>')


@bot.on(events.CallbackQuery(data='l'))
async def light(event):
    message = await event.respond(f'<i>⬇️ Отримуємо дані... ⬇️</i>')
    l = utils.light()
    await bot.edit_message(message, f'<b><i>💡 - До оплати за світло {str(l)} грн.</b></i>')


@bot.on(events.CallbackQuery(data='j'))
async def jek(event):
    message = await event.respond(f'<i>⬇️ Отримуємо дані... ⬇️</i>')
    j = await utils.jek()
    await bot.edit_message(message, f'<b><i>🏡 - До оплати за ЖКХ {str(j)} грн.</b></i>')


@bot.on(events.CallbackQuery(data='g'))
async def gas(event):
    message = await event.respond(f'<i>⬇️ Отримуємо дані... ⬇️</i>')
    g = await utils.gas()
    await bot.edit_message(message, f'<b><i>🔥 - До оплати за газ {str(g)} грн.</b></i>')


@bot.on(events.CallbackQuery(data='i'))
async def internet(event):
    message = await event.respond(f'<i>⬇️ Отримуємо дані... ⬇️</i>')
    i = utils.internet()
    await bot.edit_message(message, f'<b><i>🛜 - До оплати за інтернет {str(i)} грн.</b></i>')


bot.start()
bot.run_until_disconnected()
