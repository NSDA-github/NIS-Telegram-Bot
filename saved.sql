CREATE TABLE users(
    user_id VARCHAR PRIMARY KEY,
    user_name VARCHAR,
    last_active TIME,
    chat_id VARCHAR,
    awaiting_grade BOOLEAN DEFAULT 0
);

CREATE TABLE messages(
    message_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    from_user VARCHAR,
    date_sent DATE,
    time_sent TIME,
    text_sent VARCHAR
);

CREATE TABLE schedule(
    grade VARCHAR PRIMARY KEY NOT NULL,
    weekday INTEGER,
    one VARCHAR,
    two VARCHAR,
    three VARCHAR,
    four VARCHAR,
    five VARCHAR,
    six VARCHAR,
    seven VARCHAR,
    eight VARCHAR,
    nine VARCHAR,
    ten VARCHAR
);