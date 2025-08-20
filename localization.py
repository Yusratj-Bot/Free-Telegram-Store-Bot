# -*- coding: utf-8 -*-

from InDMDevDB import GetDataFromDB

LANGUAGES = {
    'en': 'English',
    'ru': 'Русский',
    'tj': 'Тоҷикӣ',
}

TEXTS = {
    'welcome': {
        'en': 'Welcome!',
        'ru': 'Добро пожаловать!',
        'tj': 'Хуш омадед!',
    },
    'shop_items': {
        'en': 'Shop Items 🛒',
        'ru': 'Товары 🛒',
        'tj': 'Маҳсулот 🛒',
    },
    'my_orders': {
        'en': 'My Orders 🛍',
        'ru': 'Мои заказы 🛍',
        'tj': 'Фармоишҳои ман 🛍',
    },
    'support': {
        'en': 'Support 📞',
        'ru': 'Поддержка 📞',
        'tj': 'Дастгирӣ 📞',
    },
    'home': {
        'en': 'Home 🏘',
        'ru': 'Главная 🏘',
        'tj': 'Асосӣ 🏘',
    },
    'choose_language': {
        'en': 'Please choose your language:',
        'ru': 'Пожалуйста, выберите ваш язык:',
        'tj': 'Лутфан, забони худро интихоб кунед:',
    },
    'language_updated': {
        'en': 'Language has been updated successfully.',
        'ru': 'Язык был успешно обновлен.',
        'tj': 'Забон бомуваффақият навсозӣ шуд.',
    },
    'error_occured': {
        'en': 'An error occurred. Please try again.',
        'ru': 'Произошла ошибка. Пожалуйста, попробуйте еще раз.',
        'tj': 'Хатогӣ рух дод. Лутфан, бори дигар кӯшиш кунед.',
    },
    'choose_action': {
        'en': 'Choose an action to perform ✅',
        'ru': 'Выберите действие для выполнения ✅',
        'tj': 'Амалро барои иҷро интихоб кунед ✅',
    },
    'admin_only': {
        'en': '⚠️ Only Admin can use this command !!!',
        'ru': '⚠️ Только администратор может использовать эту команду!!!',
        'tj': '⚠️ Танҳо администратор метавонад ин фармонро истифода барад!!!',
    },
    'error_processing_request': {
        'en': 'Error processing your request. Please try again.',
        'ru': 'Ошибка обработки вашего запроса. Пожалуйста, попробуйте еще раз.',
        'tj': 'Хатогии коркарди дархости шумо. Лутфан, бори дигар кӯшиш кунед.',
    },
    'manage_products': {
        'en': 'Manage Products 💼',
        'ru': 'Управление товарами 💼',
        'tj': 'Идораи маҳсулот 💼',
    },
    'manage_categories': {
        'en': 'Manage Categories 💼',
        'ru': 'Управление категориями 💼',
        'tj': 'Идораи категорияҳо 💼',
    },
    'manage_orders': {
        'en': 'Manage Orders 🛍',
        'ru': 'Управление заказами 🛍',
        'tj': 'Идораи фармоишҳо 🛍',
    },
    'payment_methods': {
        'en': 'Payment Methods 💳',
        'ru': 'Способы оплаты 💳',
        'tj': 'Усулҳои пардохт 💳',
    },
    'news_to_users': {
        'en': 'News To Users 📣',
        'ru': 'Новости для пользователей 📣',
        'tj': 'Хабарҳо барои корбарон 📣',
    },
    'switch_to_user': {
        'en': 'Switch To User 🙍‍♂️',
        'ru': 'Переключиться на пользователя 🙍‍♂️',
        'tj': 'Гузариш ба корбар 🙍‍♂️',
    },
    'store_statistics': {
        'en': "➖➖➖Store's Statistics 📊➖➖➖\n\n\nTotal Users 🙍‍♂️: {all_user_s}\n\nTotal Admins 🤴: {all_admin_s}\n\nTotal Products 🏷: {all_product_s}\n\nTotal Orders 🛍: {all_orders_s}\n\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖",
        'ru': "➖➖➖Статистика магазина 📊➖➖➖\n\n\nВсего пользователей 🙍‍♂️: {all_user_s}\n\nВсего админов 🤴: {all_admin_s}\n\nВсего продуктов 🏷: {all_product_s}\n\nВсего заказов 🛍: {all_orders_s}\n\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖",
        'tj': "➖➖➖Омори мағоза 📊➖➖➖\n\n\nШумораи умумии истифодабарандагон 🙍‍♂️: {all_user_s}\n\nШумораи умумии админҳо 🤴: {all_admin_s}\n\nШумораи умумии маҳсулот 🏷: {all_product_s}\n\nШумораи умумии фармоишҳо 🛍: {all_orders_s}\n\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖",
    },
    'admin_welcome_balance': {
        'en': "Dear {user_type},\n\nYour Wallet Balance: $ {user_data} 💰 \n\n{store_statistics}",
        'ru': "Уважаемый {user_type},\n\nВаш баланс кошелька: $ {user_data} 💰 \n\n{store_statistics}",
        'tj': "Муҳтарам {user_type},\n\nТавозуни ҳамёни шумо: $ {user_data} 💰 \n\n{store_statistics}",
    },
    'admin_welcome': {
        'en': "Dear {user_type},\n\nWelcome! 🤝\n\n{store_statistics}",
        'ru': "Уважаемый {user_type},\n\nДобро пожаловать! 🤝\n\n{store_statistics}",
        'tj': "Муҳтарам {user_type},\n\nХуш омадед! 🤝\n\n{store_statistics}",
    },
    'customer_welcome': {
        'en': "Dear {user_type},\n\nWelcome! 🤝\n\nBrowse our products, make purchases, and enjoy fast delivery! \nType /browse to start shopping. \n\n💬 Need help? \nContact our support team anytime.",
        'ru': "Уважаемый {user_type},\n\nДобро пожаловать! 🤝\n\nПросмотрите наши товары, совершайте покупки и наслаждайтесь быстрой доставкой! \nВведите /browse, чтобы начать покупки. \n\n💬 Нужна помощь? \nСвяжитесь с нашей службой поддержки в любое время.",
        'tj': "Муҳтарам {user_type},\n\nХуш омадед! 🤝\n\nМаҳсулоти моро аз назар гузаронед, харид кунед ва аз таҳвили зуд лаззат баред! \nБарои оғози харид /browse-ро ворид кунед. \n\n💬 Кӯмак лозим аст? \nБо дастаи дастгирии мо дар вақти дилхоҳ тамос гиред.",
    },
    'customer_welcome_balance': {
        'en': "Dear {user_type},\n\nYour Wallet Balance: $ {user_data} 💰 \n\nBrowse our products, make purchases, and enjoy fast delivery! \nType /browse to start shopping. \n\n💬 Need help? \nContact our support team anytime.",
        'ru': "Уважаемый {user_type},\n\nВаш баланс кошелька: $ {user_data} 💰 \n\nПросмотрите наши товары, совершайте покупки и наслаждайтесь быстрой доставкой! \nВведите /browse, чтобы начать покупки. \n\n💬 Нужна помощь? \nСвяжитесь с нашей службой поддержки в любое время.",
        'tj': "Муҳтарам {user_type},\n\nТавозуни ҳамёни шумо: $ {user_data} 💰 \n\nМаҳсулоти моро аз назар гузаронед, харид кунед ва аз таҳвили зуд лаззат баред! \nБарои оғози харид /browse-ро ворид кунед. \n\n💬 Кӯмак лозим аст? \nБо дастаи дастгирии мо дар вақти дилхоҳ тамос гиред.",
    },
    'user_mode_message': {
        'en': "You are on User Mode ✅\nSend /start command or press Home 🏘 button to switch back to Admin Mode",
        'ru': "Вы в режиме пользователя ✅\nОтправьте команду /start или нажмите кнопку «Домой» 🏘, чтобы вернуться в режим администратора",
        'tj': "Шумо дар ҳолати корбарӣ ✅\nФармони /start-ро фиристед ё тугмаи «Хона» 🏘-ро пахш кунед, то ба ҳолати администратор баргардед",
    },
    'add_new_product': {
        'en': 'Add New Product ➕',
        'ru': 'Добавить новый товар ➕',
        'tj': 'Иловаи маҳсулоти нав ➕',
    },
    'list_product': {
        'en': 'List Product 🏷',
        'ru': 'Список товаров 🏷',
        'tj': 'Рӯйхати маҳсулот 🏷',
    },
    'delete_product': {
        'en': 'Delete Product 🗑️',
        'ru': 'Удалить товар 🗑️',
        'tj': 'Нест кардани маҳсулот 🗑️',
    },
    'reply_product_name': {
        'en': 'Reply With Your Product Name or Tittle: ✅',
        'ru': 'Ответьте с названием вашего продукта или заголовком: ✅',
        'tj': 'Бо номи маҳсулот ё сарлавҳаи худ ҷавоб диҳед: ✅',
    },
    'reply_product_description': {
        'en': 'Reply With Your Product Description: ✅',
        'ru': 'Ответьте с описанием вашего продукта: ✅',
        'tj': 'Бо тавсифи маҳсулоти худ ҷавоб диҳед: ✅',
    },
    'error_404': {
        'en': 'Error 404 🚫, try again with corrected input.',
        'ru': 'Ошибка 404 🚫, попробуйте еще раз с правильным вводом.',
        'tj': 'Хатои 404 🚫, бо воридоти дуруст дубора кӯшиш кунед.',
    },
    'reply_product_price': {
        'en': 'Reply With Your Product Price: ✅',
        'ru': 'Ответьте с ценой вашего продукта: ✅',
        'tj': 'Бо нархи маҳсулоти худ ҷавоб диҳед: ✅',
    },
    'attach_product_photo': {
        'en': 'Attach Your Product Photo: ✅',
        'ru': 'Прикрепите фото вашего продукта: ✅',
        'tj': 'Акси маҳсулоти худро замима кунед: ✅',
    },
    'reply_new_category': {
        'en': "Please reply with a new category's name",
        'ru': 'Пожалуйста, ответьте с названием новой категории',
        'tj': 'Лутфан, бо номи категорияи нав ҷавоб диҳед',
    },
    'categories_list': {
        'en': 'CATEGORIES 👇',
        'ru': 'КАТЕГОРИИ 👇',
        'tj': 'КАТЕГОРИЯҲО 👇',
    },
    'select_category_or_new': {
        'en': "Click on a Category ID to select Category for this Product: ✅\n\n⚠️Or Write A New Category",
        'ru': 'Нажмите на ID категории, чтобы выбрать категорию для этого продукта: ✅\n\n⚠️Или напишите новую категорию',
        'tj': 'Барои интихоби категорияи ин маҳсулот ID-и категорияро клик кунед: ✅\n\n⚠️Ё категорияи нав нависед',
    },
    'attach_keys_file': {
        'en': "Attach Your Producy Keys In A Text File: ✅\n\n⚠️ Please Arrange Your Product Keys In the Text File, One Product Key Per Line In The File\n\n\n⚠️ Reply With Skip to skip this step if this Product has no Product Keys",
        'ru': 'Прикрепите ваши ключи продукта в текстовом файле: ✅\n\n⚠️ Пожалуйста, расположите ваши ключи продукта в текстовом файле, по одному ключу на строку\n\n\n⚠️ Ответьте Skip, чтобы пропустить этот шаг, если у этого продукта нет ключей',
        'tj': 'Калидҳои маҳсулоти худро дар файли матнӣ замима кунед: ✅\n\n⚠️ Лутфан, калидҳои маҳсулоти худро дар файли матнӣ ҷойгир кунед, як калид дар як сатр\n\n\n⚠️ Барои гузаштан аз ин қадам, агар ин маҳсулот калид надошта бошад, Skip ҷавоб диҳед',
    },
    'new_category_created': {
        'en': 'New Category created successfully  - {input_cat}',
        'ru': 'Новая категория успешно создана - {input_cat}',
        'tj': 'Категорияи нав бомуваффақият сохта шуд - {input_cat}',
    },
    'reply_download_link': {
        'en': "Reply With Download Link For This Product\n\nThis will be the Link customer will have access to after they have paid: ✅\n\n\n⚠️ Reply With Skip to skip this step if this Product has no Product Download Link",
        'ru': 'Ответьте ссылкой для скачивания этого продукта\n\nЭто будет ссылка, к которой клиент получит доступ после оплаты: ✅\n\n\n⚠️ Ответьте Skip, чтобы пропустить этот шаг, если у этого продукта нет ссылки для скачивания',
        'tj': 'Бо истиноди зеркашии ин маҳсулот ҷавоб диҳед\n\nИн истиноде хоҳад буд, ки муштарӣ пас аз пардохт ба он дастрасӣ пайдо мекунад: ✅\n\n\n⚠️ Барои гузаштан аз ин қадам, агар ин маҳсулот истиноди зеркашӣ надошта бошад, Skip ҷавоб диҳед',
    },
    'file_saved_successfully': {
        'en': 'File f"{productnumbers}.txt" saved successfully.',
        'ru': 'Файл f"{productnumbers}.txt" успешно сохранен.',
        'tj': 'Файли f"{productnumbers}.txt" бомуваффақият захира карда шуд.',
    },
    'download_link_skipped': {
        'en': 'Download Link Skipped ✅',
        'ru': 'Ссылка для скачивания пропущена ✅',
        'tj': 'Истиноди зеркашӣ гузаронида шуд ✅',
    },
    'product_details_caption': {
        'en': "\n\n\nProduct Tittle: {productname}\n\n\nProduct Number: `{productnumber}`\n\n\nProduct Price: {productprice} {store_currency} 💰\n\n\nQuantity Avaialble: {productquantity} \n\n\nProduct Description: {productdescription}",
        'ru': "\n\n\nНазвание продукта: {productname}\n\n\nНомер продукта: `{productnumber}`\n\n\nЦена продукта: {productprice} {store_currency} 💰\n\n\nКоличество в наличии: {productquantity} \n\n\nОписание продукта: {productdescription}",
        'tj': "\n\n\nСарлавҳаи маҳсулот: {productname}\n\n\nРақами маҳсулот: `{productnumber}`\n\n\nНархи маҳсулот: {productprice} {store_currency} 💰\n\n\nМиқдори дастрас: {productquantity} \n\n\nТавсифи маҳсулот: {productdescription}",
    },
    'product_added_successfully': {
        'en': 'Product Successfully Added ✅\n\nWhat will you like to do next ?',
        'ru': 'Товар успешно добавлен ✅\n\nЧто бы вы хотели сделать дальше?',
        'tj': 'Маҳсулот бомуваффақият илова карда шуд ✅\n\nМинбаъд чӣ кор кардан мехоҳед?',
    },
    'no_product_available': {
        'en': 'No product available, please send /start command to start creating products',
        'ru': 'Нет доступных товаров, пожалуйста, отправьте команду /start, чтобы начать создавать товары',
        'tj': 'Маҳсулот мавҷуд нест, лутфан фармони /start-ро фиристед, то ба эҷоди маҳсулот шурӯъ кунед',
    },
    'product_id_name': {
        'en': '👇Product ID --- Product Name👇',
        'ru': '👇ID товара --- Название товара👇',
        'tj': '👇ID-и маҳсулот --- Номи маҳсулот👇',
    },
    'click_product_to_delete': {
        'en': 'Click on a Product ID of the product you want to delete: ✅',
        'ru': 'Нажмите на ID товара, который вы хотите удалить: ✅',
        'tj': 'Барои нест кардани маҳсулот ID-и онро клик кунед: ✅',
    },
    'deleted_successfully': {
        'en': 'Deleted successfully 🗑️\n\n\nWhat will you like to do next ?\n\nSelect one of buttons 👇',
        'ru': 'Удалено успешно 🗑️\n\n\nЧто бы вы хотели сделать дальше?\n\nВыберите одну из кнопок 👇',
        'tj': 'Бомуваффақият нест карда шуд 🗑️\n\n\nМинбаъд чӣ кор кардан мехоҳед?\n\nЯке аз тугмаҳоро интихоб кунед 👇',
    },
    'no_order_found': {
        'en': 'No order found !',
        'ru': 'Заказ не найден !',
        'tj': 'Фармоиш ёфт нашуд !',
    },
    'item_sold_out': {
        'en': 'This Item is soldout !!!',
        'ru': 'Этот товар распродан !!!',
        'tj': 'Ин маҳсулот фурӯхта шудааст !!!',
    },
    'check_payment_status': {
        'en': 'Check Payment Status ⌛',
        'ru': 'Проверить статус платежа ⌛',
        'tj': 'Санҷиши ҳолати пардохт ⌛',
    },
    'send_btc_message': {
        'en': 'Please send extact {btc_amount:.8f} BTC (approximately {fiat_amount} {store_currency}) to the following Bitcoin',
        'ru': 'Пожалуйста, отправьте ровно {btc_amount:.8f} BTC (примерно {fiat_amount} {store_currency}) на следующий Bitcoin',
        'tj': 'Лутфан, дақиқан {btc_amount:.8f} BTC (тақрибан {fiat_amount} {store_currency}) ба Bitcoin-и зерин фиристед',
    },
    'payment_address': {
        'en': 'Address: `{payment_address}`',
        'ru': 'Адрес: `{payment_address}`',
        'tj': 'Суроға: `{payment_address}`',
    },
    'payment_status_instruction': {
        'en': 'Please stay on this page and click on Check Payment Status ⌛ button until payment is confirmed',
        'ru': 'Пожалуйста, оставайтесь на этой странице и нажимайте кнопку «Проверить статус платежа» ⌛ до тех пор, пока платеж не будет подтвержден',
        'tj': 'Лутфан, дар ин саҳифа бимонед ва то тасдиқи пардохт тугмаи «Санҷиши ҳолати пардохт» ⌛-ро пахш кунед',
    },
    'error_creating_payment_address': {
        'en': 'Error creating payment address. Please try again later.\n\nOR Amount value is too small',
        'ru': 'Ошибка создания платежного адреса. Пожалуйста, повторите попытку позже.\n\nИЛИ Сумма слишком мала',
        'tj': 'Хатои эҷоди суроғаи пардохт. Лутфан, баъдтар бори дигар кӯшиш кунед.\n\nЁ ин ки маблағ хеле хурд аст',
    },
    'error_converting_to_btc': {
        'en': 'Error converting amount to BTC. Please try again later.',
        'ru': 'Ошибка конвертации суммы в BTC. Пожалуйста, повторите попытку позже.',
        'tj': 'Хатои табдили маблағ ба BTC. Лутфан, баъдтар бори дигар кӯшиш кунед.',
    },
    'invalid_command': {
        'en': 'Invalid command.',
        'ru': 'Неверная команда.',
        'tj': 'Фармони нодуруст.',
    },
    'payment_confirmed': {
        'en': 'Payment received and confirmed!',
        'ru': 'Платеж получен и подтвержден!',
        'tj': 'Пардохт қабул ва тасдиқ карда шуд!',
    },
    'payment_successful': {
        'en': 'Payment successful ✅',
        'ru': 'Платеж успешен ✅',
        'tj': 'Пардохт бомуваффақият ✅',
    },
    'write_note_to_seller': {
        'en': 'Would you like to write a note to the Seller ?',
        'ru': 'Хотите написать записку продавцу?',
        'tj': 'Мехоҳед ба фурӯшанда ёддошт нависед?',
    },
    'reply_note_or_nil': {
        'en': 'Reply with your note or reply with NIL to proceed',
        'ru': 'Ответьте своей заметкой или ответьте NIL, чтобы продолжить',
        'tj': 'Бо ёддошти худ ҷавоб диҳед ё барои идома додан бо NIL ҷавоб диҳед',
    },
    'payment_status_is': {
        'en': 'Your payment is {status} for Order ID: {ordernumber}',
        'ru': 'Ваш платеж {status} для заказа ID: {ordernumber}',
        'tj': 'Пардохти шумо {status} барои фармоиши ID: {ordernumber}',
    },
    'no_pending_payment_order': {
        'en': 'No order found with pending payment confirmation !',
        'ru': 'Заказ с ожидающим подтверждения платежа не найден!',
        'tj': 'Фармоиш бо тасдиқи пардохти интизорӣ ёфт нашуд!',
    },
    'done': {
        'en': 'Done ✅',
        'ru': 'Готово ✅',
        'tj': 'Анҷом ✅',
    },
    'thank_you_for_order': {
        'en': 'Thank for your order 🤝',
        'ru': 'Спасибо за ваш заказ 🤝',
        'tj': 'Ташаккур барои фармоиши шумо 🤝',
    },
    'new_order_details': {
        'en': "YOUR NEW ORDER ✅\n\n\nOrder 🆔: {ordernumber}\nOrder Date 🗓: {orderdate}\nProduct Name 📦: {productname}\nProduct 🆔:{productnumber}\nProduct Price 💰: {productprice} {store_currency}\nPayment Method 💳: {paidmethod}\nProduct Keys 🔑: {productkeys}\nDownload ⤵️: {productdownloadlink}",
        'ru': "ВАШ НОВЫЙ ЗАКАЗ ✅\n\n\nЗаказ 🆔: {ordernumber}\nДата заказа 🗓: {orderdate}\nНазвание продукта 📦: {productname}\nID продукта:{productnumber}\nЦена продукта 💰: {productprice} {store_currency}\nСпособ оплаты 💳: {paidmethod}\nКлючи продукта 🔑: {productkeys}\nСкачать ⤵️: {productdownloadlink}",
        'tj': "ФАРМОИШИ НАВИ ШУМО ✅\n\n\nID-и фармоиш 🆔: {ordernumber}\nСанаи фармоиш 🗓: {orderdate}\nНоми маҳсулот 📦: {productname}\nID-и маҳсулот:{productnumber}\nНархи маҳсулот 💰: {productprice} {store_currency}\nУсули пардохт 💳: {paidmethod}\nКалидҳои маҳсулот 🔑: {productkeys}\nЗеркашӣ ⤵️: {productdownloadlink}",
    },
    'no_orders_yet': {
        'en': 'You have not completed any order yet, please purchase an Item now',
        'ru': 'Вы еще не совершили ни одного заказа, пожалуйста, купите товар сейчас',
        'tj': 'Шумо то ҳол ягон фармоишро анҷом надодаед, лутфан ҳоло як ашёро харидорӣ кунед',
    },
    'order_details_short': {
        'en': "{productname} ORDERED ON {orderdate} ✅\n\n\nOrder 🆔: {ordernumber}\nOrder Date 🗓: {orderdate}\nProduct Name 📦: {productname}\nProduct 🆔:{productnumber}\nProduct Price 💰: {productprice} {store_currency}\nPayment Method 💳: {paidmethod}\nProduct Keys 🔑: {productkeys}\nDownload ⤵️: {productdownloadlink}",
        'ru': "{productname} ЗАКАЗАН {orderdate} ✅\n\n\nЗаказ 🆔: {ordernumber}\nДата заказа 🗓: {orderdate}\nНазвание продукта 📦: {productname}\nID продукта:{productnumber}\nЦена продукта 💰: {productprice} {store_currency}\nСпособ оплаты 💳: {paidmethod}\nКлючи продукта 🔑: {productkeys}\nСкачать ⤵️: {productdownloadlink}",
        'tj': "{productname} ФАРМОИШ ДОДА ШУД {orderdate} ✅\n\n\nID-и фармоиш 🆔: {ordernumber}\nСанаи фармоиш 🗓: {orderdate}\nНоми маҳсулот 📦: {productname}\nID-и маҳсулот:{productnumber}\nНархи маҳсулот 💰: {productprice} {store_currency}\nУсули пардохт 💳: {paidmethod}\nКалидҳои маҳсулот 🔑: {productkeys}\nЗеркашӣ ⤵️: {productdownloadlink}",
    },
    'list_completed': {
        'en': 'List completed ✅',
        'ru': 'Список завершен ✅',
        'tj': 'Рӯйхат анҷом ёфт ✅',
    },
    'contact_us': {
        'en': 'Contact us @{username}',
        'ru': 'Свяжитесь с нами @{username}',
        'tj': 'Бо мо тамос гиред @{username}',
    },
    'reply_new_category_name': {
        'en': 'Reply with name you want to name your new category',
        'ru': 'Ответьте с названием, которое вы хотите дать вашей новой категории',
        'tj': 'Бо номе, ки мехоҳед ба категорияи нави худ диҳед, ҷавоб диҳед',
    },
    'no_category_in_store': {
        'en': 'No Category in your Store !!!',
        'ru': 'В вашем магазине нет категорий !!!',
        'tj': 'Дар мағозаи шумо категория вуҷуд надорад !!!',
    },
    'category_deleted': {
        'en': '{product_cate} successfully deleted 🗑️',
        'ru': '{product_cate} успешно удалена 🗑️',
        'tj': '{product_cate} бомуваффақият нест карда шуд 🗑️',
    },
    'category_not_found': {
        'en': 'Category not found !!!',
        'ru': 'Категория не найдена !!!',
        'tj': 'Категория ёфт нашуд !!!',
    },
    'current_category_name': {
        'en': "Current Category's Name: {product_cate} \n\n\nReply with your new Category's name",
        'ru': 'Текущее название категории: {product_cate} \n\n\nОтветьте новым названием категории',
        'tj': 'Номи ҷории категория: {product_cate} \n\n\nБо номи нави категория ҷавоб диҳед',
    },
    'category_to_edit_not_found': {
        'en': 'Category to edit not found !!!',
        'ru': 'Категория для редактирования не найдена !!!',
        'tj': 'Категория барои таҳрир ёфт нашуд !!!',
    },
    'category_name_updated': {
        'en': "Category's name successfully updated: ✅",
        'ru': 'Название категории успешно обновлено: ✅',
        'tj': 'Номи категория бомуваффақият навсозӣ шуд: ✅',
    },
    'no_category_in_store_create': {
        'en': "No Category in your Store !!!\n\n\nPlease reply with a new category's name to create Category",
        'ru': 'В вашем магазине нет категорий !!!\n\n\nПожалуйста, ответьте названием новой категории, чтобы создать ее',
        'tj': 'Дар мағозаи шумо категория вуҷуд надорад !!!\n\n\nЛутфан, бо номи категорияи нав ҷавоб диҳед, то категория эҷод кунед',
    },
    'add_new_category': {
        'en': 'Add New Category ➕',
        'ru': 'Добавить новую категорию ➕',
        'tj': 'Иловаи категорияи нав ➕',
    },
    'select_category_to_manage': {
        'en': 'Select Category you want to manage: ✅\n\nOr Create new Category',
        'ru': 'Выберите категорию, которой вы хотите управлять: ✅\n\nИли создайте новую категорию',
        'tj': 'Категорияеро, ки мехоҳед идора кунед, интихоб кунед: ✅\n\nЁ категорияи нав эҷод кунед',
    },
    'category_not_found_create': {
        'en': "Category not found !!!\n\n\nPlease reply with a new category's name to create category",
        'ru': 'Категория не найдена !!!\n\n\nПожалуйста, ответьте названием новой категории, чтобы создать ее',
        'tj': 'Категория ёфт нашуд !!!\n\n\nЛутфан, бо номи категорияи нав ҷавоб диҳед, то категория эҷод кунед',
    },
    'list_categories': {
        'en': 'List Categories 🏷',
        'ru': 'Список категорий 🏷',
        'tj': 'Рӯйхати категорияҳо 🏷',
    },
    'edit_category_name': {
        'en': 'Edit Category Name ✏️',
        'ru': 'Изменить название категории ✏️',
        'tj': 'Таҳрири номи категория ✏️',
    },
    'delete_category': {
        'en': 'Delete Category 🗑️',
        'ru': 'Удалить категорию 🗑️',
        'tj': 'Нест кардани категория 🗑️',
    },
    'what_to_do_next': {
        'en': 'What will you like to do next ?',
        'ru': 'Что бы вы хотели сделать дальше?',
        'tj': 'Минбаъд чӣ кор кардан мехоҳед?',
    },
    'new_category_created_what_next': {
        'en': 'New Category {input_cat} created successfully\n\n\nWhat will you like to do next ?',
        'ru': 'Новая категория {input_cat} успешно создана\n\n\nЧто бы вы хотели сделать дальше?',
        'tj': 'Категорияи нав {input_cat} бомуваффақият сохта шуд\n\n\nМинбаъд чӣ кор кардан мехоҳед?',
    },
    'products_list': {
        'en': 'PRODUCTS:',
        'ru': 'ТОВАРЫ:',
        'tj': 'МАҲСУЛОТ:',
    },
    'list_finished': {
        'en': 'List Finished: ✅',
        'ru': 'Список завершен: ✅',
        'tj': 'Рӯйхат анҷом ёфт: ✅',
    },
    'broadcast_message_prompt': {
        'en': 'This Bot is about to Broadcast mesage to all Shop Users\n\n\nReply with the message you want to Broadcast: ✅',
        'ru': 'Этот бот собирается разослать сообщение всем пользователям магазина\n\n\nОтветьте сообщением, которое вы хотите разослать: ✅',
        'tj': 'Ин бот паёмро ба ҳамаи истифодабарандагони мағоза пахш мекунад\n\n\nБо паёме, ки мехоҳед пахш кунед, ҷавоб диҳед: ✅',
    },
    'no_user_available': {
        'en': 'No user available in your store, /start',
        'ru': 'В вашем магазине нет доступных пользователей, /start',
        'tj': 'Дар мағозаи шумо корбари дастрас нест, /start',
    },
    'broadcasting_message': {
        'en': 'Now Broadcasting Message To All Users: ✅',
        'ru': 'Сейчас идет рассылка сообщения всем пользователям: ✅',
        'tj': 'Ҳоло паём ба ҳамаи истифодабарандагон пахш карда мешавад: ✅',
    },
    'message_sent_to': {
        'en': 'Message successfully sent ✅ To: @`{uname}`',
        'ru': 'Сообщение успешно отправлено ✅: @`{uname}`',
        'tj': 'Паём бомуваффақият фиристода шуд ✅ Ба: @`{uname}`',
    },
    'user_blocked_bot': {
        'en': 'User @{uid} has blocked the bot - {uname} ',
        'ru': 'Пользователь @{uid} заблокировал бота - {uname} ',
        'tj': 'Истифодабаранда @{uid} ботро масдуд кард - {uname} ',
    },
    'broadcast_completed': {
        'en': 'Broadcast Completed ✅',
        'ru': 'Рассылка завершена ✅',
        'tj': 'Пахш анҷом ёфт ✅',
    },
    'list_orders': {
        'en': 'List Orders 🛍',
        'ru': 'Список заказов 🛍',
        'tj': 'Рӯйхати фармоишҳо 🛍',
    },
    'delete_order': {
        'en': 'Delete Order 🗑️',
        'ru': 'Удалить заказ 🗑️',
        'tj': 'Нест кардани фармоиш 🗑️',
    },
    'no_order_available': {
        'en': 'No Order available in your store, /start',
        'ru': 'В вашем магазине нет доступных заказов, /start',
        'tj': 'Дар мағозаи шумо фармоиши дастрас нест, /start',
    },
    'your_orders_list': {
        'en': 'Your Oders List: ✅',
        'ru': 'Список ваших заказов: ✅',
        'tj': 'Рӯйхати фармоишҳои шумо: ✅',
    },
    'order_id_product_name_buyer_username': {
        'en': '👇 OrderID - ProductName - BuyerUserName👇',
        'ru': '👇 ID заказа - Название товара - Имя покупателя👇',
        'tj': '👇 ID-и фармоиш - Номи маҳсулот - Номи харидор👇',
    },
    'click_order_to_delete': {
        'en': 'Click on an Order ID of the order you want to delete: ✅',
        'ru': 'Нажмите на ID заказа, который вы хотите удалить: ✅',
        'tj': 'Барои нест кардани фармоиш ID-и онро клик кунед: ✅',
    },
    'add_bitcoin_method': {
        'en': 'Add Bitcoin Method ➕',
        'ru': 'Добавить метод Bitcoin ➕',
        'tj': 'Иловаи усули Bitcoin ➕',
    },
    'payment_method_already_added': {
        'en': '{edit_method} Payment method is already added ✅',
        'ru': 'Способ оплаты {edit_method} уже добавлен ✅',
        'tj': 'Усули пардохти {edit_method} аллакай илова карда шудааст ✅',
    },
    'reply_nowpayments_api_key': {
        'en': 'Reply With Your {edit_method} API Key for your NowPayments Account (https://account.nowpayments.io/create-account?link_id=3539852335): ✅',
        'ru': 'Ответьте своим API-ключом {edit_method} для вашей учетной записи NowPayments (https://account.nowpayments.io/create-account?link_id=3539852335): ✅',
        'tj': 'Бо калиди API-и {edit_method} барои ҳисоби NowPayments-и худ ҷавоб диҳед (https://account.nowpayments.io/create-account?link_id=3539852335): ✅',
    },
    'bitcoin_added_successfully': {
        'en': 'Bitcoin Added successfully ✅',
        'ru': 'Bitcoin успешно добавлен ✅',
        'tj': 'Bitcoin бомуваффақият илова карда шуд ✅',
    },
    'added_successfully': {
        'en': 'Added successfully ✅',
        'ru': 'Добавлено успешно ✅',
        'tj': 'Бомуваффақият илова карда шуд ✅',
    },
    'database_error': {
        'en': 'Database error occurred. Please try again later.',
        'ru': 'Произошла ошибка базы данных. Пожалуйста, повторите попытку позже.',
        'tj': 'Хатои базаи маълумот рух дод. Лутфан, баъдтар бори дигар кӯшиш кунед.',
    },
    'api_error': {
        'en': 'Error connecting to {api_name}. Please try again later.',
        'ru': 'Ошибка подключения к {api_name}. Пожалуйста, повторите попытку позже.',
        'tj': 'Хатои пайвастшавӣ ба {api_name}. Лутфан, баъдтар бори дигар кӯшиш кунед.',
    },
    'user_error': {
        'en': 'Invalid input. Please check your input and try again.',
        'ru': 'Неверный ввод. Пожалуйста, проверьте введенные данные и повторите попытку.',
        'tj': 'Вуруди нодуруст. Лутфан, вуруди худро санҷед ва бори дигар кӯшиш кунед.',
    },
    'product_details': {
        'en': "🏷️ **Product Details**\n\n**Name:** {name}\n**Price:** {price} {currency}\n**Description:** {description}\n**Quantity:** {quantity}\n**Category:** {category}",
        'ru': "🏷️ **Информация о товаре**\n\n**Название:** {name}\n**Цена:** {price} {currency}\n**Описание:** {description}\n**Количество:** {quantity}\n**Категория:** {category}",
        'tj': "🏷️ **Тафсилоти маҳсулот**\n\n**Ном:** {name}\n**Нарх:** {price} {currency}\n**Тавсиф:** {description}\n**Миқдор:** {quantity}\n**Категория:** {category}",
    },
    'order_details': {
        'en': "📦 **Order Details**\n\n**Order ID:** {id}\n**Product:** {product_name}\n**Price:** {price} {currency}\n**Date:** {date}\n**Status:** {status}",
        'ru': "📦 **Информация о заказе**\n\n**ID заказа:** {id}\n**Товар:** {product_name}\n**Цена:** {price} {currency}\n**Дата:** {date}\n**Статус:** {status}",
        'tj': "📦 **Тафсилоти фармоиш**\n\n**ID-и фармоиш:** {id}\n**Маҳсулот:** {product_name}\n**Нарх:** {price} {currency}\n**Сана:** {date}\n**Ҳолат:** {status}",
    },
    'error_message': {
        'en': '❌ {error_type}. Please try again or contact support.',
        'ru': '❌ {error_type}. Пожалуйста, повторите попытку или свяжитесь с поддержкой.',
        'tj': '❌ {error_type}. Лутфан, бори дигар кӯшиш кунед ё бо дастгирӣ тамос гиред.',
    },
    'error_message_simple': {
        'en': 'Error: {error_type}',
        'ru': 'Ошибка: {error_type}',
        'tj': 'Хато: {error_type}',
    },
    'no_product_available_soon': {
        'en': '⚠️ No Product available at the moment, kindly check back soon ',
        'ru': '⚠️ В данный момент нет доступных товаров, пожалуйста, зайдите позже ',
        'tj': '⚠️ Дар айни замон маҳсулот мавҷуд нест, лутфан баъдтар боздид кунед ',
    },
    'select_payment_method': {
        'en': '💡 Select a Payment method to pay for this product 👇',
        'ru': '💡 Выберите способ оплаты для этого товара 👇',
        'tj': '💡 Усули пардохтро барои ин маҳсулот интихоб кунед 👇',
    },
    'wrong_command': {
        'en': 'Wrong command !!!',
        'ru': 'Неверная команда !!!',
        'tj': 'Фармони нодуруст !!!',
    },
    'no_product_in_store': {
        'en': 'No Product in the store',
        'ru': 'В магазине нет товаров',
        'tj': 'Дар мағоза маҳсулот нест',
    },
    'category_products': {
        'en': "{product_cate} Gategory's Products",
        'ru': 'Товары категории {product_cate}',
        'tj': 'Маҳсулоти категорияи {product_cate}',
    },
    'buy_now': {
        'en': 'BUY NOW 💰',
        'ru': 'КУПИТЬ СЕЙЧАС 💰',
        'tj': 'ҲОЗИР ХАРИДАН 💰',
    },
    'product_details_short': {
        'en': "Product ID 🪪: /{productnumber}\n\nProduct Name 📦: {productname}\n\nProduct Price 💰: {productprice} {StoreCurrency}\n\nProducts In Stock 🛍: {productquantity}\n\nProduct Description 💬: {productdescription}",
        'ru': "ID товара 🪪: /{productnumber}\n\nНазвание товара 📦: {productname}\n\nЦена товара 💰: {productprice} {StoreCurrency}\n\nТоваров в наличии 🛍: {productquantity}\n\nОписание товара 💬: {productdescription}",
        'tj': "ID-и маҳсулот 🪪: /{productnumber}\n\nНоми маҳсулот 📦: {productname}\n\nНархи маҳсулот 💰: {productprice} {StoreCurrency}\n\nМаҳсулот дар анбор 🛍: {productquantity}\n\nТавсифи маҳсулот 💬: {productdescription}",
    },
}

def get_user_language(chat_id):
    """Gets the user's language from the database."""
    lang = GetDataFromDB.get_user_language(chat_id)
    if lang and lang in LANGUAGES:
        return lang
    return 'en'  # Default to English

def get_text(chat_id, key):
    """Gets the translated text for a given key and user."""
    lang = get_user_language(chat_id)
    return TEXTS.get(key, {}).get(lang, f"<{key}>")
