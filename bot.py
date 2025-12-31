from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import json

TOKEN = "8433505127:AAHrwGlx3Gk4IcNMr0TOu8NM399ppUDbwb4"

with open("novels.json", "r", encoding="utf-8") as f:
    NOVELS = json.load(f)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Cultivation Fandom Bot 🔥\n\n"
        "Use:\n"
        "/mc novel_name\n\n"
        "Example:\n"
        "/mc renegade_immortal"
    )

async def mc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Please give novel name")
        return

    key = "_".join(context.args).lower()

    if key not in NOVELS:
        await update.message.reply_text("❌ Novel not found")
        return

    n = NOVELS[key]

    text = (
        f"📘 {n['title']}\n\n"
        f"👤 MC: {n['mc']}\n"
        f"⚡ Realm: {n['realm']}\n"
        f"📈 Breakthrough: {n['breakthrough']}\n"
        f"🎂 Age: {n['age']}\n"
        f"📖 Manhwa: {n['manhwa']}\n"
        f"🎬 Donghua: {n['donghua']}"
    )

    keyboard = [
        [InlineKeyboardButton("⭐ Add Favorite", callback_data="fav")],
        [InlineKeyboardButton("💰 Refer & Earn", callback_data="refer")]
    ]

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("mc", mc))

print("Bot running...")
app.run_polling()
