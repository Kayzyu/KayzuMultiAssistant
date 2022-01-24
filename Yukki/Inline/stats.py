from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

stats1 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="System", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="Storage", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Bot", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="MongoDb", callback_data=f"mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Assistant", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats2 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="General", callback_data=f"gen_stats"
            ),
            InlineKeyboardButton(
                text="Storage", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Bot", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="MongoDb", callback_data=f"mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Assistant", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats3 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="System", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="General", callback_data=f"gen_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Bot", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="MongoDb", callback_data=f"mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Assistant", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats4 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="System", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="Storage", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="General", callback_data=f"gen_stats"
            ),
            InlineKeyboardButton(
                text="MongoDb", callback_data=f"mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Assistant", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats5 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="System", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="Storage", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Bot", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="General", callback_data=f"gen_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Assistant", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats6 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="System", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="Storage", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Bot", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="MongoDb", callback_data=f"mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="General", callback_data=f"gen_stats"
            )
        ],
    ]
)


stats7 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Getting Assistant Stats....",
                callback_data=f"wait_stats",
            )
        ]
    ]
)
