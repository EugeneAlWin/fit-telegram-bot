from bot import bot
from aiogram import types
import urllib3
from config import NEWS_CHAT
async def transfer_messages(handled_messages:list[dict]):
    http=urllib3.PoolManager()
    decorator='<strong>^</strong>'
    for message in handled_messages:
        if 'reply_to' in message or message['text']!='': 
            await bot.send_chat_action(NEWS_CHAT,types.ChatActions.TYPING)
            text= '<strong>'+decorator*message['level']+message['sender']+'</strong>'+'\n'+message['text']+'\n'
            if 'reply_to' in message: text+= '<i>> Ответ на сообщение от '+message['reply_to']+'</i>\n'
            await bot.send_message(NEWS_CHAT, text=text, parse_mode='HTML')

        for attachment in message['attachments']:
            match(attachment['type']):
                case 'photo':
                    await bot.send_chat_action(NEWS_CHAT, types.ChatActions.UPLOAD_PHOTO)
                    await bot.send_photo(NEWS_CHAT, attachment['url'], caption=decorator*message['level']+'Фото от: '+ message['sender'])
                case 'doc':
                    await bot.send_chat_action(NEWS_CHAT, types.ChatActions.UPLOAD_DOCUMENT)
                    r=http.request('GET',attachment['url']).data
                    await bot.send_document(NEWS_CHAT,(attachment['title'],r), caption=decorator*message['level']+'Документ от: '+ message['sender']) 
                    
                case 'video':
                    await bot.send_chat_action(NEWS_CHAT, types.ChatActions.UPLOAD_VIDEO)
                    if attachment['by_direct']: await bot.send_video(NEWS_CHAT,attachment['url'], caption=decorator*message['level']+'Видео от: '+ message['sender'])
                    else : await bot.send_message(NEWS_CHAT,text=decorator*message['level']+'<a href="'+attachment['url']+'">Видео</a> от: '+message['sender']+'\n',parse_mode='HTML')
                    
                case 'audio_message':
                    await bot.send_chat_action(NEWS_CHAT, types.ChatActions.UPLOAD_VOICE)
                    await bot.send_voice(NEWS_CHAT, attachment['link_ogg'],caption=decorator*message['level']+'Голосовое сообщение от: '+ message['sender'])  
                    
                case "audio":
                    await bot.send_chat_action(NEWS_CHAT, types.ChatActions.UPLOAD_AUDIO)
                    r=http.request('GET',attachment['url']).data
                    await bot.send_audio(NEWS_CHAT,r,performer=attachment['artist'],title=attachment['title'], duration=attachment['duration'],caption=decorator*message['level']+'Аудио от: '+ message['sender'])

                case "poll":
                    await bot.send_chat_action(NEWS_CHAT,types.ChatActions.TYPING) 
                    await bot.send_message(NEWS_CHAT, text=decorator*message['level']+'<a href="'+attachment['url']+'">Голосование</a> от '+message['sender'], parse_mode='HTML')

                case "wall":
                    await bot.send_chat_action(NEWS_CHAT,types.ChatActions.TYPING)
                    await bot.send_message(NEWS_CHAT, text=decorator*message['level']+'<a href="'+attachment['url']+'">Запись на стене</a> от '+message['sender'], parse_mode='HTML')
