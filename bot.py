from dotenv import load_dotenv
from telegram.ext import ChatJoinRequestHandler
from telegram.ext import ChatMemberHandler
import os
"""
Telegram Bot - Ex Limit Exchange
"""

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
TARGET_USER = os.getenv("TARGET_USER")
TELEGRAM_CHANNEL = os.getenv("TELEGRAM_CHANNEL", "https://t.me/+jQj9TUDx6XU5ZTEy")

async def handle_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    join_request = update.chat_join_request
    user = join_request.from_user

    # Приймаємо заявку
    await join_request.approve()

    # Відправляємо привітання в особисті
    try:
        await context.bot.send_message(
            chat_id=user.id,
            text=(
                f"Selamat hari, {user.first_name}!\n\n"
                "🚀 Selamat datang ke Ex Limit Exchange\n\n"
                "Lebih 5,000 transaksi berjaya dalam bidang pertukaran mata wang "
                "dan operasi di 8 negara — kami tahu apa itu kebolehpercayaan dan kelajuan.\n\n"
                "🔒 Sulit dan selamat\n"
                "🚚 Penghantaran tunai melalui kurier di 8 negara СНГ dan Eropah\n"
                "💸 Tiada caj tersembunyi\n"
                "⏱ Beroperasi 24/7\n\n"
                "Kelebihan kami:\n"
                "— Tanpa verifikasi\n"
                "— Pemprosesan permintaan secara pantas\n"
                "— Sokongan 24/7\n\n"
                "🏆 Terima kasih atas kepercayaan dan pilihan anda!\n\n"
                "Ex Limit Exchange — pertukaran USDT ke tunai yang selamat dan boleh dipercayai 💱"
            ),
            reply_markup=get_main_keyboard()
        )
    except Exception:
        pass

def get_main_keyboard():
    keyboard = [
        [
            KeyboardButton("📢 Saluran Telegram kami"),
            KeyboardButton("🏢 Cawangan fizikal"),
        ],
        [
            KeyboardButton("💱 Tempah pertukaran"),
            KeyboardButton("⭐ Ulasan"),
        ],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)


async def handle_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    result = update.chat_member

    # Перевіряємо що користувач саме вступив (був не членом, став членом)
    old_status = result.old_chat_member.status
    new_status = result.new_chat_member.status

    if old_status in ["left", "kicked"] and new_status == "member":
        user = result.new_chat_member.user

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    first_name = user.first_name or "Guest"

    welcome_message = (
        f"Selamat hari, {first_name}!\n\n"
        "🚀 Selamat datang ke Ex Limit Exchange\n\n"
        "Lebih 5,000 transaksi berjaya dalam bidang pertukaran mata wang "
        "dan operasi di 8 negara — kami tahu apa itu kebolehpercayaan dan kelajuan.\n\n"
        "🔒 Sulit dan selamat\n"
        "🚚 Penghantaran tunai melalui kurier di 8 negara СНГ dan Eropah\n"
        "💸 Tiada caj tersembunyi\n"
        "⏱ Beroperasi 24/7\n\n"
        "Kelebihan kami:\n"
        "— Tanpa verifikasi\n"
        "— Pemprosesan permintaan secara pantas\n"
        "— Sokongan 24/7\n\n"
        "🏆 Terima kasih atas kepercayaan dan pilihan anda!\n\n"
        "Ex Limit Exchange — pertukaran USDT ke tunai yang selamat dan boleh dipercayai 💱"
    )

    await update.message.reply_text(
        welcome_message,
        reply_markup=get_main_keyboard()
    )


async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text

    if text == "📢 Saluran Telegram kami":
        msg = (
            "🎉 Anda telah ditambahkan secara automatik ke saluran rasmi kami\n"
            "Ex Limit Exchange\n\n"
            "Di sini anda akan menerima setiap hari:\n\n"
            "📊 kadar tukaran terkini\n"
            "🛎 maklumat tentang perkhidmatan kami\n"
            "⭐ ulasan pelanggan sebenar\n"
            "🔥 tawaran eksklusif dan syarat peribadi\n\n"
            "Selamat datang — kami gembira melihat anda bersama kami 🧡"
        )
        keyboard = [
            [InlineKeyboardButton("➡️ Pergi ke saluran", url=TELEGRAM_CHANNEL)],
        ]
        await update.message.reply_text(msg, reply_markup=InlineKeyboardMarkup(keyboard))

    elif text == "🏢 Cawangan fizikal":
        msg = (
            "📍 Cawangan Fizikal ExLimit\n\n"
            "Lokasi-lokasi pertukaran kami ditunjukkan pada peta.\n"
            "Anda boleh memilih cawangan yang sesuai dan menjalankan pertukaran dengan cepat dan sulit.\n\n"
            "📍 4 cawangan fizikal di Moscow:\n\n"
            "🏦 Cawangan — Ul. Samarskaya, 1\n"
            "🏦 Cawangan — Ul. Vyatskaya, 27, bldg. 4\n"
            "🏦 Cawangan — Ul. Zemlyanoy Val, 27, bldg. 1\n"
            "🏦 Cawangan — Presnenskaya nab., 12\n\n"
            "📍 Almaty:\n"
            "🏦 Cawangan ⬅️\n\n"
            "🚚 Tiada cawangan di bandar anda?\n"
            "Kami juga menawarkan penghantaran tunai melalui kurier — mudah dan selamat.\n\n"
            "📩 Untuk maklumat lanjut dan penetapan kadar, hubungi pengurus kami - @ex_limit"
        )
        keyboard = [
            [InlineKeyboardButton("📍 Moscow — Ul. Samarskaya, 1", url="https://yandex.com/maps/213/moscow/?ll=37.626160%2C55.784775&mode=search&oid=232833101383&ol=biz&utm_source=share&z=15")],
            [InlineKeyboardButton("📍 Moscow — Ul. Vyatskaya, 27", url="https://yandex.com/maps/org/exlimit/217686214167/?ll=37.581909%2C55.796208&utm_source=share&z=15")],
            [InlineKeyboardButton("📍 Moscow — Ul. Zemlyanoy Val, 27", url="https://yandex.com/maps/213/moscow/?indoorLevel=1&ll=37.658293%2C55.759036&mode=search&oid=90459618474&ol=biz&utm_source=share&z=15")],
            [InlineKeyboardButton("📍 Moscow — Presnenskaya nab., 12", url="https://yandex.com/maps/-/CPA0FH~e")],
            [InlineKeyboardButton("📍 Almaty", url="https://yandex.com/maps/org/exlimit_crypto_exchange/115864643909/gallery/?ll=76.930499%2C43.263278&tab=gallery&z=15")],
            [InlineKeyboardButton("👤 Hubungi pengurus", url=f"https://t.me/{TARGET_USER}")],
        ]
        await update.message.reply_text(msg, reply_markup=InlineKeyboardMarkup(keyboard))

    elif text == "💱 Tempah pertukaran":
        msg = (
            "🌐 Perkhidmatan pertukaran antarabangsa\n\n"
            "Kami beroperasi di wilayah-wilayah utama dan setiap hari membantu pelanggan "
            "menjalankan pertukaran dengan cepat, selamat dan sulit:\n\n"
            "📌 CIS — Rusia, Kazakhstan, Belarus\n"
            "📌 Eropah — Jerman, Georgia, Latvia\n\n"
            "Perkhidmatan kami tersedia di pelbagai negara — anda memilih format yang sesuai, "
            "dan kami memastikan kebolehpercayaan, syarat yang telus dan kelajuan.\n\n"
            "Pilih kaedah pertukaran yang sesuai untuk anda:\n"
            "— tunai\n"
            "— penghantaran kurier\n"
            "— syarat individu atas permintaan"
        )
        keyboard = [
            [InlineKeyboardButton("💵 Pertukaran tanpa tunai", callback_data="cashless_exchange")],
            [InlineKeyboardButton("🚚 Penghantaran / Penerimaan tunai", callback_data="cash_delivery")],
        ]
        await update.message.reply_text(msg, reply_markup=InlineKeyboardMarkup(keyboard))

    elif text == "⭐ Ulasan":
        await update.message.reply_text(
            "🌟 Ulasan pelanggan kami\n\n"
            "Baca kisah nyata dan pengalaman bekerja bersama kami.\n\n"
            "💬 Kepercayaan Anda adalah nilai utama kami!",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("👤 Lihat ulasan", url=f"https://t.me/reviews_ExLimitExchange")
            ]])
        )


async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == "cashless_exchange":
        msg = (
            "💳 Tukar USDT terus ke wang tanpa tunai:\n"
            "(Tambahan dari kami +2.5% / +1.5% dari anda)\n\n"
            "🏦 Bank RF dan CIS — Tinkoff, Raiffeisen, Sberbank, Alfa, VTB, Kaspi\n"
            "🌐 Pembayaran akaun dan perkhidmatan luar negara\n"
            "🌍 Pemindahan antarabangsa: PayPal, IBAN, SEPA\n\n"
            "📩 Untuk butiran dan kadar, hubungi pengurus kami"
        )
        keyboard = [
            [InlineKeyboardButton("✍️ Tulis kepada pengurus", url=f"https://t.me/{TARGET_USER}")],
            [InlineKeyboardButton("🔙 Kembali", callback_data="back_to_exchange")],
        ]
        await query.edit_message_text(msg, reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "cash_delivery":
        msg = (
            "🌍 Kami beroperasi di negara-negara Eropah dan CIS — "
            "cawangan fizikal di Moscow dan Kazakhstan\n\n"
            "Anda juga boleh menerima wang tunai melalui kurier — "
            "pada kadar yang menguntungkan dan dengan penghantaran terus ke alamat yang dinyatakan.\n\n"
            "🚕 Pantas\n"
            "🔒 Sulit\n"
            "📋 Syarat yang telus\n\n"
            "📩 Untuk mengesahkan butiran dan menetapkan kadar, "
            "sila hubungi pengurus kami"
        )
        keyboard = [
            [InlineKeyboardButton("✍️ Tulis kepada pengurus", url=f"https://t.me/{TARGET_USER}")],
            [InlineKeyboardButton("🔙 Kembali", callback_data="back_to_exchange")],
        ]
        await query.edit_message_text(msg, reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "back_to_exchange":
        msg = (
            "🌐 Perkhidmatan pertukaran antarabangsa\n\n"
            "Kami beroperasi di wilayah-wilayah utama dan setiap hari membantu pelanggan "
            "menjalankan pertukaran dengan cepat, selamat dan sulit:\n\n"
            "📌 CIS — Rusia, Kazakhstan, Belarus\n"
            "📌 Eropah — Jerman, Georgia, Latvia\n\n"
            "Perkhidmatan kami tersedia di pelbagai negara — anda memilih format yang sesuai, "
            "dan kami memastikan kebolehpercayaan, syarat yang telus dan kelajuan.\n\n"
            "Pilih kaedah pertukaran yang sesuai untuk anda:\n"
            "— tunai\n"
            "— penghantaran kurier\n"
            "— syarat individu atas permintaan"
        )
        keyboard = [
            [InlineKeyboardButton("💵 Pertukaran tanpa tunai", callback_data="cashless_exchange")],
            [InlineKeyboardButton("🚚 Penghantaran / Penerimaan tunai", callback_data="cash_delivery")],
        ]
        await query.edit_message_text(msg, reply_markup=InlineKeyboardMarkup(keyboard))


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show this message"
    )


def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(ChatJoinRequestHandler(handle_join_request))
    application.add_handler(ChatMemberHandler(handle_new_member, ChatMemberHandler.CHAT_MEMBER))
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))
    application.add_handler(CallbackQueryHandler(handle_callback))

    application.run_polling(allowed_updates=[
        "message",
        "callback_query",
        "chat_member",
        "chat_join_request"
    ])


if __name__ == '__main__':
    main()