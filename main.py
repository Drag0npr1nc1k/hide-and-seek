#--------------------------------------------
from aiogram import Bot,types 
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import random
#--------------------------------------------

TOK = "you token"

bot = Bot(token=TOK)
dp = Dispatcher(bot)



#variables
сorrect_answer = None
сorrect_answer_home = None
#variables


#inline keyboard 1
hide_and_seek = InlineKeyboardMarkup(row_width=3)
home_1 = InlineKeyboardButton('🏡', callback_data='home1')
home_2 = InlineKeyboardButton('🏡', callback_data='home2')
home_3 = InlineKeyboardButton('🏡', callback_data='home3')
hide_and_seek.add(home_1,home_2,home_3)
#inline keyboard 1



#inline keyboard 2
lose_and_win = InlineKeyboardMarkup(row_width=2)
again = InlineKeyboardButton('again', callback_data='again')
exit = InlineKeyboardButton('exit', callback_data='exit')
lose_and_win.add(exit,again)
#inline keyboard 2





@dp.message_handler(commands=['start'])
async def start(message : types.Message):
	await message.reply("Hello this is game bot hide and seek")
	await message.answer("To start the game, write /play")





@dp.message_handler(commands=['play'])
async def play(message : types.Message):
	global сorrect_answer
	global сorrect_answer_home

	await message.answer("Lets go, rule: Just choose the house where a person can be located")
	await message.answer("choose house", reply_markup=hide_and_seek)


	сorrect_answer = random.randint(0,3)
	

	if (сorrect_answer == 1 ):
		сorrect_answer_home = 1
	elif (сorrect_answer == 2 ):
		сorrect_answer_home = 2
	elif (сorrect_answer == 3 ):
		сorrect_answer_home = 3





@dp.callback_query_handler(lambda c: c.data == 'exit')
async def process_callback(call: types.CallbackQuery):
	await bot.edit_message_text(text = "Goodbay",chat_id=call.message.chat.id,message_id=call.message.message_id)
@dp.callback_query_handler(lambda c: c.data == 'again')
async def process_callback(call: types.CallbackQuery):
	global сorrect_answer
	global сorrect_answer_home

	await bot.edit_message_text(text = "choose house",chat_id=call.message.chat.id, reply_markup=hide_and_seek,message_id=call.message.message_id)


	сorrect_answer = random.randint(0,3)
	

	if (сorrect_answer == 1 ):
		сorrect_answer_home = 1
	elif (сorrect_answer == 2 ):
		сorrect_answer_home = 2
	elif (сorrect_answer == 3 ):
		сorrect_answer_home = 3

@dp.callback_query_handler(lambda c: c.data == 'home1')
async def process_callback(call: types.CallbackQuery):
	global сorrect_answer
	global сorrect_answer_home

	if (сorrect_answer_home == 1):
		await bot.edit_message_text(text = "Well done! You won",reply_markup=lose_and_win, chat_id=call.message.chat.id,message_id=call.message.message_id)
	else:
		await bot.edit_message_text(text = "Unfortunately. You lose 😢",reply_markup=lose_and_win, chat_id=call.message.chat.id,message_id=call.message.message_id)





@dp.callback_query_handler(lambda c: c.data == 'home2')
async def process_callback(call: types.CallbackQuery):
	global сorrect_answer
	global сorrect_answer_home

	if (сorrect_answer_home == 2):
		await bot.edit_message_text(text = "Well done! You won",reply_markup=lose_and_win, chat_id=call.message.chat.id,message_id=call.message.message_id)
	else:
		await bot.edit_message_text(text = "Unfortunately. You lose 😢",reply_markup=lose_and_win, chat_id=call.message.chat.id,message_id=call.message.message_id)





@dp.callback_query_handler(lambda c: c.data == 'home3')
async def process_callback(call: types.CallbackQuery):
	global сorrect_answer
	global сorrect_answer_home

	if (сorrect_answer_home == 3):
		await bot.edit_message_text(text = "Well done! You won",reply_markup=lose_and_win, chat_id=call.message.chat.id,message_id=call.message.message_id)
	else:
		await bot.edit_message_text(text = "Unfortunately. You lose 😢",reply_markup=lose_and_win, chat_id=call.message.chat.id,message_id=call.message.message_id)






executor.start_polling(dp, skip_updates=True)