from airflow.providers.telegram.hooks.telegram import TelegramHook # импортируем хук телеграма

def send_telegram_success_message(context): # на вход принимаем словарь со контекстными переменными
    hook = TelegramHook(telegram_conn_id='test',
                        token='7382616595:AAHSTKnPeXuDorrTw6Gv54j0aRWqW-LeTVo',
                        chat_id='4109648907')
    dag = context['dag']
    run_id = context['run_id']
    
    message = f'Исполнение DAG {dag} с id={run_id} прошло успешно!' # определение текста сообщения
    hook.send_message({
        'chat_id': '4109648907',
        'text': message
    }) # отправление сообщения 

def send_telegram_failure_message(context):
	# ваш код здесь #
    hook = TelegramHook(telegram_conn_id='test',
                        token='7382616595:AAHSTKnPeXuDorrTw6Gv54j0aRWqW-LeTVo',
                        chat_id='4109648907')
    dag = context['task_instance_key_str']
    run_id = context['run_id']
    
    message = f'Исполнение DAG {dag} с id={run_id} прошло неудачно!' # определение текста сообщения
    hook.send_message({
        'chat_id': '4109648907',
        'text': message
    }) # отправление сообщения 