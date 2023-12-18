from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.start_kb import start_keyboards
from keyboards.inline.course import courses, registration

from loader import dp


@dp.message_handler(text='📚 Kurslarimiz')
async def kurs_keyboard(message: types.Message):
    photo = 'https://marsit.uz/images/tild3366-3337-4366-a162-653661373337__4___-3.png'
    await message.reply_photo(photo=photo, caption='Barcha kurslarimiz', reply_markup=courses)


@dp.callback_query_handler()
async def starter_handler(call: types.CallbackQuery, state: FSMContext):
    kursni_nomi = call.data
    if kursni_nomi == 'starter':
        photo = 'https://marsit.uz/images/tild6563-3039-4132-b664-356163646536_____1.png'
        await call.message.reply_photo(photo=photo, caption='Starter kursi  3 oy   davom etadi',
                                       reply_markup=registration)
        await state.update_data(course='Starter kursi')

    elif kursni_nomi == 'frontend':
        photo = 'https://www.boardinfinity.com/blog/content/images/2023/01/Frontend-vs-Backend.png'
        await call.message.reply_photo(photo=photo, caption='Frontend kursi 5 oy davom etadi',
                                       reply_markup=registration)
        await state.update_data(course='Frontend kursi')

    elif kursni_nomi == 'backend':
        photo = 'https://highload.today/wp-content/uploads/2022/02/image1-16.png'
        await call.message.reply_photo(photo=photo, caption='Backend kursi 9 oy davom etadi', reply_markup=registration)
        await state.update_data(course='Backend kursi')

    elif kursni_nomi == 'grafik':
        photo = 'https://visme.co/blog/wp-content/uploads/2021/10/what-is-graphic-design-header-1200.png'
        await call.message.reply_photo(photo=photo, caption='Grafik dizayn 6 oy davom etadi', reply_markup=registration)
        await state.update_data(course='Grafik kursi')

    elif kursni_nomi == '3d':
        photo = 'https://www.ansys.com/content/dam/campaigns/abm/siemens/2020-10-3d-design-business-value.jpg?wid=1200'
        await call.message.reply_photo(photo=photo, caption='3d dizayn 6 oy davom etadi', reply_markup=registration)
        await state.update_data(course='3d dizayn kursi')

    elif kursni_nomi == 'back_to_main':
        await call.message.reply('Menyuni tanlang', reply_markup=start_keyboards)

