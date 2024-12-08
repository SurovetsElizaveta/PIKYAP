import requests
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils import executor
from PIL import Image, ImageDraw, ImageFont
import io

TELEGRAM_BOT_TOKEN = '7417967380:AAEQgNS6qxK2zpQGTz5TwlYwT5txK-bZINk'
UNSPLASH_ACCESS_KEY = '9c9odrBt8HLsPK5OQn3jKrRkTblBJu85d6vu2ZDNPS4'

bot = Bot(token=TELEGRAM_BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


def wrap_text(text, font, max_width):
    lines = []
    words = text.split(' ')
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()
        if 44 * (len(test_line) // 2) <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)
    return lines


class Form(StatesGroup):
    waiting_for_word = State()
    waiting_for_photo_choice = State()
    waiting_for_caption = State()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Привет! Нажмите кнопку ниже, чтобы создать мем.", reply_markup=main_menu())


def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("Создать мем")
    markup.add(button)
    return markup


@dp.message_handler(lambda message: message.text == "Создать мем")
async def create_mem(message: types.Message):
    await Form.waiting_for_word.set()
    await message.answer("Пожалуйста, введите слово для поиска изображений.")


@dp.message_handler(state=Form.waiting_for_word)
async def search_photos(message: types.Message, state: FSMContext):
    query = message.text
    if not query:
        await message.answer("Пожалуйста, введите слово для поиска.")
        return

    url = f'https://api.unsplash.com/search/photos?page=1&query={query}&client_id={UNSPLASH_ACCESS_KEY}&per_page=10'
    response = requests.get(url)
    data = response.json()

    if data['total'] == 0:
        await message.answer("Извините, ничего не найдено. Попробуйте другое слово.")
        await state.finish()
        await Form.waiting_for_word.set()
        return

    photos = data['results']
    for photo in photos:
        await bot.send_photo(chat_id=message.chat.id, photo=photo['urls']['small'])

    await state.update_data(photos=photos)

    buttons = [types.InlineKeyboardButton(text=str(i + 1), callback_data=str(i)) for i in range(len(photos))]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)

    await Form.waiting_for_photo_choice.set()
    await message.answer("Выберите одно из фото, нажав на соответствующую цифру:", reply_markup=markup)


@dp.callback_query_handler(state=Form.waiting_for_photo_choice)
async def photo_choice(callback_query: types.CallbackQuery, state: FSMContext):
    selected_photo_index = int(callback_query.data)
    user_data = await state.get_data()
    photos = user_data.get('photos')

    if selected_photo_index < len(photos):
        selected_photo_url = photos[selected_photo_index]['urls']['small']
        await bot.send_message(callback_query.from_user.id, "Вы выбрали фото. Теперь введите текст для надписи:")
        await Form.waiting_for_caption.set()

        # Сохраняем выбранное фото в состоянии
        await state.update_data(selected_photo_url=selected_photo_url)
    else:
        await bot.send_message(callback_query.from_user.id, "Неверный выбор. Попробуйте снова.")


@dp.message_handler(state=Form.waiting_for_caption)
async def add_caption(message: types.Message, state: FSMContext):
    caption_text = message.text
    user_data = await state.get_data()
    selected_photo_url = user_data.get('selected_photo_url')

    # Скачиваем фото
    response = requests.get(selected_photo_url)
    image = Image.open(io.BytesIO(response.content))

    # Добавляем текст на изображение
    draw = ImageDraw.Draw(image)
    font_size = 44
    font_path = "Impact.ttf"
    font = ImageFont.truetype(font_path, font_size)

    max_width = image.width - 20
    wrapped_lines = wrap_text(caption_text, font, max_width)
    line_height = font_size + 8
    y_position = 12

    for line in wrapped_lines:
        x_position = 10
        draw.text((x_position, y_position), line, fill="white", font=font, stroke_width=3, stroke_fill=(0, 0, 0))
        y_position += line_height

    # Сохраняем изображение в байтовом потоке
    byte_io = io.BytesIO()
    byte_io.name = 'meme.png'
    image.save(byte_io, 'PNG')
    byte_io.seek(0)

    # Отправляем мем с текстом
    await bot.send_photo(chat_id=message.chat.id, photo=byte_io)

    await message.answer("Ваш мем готов! Если хотите создать еще один, нажмите 'Создать мем'.")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
